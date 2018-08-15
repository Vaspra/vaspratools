# -*- coding: utf-8 -*-
"""
Created on Wed Aug  15 14:35:24 2018
@author: Doug Lawrence - Github: Vaspra

Uses Google's API to obtain useful geo data.
"""

import requests as _requests
from time import sleep as _sleep


def get_latlng(place:str, iso6709_format=False):
    """
    Returns the geolocation of the location if there is a match from google.
    Returns in iso 6709 format if needed '+xx.xxx-xx.xxx/',
    but returns a float tuple by default.
    """
    
    url = 'https://maps.googleapis.com/maps/api/geocode/json'
    params = {'sensor' : 'false', 'address' : place}
    
    tries = 0
    success = False
    while tries < 20:
        
        r = _requests.get(url, params=params)
        results = r.json()['results']
        
        try:
            location = results[0]['geometry']['location']
            lat = location['lat']
            lng = location['lng']
            
            if iso6709_format:
                if lat >= 0:
                    lat_sign = '+'
                else:
                    lat_sign = ''
                
                if lng >= 0:
                    lng_sign = '+'
                else:
                    lng_sign = ''
                    
                geos = '%s%.3f%s%.3f/'\
                    % (lat_sign, lat,\
                       lng_sign, lng)
                success = True
            
            else:
                geos = (lat, lng)
                success = True
            
        except Exception:
            if iso6709_format:
                geos = ''
            else:
                geos = (None,None)
            
        if success:
            break
        
        _sleep(0.1)
        tries += 1
        
    if not success:
        print('Unable to find \'%s\' after %d tries' % (place, tries))
        
    return geos
        