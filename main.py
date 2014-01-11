#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

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

@app.route('/contact/')
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)
