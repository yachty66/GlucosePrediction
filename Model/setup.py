#!/usr/bin/env python
import setuptools


with open("README.rst", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
      name='glucose_ts',
      version='0.0.1',
      description='Glucose Timeseries',
      author='Christoph Lange',
      author_email='christoph.lange@tu-berlin.de',
      long_description=long_description,
      long_description_content_type='text/x-rst',
      packages=setuptools.find_packages(),
      install_requires=[
            # we don't really need it for the package, but things can get messy
            # without specifying it here
            'jupyter',
            'openpyxl',
            'pandas',
            'scikit-learn',
            'scipy',
            'seaborn',
            'tensorflow',
            'tensorflow_probability',
            'numpy==1.19.5'
      ],
      python_requires='>=3.6',
)
