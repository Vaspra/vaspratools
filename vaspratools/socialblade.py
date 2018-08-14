"""
Created by Doug Lawrence - Github: Vaspra

A collection of functions designed to obtain social media data from the
data scraping site 'Social Blade'.
"""

from vaspratools import pagetree


TWITTER_PRE_URL = 'https://socialblade.com/twitter/user/'
TWITCH_PRE_URL = 'https://socialblade.com/twitch/user/'
YOUTUBE_PRE_URL = 'https://socialblade.com/youtube/user/'


def get_twitter_data(username):
    """
    Returns a dictionary of Twitter user data, if the user can be found.
    """
    
    data_dict = {'url':'','followers':'','tweets':'','following':''}
    
    if not username:
        return data_dict
    
    url = TWITTER_PRE_URL + username
    tree = pagetree.get_tree(url)
    
    # Check whether the username actually exists
    if len(tree.xpath('//*[contains(text(), "Uh Oh! It seems that")]')) == 1:
        print('\t\'%s\' was not a valid Twitter username!' % username)
        return data_dict
    
    # Get the url
    try:
        twitter_url = tree.xpath('//a[contains(@href, "twitter.com/")]')[0]\
            .attrib['href']
    except:
        twitter_url = ''
        
    # Get the follower count
    followers = int(tree.xpath(\
        '//span[contains(text(), "Followers")]/following-sibling::span')[0]\
        .text.replace(',',''))
    
    # Get the channel tweets
    tweets = int(tree.xpath(\
        '//span[contains(text(), "Tweets")]/following-sibling::span')[0]\
        .text.replace(',',''))
        
    # Get the following count
    following = int(tree.xpath(\
        '//span[contains(text(), "Following")]/following-sibling::span')[0]\
        .text.replace(',',''))
    
    data_dict['url'] = twitter_url
    data_dict['followers'] = followers
    data_dict['tweets'] = tweets
    data_dict['following'] = following
    
    return data_dict


def get_twitch_data(username):
    """
    Returns a dictionary of Twitch user data, if the user can be found.
    """
    
    data_dict = {'url':'','followers':'','views':''}
    
    if not username:
        return data_dict
    
    url = TWITCH_PRE_URL + username
    tree = pagetree.get_tree(url)
    
    # Check whether the username actually exists
    if len(tree.xpath('//*[contains(text(), "Uh Oh! It seems that")]')) == 1:
        print('\t\'%s\' was not a valid Twitch username!' % username)
        return data_dict
    
    # Get the url
    try:
        twitch_url = tree.xpath('//a[contains(@href, "twitch.tv/")]')[0]\
            .attrib['href']
    except:
        twitch_url = ''
        
    # Get the follower count
    followers = int(tree.xpath('//p[contains(text(), " followers")]')\
        [0].text_content().split(' ')[1].replace(',',''))
    
    # Get the channel views
    views = int(tree.xpath('//p[contains(text(), " channel views")]')\
        [0].text_content().split(' ')[1].replace(',',''))
    
    data_dict['url'] = twitch_url
    data_dict['followers'] = followers
    data_dict['views'] = views
    
    return data_dict


def get_youtube_data(username):
    """
    Returns a dictionary of Twitter user data, if the user can be found.
    """
    
    data_dict = {'url':'','subscribers':'','views':'','uploads':''}
    
    if not username:
        return data_dict
    
    url = YOUTUBE_PRE_URL + username
    tree = pagetree.get_tree(url)
    
    # Check whether the username actually exists
    if len(tree.xpath('//*[contains(text(), "Uh Oh! It seems that")]')) == 1:
        print('\t\'%s\' was not a valid YouTube username!' % username)
        return data_dict
    
    # Get the url
    try:
        youtube_url = tree.xpath(\
            '//a[contains(@href, "youtube.com/channel/")]')[0]\
            .attrib['href']
    except:
        youtube_url = ''
        
    # Get the subscriber count
    subscribers = int(tree.xpath(\
        '//span[contains(text(), "Subscribers")]/following-sibling::span')[0]\
        .text.replace(',',''))
    
    # Get the channel views
    views = int(tree.xpath(\
        '//span[contains(text(), "Video Views")]/following-sibling::span')[0]\
        .text.replace(',',''))
        
    # Get the uploads count
    uploads = int(tree.xpath(\
        '//span[contains(text(), "Uploads")]/following-sibling::span')[0]\
        .text.replace(',',''))
    
    data_dict['url'] = youtube_url
    data_dict['subscribers'] = subscribers
    data_dict['views'] = views
    data_dict['uploads'] = uploads
    
    return data_dict