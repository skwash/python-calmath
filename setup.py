from setuptools import setup
import os
import calmath

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

