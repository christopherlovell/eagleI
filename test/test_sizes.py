
import sys
from eagle_IO import eagle_IO as E
import numpy as np
import pandas as pd

    
def get_details(ftype,sim,tag,num,threads,ptype):
    print("\nHalo: %s\nTag: %s\nftype: %s\nThreads: %s\nParticle Type: %s\n"%(num,tag,ftype,threads,ptype))
    
    sp_sgrpn = E.read_array(ftype, sim, tag, '/%s/SubGroupNumber'%ptype, numThreads=threads)
    sp_grpn = E.read_array(ftype, sim, tag, '/%s/GroupNumber'%ptype, numThreads=threads)
    
    sp_cood = E.read_array(ftype, sim, tag, '/%s/Coordinates'%ptype, noH=True, physicalUnits=True, numThreads=threads)
    sp_id = E.read_array(ftype, sim, tag, '/%s/ParticleIDs'%ptype, numThreads=threads)
    
    print("Type4 SubGroupNumber size = ", sp_sgrpn.shape)
    print("Type4 GroupNumber size = ", sp_grpn.shape)
    print("Type4 Coords size = ", sp_cood.shape)
    print("Type4 ID size = ", sp_id.shape)
    
    n_part_total =E.read_header(ftype,sim,tag,'NumPart_Total')
    
    print("NumPart_Total: %s"%n_part_total)


num = '00'
sim = '/cosma7/data/dp004/dc-payy1/G-EAGLE/GEAGLE_{}/data'.format(num) 
tag = '011_z004p770' #'012_z004p688' # '010_z005p000'

ftype='SNAP'#'PARTDATA'
threads=4
ptype='PartType0'

get_details('SNAP',sim,tag,num,threads,ptype)
get_details('PARTDATA',sim,tag,num,threads,ptype)



