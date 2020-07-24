'''
This class is to read and write the TITLE portion of the SWMM .inp file
'''

class Title(object):
    '''
    The TITLE of the SWMM .inp file
    '''

    def __init__(self):
        self.title = None

    def __str__(self):
        s = '[TITLE]\n'
        s += self.title
        return s

    @staticmethod
    def has_reached_section(line):
        '''
        Determines if the TITLE section has been reached when reading the
        .inp file

        Parameters
        ----------
        line : str
            current line from the .inp file

        Returns
        -------
        bool
            True if [TITLE], else False
        '''
        if line.strip() == '[TITLE]':
            return True
        else:
            return False

    def read_params(self, inp_file):
        '''
        Reads the TITLE parameters from the .inp file and records them
        as attributes

        Parameters
        ----------
        inp_file : input file
            the SWMM .inp file

        Returns
        -------
        str
            the line after the last param
        '''

        self.title = ''
        for line in inp_file:
            if line != '\n':
                self.title += line
            else:
                break
        return line
