def validate_sequence(dna):
    valid_nucleotides = ['A', 'T', 'G', 'C']
    dna = dna.upper()
    for nucleotide in dna:
        if nucleotide not in valid_nucleotides:
            return False
    return True

def count_nucleotides(dna):
    dna = dna.upper().strip()
    counts = {'A': 0, 'T': 0, 'G': 0, 'C': 0}
    for nucleotide in dna:
        if nucleotide == 'A':
            counts['A'] += 1
        elif nucleotide == 'T':
            counts['T'] += 1
        elif nucleotide == 'G':
            counts['G'] += 1
        elif nucleotide == 'C':
            counts['C'] += 1
    return counts

def calculate_gc_content(dna):
    dna = dna.upper()
    counts = count_nucleotides(dna)
    total = len(dna)
    
    if total == 0:
        return 0
    
    gc_count = counts['G'] + counts['C']
    gc_percentage = (gc_count / total) * 100
    
    return gc_percentage

def get_complement(dna):
    dna = dna.upper()
    complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    
    complement_strand = ''
    for nucleotide in dna:
        if nucleotide in complement:
            complement_strand += complement[nucleotide]
    
    return complement_strand

def analyze_dna(dna):
    dna = dna.upper().strip()
    
    if not validate_sequence(dna):
        print("ERROR: Invalid DNA sequence!")
        print("DNA should only contain A, T, G, C")
        return
    
    print(f"\nOriginal Sequence: {dna}")
    print(f"Length: {len(dna)} base pairs")
    
    counts = count_nucleotides(dna)
    print("\nNucleotide Counts:")
    for nucleotide in ['A', 'T', 'G', 'C']:
        print(f"  {nucleotide}: {counts[nucleotide]}")
    
    gc_content = calculate_gc_content(dna)
    print(f"\nGC Content: {gc_content:.2f}%")
    
    complement = get_complement(dna)
    print(f"\nComplementary Strand: {complement}")

print("Welcome to DNA Sequence Analyzer!")
print("\nOptions:")
print("1. Enter DNA sequence manually")
print("2. Read from file")

choice = input("\nEnter your choice (1 or 2): ")

if choice == '1':
    dna_sequence = input("\nEnter DNA sequence: ")
    analyze_dna(dna_sequence)
    
elif choice == '2':
    filename = input("\nEnter filename: ")
    try:
        with open(filename, 'r') as file:
            dna_sequence = file.read()
            analyze_dna(dna_sequence)
    except FileNotFoundError:
        print(f"ERROR: File '{filename}' not found!")
else:
    print("Invalid choice!")
