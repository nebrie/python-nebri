from setuptools import setup

setup(
    name='python-nebrios',
    version='0.1.4',
    description="python-nebrios is a simple and easy-to-use package to make nebrios api requests from a python application.",
    packages=['nebrios_client'],
    url='http://github.com/briem-bixly/python-nebrios/',
    author='briem-bixly',
    install_requires=[
        'requests==2.7.0',
    ]
)