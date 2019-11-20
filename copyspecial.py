#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import re
import sys
import os
import shutil
import subprocess
import argparse

# This is to help coaches and graders identify student assignments
__author__ = "jmsMaupin1"


def get_special_paths(directory):
    """Checks a directory to see if any files match our regex, return them"""
    files = os.listdir(directory)
    pattern = r'__\w*__'

    return ["%s" % os.path.abspath(f) for f in files if re.search(pattern, f)]


def create_dir(path):
    """Checks to see if a directory exists, if not creates it"""
    if not os.path.isdir(path):
        try:
            os.makedirs(path)
        except OSError:
            print("Creation of directory %s failed" % path)
            return -1

    return 0


def copy_to(path, copy_dir):
    """Copies files to a given directory using shutil"""
    files = get_special_paths(path)
    status = create_dir(copy_dir)

    if status:
        return status

    for f in files:
        shutil.copyfile(f, copy_dir + "/" + f.split("/")[-1])

    return 0


def zip_to(path, zip_dir):
    """given a list of paths, zip those files up into the given zipfile"""
    files = get_special_paths(path)
    zip_split = zip_dir.split("/")

    status = create_dir("/".join(zip_split[:-1]))

    if status:
        return status

    cmd = ['zip', '-j', zip_dir]
    cmd.extend(files)
    print("Command I\'m running is: {}".format(" ".join(cmd)))
    subprocess.call(cmd)

    return 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('from_dir', help='dir to grab special files from')
    args = parser.parse_args()

    if args.todir:
        status = copy_to(args.from_dir, args.todir)

    if args.tozip:
        status = zip_to(args.from_dir, args.tozip)

    sys.exit(status)


if __name__ == "__main__":
    main()
