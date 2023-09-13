#--------------------IMPORT--------------------#
from setuptools import setup

#--------------------CONFIGURATION--------------------#
setup(
    name='Assignment2PKG',
    version='0.0.1 (2023-09-21)',
    author='Derek Laister',
    author_email='dereklaister@iscool.com',
    description='Json standard library extension for encode and decode',
    install_requires=[
        'requests',
        'importlib-metadata; python_version == "3.8"',
    ],
)