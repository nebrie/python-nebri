from setuptools import setup

setup(
    name='python-nebri',
    version='0.1.5',
    description="python-nebri is a simple and easy-to-use package to make nebri api requests from a python application.",
    packages=['nebri_client'],
    url='http://github.com/briem-bixly/python-nebri/',
    author='briem-bixly',
    install_requires=[
        'requests==2.7.0',
    ]
)