#!/usr/bin/env python3

import urllib.request
import urllib.error
import clipboard
    
class Posty():
    def __init__(self):
        self.content = clipboard.paste()
        self.shortener_api_url = "http://tinyurl.com/api-create.php?url=" 
    
    def shorten(self):
        request_link = self.shortener_api_url + self.content
        
        try:
            raw_shortened_url = urllib.request.urlopen(request_link).read()
            decoded_shortened_url = raw_shortened_url.decode('utf-8')

            print(decoded_shortened_url)

        except urllib.error.HTTPError:
            print('An error ocurred.')
            print('No internet connection or invalid link.')

if __name__=="__main__":
    Posty().shorten()