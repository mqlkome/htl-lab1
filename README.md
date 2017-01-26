# HtL Lab 1

This is a [Flask](http://flask.pocoo.org) server that implements a minimal web-based interface to the Olin College
2016-2017 course catalog. The course data is scraped from the <olin.edu> web site.


## Requirements

Python 3 is required to run this program.
You can test whether Python 3 is installed on your laptop by running `python3` in the bash (shell) command line.


## Setup

```
$ pip3 install flask
$ pip3 install pandas
```


## Usage

1. Run `$ python3 server.py`
2. Browse to <http://127.0.0.1:5000/>. (Running `server.py` also prints this URL.)


## Directory Structure

`server.py` is a web application, written using the Flask web framework.
See [here](http://flask.pocoo.org) for information on using Flask.
The application uses [pandas](http://pandas.pydata.org) to read the (CSV) data file,
and to filter the list of courses down to specific areas.

`templates/*.html` are the HTML templates that are served in response to HTTP requests to the server.
See the Flask documentation for more information about how this works.
These are Jinja templates; read [here](http://jinja.pocoo.org) for information about Jinja.

`data/` contains data files. This is currently limited to:

`data/olin-courses-16-17.csv` is [CSV](https://en.wikipedia.org/wiki/Comma-separated_values) file that lists the courses.
See the first line of the file itself for a description of its columns.

`scripts/scrape_course_catalog.py` scrapes the <olin.edu> web site to create the data file.
This script makes heavy use of [pandas](http://pandas.pydata.org).
You shouldn't need to run this – in fact, running it too often may look like an attack on the web site.
As with all web scraping, this script is fragile – a minor change to the olin.edu web design or URL format
could break it with no warning.


## Contributors

Written by Oliver Steele <oliver.steele@olin.edu>.
Modified by Mimi Kome <mimi@students.olin.edu>.

##Modifications made by Mimi:
Gave pages access to their titular data in server.py, so the page title in the tab and on the page display properly.

Made the pages visually and functionally clearer using html tags organized for a screen-reader or visual user.

Added a link to Bootstrap CSS, currently un-used other than to change the default fonts.

Added a "Back to Course Catalog Home" link below each item on the page.

Attempted to add a page for each course: partially successful, some work to do grabbing only the desired data. Probably learned how to fix this, but didn't implement the fix yet.

Courses can be viewed by instructor if an instructor's name is clicked on (on home or area pages). 



## Resources
CSS (mostly un-used) linked from https://www.bootstrapcdn.com/

## License

This code is made available under the MIT License
