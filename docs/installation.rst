************
Installation
************


MOOG_SCAT Installation
======================

MOOG-SCAT is Fortran code (f77; f90 compatibility) and accordingly for compilation, requires a fortran compiler.  For a Mac OS, successful compilation has been achieved with the
gfortran compiler. Other compilers, such as ifort, have also been successfully used.  

.. code-block:: bash

    gfortran -Wall -ffixed-line-length-72 -m64 


Dependencies
============

MOOG_SCAT is largely self-contained, however it does depend on SuperMongo (and the associated sm libraries) for plot generation. MOOG_SCAT also relies on
X11 libraries. 

- Supermongo
