# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 15:45:45 2020

@author: Jacob.Brown
"""


'''
A collection of SWMM objects:
- INP_FILE
- TITLE
- OPTIONS
- FILES

Nodes
- OUTFALLS
- JUNCTIONS
- DIVIDERS
- STORAGE

Conduits
- CONDUITS
- OUTLETS
- WEIRS
'''

from objects.sim_options import Options
from objects.interface_files import Files


class SWMMProject(object):
    '''
    A collection of SWMM objects
    Can read and write to .inp files
    '''

    def __init__(self, inp_file):
        self.inp_file == inp_file
        self.read_inp_file()

    def _read_inp_file(self):
        '''
        Reads the SWMM .inp file

        Returns
        -------
        None.
        '''

        pass
