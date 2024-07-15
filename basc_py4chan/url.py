#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .templates import DOMAIN_4chan, TEMPLATE_4chan, LISTING_4chan, init_foolfukka
from .util import is_4chan

# 4chan URL generator. Inherit and override this for derivative classes  (e.g. 420chan API, 8chan/vichan API)
class Url(object):
    # default value for board in case user wants to query board list
    def __init__(self, board_name, domain: str = '4chan.org'):
        self._board_name = board_name

        # combine all dictionaries into self.URL dictionary
        if is_4chan(domain):
            self.URL = TEMPLATE_4chan
            self.URL.update({'domain': DOMAIN_4chan})
        else:
            TEMPLATE_foolfuuka, DOMAIN_foolfuuka = init_foolfukka(domain)
            self.URL = TEMPLATE_foolfuuka
            self.URL.update({'domain': DOMAIN_foolfuuka})

        self.URL.update({'listing': LISTING_4chan})
        

    # generate boards listing URL
    def board_list(self):
        return self.URL['listing']['board_list']

    # generate board page URL
    def page_url(self, page):
        return self.URL['api']['board'].format(
            board=self._board_name,
            page=page
            )

    # generate catalog URL
    def catalog(self):
        return self.URL['listing']['catalog'].format(
            board=self._board_name
            )

    # generate threads listing URL
    def thread_list(self):
        return self.URL['listing']['thread_list'].format(
            board=self._board_name
            )

   # generate archived threads list URL (disabled for compatibility)
    def archived_thread_list(self):
        return self.URL['listing']['archived_thread_list'].format(
            board=self._board_name
            )

    # generate API thread URL
    def thread_api_url(self, thread_id):
        return self.URL['api']['thread'].format(
            board=self._board_name,
            thread_id=thread_id
            )

    # generate HTTP thread URL
    def thread_url(self, thread_id):
        return self.URL['http']['thread'].format(
            board=self._board_name,
            thread_id=thread_id
            )

    # generate file URL
    def file_url(self, tim, ext):
        return self.URL['data']['file'].format(
            board=self._board_name,
            tim=tim,
            ext=ext
            )

    # generate thumb URL
    def thumb_url(self, tim):
        return self.URL['data']['thumbs'].format(
            board=self._board_name,
            tim=tim
            )

    # return entire URL dictionary
    @property
    def site_urls(self):
        return self.URL

"""
# 4chan Static Data (Unique to 4chan, needs implementation)
STATIC = {
    'flags': DOMAIN['static'] + '/image/country/{country}.gif',
    'pol_flags': DOMAIN['static'] + '/image/country/troll/{country}.gif',
    'spoiler': { # all known custom spoiler images, just fyi
        'default': DOMAIN['static'] + '/image/spoiler.png',
        'a': DOMAIN['static'] + '/image/spoiler-a.png',
        'co': DOMAIN['static'] + '/image/spoiler-co.png',
        'mlp': DOMAIN['static'] + '/image/spoiler-mlp.png',
        'tg': DOMAIN['static'] + '/image/spoiler-tg.png',
        'tg-alt': DOMAIN['static'] + '/image/spoiler-tg2.png',
        'v': DOMAIN['static'] + '/image/spoiler-v.png',
        'vp': DOMAIN['static'] + '/image/spoiler-vp.png',
        'vr': DOMAIN['static'] + '/image/spoiler-vr.png'
    }
}
"""
