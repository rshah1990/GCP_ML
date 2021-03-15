from setuptools import setup

REQUIRED_PACKAGES = ['sklearn','numpy','pandas','google-cloud-bigquery==1.22.0','six == 1.13.0']
#['sklearn','numpy','pandas','google-cloud-bigquery==1.22.0','six == 1.13.0']

setup(
    name='my_custom_code',
    version='0.1',
    install_requires=REQUIRED_PACKAGES,
    scripts=['scikit-predictor.py'])