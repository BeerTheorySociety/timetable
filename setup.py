from setuptools import setup

setup(name = 'timetable',
    version = '0.1',
    description = 'Python API for solving time-table problems (i.e. class scheduling)',
    url = 'https://github.com/BeerTheorySociety/timetable',
    packages = ['timetable'],
    install_requires=[
        'numpy',
        'scipy'
    ],
    zip_safe = False
)
