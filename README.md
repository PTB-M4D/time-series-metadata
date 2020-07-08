# time-series-metadata 

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

You can access previously provided metadata in several ways.

#### Read out metadata

You can access the whole metadata set or time and quantity metadata separately.
Quantity metadata can be either accessed for all quantities or individually via index
 or name.

```python
>>> vs_description.metadata
{'device_id': 'my_virtual_sensor', 'time_name': 'time', 'time_unit': 's', 'quantity_names': ['pressure'], 'quantity_units': ['Pa'], 'misc': None}
>>> vs_description.time
{'time_name': 'time', 'time_unit': 's'}
>>> vs_description.quantities
{'quantity_names': ('pressure_1', 'pressure_2'), 'quantity_units': ('Pa', 'mPa')}
>>> vs_description.get_quantity(1)
{'quantity_names': 'pressure_2', 'quantity_units': 'mPa'}
>>> vs_description.get_quantity(name="pressure_1")
{'quantity_names': 'pressure_1', 'quantity_units': 'Pa'}
```

## Maintainers

The package is developed and maintained at the "Physikalisch-Technische Bundesanstalt"
by [Maximilian Gruber](https://github.com/mgrub) and [Björn Ludwig](https://github.com/BjoernLudwigPTB).