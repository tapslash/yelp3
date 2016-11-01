from setuptools import find_packages
from setuptools import setup

setup(
    name='yelp3',

    version='1.0.0',

    description='Python implementation of the Yelp V3 Fusion API',

    url='https://github.com/af-inet/yelp3-python',

    author='David Hargat',

    author_email='davidmhargat@gmail.com',

    license='n/a',

    keywords='yelp',

    packages=find_packages(),

    install_requires=['six'],
)
