"""
Created for the vaspratools package on 12/07/2018
"""

from lxml import html
import requests

from raw_page_grab import raw_page_grab


def grab_images(search_terms, output_dir:str=None, img_count:int=1):
    """
    Takes an input list of strings (or a single string) and searches Google
    images for it. Downloads and stores the first hit in current directory,
    or to a provided output_dir (if given).
    """
    
    # If single term is provided, try to make it a single item list
    if type(search_terms) != list:
        allowed_types = [str, int, float]
        if type(search_terms) in allowed_types:
            search_terms = [str(search_terms)]
        else:
            raise TypeError('search_terms was an invalid type: %s'\
                            % type(search_terms))
        
    # Ensure the output_dir exists (if given)
    # MISSING#
    
    # For each search term given, run the search and download the images
    URL_HEAD = 'https://www.google.co.in/search?q='
    URL_TAIL = '&source=lnms&tbm=isch'
    
    for search_term in search_terms:
        query = search_term.replace(' ', '+')
        search_url = URL_HEAD + query + URL_TAIL
        
        page = raw_page_grab(search_url).decode()
        
        irc_mi_sections = page.split('<img class="irc_mi" src="', img_count)[1:]
        img_urls = []
        for section in irc_mi_sections:
            img_url = section.split('"',1)[0]
            img_urls.append(img_url)
        
    return img_urls
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    