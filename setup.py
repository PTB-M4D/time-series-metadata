import setuptools

from time_series_metadata import __version__ as version

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    metadata_version="2.1",
    name="time_series_metadata",
    version=version,
    author="Maximilian Gruber, Björn Ludwig , Bang Xiang Yong , Benedikt Seeger",
    author_email="bjoern.ludwig@ptb.de",
    description="This package provides a Python implementation of a metadata scheme "
    "for time-series with measurement uncertainties.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PTB-M4D/time-series-metadata",
    download_url="https://github.com/PTB-M4D/time-series-metadata/releases/download/"
    "v{0}/time-series-metadata-{0}.tar.gz".format(version),
    packages=setuptools.find_packages(exclude=["tests"]),
    keywords="metadata time-series uncertainty metrology",
    project_urls={
        "Documentation": "https://time-series-metadata.readthedocs.io/en/v{}/".format(
            version
        ),
        "Source": "https://github.com/PTB-M4D/time-series-metadata/tree/v{}/".format(
            version
        ),
        "Tracker": "https://github.com/PTB-M4D/time-series-metadata/issues",
    },
    classifiers=[
        "Topic :: Utilities",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later ("
        "LGPLv3+)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
        "Typing :: Typed",
    ],
    python_requires=">=3.7",
)
