import os
import re
from typing import List

from aisl.helpers import *
from aisl.ai_calls import run_prompt, setup_magic

def process_text(file_path: str) -> List[str]:
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
    
    return sections



def process_nonstandard(file_path: str) -> List[str]:
    with open(file_path, 'r') as file:
        data = file.read()
        sections = data.split('\n\n\n')
        sections = [section.strip() for section in sections]

    return sections


def process_directory(input_dir: str) -> List:
    txt_files = [f for f in os.listdir(input_dir) if f.endswith('.txt')]

    for txt_file in txt_files:
        full_path = os.path.join(input_dir, txt_file)

        try:
            sections = process_text(full_path)
        except IndexError:
            sections = process_nonstandard(full_path)
        
        # PROCESS SECTIONS
        for section in sections:
            print(f"{colored('-->', Color.YELLOW)} {section}", end='\n\n')

            prompt = {
                "snippet": section,
                "instruction": "Create study flashcards from the given text snippet. Provide no extra dialogue - only Q/A pairs. Answers should be short (1-6) words. Create multiple flashcards as needed for longer sentences. Create as many flashcards as possible from provided snippet."
            }

            ret = run_prompt(prompt.__str__())
            print(ret)

            input("PRESS ENTER") # pause for ENTER



def demo(args):
    setup_magic() # This command will eventually make calls to the OpenAI API

    process_directory("./dataset/extracted")
