import os
import json
from typing import List

from aisl.helpers import *

def popquiz(args: dict):
    input_dir = "./dataset/study_materials"

    txt_files = [f for f in os.listdir(input_dir) if f.endswith('.txt')]

    json_objects = []

    for txt_file in txt_files:
        full_path = os.path.join(input_dir, txt_file)

        with open(full_path, 'r') as file:
            for line in file:  # Iterate over every line in the file
                try:
                    # print(line)
                    data = json.loads(line)
                    json_objects.append(data)
                except json.JSONDecodeError:
                    pass

    print('\n\n\n\n\n\n\n\n\n')
    for qa in json_objects:
        print('-'*40)
        print(colored(qa['Question'], Color.GREEN))
        # input(colored("\nPRESS ENTER", Color.YELLOW))
        input('\n')
        print(colored(qa['Answer'], Color.YELLOW))
        print(colored(qa['SourceSentence'], Color.BLUE))
        input('\n\n\n')

        # print(qa["SourceSentence"])
        # input("PRESS ENTER\n\n")
