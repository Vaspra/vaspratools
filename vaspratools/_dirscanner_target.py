

class _Target():
    """
    The base-class of a target, ie, a directory OR file. _Directory and
    _File classes derive from this class in this project.
    """
    
    def __init__(self, path, tree):
        
        self.path = path
        self.tree = tree
        self.type = None
        self._refresh()
        
        
    def _refresh(self):
        """
        Called when the tree refreshes. Re-calculates level and others.
        """
        
        self._root = self.tree.base_dir
        self._level = self.level
    
        
    @property
    def level(self):
        """
        The depth from the root directory (read-only).
        """
        pass
    @level.getter
    def level(self):
        return self._get_level()
    
    
    @property
    def parent(self):
        """
        The parent of this directory (read-only).
        Returns None if this is the root.
        """
        pass
    @parent.getter
    def parent(self):
        return self._get_parent()
    
    
    def _get_level(self):
        """
        Returns the level associated with this target, C:\\ = 0,
        C:\\example\\ = 1, C:\\example\\file = 2 etc
        """
        
        splits = self.path.split(self._root, 1)[-1].split('\\')
        level = -1
        for split in splits:
            if split:
                level += 1
        return level
        