from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
	name='ckanext-mongodb',
	version=version,
	description="MongoDB for CKAN",
	long_description="""\
	""",
	classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	keywords='',
	author='Alex Byrnes',
	author_email='alexbyrnes@gmail.com',
	url='',
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
	# Add plugins here, eg
	# myplugin=ckanext.mongodb:PluginClass
    mongodb=ckanext.mongodb.mongo_mapper:MongoMapper
    """,
)
