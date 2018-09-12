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
    except IndexError:
        twitter_url = ''
        
    # Get the follower count
    try:
        followers = int(tree.xpath(\
            '//span[contains(text(), "Followers")]/following-sibling::span')[0]\
            .text.replace(',',''))
    except IndexError:
        followers = ''
    
    # Get the channel tweets
    try:
        tweets = int(tree.xpath(\
        '//span[contains(text(), "Tweets")]/following-sibling::span')[0]\
        .text.replace(',',''))
    except IndexError:
        tweets = ''
        
    # Get the following count
    try:
        following = int(tree.xpath(\
            '//span[contains(text(), "Following")]/following-sibling::span')[0]\
            .text.replace(',',''))
    except IndexError:
        following = ''
    
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
    except IndexError:
        twitch_url = ''
        
    # Get the follower count
    try:
        followers = int(tree.xpath('//p[contains(text(), " followers")]')\
            [0].text_content().split(' ')[1].replace(',',''))
    except IndexError:
        followers = ''
    
    # Get the channel views
    try:
        views = int(tree.xpath('//p[contains(text(), " channel views")]')\
            [0].text_content().split(' ')[1].replace(',',''))
    except IndexError:
        views = ''
    
    data_dict['url'] = twitch_url
    data_dict['followers'] = followers
    data_dict['views'] = views
    
    return data_dict


def get_youtube_data(channel_id):
    """
    Returns a dictionary of Twitter user data, if the user can be found.
    """
    
    data_dict = {'url':'','subscribers':'','views':'','uploads':''}
    
    if not channel_id:
        return data_dict
    
    url = 'https://socialblade.com/youtube/channel/' + channel_id
    tree = pagetree.get_tree(url)
    
    # Check whether the username actually exists
    if len(tree.xpath('//*[contains(text(), "Uh Oh! It seems that")]')) == 1:
        print('\t\'%s\' was not a valid YouTube channel ID!' % channel_id)
        return data_dict
    
    # Get the url
    try:
        youtube_url = tree.xpath(\
            '//a[contains(@href, "youtube.com/channel/")]')[0]\
            .attrib['href']
    except:
        youtube_url = ''
        
    # Get the subscriber count
    try:
        subscribers = int(tree.xpath(\
            '//span[@id="youtube-stats-header-subs"]')[0]\
            .text.replace(',','').strip())
    except IndexError:
        subscribers = ''
    
    # Get the channel views
    try:
        views = int(tree.xpath(\
            '//span[@id="youtube-stats-header-views"]')[0]\
            .text.replace(',','').strip())
    except IndexError:
        views = ''
        
    # Get the uploads count
    try:
        uploads = int(tree.xpath(\
            '//span[@id="youtube-stats-header-uploads"]')[0]\
            .text.replace(',','').strip())
    except IndexError:
        uploads = ''
    
    data_dict['url'] = youtube_url
    data_dict['subscribers'] = subscribers
    data_dict['views'] = views
    data_dict['uploads'] = uploads
    
    return data_dict