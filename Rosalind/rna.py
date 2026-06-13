# Rosalind problem: Transcribing DNA into RNA
# URL: https://rosalind.info/problems/rna/

with open("rna_rosalind.txt") as file :
    dna = file.read().strip().replace("\n", "") 

rna = dna.replace("T", "U")

print(rna)
