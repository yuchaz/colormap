import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "colormap",
    version = "0.0.1",
    author = "Yu-Chia Chen",
    author_email = "yuchaz@uw.edu",
    description = ("colormap modules after https://github.com/BIDS/colormap"),
    license = "BSD",
    url = "https://github.com/yuchaz/colormap",
    packages=['colormap'],
    long_description=read('README.md'),
)

