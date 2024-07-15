# 4chan API URL Subdomains
DOMAIN_4chan = {
    "api": "https://" + "a.4cdn.org",  # API subdomain
    "boards": "https://" + "boards.4chan.org",  # HTML subdomain
    "boards_4channel": "https://"
    + "boards.4channel.org",  # HTML subdomain of 4channel worksafe, but 4chan.org still redirects
    "file": "https://" + "i.4cdn.org",  # file (image) host
    #'file': 'https://' + 'is.4chan.org', # new, slower image host
    "thumbs": "https://" + "i.4cdn.org",  # thumbs host
    "static": "https://" + "s.4cdn.org",  # static host
}

# 4chan API URL Templates
TEMPLATE_4chan = {
    "api": {  # URL structure templates
        "board": DOMAIN_4chan["api"] + "/{board}/{page}.json",
        "thread": DOMAIN_4chan["api"] + "/{board}/thread/{thread_id}.json",
    },
    "http": {  # Standard HTTP viewing URLs
        "board": DOMAIN_4chan["boards"] + "/{board}/{page}",
        "thread": DOMAIN_4chan["boards"] + "/{board}/thread/{thread_id}",
    },
    "data": {
        "file": DOMAIN_4chan["file"] + "/{board}/{tim}{ext}",
        "thumbs": DOMAIN_4chan["thumbs"] + "/{board}/{tim}s.jpg",
        "static": DOMAIN_4chan["static"] + "/image/{item}",
    },
}

# 4chan API Listings
LISTING_4chan = {
    "board_list": DOMAIN_4chan["api"] + "/boards.json",
    "thread_list": DOMAIN_4chan["api"] + "/{board}/threads.json",
    "archived_thread_list": DOMAIN_4chan["api"] + "/{board}/archive.json",
    "catalog": DOMAIN_4chan["api"] + "/{board}/catalog.json",
}

# --------------------------------------------------------------------------------

# foolfuuka (archives are based on this chan framework) API URL Subdomains
DOMAIN_foolfuuka = {
    "api": "https://" + "{domain}/_/api/chan",  # API subdomain
    "main": "https://" + "{domain}", # main domain for getting everything
}

# foolfuuka API URL Templates
TEMPLATE_foolfuuka = {
    "api": {  # URL structure templates
        "index": DOMAIN_foolfuuka["api"] + "/index?board={board}&num={page}",
        "thread": DOMAIN_foolfuuka["api"] + "/thread?board={board}&num={thread_id}",
        "post": DOMAIN_foolfuuka["api"] + "/post?board={board}&num={page}"
    },
    "http": {  # Standard HTTP viewing URLs
        "board": DOMAIN_foolfuuka["main"] + "/{board}/{page}",
        "thread": DOMAIN_foolfuuka["main"] + "/{board}/thread/{thread_id}",
    },
    "data": {
        "file": DOMAIN_foolfuuka["main"] + "/{board}/redirect/{media}",
        "thumbs": DOMAIN_foolfuuka["main"] + "/files/{board}/thumb/{media}",
    },
}

def init_foolfukka(domain: str):
    import string

    class FormatDict(dict):
        def __missing__(self, key):
            return "{" + key + "}"
    
    formatter = string.Formatter()

    for key in DOMAIN_foolfuuka:
        DOMAIN_foolfuuka[key] = DOMAIN_foolfuuka[key].format(domain=domain)
    
    for top_key in TEMPLATE_foolfuuka.keys():
        for low_key in TEMPLATE_foolfuuka[top_key]:
            # partial formatting of the template
            mapping = FormatDict(domain=domain)
            TEMPLATE_foolfuuka[top_key][low_key] = formatter.vformat(TEMPLATE_foolfuuka[top_key][low_key], (), mapping)

    return TEMPLATE_foolfuuka, DOMAIN_foolfuuka