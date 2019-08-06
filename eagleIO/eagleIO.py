import numpy as np
import h5py
import glob

import schwimmbad
from functools import partial


def read_hdf5(f,dataset):
    with h5py.File(f,'r') as hf:
        dat = np.array(hf.get(dataset))

    return dat




def get_files(fileType,directory,tag):
    """
    Fetch filename

    Args:
        fileType (str)
        directory (str)
        tag (str)
    """

    if fileType in ['FOF','FOF_PARTICLES']:
      return glob.glob("%s/groups_%s/group_tab_%s*.hdf5"%(directory,tag,tag))
    elif fileType in ['SNIP_FOF','SNIP_FOF_PARTICLES']:
      return glob.glob("%s/groups_snip_%s/group_snip_tab_%s*.hdf5"%(directory,tag,tag))
    elif fileType in ['SUBFIND','SUBFIND_GROUP','SUBFIND_IDS']:
      return glob.glob("%s/groups_%s/eagle_subfind_tab_%s*.hdf5"%(directory,tag,tag))
    elif fileType in ['SNIP_SUBFIND','SNIP_SUBFIND_GROUP','SNIP_SUBFIND_IDS']:
      return glob.glob("%s/groups_snip_%s/eagle_subfind_snip_tab_%s*.hdf5"%(directory,tag,tag))
    elif fileType in ['SNIP']:
      return glob.glob("%s/snipshot_%s/snip_%s*.hdf5"%(directory,tag,tag))
    elif fileType in ['SNAP']:
      return glob.glob("%s/snapshot_%s/snap_%s*.hdf5"%(directory,tag,tag))
    elif fileType in ['PARTDATA']:
      return glob.glob("%s/particledata_%s/eagle_subfind_particles_%s*.hdf5"%(directory,tag,tag))
    elif fileType in ['SNIP_PARTDATA']:
      return glob.glob("%s/particledata_snip_%s/eagle_subfind_snip_particles_%s*.hdf5"%(directory,tag,tag))
    else:
      ValueError("Type of files not supported")


# see line 326 here https://github.com/christopherlovell/readEagle3/blob/master/readEagle.cpp
# def apply_physicalUnits_conversion():
# def apply_hfreeUnits_conversion():
# def apply_CGSUnits_conversion():


def read_array(ftype,directory,tag,dataset,numThreads=1):
    """
   
    Args:
        ftype (str)
        directory (str)
        tag (str)
        dataset (str)
        numThreads (int)
    """
    
    files = get_files(ftype,directory,tag)

    if numThreads == 1:
        pool = schwimmbad.SerialPool() 
    elif numThreads == -1:
        pool = schwimmbad.MultiPool()
    else:
        pool = schwimmbad.MultiPool(processes=numThreads)


    lg = partial(read_hdf5, dataset=dataset)
    return np.hstack(list(pool.map(lg,files)))


if __name__== "__main__": 

    directory = '/cosma5/data/Eagle/ScienceRuns/Planck1/L0050N0752/PE/S15_AGNdT9/data'
    tag = '003_z008p988'

    mstar = read_array('SUBFIND',directory,tag,"/Subhalo/Stars/Mass",numThreads=1)
    print(mstar.shape)
    print(mstar[:10])
    

