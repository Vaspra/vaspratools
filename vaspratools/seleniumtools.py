"""
Created by Doug Lawrence - Github: Vaspra

Various shortcuts for functionality with Selenium (specifically the Chrome
webdriver).
"""

from time import sleep, time


def scroll_to_bottom(driver, aggressive=False, aggr_wait=2):
    """
    Tells the driver to scroll to the bottom of the page.
    
    If the page is built to grow when you reach the bottom, set aggressive=True
    to continually scroll to the bottom until no more page extention is
    detected. The wait period for this can be set with aggr_wait.
    """
    
    # Get the initial page height
    h = driver.execute_script('return document.body.scrollHeight')
    
    # Scroll to the bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    if not aggressive:
        return
    
    # While aggressive, keep checking the page height. If it is different from
    # the last check, the page has extended and another scroll is required.
    t0 = time()
    dt = 0
    h = driver.execute_script('return document.body.scrollHeight')
    while dt < aggr_wait:
        sleep(0.1)
        dt = time() - t0
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        new_h = driver.execute_script('return document.body.scrollHeight')
        if new_h != h:
            t0 = time()
            h = new_h
            
    return