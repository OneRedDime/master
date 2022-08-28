import os
import subprocess as sp
from setuptools import setup, find_packages
from os import path


here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), 'r', encoding='utf-8') as f:
    long_description = f.read()

# Find man pages.
manfiles = []
for r, d, f in os.walk(path.join(here, 'docs', 'man')):
    manfiles = [path.join(r, f) for f in f if f.endswith('.1.gz')]
    break

install_requires = []
if 'DEBBUILD' not in os.environ:
    install_requires = [
        'argcomplete >= 1.0',
        'daily == 0.3.1',
        'icalendar',
        'parsedatetime == 2.5',
        'recurring-ical-events',
        'pyyaml',
    ]

version=sp.check_output(['git','describe','--tags'], text=True).strip()

setup(
    name='master',
    version=version,
    description='The command-line project manager.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='',
    author='Bo Cimino',
    author_email='ciminobo@protonmail.com',
    packages=find_packages(exclude=['tests']),
    license='GPLv2',
    python_requires='>3, <4',
    install_requires=install_requires,
    data_files=[
        ('/etc/bash_completion.d', ['etc/master_completion.sh']),
        ('/usr/share/man/man1', manfiles),
    ],
    entry_points={
        'console_scripts': [
            'master=master.main:main',
        ]
    },
)
