import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "hello",
    version = "0.2.0",
    author = "Fabricio Leotti",
    author_email = "fabricio.leotti@gmail.com",
    description = ("A demonstration of a simple hello-world python application using Flask"),
    license = "BSD",
    keywords = "example flask hello",
    url = "http://www.hellopython.com",
    long_description=read('README'),
    classifiers=[
        "Development Status :: Beta",
        "Topic :: Demonstration",
    ],
)