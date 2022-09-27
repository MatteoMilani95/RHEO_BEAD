"""Setuptools setup script."""
from setuptools import setup

setup(name='RHEO_BEAD',
      version='0.1',
      description='Analyze rheometer data ',
      url='https://github.com/MatteoMilani95/RHEO_BEADpy',
      author='Matteo Milani',
      author_email='matteo.milani@umontpellier.fr',
      license='GNU GPL',
      packages=['RHEO_BEAD'],
      install_requires=[
            'numpy',
            'scipy',
            'configparser',
            'pynverse',
            'IPython',
            'pandas'
	    'matplotlib'
      ], 
      #NOTE: other modules optionally used: emcee
      #      - emcee (VelMaps)
      #      - pandas (VelMaps)
      #      - astropy (PostProcFunctions)
      #test_suite='nose.collector',
      #tests_require=['nose'],
      zip_safe=False)
