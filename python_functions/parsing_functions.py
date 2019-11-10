#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" functions used to transform the raw text files into usable information
    for the modifying functions.
"""

from os import listdir



from file_operations import *


def parse_title(family, j): #i family, j member number (1...6)
    f = get_family_file_by_name(family)
    food_name = get_food_name(f, j)
    f.close()
    return food_name.decode('Latin-1').encode('utf-8')


def parse_number(family, j):
    f = get_family_file_by_name(family)
    name = get_food_name(f, j)
    k = -2
    line = ""
    while line != name:
        line = f.readline()
        k+=1
    f.close()
    return k


def parse_family(family, j):
    f = get_family_file_by_name(family)
    output = f.readline().decode('Latin-1').encode('utf-8')
    f.close()
    return output


def parse_advice(family, j):
    f = get_food_file(family, j)
    line = ""
    while not(line.startswith(str(j))):
        line = f.readline()
        
    output =  f.readline().decode('Latin-1').encode('utf-8')
    f.close()
    return output


def parse_family_members(family, j):
    f = get_family_file_by_name(family)
    f.readline()
    f.readline()
    k = 0
    rep = []
    while k != 6:
        rep.append(f.readline().decode('Latin-1').encode('utf-8'))
        k+=1

    ans1 = rep[0] + "\n" + rep[1] + "\n" + rep[2]

    ans2 = rep[3] + "\n" + rep[4] + "\n" + rep[5]
    f.close()        
    return ans1, ans2


def parse_flavor(family, j):
    f = get_food_file(family, j)
    text = ""
    line = ""
    f.readline()
    while not(line.startswith(str(j))):
        line = f.readline()
        text += line
    f.close
    return text[:-2].decode('Latin-1').encode('utf-8')
