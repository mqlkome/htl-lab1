"""
A Flask server that presents a minimal browsable interface for the Olin course catalog.

author: Oliver Steele <oliver.steele@olin.edu>
date  : 2017-01-18
license: MIT
"""

import os

import pandas as pd
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

courses = pd.read_csv('./data/olin-courses-16-17.csv')


@app.route('/health')
def health():
    return 'ok'

@app.route('/')
def home_page():
    return render_template('index.html', areas=set(courses.course_area), contacts=set(courses.course_contact.dropna()))

@app.route('/area/<course_area>')
def area_page(course_area):
    return render_template('course_area.html', course_area= course_area, courses=courses[courses.course_area == course_area].iterrows())

@app.route('/course/<course_name>')
def course_page(course_name):
	return render_template('course_page.html', course_name = course_name, course=courses[courses.course_name == course_name].iterrows())
#@app.route('/professor/<contact>')
#def professor_page(contact):
#	return render_template('professor.html', professor=contact, courses=courses[courses.course_contact==contact].iterrows())

if __name__ == '__main__':
    app.run(debug=True)
