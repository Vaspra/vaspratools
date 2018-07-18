# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 11:50:37 2018
@author: Doug

Saves an image from a url to disk.
"""

import os as _os
import urllib.request as _req


def save(url:str, filename:str='', path:str=_os.getcwd()):
    """
    Saves the img from the URL to either the current working directory, or
    a provided 'path' argument.
    """
    
    if not path.endswith('/') or not path.endswith('\\'):
        path = str(path + '/')
        
    if not _os.path.exists(path):
        _os.makedirs(path)
        
    if not filename:
        filename = str(hash(url)) + '.jpg'
        
    filepath = _os.path.join(path, filename)
        
    _req.urlretrieve(url, filepath)