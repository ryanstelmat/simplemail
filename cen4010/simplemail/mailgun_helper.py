#These functions are convenience functions for app-level mailgun request getting and posting.
import requests
import requests.auth
import os
import json

mailgun_key=os.getenv('mailgun_key')
domain ="simplemail.camlorn.net"
base_url="https://api.mailgun.net/v3/{0}/".format(domain)
auth=requests.auth.HTTPBasicAuth('api', mailgun_key)

def mget(endpoint, prepend=True):
    return requests.get(base_url+endpoint if prepend else endpoint, auth =auth)

def mpost(endpoint, data, prepend = True):
    """Data is a dict which is encoded to JSON by this function."""
    return requests.post(base_url+endpoint if prepend else endpoint, json=json.dumps(data), auth=auth)
