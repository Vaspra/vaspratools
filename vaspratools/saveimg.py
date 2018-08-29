# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 11:50:37 2018
@author: Doug

Saves an image from a url to disk. Capable of compressing the image, respecting
the original aspect ratio.
"""

import os as _os
from urllib.request import Request as _Request
from urllib.request import urlopen as _urlopen
import PIL.Image as _Image
from PIL.Image import BILINEAR as _BI


def save(url:str, filename:str='', path:str=_os.getcwd(), fit_to:tuple=None,\
         has_alpha=True, quality=95):
    """
    Saves the img from the URL to either the current working directory, or
    a provided 'path' argument.
    
    Supply a tuple of the form (int, int) as an argument to fit_to= to force
    the image to be resized (in pixels). This respects aspect ratio.
    """
        
    if has_alpha:
        ext = '.png'
    else:
        ext = '.jpg'
    
    if not url:
        print('No URL provided\nFilename provided: %s' % filename)
        return
    
    if not path.endswith('/') or not path.endswith('\\'):
        path = str(path + '/')
        
    if not _os.path.exists(path):
        _os.makedirs(path)
        
    if not filename:
        filename = str(hash(url)) + ext
        
    elif not filename.endswith(ext):
        if len(filename.split('.')[-1]) == 3 or\
           len(filename.split('.')[-1]) == 4:
               filename = filename.rsplit('.', 1)[0]
        filename += ext
        
    filepath = _os.path.join(path, filename)
        
    imgdata = _urlopen(_Request(url,\
        headers={'User-Agent': 'Mozilla/5.0'})).read()
    
    with open(filepath, 'wb') as f:
        f.write(imgdata)
        
    # Compress image if required
    if fit_to:
        
        assert len(fit_to) == 2,\
        'Argument: \'compress_to\' needs 2 integers'
        
        w = fit_to[0]
        h = fit_to[1]
        
        assert type(w) == int, 'compress_to[0] is not an int'
        assert type(h) == int, 'compress_to[1] is not an int'
        
        # Calculate the original aspect ratio
        img = _Image.open(filepath)
        img_w, img_h = img.size
        ar = img_w / img_h
        
        # If the width is dominantly large
        if w > (h * ar):
            new_w = h * ar
            new_h = h
        # If the height is dominantly large
        else:
            new_w = w
            new_h = w / ar
            
        new_size = (int(new_w), int(new_h))
            
        # Create the new image
        try:
            img = img.resize(new_size, resample=_BI)
        except OSError as e:
            print('Encountered OSError on "%s":\n%s' % (filename, e))
            return
        
        # Save the image as the same name
        if has_alpha:
            ext_arg = 'PNG'
        else:
            ext_arg = 'JPEG'
        img.save(filepath, ext_arg, optimize=True, quality=quality)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        