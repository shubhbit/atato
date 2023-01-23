import pytest
from atato.task3.app.booking import Booking


@pytest.fixture
def booking_client():
    if not hasattr(pytest, "test_data"):
        pytest.test_data = {
            "firstname": "Jim",
            "lastname": "Brown",
            "totalprice": 111,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast",
        }
    booking = Booking()
    yield booking
    del booking
    del pytest.test_data
