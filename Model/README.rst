.. image:: https://readthedocs.org/projects/glucose-ts/badge/?version=latest
   :target: https://glucose-ts.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status


Glucose TS
==========

glucose_ts will help you to measure glucose concentrations closer to real time.
When you measure a glucose concentration with a enzyme based sensor you normally
have to wait for 5 - 10 minutes to get the glucose concentration. This projects
aims for telling you this value earlier.



.. image:: documentation/glucose_example.png
  :width: 800
  :alt: Glucose Timeseries

The blue curve is the actual measurements of the glucose sensor. The orange
curve is a logistics growth model that is fitted to the sensor data. This
model gets all the sensor measurements to fit a model. The idea would be
to get the final voltage much earlier.

To ease the usage this package tries to follow the guidlines of scikit-learn
estimators
https://scikit-learn.org/stable/developers/develop.html

.. code-block:: python

   import glucose_ts

   trained_model = glucose_ts.models.ExponentialDecay().fit(points_in_time, labels)

   trained_model.predict(points_in_time)

Features
--------
The package implements the following methods to explain and predict the glucose
sensor voltage signal

- exponential decay
- logistic growth
- generalized logistic growth

Installation
------------

Install the glucose package using `pip` by

.. code-block::

   cd glucose-prediction

   pip install -e .

Here we assume that you want to install the package in editable mode, because
you would like to contribute to it.

Contribute
----------

- Issue Tracker: https://git.tu-berlin.de/ch.lange/glucose-prediction/-/issues
- Source Code: https://git.tu-berlin.de/ch.lange/glucose-prediction

Support
-------

If you are having issues, please let us know.



CI Runner
_________

For using CI we need a [runner](https://docs.gitlab.com/runner/) that executes
all the tests. As we do not have a general CI runner for the group at this 
point in time we can do it on our local computer. In case you would like to 
use you local machine as a runner for Gitlab via Docker, you can do it this way:

#. [Install Docker](https://docs.docker.com/get-docker/)
#. Open your Gitlab Project in the browser
#. Go to **Settings > CI/CD** and expand the **Runners** section
#. In the section **Set up a specific Runner manually** under point 3 copy the
   registration token
#. Start your runner using the following command

   .. code-block::

      make start_gitlab_runner

#. Register the running runner via

   .. code-block::

      make register_gitlab_runner

Now you need to answer the questions for registering your runner.
(Please note that we choose the option where we store the config in a docker
volume)

For more details check the `Makefile`. 
A detailed version for registering your runner can be found
[here](https://docs.gitlab.com/runner/install/docker.html#option-2-use-docker-volumes-to-start-the-runner-container).