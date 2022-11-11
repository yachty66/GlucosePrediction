Experiments
___________


Procedures to setup the Rasberry Pi
***********************************

Just to mention it, the current setup is not well documented, but let
us start here. When switching on the Raspberry Pi we need to ssh to the
address ``130.149.148.195``. Then we need to execute the following
commands.

.. code-block::

   cd glucose_system
   nohup python glucosesystem_server.py &
   nohup python X_MeasureAllTheTime.py &
   python glucosesystem_client_Setup.py


For the question about the port, you may choose ``"/dev/ttyACM0"``
If you try it in this order, it might work.

Glucose Measurement in Batch Cultivation
****************************************

* 4 reactors
* 4 samples per hour

.. image:: images/bo.png
  :width: 1000
  :alt: Glucose Timeseries



Callibration Standards
**********************

* putting everything in a thermal block and measure on 37 degrees
* initialization finished at 16:20
* basline on 37 degrees 1010 mV
* heat up the test solution 2 minutes on the thermal block
* start with 2.5 g/L
* afterwards we go down and measure 1.25, 1, 0.75, 0.5, 0.4, 0.3, 0.2, 0.1,
    0 g / L
* then we did a second round of measurements to check if the sensors behavior
    is stable over time



Callibration Standards 9th of June
***********************************

* started initializing at 11 a.m.
* put it in 2.5 g / L for one hour
* at 12 p.m we changed it to 5 g / L
* 37.2 degree celsius
* Start all time data ``nohup python X_MeasureAllTheTime.py &``
* At 2:32 we are already down to 658 mV
* put sensor in buffer at 2:33 p.m.

* last standard is 1 g / L at 0:55
