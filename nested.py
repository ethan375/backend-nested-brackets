#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
program goes through lines of text checking to make sure every line has the correct number of brackets
"""
__author__ = "Ethan375"

import sys


def check_nested(string):

    stack = []

    open_chars = ['(*', '(', '[', '{', '<']
    closed_chars = ['*)', ')', ']', '}', '>']

    properly_nested = False

    while string:
        o_chars = 0
        c_chars = 0
    

        split_string = list(string)
        for enumerate(i), char in split_string:
            if char == '(' and split_string[i + 1] == '*':
                o_chars += 1
            elif char == '*' and split_string[i + 1] == ')':
                c_chars += 1
            elif char in open_chars:
                o_chars += 1
            elif char in closed_chars:
                c_chars += 1
        if o_chars == c_chars:
            return 'Yes'
        else:
            return 'No'
                




def main(args):
    input_file = args[1]

    with open(input_file, "r") as file:
        file = file.read()   
        split_input = file.split('\n')

    with open("output.txt", "w") as out:
        for line in split_input:
            out.write(check_nested(line) + '\n')
    

if __name__ == '__main__':
    main(sys.argv)
