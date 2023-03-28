#!/usr/bin/env python3
""" get_page function """

import requests
import redis


class Web:
    """ class web """
    def init(self):
        """ initialization """
        self._redis = redis.Redis()

    def get_page(self, url: str) -> str:
        """ uses the requests module to obtain the HTML content of a particular
        URL and returns it """
        # Check if URL is in cache
        content = self._redis.get(url)
        count_key = f"count:{url}"

        if content:
            # URL found in cache, increment the access count
            self._redis.incr(count_key)
            return content.decode('utf-8')

        # URL not found in cache, fetch the content from the server
        response = requests.get(url)
        content = response.content.decode('utf-8')

        # Store the content in cache with an expiration time of 10 seconds
        self._redis.setex(url, 10, content)

        # Increment the access count for the URL
        self._redis.incr(count_key)

        return content
