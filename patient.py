'''
Class patient: a patient with attributes for number of weeks the patient has had a kit.
'''

from uuid import uuid4

class Patient (object):
    '''Patient: a class to hold a telemedicine device from a device pool for a clinical trial.'''
    
    def __init__(self, device_pool, patient_id=uuid4(), weeks_with_device=8):
        if weeks_with_device <= 0:
            raise ValueError("weeks_with_device must be a positive integer")
        
        try:
            self.weeks_left = int(weeks_with_device)
        except:
            raise ValueError("Failed to coerce weeks_with_device value to integer.")

        try:
            self.patient_id = str(patient_id) #Coerce to a string from UUID class if no string ID is given.
        except:
            raise ValueError("Failed to coerce patient_id to string.")

        self.device_pool = device_pool #Save the device pool the device came from for later return of device.
        self.device = device_pool.assign_device(self) #Remove one device from the pool. The pool keeps track of the patient. The assign_device method returns a Device object reference.

    def pass_week(self, num_weeks=1):
        '''Let a week pass in the trial. If the patient is done with the trial, return the device. Default to passing 1 week.'''
        self.weeks_left -= num_weeks
        if self.weeks_left == 0:
            self.return_device()


    def return_device(self):
        destination = self.device_pool
        destination.return_device(self, self.device)
        self.device_id = None #Remove the device ID from the object's attributes.

    def get_weeks_left(self):
        return self.weeks_left

    def get_patient_id(self):
        return self.patient_id

    def get_assigned_device(self):
        return self.device #The device object has its own methods.
    
