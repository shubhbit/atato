import requests


class Booking(object):
    def __init__(self):
        self.booking_url = "https://restful-booker.herokuapp.com/booking"
    
    def create_booking(self, data):
        resp = requests.post(self.booking_url, json=data)
        return resp

    def get_booking(self, booking_id):
        get_url = "{0}/{1}".format(self.booking_url, booking_id)
        resp = requests.get(get_url)
        return resp

    def delete_booking(self, booking_id):
        headers = {"Authorization": "Basic YWRtaW46cGFzc3dvcmQxMjM="}
        delete_url = "{0}/{1}".format(self.booking_url, booking_id)
        resp = requests.delete(delete_url, headers=headers)
        return resp

