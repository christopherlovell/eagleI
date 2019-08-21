.. eagle_IO documentation master file, created by
   sphinx-quickstart on Wed Aug  7 14:35:43 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. toctree::
   :maxdepth: 2

   properties/snapshots
   properties/fof
   properties/subfind


eagle_IO
====================================

Reading EAGLE HDF5 files in native Python, with optional multithreading

:Author: Christopher Lovell
:Version: 0.0.1

.. contents::


Reading data
------------

The module offers one main function, :code:`read_array`:

.. code-block:: python

  import eagle as E

  M_200 = E.readArray(fileType,  directory,  tag,   array)

:code:`read_array` accepts 4 arguments; the first is a string describing the type of file and data read. The allowed values are: 

=======================  ===============================================  ==============================================================
Value                    Description                                      Example of data that can be read
=======================  ===============================================  ==============================================================
FOF                      FoF group informations                           Group centre of mass, group length, group star formation rate
FOF_PARTICLES            IDs of the particles in a FOF group              Particle IDs 
SNIP_FOF                 FoF group informations (snipshot)                Group centre of mass, group length, group star formation rate
SNIP_FOF_PARTICLES       IDs of the particles in a FOF group (snipshot)   Particle IDs
PARTDATA                 Particles that are in a FOF group                Particle Mass, velocity, entropy, stellar age 
SNIP_PARTDATA            Particles that are in a FOF group (snipshot)     Particle Mass, velocity, entropy, stellar age 
SNAPSHOT                 Full information about all particles             Particle Mass, velocity, entropy, stellar age 
SNIPSHOT                 Reduced information about all particles          Mass, velocity
SUBFIND                  Subhalo information                              Subhalo mass, subhalo centre of potential
SUBFIND_GROUP            Subfind halo information                         Group centre of potential, M_200, R_500
SUBFIND_PARTICLES        IDs of the particles in a subhalo                Particle IDs
SNIP_SUBFIND             Subhalo information (snipshot)                   Subhalo mass, subhalo centre of potential
SNIP_SUBFIND_GROUP       Subfind halo information (snipshot)              Group centre of potential, M_200, R_500
SNIP_SUBFIND_PARTICLES   IDs of the particles in a subhalo (snipshot)     Particle IDs 
=======================  ===============================================  ==============================================================



The second argument is the location of the directory containing the data. For instance::

  "/cosma5/data/Eagle/ScienceRuns/Planck1/L0100N1504/PE/EagleReference/data/"

The third argument is the “tag” of the output. This is the part of the filename that contains the snapshot number and the redshift. For the 29 main output times in the fiducial periodic volumes, the values are: 

  “000_z020p000”	“001_z015p132”	“002_z009p993”	“003_z008p988”
  “004_z008p075”	“005_z007p050”	“006_z005p971”	“007_z005p487”
  “008_z005p037”	“009_z004p485”	“010_z003p984”	“011_z003p528”
  “012_z003p017”	“013_z002p478”	“014_z002p237”	“015_z002p012”
  “017_z001p487”	“018_z001p259”	“019_z001p004”	“020_z000p865”
  “021_z000p736”	“022_z000p615”	“023_z000p503”	“024_z000p366”
  “025_z000p271”	“026_z000p183”	“027_z000p101”	“028_z000p000”


The last argument is the name of the array or attribute to be read. For instance::

  "/PartType4/Metallicity"

or::

  "/PartType5/BH_TimeLastmerger"

The routine returns a numpy array containing the values extracted from the files. The order of the elements is preserved and the type of the values is the same as that stored in the HDF5 files.

 To read the value of :math:`M_200` for all halos at :math:`z=1.5` in the reference volume, one would use:

.. code-block:: python

  import eagle_IO as E
 
  sim = "/cosma5/data/Eagle/ScienceRuns/Planck1/L0100N1504/PE/EagleReference/data/"
  tag = "017_z001p487"

  M_200 = E.read_array("SUBFIND_GROUP", sim, tag, "FOF/Group_M_Crit200")
  

Unit conversion
---------------

By default, the :code:`read_array` function converts the data read from the file into “h free” physical units. This is done by reading the relevant conversion factors from the HDF5 file. If :code:`verbose` is :code:`True`, the conversions applied to the data are reported by the function and printed to the standard output. This behaviour can be modified using the two optional parameters :code:`noH` and :code:`physicalUnits`. If :code:`noH` is set to :code:`False` then the routine does not apply any h factor correction. If :code:`physicalUnits` is set to :code:`False` then no a-factor correction is applied. Running with :code:`noH=False, physicalUnits=False` will hence read in the data as it is in the file without applying any correction. For instance, reading the particle coordinates at :math:`z=1` with this code:

.. code-block:: python

  pos = E.read_array("SUBFIND_GROUP", sim, tag, "FOF/Group_R_Crit500", noH=True, physicalUnits=True)

will yield::

  Converting to physical units. (Multiplication by a^1, a=1)
  Converting to h-free units. (Multiplication by h^-1, h=0.6777)

**This relies on the fact that the units written in the file are correct. Always check that this is the case by looking at the standard output!!**


Future Development
------------------

- read attributes function
- tests for file existence, file ordering etc.
