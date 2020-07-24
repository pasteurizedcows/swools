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

import re
from pathlib import Path
import sys
from objects.sim_options import Options
from objects.interface_files import Files
from objects.title import Title

# GLOBAL VARIABLES

# FUNCTIONS
def unrecorded_section_check(line):
    '''
    Tells the user if a section of the .inp file has no associated class

    Parameters
    ----------
    line: str
        the current line of the .inp file

    Returns
    -------
    None
    '''

    not_found = True
    if line[0] == '[' and line.strip()[-1] == ']':
        print('Section {} has no associated class'.format(line.strip()))

# exceptions
class InpNameError(Exception):
    '''
    Used when there is an error in the .inp file name
    '''
    pass

# CORE CLASS
class SWMMProject(object):
    '''
    A collection of SWMM objects
    Can read and write to .inp files
    '''

    def __init__(self, inp_file):
        self.inp_file = inp_file
        self._to_write = []
        self._read_inp_file()


    def _read_inp_file(self):
        '''
        Reads the SWMM .inp file and records the sections

        Returns
        -------
        None.
        '''

        # list of swmm elements
        swmm_elements = [Title(),
                        Options(),
                        Files()]

        # create a new attribute when a section has been located
        with open(self.inp_file, 'r') as inp_file:
            for line in inp_file:
                for element in swmm_elements:
                    if element.has_reached_section(line):
                        line = element.temp_read_params(inp_file)

                        # use the element type to designate the new attribute
                        if isinstance(element, Title) = 'Title':
                            self.title = element
                        elif isinstance(element, Options) = 'Options':
                            self.options = element
                        elif isinstance(element, Files) = 'Files':
                            self.files = element

                        self._to_write.append(element)
                    else:
                        pass
                else:
                    self._to_write.append(line)
                    unrecorded_section_check(line)

    def write_to_file(self, name, dir_path):
        '''
        Writes to a SWMM inp file

        Parameters
        ----------
        name: str
            Name of the output file

        dir_path: str
            Path to the folder in which the file will be saved

        Returns
        -------
        None
        '''
        if name[-4:] != '.inp':
            raise InpNameError('The SWMM inp file must end in .inp')

        s = ''
        for line in self._to_write:
            s += str(line)

        path = Path(dir_path)
        full_path = path / name
        with open(full_path, 'w') as out_file:
            out_file.write(s)

if __name__ == '__main__':
    test_dir = Path('C:/C_PROJECTS/Python/swools/tests/_project_tests')
    out_dir = test_dir / 'outputs'

    # test 1
    inp_file_1 = test_dir / 'ArvadaSWMP.inp'
    swmm_1 = SWMMProject(inp_file_1)

    out_name = 'test1.inp'
    out_path = out_dir

    swmm_1.write_to_file(out_name, out_path)
