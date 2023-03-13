#!/usr/bin/python3
import codecs
from setuptools import setup, find_packages

ILLUMINATIO_VERSION = "0.0.1"
ILLUMINATIO_DOWNLOAD = ('https://github.com/blackleakz/xsploit/tarball/' + ILLUMINATIO_VERSION)


def read_file(filename):
	"""
	Read a utf8 encoded text file and return its contents.
	"""
	with codecs.open(filename, 'r', 'utf8') as f:
		return f.read()

def read_requirements():
    with open('requirements.txt') as f:
        return f.readlines()


setup(
	name='oledssd1306_bpi_m2b',
	packages=[
		'examples'],
	package_data={
          'illuminatio.core': [
              'utils/*',
          ],
      },

	version=ILLUMINATIO_VERSION,
	description='oledssd1306_examples',


	license='MIT',
	author='blackleakz',
	author_email='blackleakz@luxuzleakz.de',
	url='https://github.com/blackleakz/xsploit',
	download_url=ILLUMINATIO_DOWNLOAD,
	keywords=['python3', 'xsploit', 'xst', 'MITM', 'wifi', 'arp spoof'],
	classifiers=[
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8',
		'Natural Language :: English',
	],

	install_requires= read_requirements(),

)
