# Genome Pattern Search

This project allows you to search for occurrences of a given DNA pattern and its reverse complement in a genome sequence. The program counts how many times a specific pattern or its reverse complement appears in the genome.

## Features

- **Reverse Complement Calculation**: The program calculates the reverse complement of a DNA sequence. For example, the reverse complement of `"ACTAT"` is `"TATCA"`.
- **Pattern Search**: It searches for both the original pattern and its reverse complement within a given genome sequence.
- **Case Handling**: Handles matching between the given genome and the patterns of interest.

## Example
Given the genome sequence:
   ```bash
   ACAACTATGCATACTATCGGGAACTATCCTATAGT
   ```

And the input pattern :
  ```bash
  ACTAT
   ```

The output will be :
  ```bash
   3
   ```

This means the pattern "ACTAT" and its reverse complement "TATCA" are found a total of 3 times in the genome sequence.

### Requirements
No external dependencies are required for this project. You only need a Python interpreter.

### Running the Program

1. Clone or download the project.
2. Open a terminal and navigate to the project directory.
3. Run the script using Python.

   ```bash
   python genome_pattern_search.py
   ```

# License
This project is open source and free to use
