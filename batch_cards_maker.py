#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Automates the production of a 7 families cardgame.
    cards background should be put in the background folder,
    the members of each family in order in a text file in folder families.
    the text of each card should go in the folder text in the following format:
      Name
      Flavor text
      Family
      Rank in the family
      Consumption advice
"""

import sys

try:
    import scribus
except ImportError:
    print "This script only runs from within Scribus."
    sys.exit(1)

import re

from os import listdir



from python_functions.modifying_functions import *
from python_functions.parsing_functions import get_families_ascii_names



TITLE = "Batch Card Maker"


def main():

    familles = get_families_ascii_names()
    for famille in familles:
        for n in range(1,7):
            scribus.openDoc("template.sla")
            items = scribus.getPageItems()
        
            change_title(famille, n, items)
            change_number(famille, n, items)
            change_family(famille, n, items)
            change_advice(famille, n, items)
            change_family_members(famille, n, items)
            change_flavor(famille, n, items)
            change_background(famille, n, items)

            image = scribus.ImageExport()
            image.type = 'PNG'
            image.scale = 100
            image.saveAs(famille + "_" + str(n) + ".png")

            scribus.closeDoc()


if __name__ == '__main__':
    if scribus.haveDoc():
        main()
    else:
        scribus.messageBox(TITLE, "No document open", scribus.ICON_WARNING)
