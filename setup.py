# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

# I wish there was a way to do this w/o having to put data files in
# package dir. Couldn't ever get data_files arg working correctly...


setup(
    name='cdk',
    version='1.0.9',
    description='Courseware Developement Kit based on asciidoc and deck.js',
    long_description=readme,
    author='Simeon Franklin',
    author_email='simeonf@gmail.com',
    url='https://github.com/twitter-university/cdk',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    include_package_data=True,
    entry_points = {'console_scripts': ['cdk = cdk:main', 'b64 = cdk.b64:run']},
    install_requires=['docopt', 'pygments'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: Apache Software License"
    ]
)
