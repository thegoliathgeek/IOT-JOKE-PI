import platform
from setuptools import setup

VERSION = "0.1.1"

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pyiotjokepi',
    packages=['iotjokepi'],
    version=VERSION,
    long_description=long_description,
    description='',
    author='Dhanush HL',
    url='https://github.com/dazzHere/IOT-JOKE-PI',
    author_email='dhanushdazz@gmail.com',
    keywords=['iot', 'iot-joke-pi', 'iot-joke', 'iot-joker'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        "Programming Language :: Python :: 3"
    ]
)
