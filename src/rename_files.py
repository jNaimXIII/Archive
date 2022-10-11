#!/usr/bin/env python

import os
import sys
import random

args = sys.argv

if len(args) < 2:
    raise Exception("missing arguments. <directory>")

relative_directory_path = args[1]
absolute_directory_path = os.path.abspath(relative_directory_path)

original_files = os.listdir(absolute_directory_path)
used_names = []

for original_file in original_files:
    random_number = random.randint(1_000_000, 9_999_999)
    while random_number in used_names:
        random_number = random.randint(1_000_000, 9_999_999)

    extension = ""
    if original_file.find("."):
        extension = original_file[original_file.rindex('.'):]

    renamed_file = str(random_number) + extension

    original_path = os.path.join(absolute_directory_path, original_file)
    renamed_path = os.path.join(absolute_directory_path, renamed_file)
    os.rename(original_path, renamed_path)
