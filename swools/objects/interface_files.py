'''
This class is to read and write the FILES portion of the SWMM .inp file
'''

from pathlib import PurePath, Path
import re

FILE_TYPES = ['RAINFALL', 'RUNOFF', 'RDII', 'HOTSTART', 'INFLOWS', 'OUTFLOWS']

# EXCEPTIONS
class IncorrectFileType(Exception):
    '''
    An exception for the incorrect file type
    '''
    pass

class FileNotFoundError(Exception):
    '''
    An exception for the when the file is not found while trying to retrieve it
    '''
    pass

# CORE CLASSES
class InterfaceFile(object):
    '''
    A generic interface file used in SWMM
    '''

    def __init__(self, type, path):

        self.type = type.upper()
        if self.type not in FILE_TYPES:
            raise IncorrectFileType('{} is not an allowed file type.'.format(type))

        self.path = Path(path)
        self.name = self.path.name

    def __str__(self):
        save_types = ['RAINFALL', 'RUNOFF', 'RDII', 'HOTSTART', 'OUTFLOWS']
        use_types = ['INFLOWS']

        if self.type in save_types:
            s = 'SAVE {} "{}"'.format(self.type, self.path)
        else:
            s = 'USE {} "{}"'.format(self.type, self.path)

        return s

class Files(object):
    '''
    The FILES class from the SWMM .inp file
    '''

    def __init__(self):
        self.interface_files = []

    def __str__(self):
        s = '[FILES]\n'
        for f in self.interface_files:
            s += str(f) + '\n'
        s += '\n'
        return s

    @staticmethod
    def has_reached_section(line):
        '''
        Determines if the FILES section has been reached when reading the
        .inp file

        Parameters
        ----------
        line : str
            current line from the .inp file

        Returns
        -------
        bool
            True if [OPTIONS], else False
        '''
        if line.strip() == '[FILES]':
            return True
        else:
            return False

    def read_params(self, inp_file):
        '''
        Reads the OPTIONS parameters from the .inp file and records them
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

        # the cutoff to stop reading the params is a new line
        for line in inp_file:
            if line != '\n':
                temp = line.split()
                file_type = temp[1].strip()

                # the path may have a space in it, but it is always in double
                # quotes, so use a regular expression to find the path
                file_path = re.search('\"(.*)\"', line)
                file_path = file_path.group().strip('"')
                temp_file = InterfaceFile(file_type, file_path)
                self.interface_files.append(temp_file)
            else:
                break
        return line

    def add_file(self, type, file_path):
        '''
        Adds a file to the Files class

        Parameters
        ----------
        type: str
            The type of file to be added
        file_path: str
            The path to the file

        Returns
        -------
        None
        '''

        new_file = InterfaceFile(type, file_path)
        self.interface_files.append(new_file)

    def return_file(self, name, file_path = None):
        '''
        Returns a specific InterfaceFile

        Parameters
        ----------
        name: str
            The name of the file
        file_path: str
            The path of the file if specified

        Returns
        -------
        InterfaceFile
            The associated InterfaceFile object
        '''

        # return the first file in the list of interface files with the
        # correct name. if path is specified, return the file with the specified
        # name and path
        if file_path is None:
            file = [f for f in self.interface_files if f.name == name]
        else:
            temp_path = PurePath(file_path)
            file = [f for f in self.interface_files if f.name == name and f.path == temp_path]

        if len(file) == 0:
            raise FileNotFoundError('The file {} was not found'.format('name'))
        else:
            r_file = file[0]

        return r_file

if __name__ == '__main__':
    from pathlib import Path
    import difflib

    home_dir = Path('C:/C_PROJECTS/Python/swools')
    test_dir = home_dir / 'tests' / 'files_tests'


    # test 1
    files_1 = Files()

    test_1_file = test_dir / 'files_1.inp'
    with open(test_1_file, 'r') as test_1:
        for line in test_1:
            if Files.has_reached_section(line):
                line = files_1.read_params(test_1)

    out_1 = test_dir / 'outputs' / 'out_1.inp'
    with open(out_1, 'w') as out_file:
        out_file.write(str(files_1))

    # test 2
    files_2 = Files()

    test_2_file = test_dir / 'files_2.inp'
    with open(test_2_file, 'r') as test_2:
        for line in test_2:
            if Files.has_reached_section(line):
                line = files_2.read_params(test_2)

    out_2 = test_dir / 'outputs' / 'out_2.inp'
    with open(out_2, 'w') as out_file:
        out_file.write(str(files_2))

    # test 3
    files_3 = Files()

    test_3_file = test_dir / 'files_3.inp'
    with open(test_3_file, 'r') as test_3:
        for line in test_3:
            if Files.has_reached_section(line):
                line = files_3.read_params(test_3)

    out_3 = test_dir / 'outputs' / 'out_3.inp'
    with open(out_3, 'w') as out_file:
        out_file.write(str(files_3))
