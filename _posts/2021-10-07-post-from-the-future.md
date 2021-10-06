---
layout: post
title: A post from the future
tags:
  - professional-practice
description: >
  Example text
hero: /uploads/spaghetti.jpg
overlay: purple
published: true
---
Cum sociis natoque penatibus et magnis <a href="#">dis parturient montes</a>, nascetur ridiculus mus. *Aenean eu leo quam.* Pellentesque ornare sem lacinia quam venenatis vestibulum.
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