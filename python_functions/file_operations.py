#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" set of functions that serves as a high level interface
    to get information from the content files.
"""


from os import listdir



def get_family_file(i): # i between 0 and 6
    families = [family for family in listdir("families")]
    f = open("families/" + families[i],'r')
    return f


def get_families_names():
    families = []
    for i in range(7):  
        f = get_family_file(i)
        families.append(f.readline()[:-1])
        f.close()
    return families


def get_families_ascii_names():
    return [family[:-4] for family in listdir("families")]


def get_family_file_by_name(name):
    return open("families/" + name + ".txt",'r')


def get_food_name(f, i):
    k = -2
    line = ""
    while k != i:
        line = f.readline()
        k+=1
    return line


def get_food_filename(f, i):
    k = -9
    line = ""
    while k != i:
        line = f.readline()
        k+=1
    if k != 6:
        line = line[:-1]
    return line


def get_food_file(family, j):
    f = get_family_file_by_name(family)
    name = get_food_filename(f, j)
    f.close()
    return open("text/" + name + ".txt",'r')
