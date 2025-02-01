# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 22:18:41 2025

@author: SambesiweSli
"""

# importing the necessary modules
import json
import requests

from pywebio.input import *
from pywebio.output import *
from pywebio.session import *

def get_fun_fact(_):
    # clearing the screen
    clear()
    
    # putting HTML content for the fun fact generator header
    put_html('<p align="left">'
             '<h2><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAACaElEQVRIS7WVWYhPURzHZyRLZHuQLUse0AgpXkzxJEsSsjyglJkkIokyEzMhRZZsJYpQ4kGyEw+yvMkgknWIBw+KlCXC5zOdW9fp/u9l6n/q0+/ec37nfH/3nN/53cqKMrfKMq9fUSTQngBmwSQYCQPhNzRDE1yC0/CjVKB5ApOZtD8smvehzxlcAteznEoJNOC8IUx4gz0JF+B+6BuFnQZzoF/oW43dHotkCSSLf8Z5PpwL25IVYBs6Z8Nh6AgrYHfaMRYwqrPwFcbAo7y9SY2N5fk2KDgebiVjaYHOdD6F3rAAjv/j4onbSh52whMYAS0HnxZYyvs+eAzDwWz5n9YO5+YQ4AzsmVjgIh1mzrIg5PgmqIPNUB+pZY3ptw4OQm0s8JaOvjAYXobFPmK7wifoFglkjVXjcxPuwehY4AsdZoJ8C4vlfcEqfEzNrbAr+PfAfgDFu8cCpqUH3QV8bk1zrl/rfJ//OmRPfwiYAQ9bs3rYlrtYE6UqFjhBxzxYA9uCQC/sWmgIkaV1e/LigW6B92HARNgIx2BhLGDuH4VnMBR+QZJZHrp57q02tSfCIbBMXAazry28gP4wF07FAh6u26TDIjgCfeAaDAsRxuY1HePgHSwHy4SX1W3+Hgv4bmRXIF0qLNk1YNYMCgqvsDvAfHchy8odsFRMAFO1pWUVOy+W6Wk2WOzOJ84Z1gXdDoU6gV+xN+1Xqlyvx6kxFa3l2vN4AJYES8l0sJK6jZYVK+meOIi8H85UnA+Atzuv+cNZDDeynIp+mR2YNBOmgAc3IERrtpjvV8Gi9rNUBEUCBcEXD5dd4A8h33wZkltP8QAAAABJRU5ErkJggg==" width="7%"/> Fun Fact Generator</h2>'
             '</p>'
    )
    
    # URL from where we will fetch the useless facts
    url = 'https://uselessfacts.jsph.pl/api/v2/facts/random?language=en'
    
    # creating variable to use GET request
    response = requests.get(url)
    
    # loading the request in a JSON file
    data = json.loads(response.text)
    
    # We will need 'text' from the data
    useless_fact = data['text']
    
    # Putting the fact in blue color and increasing the font size
    style(put_text(useless_fact), 'color:blue; font-size: 30px')
    
    # Put the 'Click me' button
    put_buttons(
        [dict(label='Click me', value='outline-success', color='outline-success')], 
        onclick=get_fun_fact
        )
    
# Driver function
if __name__ == '__main__':
    # Putting a heading 'Fun Fact Generator'
    put_html(
        '<p align="left">'
        '<h2><img src="https://media.geeksforgeeks.org/wp_content/uploads/20210720224119/MessagingHappyicon.png" width="7%"> Fun Fact Generator</h2>'
        '</p>'
    )
    
    # Hold session for a long time and put the 'Click Me' button
    put_buttons(
        [dict(label='Click me', value='outline-success', color='outline-success')],
        onclick=get_fun_fact
    )
    
    hold()