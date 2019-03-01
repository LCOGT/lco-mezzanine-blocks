import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

NAME = 'lco-mezzanine-blocks'

VERSION = '0.9.5'

DESCRIPTION = """
A fork of https://github.com/renyi/mezzanine-blocks to make it work with Django 1.9+
A mezzanine flavored fork of django-flatblocks.
The goal of this project is to be able to easily create custom blocks of
text/HTML in the template, and can be editable via admin.
"""

setup(
    name=NAME,
    description=DESCRIPTION,
    long_description=README,
    version=VERSION,
    author='Edward Gomez',
    author_email='egomez@lco.global',
    url='https://github.com/LCOGT/lco-mezzanine-blocks',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['django','mezzanine'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
