#!/usr/bin/env python3
import functools
import requests
import redis

r = redis.Redis()


def cache(func):
    """
    Decorator that caches the result of a function call.

    Args:
        func (callable): The function to be cached.

    Returns:
        callable: The wrapped function.
    """
    @functools.wraps(func)
    def wrapper(url: str) -> str:
        cache_key = f"count:{url}"
        cached_content = r.get(cache_key)

        if cached_content:
            # Return the cached content
            return cached_content.decode("utf-8")

        # Call the original function
        content = func(url)

        # Cache the content and increment the count
        r.set(cache_key, content, ex=10)
        r.incr(cache_key)

        return content

    return wrapper


@cache
def get_page(url: str) -> str:
    """
    Fetches the HTML content of a given URL.

    Args:
        url (str): The URL to fetch the content from.

    Returns:
        str: The HTML content of the page.
    """
    response = requests.get(url)
    return response.text
