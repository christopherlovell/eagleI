.. eagle_IO documentation master file, created by
   sphinx-quickstart on Wed Aug  7 14:35:43 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to eagle_IO's documentation!
====================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:


:Author: Christopher Lovell
:Version: $Revision: 5801 $

.. contents::



Reading data
------------

The module offers two functions. One to read attributes and one to read arrays::

  import eagle as E
 
  z = E.readAttribute(fileType,  directory,  tag,   attribute)
  M_200 = E.readArray(fileType,  directory,  tag,   array)

Both routines are constructed in the same way and need to be supplied with the same 4 arguments. The first one is a string describing the type of file and data read. The allowed values of this parameter are: 

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
