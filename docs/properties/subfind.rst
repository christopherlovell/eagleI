Subfind arrays
**************

Subgroup numbers begin at 0.  Subgroup 0 of a FOF group corresponds to the most massive subgroup within the group.

The following arrays can be found in the Eagle subfind files: 

========== ================================================= ===============================================================================================================================================================================================================
Group      Array Name                                        Description
========== ================================================= ===============================================================================================================================================================================================================
 FOF        ContaminationMass                                 Contaminating mass. Physical M = Mass U_M[g] |  
 FOF        FirstSubhaloID                                    Index of first sub halo in SubHalo list (starts at 0) |  
 FOF        GroupCentreOfPotential                            Co-moving position of most bound particle. Physical position = position h to the power of-1 a U_L[cm] |  
 FOF        GroupLength                                       Number of particles in this group |  
 FOF        GroupMass                                          Total mass of FoF group. Physical M = Mass h to the power of-1 U_M[g] |  
 FOF        GroupOffset                                       Offset of IDs of this group, starts at 0 |  
 FOF        Group_M_Crit200                                    Mass within Rcrit200. Physical M = Mass h to the power of-1 U_M[g] |  
 FOF        Group_M_Crit2500                                  M_Crit2500 |  
 FOF        Group_M_Crit500                                   M_Crit500 |  
 FOF        Group_M_Mean200                                   Mass within RMean200. Physical M = Mass h to the power of-1 U_M[g] |  
 FOF        Group_M_Mean2500                                  M_Mean2500 |  
 FOF        Group_M_Mean500                                   M_Mean500 |  
 FOF        Group_M_TopHat200                                 Mass within RTophat200. Physical M = Mass h to the power of-1 U_M[g] |  
 FOF        Group_R_Crit200                                   Co-moving radius within which density is 200 times critical density. Physical radius = radius h to the power of-1 a U_L[cm] |  
 FOF        Group_R_Crit2500                                  R_Crit2500 |  
 FOF        Group_R_Crit500                                   R_Crit500 |  
 FOF        Group_R_Mean200                                    Co-moving radius within which density is 200 times mean density. Physical radius = radius h to the power of-1 a U_L[cm] |  
 FOF        Group_R_Mean2500                                  R_Mean2500 |  
 FOF        Group_R_Mean500                                   R_Mean500 |  
 FOF        Group_R_TopHat200                                  Co-moving radius within which density is 200 times (18 * pi to the power of2 + 82 * (Omega_m(z)-1) - 39 * (Omega_m(z)-1) to the power of2); Physical radius = radius h to the power of-1 a U_L[cm] |  
 FOF        NumOfSubhalos                                     Number of subhaloes in this FoF group |  
 ^ ^       
 IDs        ParticleID                                        PID |  
 IDs        Particle_Binding_Energy                           Binding energy of particles |  
 ^ ^        
 Subhalo    ApertureMeasurements/Mass/001kpc                  Masses within apertures from 1 to 100 kpc (physical) of the centre of potential of the subhalo |  
 Subhalo    ApertureMeasurements/Mass/003kpc                  Masses within apertures from 1 to 100 kpc (physical) of the centre of potential of the subhalo |  
 Subhalo    ApertureMeasurements/Mass/005kpc                  Masses within apertures from 1 to 100 kpc (physical) of the centre of potential of the subhalo |  
 Subhalo    ApertureMeasurements/Mass/010kpc                  Masses within apertures from 1 to 100 kpc (physical) of the centre of potential of the subhalo |  
 Subhalo    ApertureMeasurements/Mass/020kpc                  Masses within apertures from 1 to 100 kpc (physical) of the centre of potential of the subhalo |  
 Subhalo    ApertureMeasurements/Mass/030kpc                  Masses within apertures from 1 to 100 kpc (physical) of the centre of potential of the subhalo |  
 Subhalo    ApertureMeasurements/Mass/040kpc                  Masses within apertures from 1 to 100 kpc (physical) of the centre of potential of the subhalo |  
 Subhalo    ApertureMeasurements/Mass/050kpc                  Masses within apertures from 1 to 100 kpc (physical) of the centre of potential of the subhalo |  
 Subhalo    ApertureMeasurements/Mass/070kpc                  Masses within apertures from 1 to 100 kpc (physical) of the centre of potential of the subhalo |  
 Subhalo    ApertureMeasurements/Mass/100kpc                  Masses within apertures from 1 to 100 kpc (physical) of the centre of potential of the subhalo |  
 Subhalo    ApertureMeasurements/SFR/001kpc                   Star formation rate within apertures from 1 to 100 kpc (physical) of the centre of potential of the subhalo |  
 Subhalo    ApertureMeasurements/SFR/003kpc                   Star formation rate within apertures from 1 to 100 kpc (physical) of the centre of potential of the subhalo |  
 Subhalo    ApertureMeasurements/SFR/005kpc                   Star formation rate within apertures from 1 to 100 kpc (physical) of the centre of potential of the subhalo |  
 Subhalo    ApertureMeasurements/SFR/010kpc                   Star formation rate within apertures from 1 to 100 kpc (physical) of the centre of potential of the subhalo |  
 Subhalo    ApertureMeasurements/SFR/020kpc                   Star formation rate within apertures from 1 to 100 kpc (physical) of the centre of potential of the subhalo |  
 Subhalo    ApertureMeasurements/SFR/030kpc                   Star formation rate within apertures from 1 to 100 kpc (physical) of the centre of potential of the subhalo |  
 Subhalo    ApertureMeasurements/SFR/040kpc                   Star formation rate within apertures from 1 to 100 kpc (physical) of the centre of potential of the subhalo |  
 Subhalo    ApertureMeasurements/SFR/050kpc                   Star formation rate within apertures from 1 to 100 kpc (physical) of the centre of potential of the subhalo |  
 Subhalo    ApertureMeasurements/SFR/070kpc                   Star formation rate within apertures from 1 to 100 kpc (physical) of the centre of potential of the subhalo |  
 Subhalo    ApertureMeasurements/SFR/100kpc                   Star formation rate within apertures from 1 to 100 kpc (physical) of the centre of potential of the subhalo |  
 Subhalo    ApertureMeasurements/VelDisp/001kpc               Stellar velocity dispersion within apertures from 1 to 100 kpc (physical) of the centre of potential of the subhalo ((Expansion factor, aexp-scale-exponent, is incorrect, should be 0.  See [[eagle:simulations:simulation_overview:known_bugs]] for more details.)) |  
 Subhalo    ApertureMeasurements/VelDisp/003kpc               Stellar velocity dispersion within apertures from 1 to 100 kpc (physical) of the centre of potential of the subhalo <sup>1)</sup> |  
 Subhalo    ApertureMeasurements/VelDisp/005kpc               Stellar velocity dispersion within apertures from 1 to 100 kpc (physical) of the centre of potential of the subhalo <sup>1)</sup>|  
 Subhalo    ApertureMeasurements/VelDisp/010kpc               Stellar velocity dispersion within apertures from 1 to 100 kpc (physical) of the centre of potential of the subhalo <sup>1)</sup>|  
 Subhalo    ApertureMeasurements/VelDisp/020kpc               Stellar velocity dispersion within apertures from 1 to 100 kpc (physical) of the centre of potential of the subhalo <sup>1)</sup>|  
 Subhalo    ApertureMeasurements/VelDisp/030kpc               Stellar velocity dispersion within apertures from 1 to 100 kpc (physical) of the centre of potential of the subhalo <sup>1)</sup>|  
 Subhalo    ApertureMeasurements/VelDisp/040kpc               Stellar velocity dispersion within apertures from 1 to 100 kpc (physical) of the centre of potential of the subhalo <sup>1)</sup>|  
 Subhalo    ApertureMeasurements/VelDisp/050kpc               Stellar velocity dispersion within apertures from 1 to 100 kpc (physical) of the centre of potential of the subhalo <sup>1)</sup>|  
 Subhalo    ApertureMeasurements/VelDisp/070kpc               Stellar velocity dispersion within apertures from 1 to 100 kpc (physical) of the centre of potential of the subhalo <sup>1)</sup>|  
 Subhalo    ApertureMeasurements/VelDisp/100kpc               Stellar velocity dispersion within apertures from 1 to 100 kpc (physical) of the centre of potential of the subhalo <sup>1)</sup>|  
 Subhalo    BlackHoleMass                                     BH mass. Physical m = Mass h to the power of-1 U_M [g] |  
 Subhalo    BlackHoleMassAccretionRate                        BH accretion rate. Physical mdot = BH_Mdot h to the power of-1 U_M /U_T [g/s] |  
 Subhalo    CentreOfMass                                      Co-moving position of COM. Physical position = position h to the power of-1 a U_L[cm] |  
 Subhalo    CentreOfPotential                                 Co-moving position of most bound particle. Physical position = position h to the power of-1 a U_L[cm] |  
 Subhalo    GasSpin                                           Angular momentum per unit mass of gas particles |  
 Subhalo    GroupNumber                                       FOF Group Number subhalo belongs to |  
 Subhalo    HalfMassProjRad                                   Projected (av. over 3 axes) radius enclosing half of the subhalo mass comprised by each particle type <sup>1)</sup>|  
 Subhalo    HalfMassRad                                       Radius enclosing half of the subhalo mass comprised by each particle type <sup>1)</sup>|  
 Subhalo    IDMostBound                                       Particle ID of lowest *total* energy particle |  
 Subhalo    InertiaTensor                                     Matrix for the second moment of matter distribution. <sup>1)</sup>|  
 Subhalo    InitialMassWeightedBirthZ                         Initial mass weighted metallicity of stars |  
 Subhalo    InitialMassWeightedStellarAge                     Initial mass weighted age of stars in Gyr |  
 Subhalo    KineticEnergy                                     Total kinetic energy of particles bound to this halo |  
 Subhalo    Mass                                              Total mass of this group. Physical M = Mass h to the power of-1 U_M[g] |  
 Subhalo    MassTwiceHalfMassRad                              Mass contained within twice the half mass radius for each particle type |  
 Subhalo    MassType                                          Total mass of this group for each particle type. Physical M = Mass h to the power of-1 U_M[g] |  
 Subhalo    NSF/ElementAbundances/Carbon                      ((Some values are incorrect, see [[eagle:simulations:simulation_overview:known_bugs]] for details)) |  
 Subhalo    NSF/ElementAbundances/Helium                      <sup>2)</sup>|  
 Subhalo    NSF/ElementAbundances/Hydrogen                    <sup>2)</sup> |  
 Subhalo    NSF/ElementAbundances/Iron                        <sup>2)</sup> |  
 Subhalo    NSF/ElementAbundances/Magnesium                   <sup>2)</sup> |  
 Subhalo    NSF/ElementAbundances/Neon                        <sup>2)</sup> |  
 Subhalo    NSF/ElementAbundances/Nitrogen                    <sup>2)</sup> |  
 Subhalo    NSF/ElementAbundances/Oxygen                      <sup>2)</sup> |  
 Subhalo    NSF/ElementAbundances/Silicon                     <sup>2)</sup> |  
 Subhalo    NSF/IronFromSNIa                                  Iron from SNIa |  
 Subhalo    NSF/IronFromSNIaSmoothed                          Smoothed iron from SNIa |  
 Subhalo    NSF/KineticEnergy                                 Kinetic energy of NSF gas |  
 Subhalo    NSF/Mass                                          Mass |  
 Subhalo    NSF/MassFromAGB                                   Mass from AGB |  
 Subhalo    NSF/MassFromSNII                                  Mass from SNII |  
 Subhalo    NSF/MassFromSNIa                                  Mass from SNIa |  
 Subhalo    NSF/MassWeightedEntropy                           Mass weighted mean entropy of NSF gas |  
 Subhalo    NSF/MassWeightedPotential                         Mass weighted potential |
 Subhalo    NSF/MassWeightedTemperature                       Mass weighted mean temperature of NSF gas |  
 Subhalo    NSF/Metallicity                                   Metallicity weighted by mass of non star forming gas in subhalos |  
 Subhalo    NSF/MetalsFromAGB                                 Mass in metals from AGB |  
 Subhalo    NSF/MetalsFromSNII                                Mass in metals from SNII |  
 Subhalo    NSF/MetalsFromSNIa                                Mass in metals from SNIa |  
 Subhalo    NSF/SmootheElementAbuncdances/Carbon              <sup>2)</sup> |  
 Subhalo    NSF/SmootheElementAbuncdances/Helium              <sup>2)</sup> |  
 Subhalo    NSF/SmootheElementAbuncdances/Hydrogen            <sup>2)</sup> |  
 Subhalo    NSF/SmootheElementAbuncdances/Iron                <sup>2)</sup> |  
 Subhalo    NSF/SmootheElementAbuncdances/Magnesium           <sup>2)</sup> |  
 Subhalo    NSF/SmootheElementAbuncdances/Neon                <sup>2)</sup> |  
 Subhalo    NSF/SmootheElementAbuncdances/Nitrogen            <sup>2)</sup> |  
 Subhalo    NSF/SmootheElementAbuncdances/Oxygen              <sup>2)</sup> |  
 Subhalo    NSF/SmootheElementAbuncdances/Silicon             <sup>2)</sup> |  
 Subhalo    NSF/SmoothedMetallicity                           Smoothed metallicity weighted by mass of non star forming gas in subhalos |  
 Subhalo    NSF/Spin                                          Angular momentum per unit mass of non-star-forming gas particles |  
 Subhalo    NSF/ThermalEnergy                                 Thermal energy of NSF gas |  
 Subhalo    NSF/TotalEnergy                                   Total energy of NSF gas |  
 Subhalo    SF/ElementAbundances/Carbon                       <sup>2)</sup> |  
 Subhalo    SF/ElementAbundances/Helium                       <sup>2)</sup> |  
 Subhalo    SF/ElementAbundances/Hydrogen                     <sup>2)</sup> |  
 Subhalo    SF/ElementAbundances/Iron                         <sup>2)</sup> |  
 Subhalo    SF/ElementAbundances/Magnesium                    <sup>2)</sup> |  
 Subhalo    SF/ElementAbundances/Neon                         <sup>2)</sup> |  
 Subhalo    SF/ElementAbundances/Nitrogen                     <sup>2)</sup> |  
 Subhalo    SF/ElementAbundances/Oxygen                       <sup>2)</sup> |  
 Subhalo    SF/ElementAbundances/Silicon                      <sup>2)</sup> |  
 Subhalo    SF/IronFromSNIa                                   Iron from SNIa |  
 Subhalo    SF/IronFromSNIaSmoothed                           Smoothed iron from SNIa |  
 Subhalo    SF/KineticEnergy                                  Kinetic energy of SF gas |  
 Subhalo    SF/Mass                                           Mass |  
 Subhalo    SF/MassFromAGB                                    Mass from AGB |  
 Subhalo    SF/MassFromSNII                                   Mass from SNII |  
 Subhalo    SF/MassFromSNIa                                   Mass from SNIa |  
 Subhalo    SF/MassWeightedEntropy                            Mass weighted mean entropy of SF gas |  
 Subhalo    SF/MassWeightedPotential                          Mass weighted potential |  
 Subhalo    SF/MassWeightedTemperature                        Mass weighted mean temperature of SF gas |  
 Subhalo    SF/Metallicity                                    Metallicity weighted by mass of star forming gas in subhalos |  
 Subhalo    SF/MetalsFromAGB                                  Mass in metals from AGB |  
 Subhalo    SF/MetalsFromSNII                                 Mass in metals from SNII |  
 Subhalo    SF/MetalsFromSNIa                                 Mass in metals from SNIa |  
 Subhalo    SF/SFWeightedMetallicity                          Metallicity weighted by star formation rate of star forming gas in subhalos |  
 Subhalo    SF/SmoothedElementAbundances/Carbon               <sup>2)</sup> |  
 Subhalo    SF/SmoothedElementAbundances/Helium               <sup>2)</sup> |  
 Subhalo    SF/SmoothedElementAbundances/Hydrogen             <sup>2)</sup> |  
 Subhalo    SF/SmoothedElementAbundances/Iron                 <sup>2)</sup> |  
 Subhalo    SF/SmoothedElementAbundances/Magnesium            <sup>2)</sup> |  
 Subhalo    SF/SmoothedElementAbundances/Neon                 <sup>2)</sup> |  
 Subhalo    SF/SmoothedElementAbundances/Nitrogen             <sup>2)</sup> |  
 Subhalo    SF/SmoothedElementAbundances/Oxygen               <sup>2)</sup> |  
 Subhalo    SF/SmoothedElementAbundances/Silicon              <sup>2)</sup> |  
 Subhalo    SF/SmoothedMetallicity                            Smoothed metallicity weighted by mass of star forming gas in subhalos |  
 Subhalo    SF/SmoothedSFWeightedMetallicity                  Smoothed metallicity weighted by star formation rate of star forming gas in subhalos |  
 Subhalo    SF/Spin                                           Angular momentum per unit mass of star-forming gas particles |  
 Subhalo    SF/ThermalEnergy                                  Thermal energy of SF gas |  
 Subhalo    SF/TotalEnergy                                    Total energy of SF gas |  
 Subhalo    StarFormationRate                                 Total gas star formation rate in solar masses / yr |  
 Subhalo    Stars/ElementAbundances/Carbon                    <sup>2)</sup> |  
 Subhalo    Stars/ElementAbundances/Helium                    <sup>2)</sup> |  
 Subhalo    Stars/ElementAbundances/Hydrogen                  <sup>2)</sup> |  
 Subhalo    Stars/ElementAbundances/Iron                      <sup>2)</sup> |  
 Subhalo    Stars/ElementAbundances/Magnesium                 <sup>2)</sup> |  
 Subhalo    Stars/ElementAbundances/Neon                      <sup>2)</sup> |  
 Subhalo    Stars/ElementAbundances/Nitrogen                  <sup>2)</sup> |  
 Subhalo    Stars/ElementAbundances/Oxygen                    <sup>2)</sup> |  
 Subhalo    Stars/ElementAbundances/Silicon                   <sup>2)</sup> |  
 Subhalo    Stars/IronFromSNIa                                Iron from SNIa |  
 Subhalo    Stars/IronFromSNIaSmoothed                        Smoothed iron from SNIa |  
 Subhalo    Stars/KineticEnergy                               Kinetic energy of stars |  
 Subhalo    Stars/Mass                                        Mass in stars |  
 Subhalo    Stars/MassFromAGB                                 Mass from AGB |  
 Subhalo    Stars/MassFromSNII                                Mass from SNII |  
 Subhalo    Stars/MassFromSNIa                                Mass from SNIa |  
 Subhalo    Stars/MassWeightedPotential                       Mass weighted potential |  
 Subhalo    Stars/Metallicity                                 Metallicity weighted by mass of stars in subhalos |  
 Subhalo    Stars/MetalsFromAGB                               Mass in metals from AGB |  
 Subhalo    Stars/MetalsFromSNII                              Mass in metals from SNII |  
 Subhalo    Stars/MetalsFromSNIa                              Mass in metals from SNIa |  
 Subhalo    Stars/SmoothedElementAbundances/Carbon            <sup>2)</sup> |  
 Subhalo    Stars/SmoothedElementAbundances/Helium            <sup>2)</sup> |  
 Subhalo    Stars/SmoothedElementAbundances/Hydrogen          <sup>2)</sup> |  
 Subhalo    Stars/SmoothedElementAbundances/Iron              <sup>2)</sup> |  
 Subhalo    Stars/SmoothedElementAbundances/Magnesium         <sup>2)</sup> |  
 Subhalo    Stars/SmoothedElementAbundances/Neon              <sup>2)</sup> |  
 Subhalo    Stars/SmoothedElementAbundances/Nitrogen          <sup>2)</sup> |  
 Subhalo    Stars/SmoothedElementAbundances/Oxygen            <sup>2)</sup> |  
 Subhalo    Stars/SmoothedElementAbundances/Silicon           <sup>2)</sup> |  
 Subhalo    Stars/SmoothedMetallicity                         Smoothed metallicity weighted by mass of stars in subhalos |  
 Subhalo    Stars/Spin                                        Angular momentum per unit mass of star particles |  
 Subhalo    Stars/TotalEnergy                                 Total energy of stars |  
 Subhalo    StellarInitialMass                                Stellar initial mass |  
 Subhalo    StellarVelDisp                                    Stellar velocity dispersion <sup>1)</sup>|  
 Subhalo    StellarVelDisp_HalfMassProjRad                    Stellar velocity dispersion within half mass radius <sup>1)</sup>|  
 Subhalo    SubGroupNumber                                    SubGroup Number of subhalo, begins at 0 for most massive subhalo within a group |  
 Subhalo    SubLength                                         Number of particles in this subhalo |  
 Subhalo    SubLengthType                                     Number of particles of each type in this subhalo |  
 Subhalo    SubOffset                                         Offset of IDs in this subhalo.  Starts at 0 |  
 Subhalo    ThermalEnergy                                     Total thermal energy of particles bound to this halo |  
 Subhalo    TotalEnergy                                       Total energy of particles bound to this halo |  
 Subhalo    Velocity                                          Vel |  
 Subhalo    Vmax                                              Co-moving maximum circular velocity. Physical velocity = ??? |  
 Subhalo    VmaxRadius                                        VmaxRad |  
========== ================================================= ===============================================================================================================================================================================================================
