import pytest
from atato.task3.utils import *


class TestBooking:


    def test_booking_creation(self, booking_client):
        """
        test to verify booking creation
        """
       # I've hardcoded booking data from API site for the example purpose,
        # data generation could be set as a different method in utils
        booking_response = booking_client.create_booking(pytest.test_data)
        assert booking_response.status_code == 200
        response_json = booking_response.json()
        assert compare_json(pytest.test_data, response_json['booking'])

    def test_get_booking(self, booking_client):
        """
        test to verify that created booking can be fetched and verified
        """
        booking_response = booking_client.create_booking(pytest.test_data)
        booking_details = booking_client.get_booking(
            booking_response.json()['bookingid'])
        assert booking_details.status_code == 200
        booking_json = booking_details.json()
        assert compare_json(pytest.test_data, booking_json)

    def test_delete_booking(self, booking_client):
        """
        test to verify that created booking can be deleted
        and once deleted, can't be found again.
        """
        booking_response = booking_client.create_booking(pytest.test_data)
        booking_id = booking_response.json()['bookingid']
        booking_details = booking_client.delete_booking(booking_id)
        assert booking_details.status_code == 201
        deleted_booking = booking_client.get_booking(booking_id)
        assert deleted_booking.status_code == 404
