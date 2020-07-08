import setuptools

from time_series_metadata import __version__ as version

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="time_series_metadata",
    version=version,
    author="Maximilian Gruber, Björn Ludwig , Bang Xiang Yong , Benedikt Seeger",
    author_email="bjoern.ludwig@ptb.de",
    description="This package provides a Python implementation of a metadata scheme "
    "for time-series with measurement uncertainties.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PTB-PSt1/time-series-metadata",
    packages=setuptools.find_packages(),
    keywords="metadata time-series uncertainty metrology",
    classifiers=[
        "Topic :: Utilities",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
        "Typing :: Typed",
    ],
    python_requires=">=3.5",
)
