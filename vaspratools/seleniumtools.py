"""
Created by Doug Lawrence - Github: Vaspra

Various shortcuts for functionality with Selenium (specifically the Chrome
webdriver).
"""

from time import sleep


def scroll_to_bottom(driver, aggressive=False):
    """
    Tells the driver to scroll to the bottom of the page.
    
    If the page is built to grow when you reach the bottom, set aggressive=True
    to continually scroll to the bottom until no more page extention is
    detected.
    """
    
    # Get the initial page height
    h = driver.execute_script('return document.body.scrollHeight')
    
    # Scroll to the bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    if not aggressive:
        return
    
    # While aggressive, keep checking the page height. If it is different from
    # the last check, the page has extended and another scroll is required.
    new_h = driver.execute_script('return document.body.scrollHeight')
    sleep(1)
    while new_h != h:
        h = new_h
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(2)
        new_h = driver.execute_script('return document.body.scrollHeight')
        
    return