#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import re
import os
import shutil
import subprocess
import argparse

# This is to help coaches and graders identify student assignments
__author__ = "jmsMaupin1"

def get_absolute_paths(directory):
    """Checks a directory to see if any files match our regex, return them if so"""
    files = os.listdir(directory)
    regex = re.compile(r'__\w*__')

    return [os.path.abspath(f) for f in files if regex.search(f)]

def copy_files_to(files, directory):
    """Copies files to a given directory using shutil"""
    if not os.path.isdir(directory):
        try:
            os.makedirs(directory)
        except OSError:
            print("Creation of directory %s failed" % directory)
            return 1

    for f in files:
        shutil.copyfile(f, directory + "/" + files.split("/")[-1])      

def main():
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    # TODO need an argument to pick up 'from_dir'
    args = parser.parse_args()
    # print(get_absolute_paths("./"))
    # copy_files_to(get_absolute_paths("./"), "./tmp")

    # TODO you must write your own code to get the cmdline args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation.  If something is wrong (or missing) with any
    # required args, the general rule is to print a usage message and exit(1).

    # +++your code here+++
    # Call your functions


if __name__ == "__main__":
    main()
