#
#
with open("rosalind_revc (1).txt") as file :
    dna = file.read().strip()
    table = str.maketrans("ATCG","TAGC")
    reversed_complement_dna = dna.translate(table)[::-1]
print(reversed_complement_dna)
