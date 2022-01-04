import time
import numpy as np

import eagle_IO.eagle_IO as E


directory = '/cosma5/data/Eagle/ScienceRuns/Planck1/L0050N0752/PE/S15_AGNdT9/data'
tag = '003_z008p988'


def speed_test(threads=1):
    start = time.time()
    
    smass = E.read_array('SNAP',directory,tag,"/PartType4/Mass",numThreads=threads,noH=True,physicalUnits=True)
    mstar = E.read_array('SUBFIND',directory,tag,"/Subhalo/Stars/Mass",numThreads=threads,noH=True,physicalUnits=True)
    
    end = time.time()
    print("Threads: %i\nTime elapsed: %.4f\n"%(threads,end - start))



for i in np.arange(1,16):
    speed_test(i)

