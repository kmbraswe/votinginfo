# Copyright 2016 Google Inc.
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

import webapp2
import jinja2
import os


the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

# other functions should go above the handlers
def get_meme_url(meme_choice):
    if meme_choice == 'old-class':
        url = 'https://upload.wikimedia.org/wikipedia/commons/4/47/StateLibQld_1_100348.jpg'
    elif meme_choice == 'college-grad':
        url = 'https://upload.wikimedia.org/wikipedia/commons/c/ca/LinusPaulingGraduation1922.jpg'
    elif meme_choice == 'thinking-ape':
        url = 'https://upload.wikimedia.org/wikipedia/commons/f/ff/Deep_in_thought.jpg'
    elif meme_choice == 'coding':
        url = 'https://upload.wikimedia.org/wikipedia/commons/b/b9/Typing_computer_screen_reflection.jpg'
    return url

# the handler section
class EnterInfoHandler(webapp2.RequestHandler):
    def get(self):  # for a get request
        welcome_template = the_jinja_env.get_template('templates/welcome.html')
        a_variable_dict = {"greeting": "Howdy",
                           "adjective": "amazing"
        }
        self.response.write(welcome_template.render(a_variable_dict))

    def post(self):
        self.response.write("A post request to the EnterInfoHandler")


class ShowMemeHandler(webapp2.RequestHandler):
    def get(self):
        results_template = the_jinja_env.get_template('templates/results.html')
        the_variable_dict = {"line1": "If Cinderella's shoe was a perfect fit",
        "line2": "Why did it fall off?",
        "img_url": "https://i.imgflip.com/vzzhn.jpg"}
        self.response.write(results_template.render(the_variable_dict))

    def post(self):
        results_template = the_jinja_env.get_template('templates/results.html')
        meme_choice = self.request.get('meme-type')
        meme_first_line = self.request.get('user-first-ln')
        meme_second_line = self.request.get('user-second-ln')

        pic_url = get_meme_url(meme_choice)

        the_variable_dict = {"line1": meme_first_line,
                             "line2": meme_second_line,
                             "img_url": pic_url}
        self.response.write(results_template.render(the_variable_dict))



app = webapp2.WSGIApplication([
    ('/', EnterInfoHandler),
    ('/memeresult', ShowMemeHandler)
], debug=True)
