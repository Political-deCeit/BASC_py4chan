#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Utility functions."""

import re
import sys

#HTML parser compat fix for python 3.9 and onwards
if sys.version_info[0] == 3 and sys.version_info[1] >= 9:
    import html
    _parser = html 
else:
    # HTML parser was renamed in python 3.x
    try:
        from html.parser import HTMLParser
    except ImportError:
        from HTMLParser import HTMLParser

    _parser = HTMLParser()

def clean_comment_body(body):
    """Returns given comment HTML as plaintext.

    Converts all HTML tags and entities within 4chan comments
    into human-readable text equivalents.
    """
    body = _parser.unescape(body)
    body = re.sub(r'<a [^>]+>(.+?)</a>', r'\1', body)
    body = body.replace('<br>', '\n')
    body = re.sub(r'<.+?>', '', body)
    return body

#### URL PARSING ####

http_re = r"http(?:s)?:\/\/"

website_urls = [
    r"(boards\.(?:4chan|4channel)\.org)",
    r"(archive\.palanq\.win)",
    r"(desuarchive\.org)",
    r"(archived\.moe)",
    r"(archive\.4plebs\.org)",
    r"(warosu\.org)",
    r"(archiveofsins\.com)",
]

website_urls_with_slash = [
    f"{url}\/" for url in website_urls
]

board_re = r"([a-z]*)\/"
thread_re = r"thread\/([0-9]*)"
post_re = r"(\/?#[0-9a-z]*)?"
post_re2 = r"(\/[0-9a-z]*)?"

after_regex = f"{board_re}{thread_re}{post_re}{post_re2}"

all_board_regex = [f"{http_re}{url}{after_regex}" for url in website_urls_with_slash]

def match_chan_url(url: str):
    for regex in all_board_regex:
        if m := re.search(regex, url):
            return m
    return None


def get_4chan_url_parts(base_url):
    x = match_chan_url(base_url)
    if x:
        groups = [y for y in x.groups() if y is not None]
        return {
            "domain": groups[0],
            "board": groups[1],
            "thread_id": groups[2],
            # Remove # and p/q
            "post_id": int(groups[3][2:]) if "#" in base_url else None,
        }

def is_4chan(url):
    return bool(re.match(website_urls[0], url))