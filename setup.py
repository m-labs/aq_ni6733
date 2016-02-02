#!/usr/bin/env python3.5

from setuptools import setup, find_packages
import sys
import os


if sys.version_info[:3] < (3, 5, 1):
    raise Exception("You need Python 3.5.1+")


setup(
    name="aq_ni6733",
    version="0.0",
    author="M-Labs / NIST Ion Storage Group",
    author_email="sb@m-labs.hk",
    url="http://m-labs.hk/artiq",
    description="ARTIQ NDSP for NI 6733",
    long_description=open("README.rst").read(),
    license="GPL",
    install_requires=["pydaqmx"],
    extras_require={},
    packages=find_packages(),
    namespace_packages=[],
    ext_modules=[],
    entry_points={
        "console_scripts": ["pxi6733_controller=aq_ni6733.pxi6733_controller:main"],
    }
)
