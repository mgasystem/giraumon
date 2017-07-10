# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='giraumon',
    version='0.1.0',

    description='Tools for developer to manage Mirounga Hosting Service',
    long_description=long_description,

    url='https://github.com/mgasystem/giraumon',

    author='Mirounga Team',
    author_email='info(@)mirounga.net',

    license='GPLv3',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='hosting development',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['click==6.6'],
    entry_points='''
        [console_scripts]
        giraumon=giraumon.cli:cli
    '''
)
