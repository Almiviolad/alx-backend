#!/usr/bin/env python3
""" Flask app module tha prints welcome message"""
from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def home() -> Any:
    """outputs welcome message"""
    return render_template('0-index.html')

if __name__ == '__main__':
    app.run()
