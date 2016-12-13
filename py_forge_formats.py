#!/usr/bin/python
#
# /a/src/web/forge/forge_python_script/py_forge_formats.py
#
# Implement a Python wrapper around the Forge calls to
# authenticate an app and query the file formats currently
# supported by the translation processes.
#
# This script replaces and improves on the previous
# forgeauth and forgeformats Unix shell cURL scripts
# documented in
#
# http://thebuildingcoder.typepad.com/blog/2016/10/forge-intro-formats-webinars-and-fusion-360-client-api.html#3
#
# Copyright (C) 2016 Jeremy Tammik
#
import os, requests, textwrap

verbose = False
url_authenticate = 'https://developer.api.autodesk.com/authentication/v1/authenticate'
url_formats = 'https://developer.api.autodesk.com/modelderivative/v2/designdata/formats'

def forge_authenticate_app( client_id, client_secret, verbose ):
  """Retrieve and return an authentication token
  for this app's API key and secret."""

  data = {
    'client_id' : client_id,
    'client_secret' : client_secret,
    'grant_type' : 'client_credentials',
    'scope' : 'data:read'
  }
  
  r = requests.post(url_authenticate, data=data)

  if verbose:
    print '\nForge authenticate call:'
    print '  Status:', r.status_code
    print '  Headers:', r.headers['content-type']
    print '  Content:', r.content

  if 200 == r.status_code:
    token = r.json()['access_token']
  else:
    token = None

  return token
  
def forge_formats( token, verbose ):
  """Retrieve and return the file formats currently
   supported by the translation processes."""

  headers = {'Authorization': 'Bearer ' + token}
  r = requests.get(url_formats, headers=headers)

  if verbose:
    print '\nForge formats call:'
    print '  Status:', r.status_code
    print '  Headers:', r.headers['content-type']
    print '  Content:', r.content

  if 200 == r.status_code:
    formats = r.json()['formats']
  else:
    formats = None

  return formats

def jprettyprint(formats):
  "Prettyprint the JSON file format list returned by Forge."
  keys = formats.keys()
  keys.sort()
  return '\n'.join( ['  ' + key + ': '
    + textwrap.fill( ', '.join( formats[key] ), subsequent_indent='    ')
      for key in keys] )

def main():
  """Authenticate ourselves with Forge and
  list the file formats currently supported."""
  
  # Retrieve my Forge app credentials stored in
  # system environment variables.
  
  client_id = os.environ['FORGE_CLIENT_ID']
  client_secret = os.environ['FORGE_CLIENT_SECRET']

  # Authenticate the app and retrieve a
  # time limited access token.
  
  token = forge_authenticate_app(
    client_id, client_secret, verbose )
  
  if verbose: print 'token:', token

  # Retrieve list of currently supported
  # translation file formats.
  
  formats = forge_formats( token, verbose )
  
  # Present the results in a human readable manner.
  
  # s = json.dumps(formats, indent=2, sort_keys=True) # not so nice
  s = jprettyprint(formats) # nicer
  s = s.replace('\.\d+$', '.NNN')
    
  print len(formats), 'Forge output formats:'
  print s
  
if __name__ == "__main__":
  main()
