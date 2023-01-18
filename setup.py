from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in orginfo/__init__.py
from orginfo import __version__ as version

setup(
	name="orginfo",
	version=version,
	description="Organization Information to define constants and use in application",
	author="Hephzibah Technologies Inc",
	author_email="david.alexander@hephzibahtech.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
