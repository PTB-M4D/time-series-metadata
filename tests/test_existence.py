import pytest

from time_series_metadata.scheme import MetaData


@pytest.fixture
def metadata():
    return MetaData(
        device_id="my_virtual_sensor",
        time_name="time",
        time_unit="s",
        quantity_names=("pressure_1", "pressure_2"),
        quantity_units=("Pa", "mPa"),
        misc="additional information",
    )


def test_member_calls(metadata):
    assert isinstance(metadata.get_quantity(), dict)
    assert isinstance(metadata.metadata, dict)
    assert isinstance(metadata.quantities, dict)
    assert isinstance(metadata.time, dict)
    assert metadata.misc
