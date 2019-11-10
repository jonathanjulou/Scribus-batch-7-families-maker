#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" functions that perform the modification of each object
    using the scribus API
"""

import sys

try:
    import scribus
except ImportError:
    print "This script only runs from within Scribus."
    sys.exit(1)


from parsing_functions import *
    

TITLE = "Batch Card Maker"


def change_text(text, item):

    l = scribus.getTextLength(item)
    scribus.selectText(0, l, item)
    fs = scribus.getFontSize(item)
    f = scribus.getFont(item)
    
    scribus.insertText(text, 0, item)
    l2 = scribus.getTextLength(item)
    scribus.selectText(0, l2, item)
    scribus.setFontSize(fs, item)
    scribus.setFont(f, item)

    scribus.selectText(l2-l, l, item)
    scribus.deleteText(item)

    scribus.deselectAll()
    

def change_title(family, j, item):
    titre = item[1][0]
    change_text(parse_title(family, j), titre)


def change_family(family, j, item):
    familytext = item[2][0]
    change_text(parse_family(family, j), familytext)


def change_number(family, j, item):
    number = item[3][0]
    change_text(str(j), number)


def change_advice(family, j, item):
    advice = item[5][0]
    change_text(parse_advice(family, j), advice)


def change_family_members(family, j, item):
    fam1 = item[6][0]
    fam2 = item[7][0]
    text1, text2 = parse_family_members(family, j)
    change_text(text1, fam1)
    change_text(text2, fam2)

    
def change_flavor(family, j, item):
    flavor = item[4][0]
    change_text(parse_flavor(family, j), flavor)


def change_background(family, j, item):
    f = get_family_file_by_name(family)
    image = item[0][0]
    scribus.loadImage("background/" + get_food_filename(f,j) + ".png", image)
    
