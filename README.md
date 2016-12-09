# telemedicine_planner
Python application for the planning of a telemedicine-enabled clinical trial.
Author: Brian S. Cole, PhD
Copyright Brian S. Cole, 2016

run main.py from the command line to get a list of options.

E.g. to simulate a trial with 200 patients recruited at 5/week with just 40 devices assigned for 8 week blocks:

    $ python main.py -n 80 -p 200 -r 10 -w 8
    Initializing trial.
    Trial completed in [19] weeks.

Note: the reported number of weeks is the number of weeks until the last telemedicine devices *leave the pool*, not when the trial actually completes.  Add 8 weeks (or whatever your value of -w is, which is the number of weeks a patient needs to have the device).
