#!/usr/bin/env python3

import urllib.request
import urllib.error
import re
import clipboard
    
class Posty():
    def __init__(self):
        self.regex_url_pattern = r"((([A-Za-z]{3,9}:(?:\/\/)?)(?:[-;:&=\+\$,\w]+@)?[A-Za-z0-9.-]+|(?:www.|[-;:&=\+\$,\w]+@)[A-Za-z0-9.-]+)((?:\/[\+~%\/.\w\-_]*)?\??(?:[-\+=&;%@.\w_]*)#?(?:[\w]*))?)"
        self.content = clipboard.paste()
        self.shortener_api_url = "http://tinyurl.com/api-create.php?url=" 
    
    def shorten(self):
        request_link = self.shortener_api_url + self.content
        
        if re.match(self.regex_url_pattern, self.content):
            try:
                raw_shortened_url = urllib.request.urlopen(request_link).read()
                decoded_shortened_url = raw_shortened_url.decode('utf-8')

                clipboard.copy(decoded_shortened_url)
                
                print('Copied to clipboard: ' + decoded_shortened_url)


            except urllib.error.HTTPError:
                print('An HTTP error ocurred.')
        else:
            print('Error: Invalid link.')

def main():
    Posty().shorten()