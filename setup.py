#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Setup script for bezier-editor package.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="bezier-editor",
    version="0.1.1",
    author="Laurent Brisson",
    author_email="laurent.brisson@imt-atlantique.fr",
    description="Interactive Bezier Curve Editor with Streamlit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/bezier-editor",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "streamlit>=1.15.0",
        "numpy>=1.20.0",
        "matplotlib>=3.4.0",
        "pandas>=1.3.0",
    ],
    entry_points={
        "console_scripts": [
            "bezier-editor=bezier_editor.cli:main",
        ],
    },
)