.. MOOG_SCAT documentation master file, created by
   sphinx-quickstart on Thu Jun  1 16:03:25 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

**********
MOOG_SCAT
**********

Overview 
--------
``MOOG_SCAT`` is based on the LTE radiative transfer code MOOG developed by C. Sneden (1973).  It contains modifications that allow for the treatment of 
isotropic, coherent scattering in stars.  ``MOOG_SCAT`` employs a modified form of the source function and solves radiative transfer with a short 
charactersitics approach and an acclerated lambda iteration scheme.

.. toctree::
   :maxdepth: 2
   :caption: Installation and Build
   
   installation
   
.. toctree::   
   :maxdepth: 2
   :caption: LTE and SCAT Code Routines

   moog_scat_routines
   moog_lte_routines

.. toctree::
   :maxdepth: 1
   :caption: Code Reference Sites and Materials

   Changelog <changelog>
   GitHub Repository <https://github.com/jsobeck/MOOG_SCAT>
   Issues <https://github.com/jsobeck/MOOG_SCAT/issues>


Indices and Tables
------------------
* :ref:`genindex`
* :ref:`modindex`
