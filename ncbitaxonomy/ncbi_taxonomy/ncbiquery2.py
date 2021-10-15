#!/usr/bin/env python
# -*- coding: utf-8 -*-
from . import ncbiquery

__all__ = ["NCBITaxa"]

RANKS = [
    "superkingdom",
    "kingdom",
    "phylum",
    "class",
    "order",
    "family",
    "genus",
    "species",
]


class NCBITaxa(ncbiquery.NCBITaxa):

    def get_ranked_lineage(self, taxid):
        """
        Wrapper around self.get_lineage
        """
        if not taxid:
            return {}
        try:
            lineage = self.get_rank(super().get_lineage(taxid))
            return {r: str(t) for t, r in lineage.items() if r in RANKS}
        except ValueError:
            # This will happen if the ID is not found or the dbs are out of date
            return {}

    def get_lineage_safe(self, taxid, safe=True):
        """
        Wrapper around NCBI.get_lineage to return an empty list when ID isn't
        recognised. Get the full lineage of NCBI and get a {} if ID isn't
        recognised
        :param taxid: NCBI Taxon ID
        :type taxid: int or str
        :param safe: catch ValueErrors and return empty dict
        :type safe: bool
        :returns dictionary of taxids that represent taxid's full lineage.
        :raises ValueError: Taxonomic ID is not recognised when safe=False.
        """
        try:
            return super().get_lineage(int(taxid))
        except ValueError as e:
            if safe:
                return []
            else:
                raise e
