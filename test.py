import ete3

NCBI = ete3.NCBITaxa()
NCBI.update_taxonomy_database()
print(NCBI.get_lineage("9606"))
assert NCBI.get_lineage("9606") == [1, 131567, 2759, 33154, 33208, 6072, 33213, 33511, 7711, 89593, 7742, 7776, 117570, 117571, 8287, 1338369, 32523, 32524, 40674, 32525, 9347, 1437010, 314146, 9443, 376913, 314293, 9526, 314295, 9604, 207598, 9605, 9606]
print(NCBI.translate_to_names([9606])[0])
assert NCBI.translate_to_names([9606])[0] == "Homo sapiens"
