#!/usr/bin/env python3

def return_evens(num_list):
    evenList = [n for n in num_list if n % 2 == 0]
    return evenList


def make_exclamation(sentence_list):
    exclamationlist=[sentence + "!" for sentence in sentence_list] 

    return exclamationlist