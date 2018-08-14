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
    
    if not username:
        return
    
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
    except:
        pass
    
    return followers


def get_twitch_followers(username):
    """
    Takes a twitch username and returns the number of followers that
    account has.
    """
    
    """if not username:
        return
    
    TWITCH_URL = 'https://www.twitch.tv'
    
    url = TWITCH_URL + '/' + username
    tree = pagetree.get_tree(url)"""
    
    followers = ''
    
    return followers


def get_facebook_likes(username):
    """
    Takes a facebook username and returns the number of likes that
    account has.
    """
    
    if not username:
        return
    
    FACEBOOK_URL = 'https://www.facebook.com'
    
    url = FACEBOOK_URL + '/' + username
    tree = pagetree.get_tree(url)
    
    likes = ''
    
    try:
        likes = int(tree.xpath('//*[contains(text(), "people like this")]')\
            [0].text.split(' ',1)[0].replace(',',''))
    except:
        pass
    
    return likes
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    