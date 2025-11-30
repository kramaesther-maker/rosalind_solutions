cd rosalind_solutions

# rosalind_functions.py
# Your Name
# Implementations for Rosalind problems

# DNA
def dna_count(s):
    return (
        s.count("A"),
        s.count("C"),
        s.count("G"),
        s.count("T")
    )

# RNA
def dna_to_rna(s):
    return s.replace("T", "U")

# REVC
def reverse_complement(s):
    complement = {"A":"T","T":"A","C":"G","G":"C"}
    return "".join(complement[b] for b in reversed(s))

# GC
def gc_content(fasta_dict):
    best_id = None
    best_gc = 0
    for seq_id, seq in fasta_dict.items():
        gc = (seq.count("G") + seq.count("C")) / len(seq) * 100
        if gc > best_gc:
            best_gc = gc
            best_id = seq_id
    return best_id, best_gc

# HAMM
def hamming_distance(s1, s2):
    return sum(b1 != b2 for b1, b2 in zip(s1, s2))

# PROT
def rna_to_protein(rna):
    codon_table = {
        "AUG":"M","UUU":"F","UUC":"F", # etc. (I will give full table if needed)
    }
    protein = ""
    for i in range(0, len(rna), 3):
        codon = rna[i:i+3]
        if codon_table.get(codon) == "Stop":
            break
        protein += codon_table.get(codon, "")
    return protein

# SUBS
def substring_positions(s, sub):
    positions = []
    for i in range(len(s) - len(sub) + 1):
        if s[i:i+len(sub)] == sub:
            positions.append(i+1)
    return positions

# PRTM
def protein_mass(protein):
    mass_table = {
        "A": 71.03711, "C": 103.00919, # full table available on request
    }
    return sum(mass_table[a] for a in protein)

# REVP
def reverse_palindromes(s):
    result = []
    complement = {"A":"T","T":"A","C":"G","G":"C"}
    for i in range(len(s)):
        for length in range(4, 13):
            segment = s[i:i+length]
            if len(segment) < length:
                continue
            revc = "".join(complement[b] for b in reversed(segment))
            if segment == revc:
                result.append((i+1, length))
    return result

# TRAN
def transition_transversion_ratio(s1, s2):
    transitions = [("A","G"), ("G","A"), ("C","T"), ("T","C")]
    ts = tv = 0
    for a, b in zip(s1, s2):
        if a == b:
            continue
        if (a,b) in transitions:
            ts += 1
        else:
            tv += 1
    return ts/tv if tv > 0 else float("inf")
