"""
A series of commonly used formatting functions for clean, consistent data.
"""
    
from glob import glob                                                           
import cv2
import os

    
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


def convert_to_png(directory='./', locator='*', replace=True):
    """
    Attemtps to convert all image files in a folder into .png format.
    """
    
    files = glob(os.path.join(directory, locator))
    
    skip = 0
    success = 0
    fail = 0
    converted = []
    for f in files:
        if f.rsplit('.',1)[-1].lower() == 'png':
            skip += 1
            continue
        try:
            img = cv2.imread(f)
            cv2.imwrite(f[:-3] + 'png', img)
            success += 1
            converted.append(f)
        except:
            print('Failed to convert \'{}\''.format(f))
            fail += 1
            
    if replace:
        for f in converted:
            os.remove(f)
        
    print('\nRan conversion on {} files'.format(len(files)))
    print('Succeeded: {}  Failed: {}  Skipped: {}'\
          .format(success, fail, skip))
    
    
def remove_empty_images(directory='./', locator='*', verbose=False):
    """
    Removes any images in the specified directory which contain nothing but
    black.
    """
    
    print('\nCleaning \'{}\' of blank images'.format(directory))
    
    files = list(os.walk(directory))[0][2]
    print('Found {} files'.format(len(files)))
    
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
            if verbose: print('Skipped: \'{}\''.format(fp))
            skipped += 1
            continue
        
        if type(img) == None:
            if verbose: print('Skipped: \'{}\''.format(fp))
            skipped += 1
            continue

        # Test whether any of the pixels contain more than a zero
        try:
            is_empty = False if img.any() else True
        except AttributeError:
            if verbose: print('Skipped: \'{}\''.format(fp))
            skipped += 1
            continue
        
        # If the image contains data, skip it
        if not is_empty:
            if verbose: print('Skipped: \'{}\''.format(fp))
            skipped += 1
            continue
        
        # Otherwise, delete it
        os.remove(fp)
        if verbose: print('Removed: \'{}\''.format(fp))
        removed += 1
        
    print('Checked: {}  Removed: {}  Skipped: {}\n'\
          .format(checked, removed, skipped))
