from setuptools import setup, find_packages

import nebrios_client

setup(
    name='python-nebrios',
    version=nebrios_client.__version__,
    description=nebrios_client.__doc__,
    packages=find_packages(),
    url='http://github.com/briem-bixly/python-nebrios/',
    author='briem-bixly',
    include_package_data=True,
)