"""
Created for the vaspratools package on 12/07/2018
"""

import time
import requests
import os

from selenium import webdriver



def grab_images(search_terms, output_dir:str=None, img_count:int=1, minimized=True):
    """
    Takes an input list of strings (or a single string) and searches Google
    images for it. Downloads and stores the first hit in current directory,
    or to a provided output_dir (if given).
    
    You MUST have Selenium installed, and the Chrome driver downloaded and
    added to your PATH, as described on the Selenium website for this to work.
    """
    
    # Google images header / footer
    URL_HEAD = 'https://www.google.co.in/search?q='
    URL_TAIL = '&source=lnms&tbm=isch#imgrc=_'

    # Setup Selenium (this will open an automated browser)
    driver = webdriver.Chrome()
    
    # Minimise the window to not be in the way unless specified not too
    if minimized:
        driver.minimize_window()
    
    # If single term is provided, try to make it a single item list
    if type(search_terms) != list:
        allowed_types = [str, int, float]
        if type(search_terms) in allowed_types:
            search_terms = [str(search_terms)]
        else:
            raise TypeError('search_terms was an invalid type: %s'\
                            % type(search_terms))
            
    # Define the output directory
    img_dir = os.getcwd()
    if output_dir:
        img_dir = os.path.join(img_dir, output_dir)
                          
    # Ensure the img directory exists
    if not os.path.exists(img_dir):
        try:
            os.makedirs(img_dir)
        except:
            raise Exception('Could not create directory: %s' % img_dir)
    
    # For each search term given, run the search
    for search_term in search_terms:
        
        search_term = search_term.replace('/',' ').replace('\\',' ')
        
        query = search_term.replace(' ', '+')
        search_url = URL_HEAD + query + URL_TAIL
        
        driver.get(search_url)
        time.sleep(0.2)
        
        img_thumbnail_nodes = driver.find_elements_by_xpath\
                                ('//img[@class="rg_ic rg_i"]')
        
        # Download each thumbnail
        obtained_urls = []
        successful_downloads = 0
        for i, node in enumerate(img_thumbnail_nodes):
            
            # Click on the thumbnail image node to expand it and wait
            node.click()
            time.sleep(0.8)
            
            # Get the large image node
            large_img_nodes = driver.find_elements_by_xpath\
              ('//img[@class="irc_mi" and @alt="Image result for %s"]' % search_term)
            
            large_img_url = None
            for large_img_node in large_img_nodes:
                url = large_img_node.get_attribute('src')
                if url not in obtained_urls:
                    obtained_urls.append(url)
                    large_img_url = url
                    break
            if not large_img_url:
                print('Found no large images when searching for %s (%d)' %\
                       (search_term, i))
                time.sleep(0.2)
                continue
            
            # Get the image url
            img_url = large_img_node.get_attribute('src')
            
            # Attempt download
            try:
                img = requests.get(img_url).content
                
                img_filetype = str('.' + img_url.rsplit('.',1)[-1])\
                                 .split('/',1)[0].split('\\',1)[0].split('?',1)[0]
                                 
                if img_filetype == '.com':
                    img_filetype = '.jpg'
                                 
                local_filename = str(search_term.replace(' ','_') +\
                                 str(successful_downloads) + img_filetype)
                
                with open(img_dir + local_filename, 'wb') as f:
                    f.write(img)
                print('Successfully downloaded: %s\nOUTPUT --> %s\n'\
                       % (img_url, local_filename))
                
                successful_downloads += 1
                
            except Exception as e:
                error = 'Could not download "%s":\n%s\n' % (img_url, e)
                print(error)
                continue
            
            if successful_downloads == img_count:
                break
                
    driver.close()
    
    
    
    
    
