#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import subprocess
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/clients/')
def clients():
    return render_template('clients.html')

@app.route('/services/')
def services():
    return render_template('services.html')

if __name__ == "__main__":
    p = None
    try:
        if not os.getenv('COMPASSB', False):
            # TODO: In Python 3.0 use "with"
            p = subprocess.Popen(['compass', 'watch', 'static'])
            os.environ['COMPASSB'] = 'Running'
    except OSError:
        os.environ['COMPASSB'] = 'Failed'
    finally:
        try:
        	app.run(debug=True)
        except:
            if p:
                p.kill()
            raise
