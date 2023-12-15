#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import argparse
import doc_functions

parser = argparse.ArgumentParser(description='Generate documentation.')
parser.add_argument('--name', '-n', type=str, help='Code name')
parser.add_argument('--type', '-t', type=str, help='Code types')
parser.add_argument('--input', '-i', type=str, help='Input file path')
parser.add_argument('--output', '-o', type=str, help='Output file path')

args = parser.parse_args()
if args.name: name_project = args.name
type_code = 'python'
if args.type: type_code = args.type
dir_input = 'src'
if args.input: dir_input = args.input
dir_output = 'docs'
if args.output: dir_output = args.output

if not os.path.exists(dir_output):
    os.makedirs(dir_output)
    os.chdir(dir_output)
    if 'python' in type_code: doc_functions.doc_python(name_project, dir_input)
    print('')
    if 'cpp' in type_code: doc_functions.doc_cpp(name_project, dir_input)
    os.chdir('..')
else: print('docs already exists')