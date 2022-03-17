#!/usr/bin/python3
""" function that finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """ function that finds a peak in a list of unsorted integers """

    if len(list_of_integers) < 2:
        return (None)
    if len(set(list_of_integers)) < 2:
        return (list_of_integers[0])
    else:
        peak = list_of_integers[0]
        for i in range(len(list_of_integers)):
            if ((list_of_integers[i] > list_of_integers[i + 1]) and
                    (list_of_integers[i] > list_of_integers[i - 1])):
                peak = list_of_integers[i]
                break
        return (peak)
