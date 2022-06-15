from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in news/__init__.py
from news import __version__ as version

setup(
	name='news',
	version=version,
	description='News Website Design App',
	author='Hidayatali',
	author_email='hidayatmanusiya1@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
