from setuptools import setup
import os
import calmath

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='calmath',
    description='Does simple calender math operations on date and datetime objects.',
    version=calmath.__version__,
    py_modules=['calmath'],
    author="Josh Hansen",
    author_email="josh@skwash.net",
    url="http://www.github.com/skwash/python-calmath",
    license="BSD"
)

