'''
class Device_Pool: a pool of telemedicine devices to be assigned to patients.
'''

from uuid import uuid4
from collections import OrderedDict
from device import Device

class Device_Pool (object):
    '''Holds a number of telemedicine devices to be assigned to patients.
    Maintains a list of Device objects as well as a dictionary of which device is assigned to which '''
    def __init__(self, number_of_devices):
        self.devices = [Device(self) for x in xrange(number_of_devices)] #Instantiate device objects, with a default UUID4 id from the Device's constructor.
        self.device_assignments = OrderedDict() #Maintain an ordered dictionary of which patients are assigned which device.

    def get_device_count(self):
        return len(self.devices) #Return the length of the device pool as an integer.
        
    def assign_device(self, patient):
        '''Assign the next available device in the devices attribute, or raise an exception.'''
        if self.get_device_count() > 0: #Still have some devices left to assign.
            self.device_assignments[patient.get_patient_id()] = self.devices.pop() #Assign a device from the list of device objects.
        else:
            raise Exception("No devices left to assign!")
            #This is where code to add a queue for patients who are recruited but don't have a device yet would go.

    def return_device(self, patient, device):
        self.devices.append(device)
        if self.device_assignments.has_key(patient.get_patient_id()):
            del self.device_assignments[patient.get_patient_id()] #Will raise an KeyError if the patient ID isn't in the device assignment.
        else:
            pass #Or catch the KeyError.



        
