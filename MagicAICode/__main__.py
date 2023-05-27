import sys
import os
import re
from typing import List

from MagicAICode.helpers import *
from . import summarize


# def process_text(file_path: str) -> List[str]:
#     with open(file_path, 'r') as file:
#         data = file.read()

#         # Split the text into sections based on Roman numerals followed by a period
#         # sections = re.split(r'\b(X{0,3}|X{0,2}VI{0,3}|X{0,2}I{0,4}|XL|L)\.\s*', data)
#         sections = re.split(r'(\b(X{0,3}|X{0,2}VI{0,3}|X{0,2}I{0,4}|XL|L)\.\s+[^.\n]+\s+)', data)


#         # If sections list is odd, append an empty string to make it even
#         # if len(sections) % 2 != 0:
#         #     sections.append('')

#         # sections = [sections[i] + sections[i + 1] for i in range(0, len(sections), 2)]
        
#         # Remove leading and trailing whitespace from each line in each section
#         # sections = ['\n'.join(line.strip() for line in section.split('\n')) for section in sections]

#         for section in sections:
#             # summary = summarize.summarize(section)
#             print(f"{colored('-->', Color.YELLOW)} {section}", end='\n\n')



# def process_text(file_path: str) -> List[str]:
#     with open(file_path, 'r') as file:
#         data = file.read()
#         sections = re.split(r'(^((I{1,3}|IV|V?I{0,3}|IX|X?(I{1,3}|IV|V?I{0,3}|IX){0,4})L?)\.\s+.*?$)', data, flags=re.MULTILINE)
#         sections = [section.strip() for section in sections if section and section.strip()]

#         for section in sections:
#             print(f"{colored('-->', Color.YELLOW)} {section}", end='\n\n')


def process_text(file_path: str) -> List[str]:
    with open(file_path, 'r') as file:
        data = file.read()
        
        # Find the start indices of each section
        matches = list(re.finditer(r'^((I{1,3}|IV|V?I{0,3}|IX|X?(I{1,3}|IV|V?I{0,3}|IX){0,4})L?)\.\s+.*?$', data, flags=re.MULTILINE))
        start_indices = [match.start() for match in matches]

        # Add the end of the file to the list of indices
        start_indices.append(len(data))

        # Create sections using start indices
        sections = [data[start_indices[i]:start_indices[i+1]].strip() for i in range(len(start_indices) - 1)]

        # Modify the last section in the document to remove the dates revised and chief "signoff"
        # TODO: this is not tested for each document...
        sections[-1] = sections[-1].split('\n\n\n')[0]

        for section in sections:
            print(f"{colored('-->', Color.YELLOW)} {section}", end='\n\n')



# def process_text(file_path: str) -> List[str]:
#     with open(file_path, 'r') as file:
#         data = file.read()


#         # You can process each section here with your AI model.
#         # processed_sections = [some_model.predict(section) for section in sections]


# def process_text(file_path: str) -> None:
#     with open(file_path, 'r') as file:
#         data = file.read()
#         print(f'Processing file: {file_path}')

#         # Split the text into sections based on uppercase letters followed by a period
#         # sections = re.split(r'\n\s*([A-Z])\.\s*', data)
#         sections = re.split(r'\n(I|IV|V|IX|X)\.\s*', data)

#         for section in sections:
#             # summary = summarize.summarize(section)
#             print(f"{colored('-->', Color.YELLOW)} {section}", end='\n\n')


        # re.split creates an array with the delimiters (section names) as separate elements.
        # We want to reattach these to the start of each section.
        # sections = [sections[i] + sections[i + 1] for i in range(0, len(sections), 2)]

        # for section in sections:
        #     summary = summarize.summarize(section)
        #     print(summary)





if __name__ == "__main__":
    # Process all .txt files in the 'study_materials/processed' directory
    # process_directory('./study_materials/processed')

    process_text('./study_materials/processed/GO1.txt')






# def process_directory(input_dir: str) -> List:
#     # Get a list of all .txt files in the directory
#     txt_files = [f for f in os.listdir(input_dir) if f.endswith('.txt')]

#     results = []
#     for txt_file in txt_files:
#         # Get the full path to the file
#         full_path = os.path.join(input_dir, txt_file)

#         # Process the file and store the result
#         result = process_text(full_path)
#         results.append(result)

#     return results


# def process_directory(input_dir: str) -> List[List[str]]:
#     txt_files = [f for f in os.listdir(input_dir) if f.endswith('.txt')]

#     results = []
#     for txt_file in txt_files:
#         full_path = os.path.join(input_dir, txt_file)
#         sections = process_text(full_path)
#         results.append(sections)

#     return results

# process_directory('./study_materials/processed')
