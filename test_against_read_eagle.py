
import eagle as E
import eagleIO as Eio

directory = '/cosma5/data/Eagle/ScienceRuns/Planck1/L0050N0752/PE/S15_AGNdT9/data'
tag = '003_z008p988'

mstar = Eio.read_array('SUBFIND',directory,tag,"/Subhalo/Stars/Mass",numThreads=1)

print(mstar.shape)
print(mstar[:10])


mstar = E.readArray('SUBFIND',directory,tag,"/Subhalo/Stars/Mass",numThreads=1)

print(mstar.shape)
print(mstar[:10])
