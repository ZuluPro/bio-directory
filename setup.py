#!/usr/bin/env python
from setuptools import setup, find_packages
import bio


def read_file(name):
    with open(name) as fd:
        return fd.read()

setup(
    name='bio',
    version=bio.__version__,
    description=bio.__doc__,
    long_description=read_file('README.rst'),
    author=bio.__author__,
    author_email=bio.__email__,
    url=bio.__url__,
    download_url=bio.__download__,
    include_package_data=True,
    packages=find_packages(),
    install_requires=read_file('requirements.txt'),
    license=bio.__licence__,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ]
)
