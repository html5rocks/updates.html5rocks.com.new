#!/usr/bin/env python
#
# Copyright 2014 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import json
import logging
from datetime import datetime, timedelta
from google.appengine.ext import ndb
from google.appengine.api import urlfetch
from urlparse import urljoin
import os
import re

fundamentals_url = "https://developers.google.com/web/updates/%s"

class RedirectHandler(webapp2.RequestHandler):
  def get(self, path):
    
    path_part = ""
    
    if path[0:6] == "/page/":
      path_part = "pages/%s" % path[6:] 
    elif path[0:5] == "/tag/":
      path_part = "tags/%s" % path[5:] # keept the user on the home page
    else:
      path_part = path
    
    logging.info("Info: " + fundamentals_url % path_part)
    
    return self.redirect(fundamentals_url % path_part, permanent=True)

class RedirectRSSFeed(webapp2.RequestHandler):
    def get(self):
      newFeedURL = fundamentals_url % "rss.xml"
      self.redirect(newFeedURL, permanent=True)

class RedirectAtomFeed(webapp2.RequestHandler):
    def get(self):
      newFeedURL = fundamentals_url % "atom.xml"
      self.redirect(newFeedURL, permanent=True)

app = webapp2.WSGIApplication([
    ('/feeds/rss.xml', RedirectRSSFeed),
    ('/feeds/.*', RedirectAtomFeed),
    ('/(.*)', RedirectHandler),
    ('/', RedirectHandler)
], debug=True)
