"""
A series of commonly used formatting functions for clean, consistent data.
"""
    
from glob import glob                                                           
import cv2
import os
import numpy as np

    
def format_list_to_commastring(ls):
    """
    Converts and returns a list into a string, comma separated format.
    """
    
    string = ''
    for item in ls:
        string += str(item).strip() + ','
    string = string.strip(',')
    
    return string


def clean_string(string, allow_numbers=False):
    """
    Returns the string in all lowercase, only alphabetic and '_' format.
    """
    
    _ = string.strip().replace(' ','_').replace('-','_').lower()
    clean = ''
    
    if allow_numbers:
        for char in _:
            if char.isalpha() or char == '_' or char.isnumeric():
                clean += char
    else:
        for char in _:
            if char.isalpha() or char == '_':
                clean += char
                
    clean = clean.strip('_')\
        .replace('__','_').replace('__','_').replace('__','_')
            
    return clean


def convert_to_png(directory='./', locator='*'):
    """
    Attemtps to convert all image files in a folder into .png format.
    """
    
    files = glob(os.path.join(directory, locator))
    
    skip = 0
    success = 0
    fail = 0
    for f in files:
        if f.rsplit('.',1)[-1].lower() == 'png':
            skip += 1
            continue
        try:
            img = cv2.imread(f)
            os.remove(f)
            cv2.imwrite(f[:-3] + 'png', img)
            success += 1
        except:
            print('Failed to convert \'{}\''.format(f))
            fail += 1
        
    print('\nRan conversion on {} files'.format(len(files)))
    print('Succeeded: {}  Failed: {}  Skipped: {}'\
          .format(success, fail, skip))
    
    
def remove_empty_images(directory='./', locator='*'):
    """
    Removes any images in the specified directory which contain nothing but
    black.
    """
    
    print('Cleaning \'{}\' of blank images'.format(directory))
    
    files = list(os.walk(directory))[0][1]
    
    checked = 0
    removed = 0
    skipped = 0
    for f in files:
        
        fp = os.path.join(directory, os.path.basename(f))
        
        # Try to open the file using opencv
        try:
            img = cv2.imread(fp)
            checked += 1
        except:
            removed += 1
            continue

        # Test whether any of the pixels contain more than a zero
        is_empty = False if img.any() else True
        
        # If the image contains data, skip it
        if not is_empty:
            skipped += 1
            continue
        
        # Otherwise, delete it
        os.remove(fp)
        
    print('Checked: {}  Removed: {}  Skipped: {}'\
          .format(checked, removed, skipped))
        
        
        
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 