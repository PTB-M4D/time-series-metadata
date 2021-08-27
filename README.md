# time-series-metadata

[![CircleCI](https://circleci.com/gh/PTB-M4D/time-series-metadata.svg?style=shield)](https://circleci.com/gh/PTB-M4D/time-series-metadata)
[![Documentation Status](https://readthedocs.org/projects/time-series-metadata/badge/?version=latest)](https://time-series-metadata.readthedocs.io/en/latest/)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3935860.svg)](https://doi.org/10.5281/zenodo.3935859)


## A metrologically enabled time-series metadata scheme

_time-series-metadata_ is a Python implementation of a metadata scheme for
time-series with measurement uncertainties. It is developed jointly by software
developers and researchers from
[Physikalisch-Technische Bundesanstalt](https://www.ptb.de) (Germany) and
[Institute for Manufacturing](https://www.ifm.eng.cam.ac.uk/) (UK) as part of the
joint European Research Project [EMPIR 17IND12 Met4FoF](https://met4fof.eu) and the
German research project [FAMOUS](https://famous-project.eu).

*time-series-metadata* is written in Python 3 and strives to run with
[all Python versions with upstream support](https://devguide.python.org/#status-of-python-branches).
Currently it is tested to work with Python 3.5 to 3.8.

## Scheme

The following image illustrates an abstract representation of a time series:

 ![time-series metadata scheme illustration](https://user-images.githubusercontent.com/50821607/80489031-8dac5000-895f-11ea-9b99-2add88c21d4b.png)
 
The scheme contains all metadata to interpret the actual time and quantity values.

It is comprised of a dictionary containing the following keys with (default) values of
the specified type:

```python
metadata = {
    "device_id": string (default: ""),
    "time_name": string (default: "time"),
    "time_unit": string (default: "om:second"),
    "quantity_names": string or list of strings (default: ""),
    "quantity_units": string or list of strings (default: ""),
    "misc": optional, any other data you want to provide (default: None),
}
```

## Example use

We illustrate the use of the scheme assuming you already have a project set up.

### Installation

First you need to install the scheme with the usual command into your project's
Python virtual environment:

```shell
pip install time-series-metadata
```

### Import scheme

Inside your project's code import the scheme at the top of your module.

```python
from time_series_metadata.scheme import MetaData
```

### Assign initial values

After importing the package you can make use of it and assign initial values.

```python
vs_description = MetaData(
    device_id="my_virtual_sensor",
    time_name="time",
    time_unit="s",
    quantity_names=("pressure_1", "pressure_2"),
    quantity_units=("Pa","mPa"),
    misc="additional information"
)
```

### Read out metadata

You can access the metadata as a whole or time and quantity metadata separately.
Quantity metadata can be either accessed for all quantities at once or individually via index
or name. If you do not specify name or index, the first's quantity metadata is returned.
This might be especially convenient, if there is only one quantity.

```python
>>> vs_description.metadata
{"device_id": "my_virtual_sensor", "time_name": "time", "time_unit": "s", "quantity_names": ["pressure_1", "pressure_2"], "quantity_units": ["Pa", "mPa"], "misc": None}
>>> vs_description.time
{'time_name': 'time', 'time_unit': 's'}
>>> vs_description.quantities
{'quantity_names': ('pressure_1', 'pressure_2'), 'quantity_units': ('Pa', 'mPa')}
>>> vs_description.get_quantity(1)
{'quantity_names': 'pressure_2', 'quantity_units': 'mPa'}
>>> vs_description.get_quantity(name="pressure_1")
{'quantity_names': 'pressure_1', 'quantity_units': 'Pa'}
>>> vs_description.get_quantity()
{'quantity_names': 'pressure_1', 'quantity_units': 'Pa'}
```

## Maintainers

The package is developed and maintained at the "Physikalisch-Technische Bundesanstalt"
by [Maximilian Gruber](https://github.com/mgrub) and [Björn Ludwig](https://github.com/BjoernLudwigPTB).
