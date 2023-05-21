# Automatically created by: scrapyd-deploy

from setuptools import setup, find_packages

setup(
    name         = 'gushige',
    version      = '1.0',
    packages     = find_packages(),
    entry_points = {'scrapy': ['settings = gushici.settings']},
    package_data = {'gushige': ['path/to/*.json']}
)
