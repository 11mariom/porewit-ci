# -*- coding: utf-8 -*-

"""
    Setup porewit-ci package
"""

from setuptools import setup, find_packages
from pip.req import parse_requirements

setup(
    name="porewit-ci",
    version="0.0.0",
    license="MIT",

    description="dead simple Continous Integration system",

    author="Mariusz Kozakowski",
    author_email="11mariom@gmail.com",

    url="https://mariom.pl",

    packages=find_packages(),
    include_package_data=True,

    install_requires=list(x.name for x in parse_requirements("./requirements.txt", session=False)),

    classifiers=[
        'Development Status :: 1 - Planning',

        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',

        'License :: OSI Approved :: MIT License',

        'Topic :: Software Development :: Bug Tracking',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],

    keywords=[
        'porewit-pi', 'porewit',
        'ci', 'continuous integration',
        'git',
    ],

    entry_points={
        "console_scripts": [
            "porewit-ci=porewit.__main__:main"
        ]
    },

    test_suite='nose.collector',
    tests_require=['nose'],
)
