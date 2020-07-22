# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 11:36:56 2020

@author: Jacob.Brown
"""


def flt_int(n):
    '''
    Determines if the value should be a float or an int
    Credit for this little trick goes to Mike Bannister

    Parameters
    ----------
    n : str
        a number to determine

    Returns
    -------
    float or int
        if an int, returns an int, else returns a float
    '''
    
    val = float(n)
    if val.is_integer():
        val = int(val)
    return val