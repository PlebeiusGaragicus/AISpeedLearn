import sys
import os
import re
from typing import List

from helpers import *
from . import summarize


def process_text(file_path: str) -> List[str]:
    with open(file_path, 'r') as file:
        data = file.read()


        # You can process each section here with your AI model.
        # processed_sections = [some_model.predict(section) for section in sections]


def process_text(file_path: str) -> None:
    # Replace this function with the actual processing you need to do
    with open(file_path, 'r') as file:
        data = file.read()
        print(f'Processing file: {file_path}')

        # Split the text into sections based on uppercase letters followed by a period
        sections = re.split(r'\n\s*([A-Z])\.\s*', data)

        # print(sections, end='\n\n')

        for section in sections:
            # summary = summarize.summarize(section)
            print(f"{colored('-->', Color.YELLOW)} {section}", end='\n\n')

        sys.exit(0)

        # re.split creates an array with the delimiters (section names) as separate elements.
        # We want to reattach these to the start of each section.
        sections = [sections[i] + sections[i + 1] for i in range(0, len(sections), 2)]

        for section in sections:
            summary = summarize.summarize(section)
            print(summary)



def process_directory(input_dir: str) -> List:
    # Get a list of all .txt files in the directory
    txt_files = [f for f in os.listdir(input_dir) if f.endswith('.txt')]

    results = []
    for txt_file in txt_files:
        # Get the full path to the file
        full_path = os.path.join(input_dir, txt_file)

        # Process the file and store the result
        result = process_text(full_path)
        results.append(result)

    return results



if __name__ == "__main__":
    # Process all .txt files in the 'study_materials/processed' directory
    # process_directory('./study_materials/processed')

    process_text('./study_materials/processed/GO1.txt')







def process_directory(input_dir: str) -> List[List[str]]:
    txt_files = [f for f in os.listdir(input_dir) if f.endswith('.txt')]

    results = []
    for txt_file in txt_files:
        full_path = os.path.join(input_dir, txt_file)
        sections = process_text(full_path)
        results.append(sections)

    return results

process_directory('./study_materials/processed')
