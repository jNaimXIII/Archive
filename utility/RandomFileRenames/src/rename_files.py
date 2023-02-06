#!/usr/bin/env python

import os
import sys
import random
import shutil

cli_args = sys.argv

if len(cli_args) < 2:
    raise Exception("missing arguments. <directory>")

relative_source_dir_path = cli_args[1]
absolute_source_dir_path = os.path.abspath(relative_source_dir_path)

relative_destination_dir_path = relative_source_dir_path
absolute_destination_dir_path = absolute_source_dir_path

if len(cli_args) == 3:
    relative_destination_dir_path = cli_args[2]
    absolute_destination_dir_path = os.path.abspath(relative_destination_dir_path)

source_file_names = os.listdir(absolute_source_dir_path)
used_file_names = []
used_file_names.extend(source_file_names)


def name_generator(used_names):
    random_int_name = str(random.randint(1_000_000, 9_999_999))

    while random_int_name in used_names:
        random_int_name = str(random.randint(1_000_000, 9_999_999))

    return random_int_name


for source_file_name in source_file_names:
    generated_name = name_generator(used_file_names)

    file_extension = ""
    if source_file_name.find("."):
        file_extension = source_file_name[source_file_name.rindex('.'):]

    renamed_file_name = generated_name + file_extension

    source_file_path = os.path.join(absolute_source_dir_path, source_file_name)
    destination_file_path = os.path.join(absolute_destination_dir_path, renamed_file_name)

    if absolute_source_dir_path == absolute_destination_dir_path:
        os.rename(source_file_path, destination_file_path)
    else:
        shutil.copy(source_file_path, destination_file_path)
