---
layout: post
title: Hello World!
tags:
  - professional-practice
description: >
  Example text
hero: /uploads/spaghetti.jpg
overlay: purple
published: true
---
This is an example post I used to test out my shiny new blog!
{: .lead}

<!–-break-–>
<!--break-->

hdfghf
```py
from flask import url_for

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
```
**hihi**