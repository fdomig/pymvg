from setuptools import setup, find_packages
from codecs import open
from os import path

directory = path.abspath(path.dirname(__file__))

with open(path.join(directory, 'README.md'), encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='pymvg',
    version='0.0.1',
    description='Get departures from MVG (Munich Public Transport Service) static live website',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Franziskus Domig',
    author_email='fdomig@gmail.com',
    url='https://github.com/fdomig/pymvg',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
    ],
    install_requires=['requests', 'requests_html'],
    packages=find_packages(exclude=['tests']),
)
