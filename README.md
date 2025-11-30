# rosalind_solutions

Solutions to selected Rosalind bioinformatics problems in Python.

## Overview

This repository contains a small library of Python functions that solve classic Rosalind problems, all implemented in a single file: `rosalind_functions.py`.

Each function returns a value instead of printing, and no external libraries are used.

## Problems Implemented

- **DNA** – Counting DNA Nucleotides  
  - Input: DNA string  
  - Output: 4 integers giving the count of `A`, `C`, `G`, and `T`.

- **RNA** – Transcribing DNA into RNA  
  - Input: DNA string  
  - Output: RNA string with all `T` replaced by `U`.

- **REVC** – Complementing a Strand of DNA  
  - Input: DNA string  
  - Output: Reverse complement of the string.

- **GC** – Computing GC Content  
  - Input: FASTA-formatted strings  
  - Output: ID of the string with highest GC content and its percentage.

- **HAMM** – Counting Point Mutations  
  - Input: Two equal-length strings  
  - Output: Hamming distance (number of differing positions).

- **PROT** – Translating RNA into Protein  
  - Input: RNA string  
  - Output: Amino acid sequence until the first stop codon.

- **SUBS** – Finding a Motif in DNA  
  - Input: DNA string and a motif  
  - Output: 1-based positions where the motif occurs in the DNA string.

- **PRTM** – Calculating Protein Mass  
  - Input: Protein string  
  - Output: Total monoisotopic mass of the protein.

- **REVP** – Locating Restriction Sites  
  - Input: DNA string  
  - Output: Positions and lengths of reverse-palindromic substrings.

- **TRAN** – Transitions and Transversions  
  - Input: Two DNA strings  
  - Output: Ratio of transitions to transversions.

## File Structure

- `README.md` – This description of the project and problems.  
- `rosalind_functions.py` – All Python implementations for the problems above.

## Usage

Import the functions in a Python script or Jupyter notebook, e.g.:

```python
from rosalind_functions import dna_count, dna_to_rna

counts = dna_count("AGCT")
rna = dna_to_rna("GATACA")
# rosalind_solutions
Solutions to selected Rosalind bioinformatics problems in Python
