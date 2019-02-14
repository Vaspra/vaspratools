# -*- coding: utf-8 -*-
"""
Created on Wed Aug  15 14:35:24 2018
@author: Doug Lawrence - Github: Vaspra

Uses Google's API to obtain useful geo data.
"""

import requests as _requests
import json as _json


def get_geolocation(location, key, return_req_content=False):
    """
    Calls the MAPQUEST Developer API to get the geolocation (iso-6709) of
    a specified (str) address / location.
    
    API key available from 'https://developer.mapquest.com/user/me/apps'
    once you have a free account setup, under 'Consumer Key'.
    """
    
    location = location.replace('\n', ' ')
    r = _requests.get('http://www.mapquestapi.com/geocoding/v1/address?key={}&location={}'.format(key, location))
    if r.status_code != 200:
        raise Exception('Request failed (status code: {})'.format(r.status_code))

    if return_req_content:
        return _json.loads(r.content)
    
    latlng_dict = _json.loads(r.content)['results'][0]['locations'][0]['displayLatLng']
    lat, lng = latlng_dict.values()
    string = ''
    for val in [lat, lng]:
        val = str(val)
        if not val.startswith('-'):
            val = '+' + val
        string += val
    string += '/'
    
    return string