# -*- coding: utf-8 -*-
"""The module :mod:`time_series_metadata.scheme` contains the main class of the
package. It provides the Python implementation of the scheme.

This module contains the following class:

* :class:`MetaData`: Wrapper class for metrologically enabled time-series metadata

"""
from typing import Any, Dict, Optional, Tuple, Union


class MetaData:
    def __init__(
        self,
        device_id: str = "",
        time_name: str = "time",
        time_unit: str = "om:second",
        quantity_names: Union[str, Tuple[str, ...]] = "",
        quantity_units: Union[str, Tuple[str, ...]] = "",
        misc: Optional[Any] = None,
    ):
        """Wrapper class for metrologically enabled time-series metadata

        Parameters
        ----------
            device_id : str (default: "")
            time_name : str (default: "time")
            time_unit : str (default: "om:second")
            quantity_names : str or list of str (default: "")
            quantity_units : str or list of str (default: "")
            misc : dict (default: None)
                other time series-specific descriptions
        """
        # Cast the potential strings to list of strings.
        if isinstance(quantity_names, str):
            quantity_names = (quantity_names,)
        if isinstance(quantity_units, str):
            quantity_units = (quantity_units,)

        # Assemble metadata.
        self._metadata = dict(locals())
        if "self" in self._metadata.keys():
            del self._metadata["self"]

        # Prepare keys for unified access.
        self._time_metadata_keys = ("time_name", "time_unit")
        self._quants_metadata_keys = ("quantity_names", "quantity_units")

    @property
    def time(self) -> Dict:
        """Return the time metadata

        Returns
        -------
        metadata : dict
            all time metadata key value pairs
        """
        return {key: self.metadata[key] for key in self._time_metadata_keys}

    @property
    def quantities(self) -> Dict:
        """Return all quantities metadata

        Returns
        -------
        metadata : dict
            all quantity metadata key value pairs
        """
        return {key: self.metadata[key] for key in self._quants_metadata_keys}

    @property
    def misc(self) -> Dict:
        """Return the additionally provided metadata

        Returns
        -------
        metadata : dict
            all misc metadata key value pairs
        """
        return self._metadata["misc"]

    @property
    def metadata(self) -> Dict:
        """Return the metadata as a whole

        Returns
        -------
        metadata : Dict
            the metadata dictionary as a whole
        """
        return self._metadata

    def get_quantity(self, index: int = 0, name: str = None) -> Dict:
        """Return the metadata for one of the quantities

        Parameters
        ----------
        index : int, optional
            Index of the quantity in the initial tuple (default = 0). If `name` is
            set, `index` is ignored.
        name : str, optional
            Name of the quantity. If `name` is set, `index` is ignored.

        Returns
        -------
        metadata : dict
            the metadata for the specified quantity
        """
        if name is not None:
            # Find the index of the desired quantity in the tuples.
            index = self.metadata["quantity_names"].index(name)
        return {key: self.metadata[key][index] for key in self._quants_metadata_keys}
