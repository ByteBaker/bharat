from setuptools import setup, find_packages

long_description = open("README.md").read()

setup(
	name="bharat",
	version="0.1",
	author="Shraddha Kishan",
	author_email="shraddha.kishan@gmail.com",
	url="https://github.com/bytebaker/bharat",
	description="India states metadata",
	long_description=long_description,
	long_description_content_type="text/markdown",
	license="BSD",
	packages=find_packages(),
	include_package_data=True,
	install_requires=[],
	entry_points={},
	platforms=["any"],
	classifiers=[
		"Programming Language :: Python :: 3"
	],
)