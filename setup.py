from setuptools import setup

VERSION = '0.1'

setup(
    name='datasette-sql-scraper',
    description='Experimental plugin for Datasette',
    author='Simon Willison',
    url='https://github.com/simonw/datasette-sql-scraper',
    license='Apache License, Version 2.0',
    version=VERSION,
    packages=['datasette_sql_scraper'],
    entry_points={
        'datasette': [
            'sql_scraper = datasette_sql_scraper'
        ]
    },
    install_requires=['datasette', 'vtfunc']
)
