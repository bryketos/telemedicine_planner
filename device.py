'''
class Device: a telemedicine device to be assigned to patients during a clinical trial.
'''

from uuid import uuid4

class Device (object):
    '''A telemedicine device to be assigned to a patient. Must come from a parent device pool.'''
    def __init__(self, device_pool, device_id=uuid4()): #Default to a UUID4 unique ID.
        self.device_id = device_id
        self.device_pool = device_pool

    def get_device_id(self):
        return self.device_id


