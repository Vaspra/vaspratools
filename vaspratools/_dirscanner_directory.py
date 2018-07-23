# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 14:15:44 2018

@author: Doug
"""

from _dirscanner_target import _Target


class _Directory(_Target):
    """
    A descendant of the _Target class, this represents a folder, in contrast
    to a file.
    """
    
    def __init__(self, path, tree):
        
        # Respect _Target's constructor
        _Target.__init__(self, path, tree)
        
        # Declare variables
        self.tree = tree
        self.type = 'directory'
        
        # Do first scan for children
        self._children = self._get_children
        
        
    def _get_children(self):
        """
        Returns a list of the children stored under this directory.
        """
        pass
    
    
    @property
    def children(self):
        """
        A list of the children under this directory (read-only).
        """
        pass
    @children.getter
    def children(self):
        return self._get_children
    
    
    @property
    def name(self):
        """
        Returns the file's name.
        
        Use ignore_extension=True to return the extensionless filename.
        """
    @name.getter
    def name(self):
        if self._root == self.path:
            if '\\' not in self.tree._format_directory(self._root).\
                                    split('\\', 1)[0]:
                return self._root.split('\\')[0]
            
        name = self.path.rsplit('\\', 1)[0].rsplit('\\', 1)[-1]
        return name
    
    
    
    
    
    
    
    
    