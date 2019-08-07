.. eagle_IO documentation master file, created by
   sphinx-quickstart on Wed Aug  7 14:35:43 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to eagle_IO's documentation!
====================================

:Author: Christopher Lovell
:Version: $Revision: 0.0.1 $

.. contents::



Reading data
------------

The module offers two functions. One to read attributes and one to read arrays::

  import eagle as E
 
  z = E.readAttribute(fileType,  directory,  tag,   attribute)
  M_200 = E.readArray(fileType,  directory,  tag,   array)

Both routines are constructed in the same way and need to be supplied with the same 4 arguments. The first one is a string describing the type of file and data read. The allowed values of this parameter are: 

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

The third argument is the “tag” of the output. This is the part of the filename that contains the snapshot number and the redshift. For the 29 main output times, the values are: 

  “000_z020p000”	“001_z015p132”	“002_z009p993”	“003_z008p988”
  “004_z008p075”	“005_z007p050”	“006_z005p971”	“007_z005p487”
  “008_z005p037”	“009_z004p485”	“010_z003p984”	“011_z003p528”
  “012_z003p017”	“013_z002p478”	“014_z002p237”	“015_z002p012”
  “017_z001p487”	“018_z001p259”	“019_z001p004”	“020_z000p865”
  “021_z000p736”	“022_z000p615”	“023_z000p503”	“024_z000p366”
  “025_z000p271”	“026_z000p183”	“027_z000p101”	“028_z000p000”


The last argument is the name of the array or attribute to be read. For instance:

  "/PartType4/Metallicity"

or

  "/PartType5/BH_TimeLastmerger"

The routine returns a numpy array containing the values extracted from the files. The order of the elements is preserved and the type of the values is the same than stored in the HDF5 files.

