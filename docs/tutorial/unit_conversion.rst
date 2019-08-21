Unit conversion
****************

By default, the :code:`read_array` function converts the data read from the file into “h free” physical units. This is done by reading the relevant conversion factors from the HDF5 file. If :code:`verbose` is :code:`True`, the conversions applied to the data are reported by the function and printed to the standard output. This behaviour can be modified using the two optional parameters :code:`noH` and :code:`physicalUnits`. If :code:`noH` is set to :code:`False` then the routine does not apply any h factor correction. If :code:`physicalUnits` is set to :code:`False` then no a-factor correction is applied. Running with :code:`noH=False, physicalUnits=False` will hence read in the data as it is in the file without applying any correction. For instance, reading the particle coordinates at :math:`z=1` with this code:

.. code-block:: python

  pos = E.read_array("SUBFIND_GROUP", sim, tag, "FOF/Group_R_Crit500", noH=True, physicalUnits=True)

will yield::

  Converting to physical units. (Multiplication by a^1, a=1)
  Converting to h-free units. (Multiplication by h^-1, h=0.6777)

**This relies on the fact that the units written in the file are correct. Always check that this is the case by looking at the standard output!!**


