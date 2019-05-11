from setuptools import setup

VERSION = "0.2.2"

with open('README.rst', 'r') as f:
    long_description = f.read()

setup(
    name='pyiotjokepi',
    packages=['iotjokepi'],
    version=VERSION,
    long_description=long_description,
    description='',
    author='Dhanush HL',
    license = 'MIT',
    url='https://github.com/dazzHere/IOT-JOKE-PI',
    author_email='dhanushdazz@gmail.com',
    keywords=['iot', 'iot-joke-pi', 'iot-joke', 'iot-joker'],
    install_requires=['requests'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        "Programming Language :: Python :: 3"
    ]
)
