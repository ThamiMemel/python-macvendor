"""A setuptools based setup module.
See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='macvendor',

    version='1.0.12',

    description='A Python Liberary and CLI Tool for Fiding Vendors of MAC Addresses',
    long_description=long_description,

    long_description_content_type='text/markdown',

    url='https://github.com/ThamiMemel/python-macvendor',

    author='Thami Memel',

    author_email='memelthami@gmail.com',

    classifiers=[ 
        'Development Status :: 5 - Production/Stable',
        'Operating System :: OS Independent ',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Telecommunications Industry',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Networking :: Monitoring :: Hardware Watchdog',


        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],

    keywords='MAC vendors register OUI',


 
    py_modules=["macvendor"],
    packages= ["macvendor"],
    package_data={'macvendor': ['data/*']},
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, <4',

    install_requires=['tabulate'],

    entry_points={
        'console_scripts': [
            'macvendor=macvendor:main',
        ],
    },

    project_urls={
        'Bug Reports': 'https://github.com/ThamiMemel/python-macvendor/issues',
        'Source': 'https://github.com/ThamiMemel/python-macvendor',
    },
)