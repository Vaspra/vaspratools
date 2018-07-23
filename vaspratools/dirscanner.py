"""
Created by Doug Lawrence - Github: Vaspra

A tool to scan a given base directory for directories and files. Capable of
getting all the files associated with extensions (such as images) for use in
other tasks.

! CURRENTLY INCOMPLETE ! - Missing features like get_children and parent.
"""

import os
import glob

from _dirscanner_directory import _Directory
from _dirscanner_file import _File


class Scan():
    """
    The main class object used in this tool. Upon creation, it analyses the
    tree of directories under the base_dir provided.
    
    Call tree.refresh() to reanalyse the tree.
    """
    
    def __init__(self, base_dir=os.getcwd()):
        
        if base_dir == os.getcwd():
            print('Scanned current working directory')
        
        self.base_dir = self._format_directory(base_dir)
        
        self._old_asset_dict = {}
        self._asset_dict = {}
        self.refresh()
        
        
    def refresh(self, block_comparison=False):
        """
        Refreshes the tree by initiating a new search through the base_dir.
        Compares changes prior after refreshing - blockable.
        """
        
        # Refresh the tree
        _ = self._asset_dict.copy()
        
        self._asset_dict.clear()
        changes = 0
        dirs = []
        files = []
        for target in glob.glob(self.base_dir + '**', recursive=True):
            if os.path.islink(target):
                raise Exception('Not built to handle links in tree:\n%s'\
                                % target)
                
            if os.path.isdir(target):
                target = self._format_directory(target)
                if target not in _:
                    changes += 1
                dirs.append(_Directory(target, self))
                
            elif os.path.isfile(target):
                if target not in _:
                    changes += 1
                files.append(_File(target, self))
                
            else:
                raise Exception('Unrecognised target type:\n%s'\
                                % target)
                
        for directory in dirs:
            self._asset_dict[directory.path] = directory
        for file in files:
            self._asset_dict[file.path] = file
            
    
        # Find the changes since last refresh
        if not block_comparison:
            if changes != 0:
                self._old_asset_dict = self._asset_dict
                print('%d changes since last refresh.' % changes)
            else:
                self._old_asset_dict = _
                print('No changes were encountered in the last refresh.')
                
                
    def get_files_of_type(self, extensions:list=[],\
                          img_search=False, return_objs=False):
        """
        Returns a list of paths of every unique file in the tree complying to
        the list of allowed extensions.
        
        Use img_search=True to return common image types (overrides extensions=).
        
        Use return_objs=True to return the file objects in the tree, rather
        than the path strings.
        """
        
        if img_search:
            extensions = ['.jpg', '.jpeg', '.png']
            
        elif not extensions:
            return
        
        _ = []
        for ext in extensions:
            if ext.startswith('.'):
                ext = ext[1:]
            _.append(ext.lower())
        extensions = _
        
        ret_paths = []
        ret_objs = []
        for path, obj in self._asset_dict.items():
            if obj.type == 'file' and obj.extension:
                if obj.extension.lower() in extensions:
                    ret_paths.append(obj.path)
                    ret_objs.append(obj)
                    
        if return_objs:
            return ret_objs
        else:
            return ret_paths
    
    
    def _format_directory(self, path:str):
        """
        Ensures the provided directory is of the form ..'\\example\\',
        ending in a backslash.
        """
        
        path = path.replace('/', '\\')
        if not path.endswith('\\'):
            path += '\\'
            
        return path
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        