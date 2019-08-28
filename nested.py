#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
program goes through lines of text checking to make sure every line has the correct number of brackets
"""
__author__ = "Ethan375"

import sys

def main(args):
    input_file = open(args[1],'r')
    read_file = input_file.read()

    split_input = read_file.split('\n')
    refined_list = []
    for val in split_input:
        if val != '':
            refined_list.append(val)
    print(refined_list)
    

    open_chars = 0
    closed_chars = 0 
    for string in refined_list:
        for s in string:
            if s == '(*':
                open_chars += 1
            elif s == '(':
                open_chars += 1 
            elif s == '[':
                open_chars += 1 
            elif s == '{':
                open_chars += 1 
            elif s == '*)':
                closed_chars += 1 
            elif s == ')':
                closed_chars += 1 
            elif s == '(':
                closed_chars += 1 
            elif s == '(':
                closed_chars += 1 
            elif s == '(':
                closed_chars += 1
            if closed_chars > open_chars:
                return 'theres been a problem'
    print(open_chars)
    print(closed_chars)
    if open_chars != closed_chars:
        return 'something went wrong'
    else:
        return 'something went just fine'
    input_file.close

if __name__ == '__main__':
    main(sys.argv)
