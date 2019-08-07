
import eagle_IO.eagle_IO as Eio
import eagle as E

directory = '/cosma5/data/Eagle/ScienceRuns/Planck1/L0050N0752/PE/S15_AGNdT9/data'
tag = '003_z008p988'
N = 10

files = Eio.get_files('SUBFIND',directory,tag)
# print(files)

print("\n\nnoH = True | physicalUnits = True\n")

mstar = Eio.read_array('SUBFIND',directory,tag,"/Subhalo/Stars/Mass",numThreads=1,noH=True,physicalUnits=True)
print(mstar.shape,mstar[:N])

mstar = E.readArray('SUBFIND',directory,tag,"/Subhalo/Stars/Mass",numThreads=1,noH=True,physicalUnits=True,verbose=True)
print(mstar.shape,mstar[:N])


print("\n\nnoH = False | physicalUnits = True\n")

mstar = Eio.read_array('SUBFIND',directory,tag,"/Subhalo/Stars/Mass",numThreads=1,noH=False,physicalUnits=True,verbose=True)
print(mstar.shape,mstar[:N])

mstar = E.readArray('SUBFIND',directory,tag,"/Subhalo/Stars/Mass",numThreads=1,noH=False,physicalUnits=True,verbose=True)
print(mstar.shape,mstar[:N])


print("\n\nnoH = False | physicalUnits = False\n")

mstar = Eio.read_array('SUBFIND',directory,tag,"/Subhalo/Stars/Mass",numThreads=1,noH=False,physicalUnits=False)
print(mstar.shape,mstar[:N])

mstar = E.readArray('SUBFIND',directory,tag,"/Subhalo/Stars/Mass",numThreads=1,noH=False,physicalUnits=False,verbose=True)
print(mstar.shape,mstar[:N])


print("\n\nnoH = True | physicalUnits = False\n")

mstar = Eio.read_array('SUBFIND',directory,tag,"/Subhalo/Stars/Mass",numThreads=1,noH=True,physicalUnits=False)
print(mstar.shape,mstar[:N])

mstar = E.readArray('SUBFIND',directory,tag,"/Subhalo/Stars/Mass",numThreads=1,noH=True,physicalUnits=False,verbose=True)
print(mstar.shape,mstar[:N])

