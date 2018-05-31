# -*- coding: utf-8 -*-
import urllib

class HtmlDownloader(object):
    

    def download(self, url):
        if url == None:
            return None
        
        response = urllib.request.urlopen(url)
        #The getcode() method returns the HTTP status code that was sent with the response, or None if the URL is no HTTP URL.
        if response.getcode != 200:
            return None
        
        return response.read()
    
