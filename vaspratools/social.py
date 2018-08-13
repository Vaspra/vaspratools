"""
Created by Doug Lawrence - Github: Vaspra

A collection of tools to help make social data scraping easier.
"""

from vaspratools import pagetree


def get_twitter_followers(username):
    """
    Takes a twitter usename and returns the number of followers that
    account has.
    """
    
    TWITTER_URL = 'https://twitter.com'
    
    # Remove '@' if it exists in the username
    username = username.replace('@','')
    
    url = TWITTER_URL + '/' + username
    tree = pagetree.get_tree(url)
    
    followers = ''
    try:
        node = tree.xpath(\
            '//a[@data-nav="followers"]')[0]
        
        followers = int(node.attrib['title'].strip().split(' ',1)[0]\
            .replace(',',''))
    except Exception as e:
        pass
    
    return followers


def get_twitch_followers(username):
    """
    Takes a twitch username and returns the number of followers that
    account has.
    """
    
    TWITCH_URL = 'https://www.twitch.tv'
    
    url = TWITCH_URL + '/' + username
    tree = pagetree.get_tree(url)
    
    followers = ''
    try:
        pre_node = tree.xpath(\
            '//span[contains(text(), "Followers")]/following-sibling::div/span')[0].text