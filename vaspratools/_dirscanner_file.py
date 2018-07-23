# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 14:15:44 2018

@author: Doug
"""

from _dirscanner_target import _Target


class _File(_Target):
    """
    A descendant of the _Target class, this represents an endpoint file, in
    contrast to a directory.
    """
    
    def __init__(self, path, tree):
        
        _Target.__init__(self, path, tree)
        self.type = 'file'
        
        
    @property
    def extension(self):
        """
        Returns the file's extension.
        """
        pass
    @extension.getter
    def extension(self):
        if '.' not in self.path:
            return None
        else:
            return self.path.rsplit('.', 1)[-1]
        
        
    @property
    def name(self):
        """
        Returns the file's name.
        
        Use ignore_extension=True to return the extensionless filename.
        """
    @name.getter
    def name(self, ignore_extension=False):
        name = self.path.split('\\')[-1]
        if ignore_extension and '.' in name:
            name = name.rsplit('.', 1)[0]
        return name
            