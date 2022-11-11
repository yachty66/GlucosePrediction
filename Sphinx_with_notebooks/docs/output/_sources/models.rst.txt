Models
======

The package contains different models to capture the voltage signal of the
glucose sensor over time. The types of models that are included in the package
right now are the following.

.. contents:: Table of Contents
    :depth: 3

Exponential Decay
_________________

The model behind exponential decay is

.. math::

   V(t) = K + (A - K) \exp(- B t)

The three parameters are represented in the named tuple

.. autoclass:: glucose_ts.models.exponential_decay.ExpDParameter


In order to learn the parameters that are a good fit to your training data we
use the following estimator.

.. autoclass:: glucose_ts.models.ExponentialDecay
    :members:


Logistic Growth
_______________

The family of function we refer to as logistic growth models is described by

.. math::

    V(t) = A + \frac {K - A} { 1 + \exp( - B ( t - M ) ) }

The four parameters are represented in the named tuple

.. autoclass:: glucose_ts.models.logistic_decrease.LDParameter


In order to learn the parameters that are a good fit to your training data we
use the following estimator.

.. autoclass:: glucose_ts.models.LogisticDecrease
    :members:



Generalized Logistic Growth
___________________________

The formula behind the generalized exponential growth is very similar to the
last one.

.. math::

    V(t) = A + \frac {K - A} { (1 + \exp( - B ( t - M ))^{\frac 1 {\nu}}}

The :ref:`Logistic Growth` is a special case of this model for
:math:`\nu = 1` which breaks the symmetry of the curve.
The five parameter that are needed to characterize one specific growth curve
are stored in the following namedtuple:

.. autoclass:: glucose_ts.models.generalized_logistics.GLParameter

So learn a specific parameter set from training data we use the following
estimator.

.. autoclass:: glucose_ts.models.GeneralizedLogisticGrowth
    :members:


