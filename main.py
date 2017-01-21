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
import webapp2
import random


def getRandomfortune():
    #Make list of possible fortunes
    fortunes =[
        'I see much code in your future.',
        'Consider eating more fortune cookies.',
        'You have tamed the mighty python. Now you much free it onto the great spiders web!'
    ]
    index = random.randint(0, 2)
    
    return fortunes[index]

class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = '<h1>Fortune Cookie</h1>'
        
        fortune = '<strong>' + getRandomfortune() + '</strong>'
        fortune_paragraph = '<p>Your fortune:' + fortune + '</p>'
        
        
        luckynumber = random.randint(1, 100)
        num_sentence = 'Your lucky number: '+ '<strong>' + str(luckynumber) + '</strong>'
        num_paragraph = '<p>' + num_sentence + '</p>'
        
        cookie_again_button = '<button><a href=".">Another cookie please!</a></button>'
        
        content = header + fortune_paragraph + num_paragraph + cookie_again_button
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
