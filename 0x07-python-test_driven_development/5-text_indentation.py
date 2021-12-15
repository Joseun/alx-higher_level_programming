#!/usr/bin/python3
"""Indenting a text"""


def text_indentation(text):
    """Prints a indented format of a text using ., ? and : as delimiters.

    Args:
        text(:obj:'str'): text to be indented


     """
    if not type(text) is str:
        raise TypeError("text must be a string")

    i = 0
    while i < len(text) and text[i] == ' ':
        i += 1

    while i < len(text):
        print(text[i], end="")
        if text[i] == "\n" or text[i] in ".?:":
            if text[i] in ".?:":
                print("\n")
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
