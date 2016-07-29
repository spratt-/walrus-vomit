#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
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
import jinja2
import webapp2
from advice import Advice

env = jinja2.Environment(loader=jinja2.FileSystemLoader("templates"))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("walrus.html")
        self.response.write(template.render())


class AdviceHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("advice.html")

        advice_query = Advice.query()
        advice_results = advice_query.fetch()
        advice_result = advice_results[0]

        data = {
            'content':advice_result.content,
            'source': advice_result.source
        }
        self.response.write(template.render(data))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/advice', AdviceHandler)

], debug=True)
