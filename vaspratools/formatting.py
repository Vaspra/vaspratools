"""
A series of commonly used formatting functions for clean, consistent data.
"""
    
from glob import glob                                                           
from cv2 import imread, imwrite
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
            img = imread(f)
            imwrite(f[:-3] + 'png', img)
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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    