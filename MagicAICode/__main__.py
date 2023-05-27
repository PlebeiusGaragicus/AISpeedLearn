import os
import re
from typing import List

from MagicAICode.helpers import *
from . import summarize


def process_text(file_path: str) -> List[str]:
    print(file_path)
    with open(file_path, 'r') as file:
        data = file.read()
        
        # Find the start indices of each section
        matches = list(re.finditer(r'^\s*((I{1,3}|IV|V?I{0,3}|IX|X?(I{1,3}|IV|V?I{0,3}|IX){0,4})L?)\.\s+.*?$', data, flags=re.MULTILINE))
        start_indices = [match.start() for match in matches]

        # Add the end of the file to the list of indices
        start_indices.append(len(data))

        # Create sections using start indices
        sections = [data[start_indices[i]:start_indices[i+1]].strip() for i in range(len(start_indices) - 1)]

        # Identify the index of the line with "Portland Fire & Rescue" in the last section
        # NOTE: this will throw an IndexError for documents with NON-STANDARD FORMATTING
        lines = sections[-1].split("\n")

        try:
            idx = next(i for i, line in reversed(list(enumerate(lines))) if line.strip() == "Portland Fire & Rescue")
            # Remove this line and the 2 preceding lines, and everything after
            sections[-1] = "\n".join(lines[:idx-2])
        except StopIteration:  # "Portland Fire & Rescue" line not found
            pass
        
        for section in sections:
            print(f"{colored('-->', Color.YELLOW)} {section}", end='\n\n')
    
    print(file_path)



def process_nonstandard(file_path: str) -> None:
    print("non-standard processing: ", file_path)

    with open(file_path, 'r') as file:
        data = file.read()
        sections = data.split('\n\n\n')
        sections = [section.strip() for section in sections]

    for section in sections:
        print(f"{colored('-->', Color.YELLOW)} {section}", end='\n\n')

    print(file_path)




def process_directory(input_dir: str) -> List:
    txt_files = [f for f in os.listdir(input_dir) if f.endswith('.txt')]

    for txt_file in txt_files:
        full_path = os.path.join(input_dir, txt_file)

        try:
            process_text(full_path)
        except IndexError:
            process_nonstandard(full_path)
        input("PRESS ENTER") # pause for ENTER


if __name__ == "__main__":
    process_directory('./study_materials/processed')
