from setuptools import setup

version = '1.0.2'

setup(
    name='beancount-importers',
    version=version,
    description="Personal beancount importers",
    author="jamatute",
    author_email="jmm@riseup.net",
    url="https://github.com/floco/beancount-importer",
    license='GPLv2',
    packages=['beancount_importers'],
    long_description=open('README.md').read(),
)
