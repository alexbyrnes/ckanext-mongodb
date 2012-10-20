from setuptools import setup, find_packages
import sys, os

version = '0.2'

setup(
	name='ckanext-mongodb',
	version=version,
	description="MongoDB for CKAN",
	long_description="""\
	""",
	classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	keywords='mongodb, ckan',
	author='Alex Byrnes',
	author_email='alexbyrnes@gmail.com',
	url='https://github.com/alexbyrnes/ckanext-mongodb',
	license='',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	namespace_packages=['ckanext', 'ckanext.mongodb'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		# -*- Extra requirements: -*-
    "pymongo"
    ],
	entry_points=\
	"""
        [ckan.plugins]
    mongodb=ckanext.mongodb.mongo_mapper:MongoMapper
    """,
)
