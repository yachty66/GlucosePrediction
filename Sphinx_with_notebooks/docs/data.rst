Data Structures
===============

As this package predominantly deals with time series we have the following main
structure.

Time-series Container
_____________________

The idea is to bundle all datapoints that were measures during one
experiment.

.. autoclass:: glucose_ts.data.GlucoseTS



This data structure can be obtained from excel file that are produced in the
lab:

.. autofunction:: glucose_ts.data.read_glucose_ts

Manipulating Time-series
________________________

One common operation we need for making predictions is to cut the time-series.


.. autofunction:: glucose_ts.data.cut_time_series