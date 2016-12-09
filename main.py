'''
Simulate a clinical trial with telemedicine devices.
Initialize a device pool.
Recruit patients at a fixed rate.
Start weekly cycles: at the start of each week, recruit patients and assign devices for 8 weeks.
Run until you can't assign devices.
'''

import sys, os, argparse
from patient import Patient
from device_pool import Device_Pool

def print_report(current_week, number_of_patients, device_count):
    print "End of week {}. {} patients left to receive devices. {} devices currently in the pool.".format(current_week, number_of_patients, device_count)

def get_args():
    parser = argparse.ArgumentParser(description="Simulate a clinical trial with telemedicine devices.")
    parser.add_argument('-n', '--number_of_devices', type=int, default=40, help="Number of telemedicine devices to use.")
    parser.add_argument('-r', '--recruitment_per_week', type=int, default=5, help="Number of patients recruited per week.")
    parser.add_argument('-p', '--number_of_patients', type=int, default=200, help="Number of patients needed to run through trial.")
    parser.add_argument('-w', '--weeks_with_device', type=int, default=8, help="Number of weeks a patient needs to have the telemedicine device.")
    parser.add_argument('-v', '--verbose', action="store_true")
    return parser.parse_args()

def main ():
    args = get_args()
    print "Initializing trial."
    current_week = 0
    device_pool = Device_Pool(args.number_of_devices) #Instantiate pool of telemedicine devices.
    patient_pool = [] #Keep a list of the patients currently recruited.

    if args.verbose: print_report(current_week, args.number_of_patients, device_pool.get_device_count())

    patient_pool.extend([Patient(device_pool, weeks_with_device=args.weeks_with_device) for x in range(args.recruitment_per_week)]) #Updates the device pool automatically.
    args.number_of_patients -= args.recruitment_per_week

    while args.number_of_patients > 0: #While there are still patients to assign devices to
        current_week += 1
        for patient in patient_pool: patient.pass_week() #Automatically returns assigned devices to the pool if the patient is done.
        patient_pool.extend([Patient(device_pool, weeks_with_device=args.weeks_with_device) for x in range(args.recruitment_per_week)]) #Updates the device pool automatically.
        args.number_of_patients -= args.recruitment_per_week
        if args.verbose: print_report(current_week, args.number_of_patients, device_pool.get_device_count())
    
    print "Trial completed in {} weeks.\n".format([current_week])

if __name__ == "__main__": main() #You the main mang, mang.
