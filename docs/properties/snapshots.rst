Snapshot arrays
****************

============== ======================================== ==========================================================================================================================================================================================================
Particle Type  Array Name                               Array Description
============== ======================================== ==========================================================================================================================================================================================================
PartType0       AExpMaximumTemperature                   Expansion factor a when particle had highest temperature|
PartType0       Coordinates                              Co-moving coordinates. Physical: r = a x = Coordinates h to the power of-1 a U_L [cm]|
PartType0       Density                                  Co-moving mass densities. Physical rho = Densities h to the power of2 a to the power of-3 U_M U_L to the power of-3 [g/cm to the power of3]|
PartType0       ElementAbundance/Carbon                 ||
PartType0       ElementAbundance/Helium                 ||
PartType0       ElementAbundance/Hydrogen               ||
PartType0       ElementAbundance/Iron                   ||
PartType0       ElementAbundance/Magnesium              ||
PartType0       ElementAbundance/Neon                   ||
PartType0       ElementAbundance/Nitrogen               ||
PartType0       ElementAbundance/Oxygen                 ||
PartType0       ElementAbundance/Silicon                ||
PartType0       Entropy                                  Particle entropy. Physical s = Entropy h to the power of(2-2*GAMMA) UnitPressure UnitDensity to the power of-GAMMA|
PartType0       GroupNumber                              FoF group number particle is in|
PartType0       HostHalo_TVir_Mass                       Estimate of halo's virial temperature, calculated from the DM halo mass.   T_vir = (MEANMOLIONIZED * PROTONMASS / 3. / BOLTZMANN) * (G * m200 * H(z)) to the power of(2./3.) [K]|
PartType0       InternalEnergy                           Thermal energy per unit mass. Physical u = InternalEnergy U_V to the power of2 [(cm/s) to the power of2]|
PartType0       IronMassFracFromSNIa                     Iron mass from SNIa divided by particle mass. (Initial particle mass for stars)|
PartType0       Mass                                     Particle mass. Physical m = Mass h to the power of-1 U_M [g]|
PartType0       MaximumTemperature                       Maximum temperature ever reached by a particle [K]|
PartType0       MetalMassFracFromAGB                     Metal mass from AGB and their progenitors divided by particle mass. (Initial particle mass for stars)|
PartType0       MetalMassFracFromSNII                    Metal mass from SNII and their progenitors divided by particle mass. (Initial particle mass for stars)|
PartType0       MetalMassFracFromSNIa                    Metal mass from SNIa divided by particle mass. (Initial particle mass for stars)|
PartType0       MetalMassWeightedRedshift                Metal mass weighted redshift at which particle was enriched.|
PartType0       Metallicity                              Mass fraction of elements heavier than Helium|
PartType0       OnEquationOfState                        Star-formation flag. 0 if has never been star-forming, +ve if currently sf, -ve if not currently sf, value indicates aexp at which it obtained its current state|
PartType0       ParticleIDs                              Unique particle identifier|
PartType0       SmoothedElementAbundance/Carbon         ||
PartType0       SmoothedElementAbundance/Helium         ||
PartType0       SmoothedElementAbundance/Hydrogen       ||
PartType0       SmoothedElementAbundance/Iron           ||
PartType0       SmoothedElementAbundance/Magnesium      ||
PartType0       SmoothedElementAbundance/Neon           ||
PartType0       SmoothedElementAbundance/Nitrogen       ||
PartType0       SmoothedElementAbundance/Oxygen         ||
PartType0       SmoothedElementAbundance/Silicon        ||
PartType0       SmoothedIronMassFracFromSNIa             Smoothed mass from SNIa divided by particle mass. (Initial particle mass for stars)|
PartType0       SmoothedMetallicity                      Smoothed mass fraction of elements heavier than Helium|
PartType0       SmoothingLength                          Co-moving smoothing length. Physical h = SmoothingLength h to the power of-1 a U_L [cm]|
PartType0       StarFormationRate                        Gas star formation rate in solar masses / yr|
PartType0       SubGroupNumber                           Subgroup number particle is in|
PartType0       Temperature                              Temperature [K]|
PartType0       TotalMassFromAGB                         Total mass received from AGB and their progenitors|
PartType0       TotalMassFromSNII                        Total mass received from SNII and their progenitors|
PartType0       TotalMassFromSNIa                        Total mass received from SNIa|
PartType0       Velocity                                 Co-moving velocities. Physical v_p = a dx/dt  = Velocities a to the power of1/2 U_V [cm/s]|
                                                          ^
PartType1       Coordinates                              Co-moving coordinates. Physical: r = a x = Coordinates h to the power of-1 a U_L [cm]|
PartType1       GroupNumber                              FoF group number particle is in|
PartType1       ParticleIDs                              Unique particle identifier|
PartType1       SubGroupNumber                           Subgroup number particle is in|
PartType1       Velocity                                 Co-moving velocities. Physical v_p = a dx/dt  = Velocities a to the power of1/2 U_V [cm/s]|
                                                          ^
PartType4        AExpMaximumTemperature                  Expansion factor a when particle had highest temperature|
PartType4        BirthDensity                            Local gas density (physical units)  when a star particle was born. No a-factor correction as the a-factor at birth time is factored in.|
PartType4        Coordinates                             Co-moving coordinates. Physical: r = a x = Coordinates h to the power of-1 a U_L [cm]|
PartType4        ElementAbundance/Carbon                ||
PartType4        ElementAbundance/Helium                ||
PartType4        ElementAbundance/Hydrogen              ||
PartType4        ElementAbundance/Iron                  ||
PartType4        ElementAbundance/Magnesium             ||
PartType4        ElementAbundance/Neon                  ||
PartType4        ElementAbundance/Nitrogen              ||
PartType4        ElementAbundance/Oxygen                ||
PartType4        ElementAbundance/Silicon               ||
PartType4        Feedback_EnergyFraction                 Energy fraction used for SNII feedback (no units).|
PartType4        GroupNumber                             FoF group number particle is in|
PartType4        HostHalo_TVir                           Halo's virial temperature used in Type II SNe feedback [K]|
PartType4        HostHalo_TVir_Mass                      Estimate of halo's virial temperature, calculated from the DM halo mass.   T_vir = (MEANMOLIONIZED * PROTONMASS / 3. / BOLTZMANN) * (G * m200 * H(z)) to the power of(2./3.) [K]|
PartType4        InitialMass                             Star particle mass at formation time. Physical m = InitialMass h to the power of-1 U_M [g]|
PartType4        IronMassFracFromSNIa                    Iron mass from SNIa divided by particle mass. (Initial particle mass for stars)|
PartType4        Mass                                    Particle mass. Physical m = Mass h to the power of-1 U_M [g]|
PartType4        MaximumTemperature                      Maximum temperature ever reached by a particle [K]|
PartType4        MetalMassFracFromAGB                    Metal mass from AGB and their progenitors divided by particle mass. (Initial particle mass for stars)|
PartType4        MetalMassFracFromSNII                   Metal mass from SNII and their progenitors divided by particle mass. (Initial particle mass for stars)|
PartType4        MetalMassFracFromSNIa                   Metal mass from SNIa divided by particle mass. (Initial particle mass for stars)|
PartType4        MetalMassWeightedRedshift               Metal mass weighted redshift at which particle was enriched.|
PartType4        Metallicity                             Mass fraction of elements heavier than Helium|
PartType4        ParticleIDs                             Unique particle identifier|
PartType4        PreviousStellarEnrichment               This is the expansion factor when the star last did enrichment.|
PartType4        SmoothedElementAbundance/Carbon        ||
PartType4        SmoothedElementAbundance/Helium        ||
PartType4        SmoothedElementAbundance/Hydrogen      ||
PartType4        SmoothedElementAbundance/Iron          ||
PartType4        SmoothedElementAbundance/Magnesium     ||
PartType4        SmoothedElementAbundance/Neon          ||
PartType4        SmoothedElementAbundance/Nitrogen      ||
PartType4        SmoothedElementAbundance/Oxygen        ||
PartType4        SmoothedElementAbundance/Silicon       ||
PartType4        SmoothedIronMassFracFromSNIa            Smoothed mass from SNIa divided by particle mass. (Initial particle mass for stars)|
PartType4        SmoothedMetallicity                     Smoothed mass fraction of elements heavier than Helium|
PartType4        SmoothingLength                         Co-moving smoothing length. Physical h = SmoothingLength h to the power of-1 a U_L [cm]|
PartType4        StellarEnrichmentCounter                The counter shows the number of time steps since enrichment was last done.|
PartType4        StellarFormationTime                    Expansion factor a when star particle was born|
PartType4        SubGroupNumber                          Subgroup number particle is in|
PartType4        TotalMassFromAGB                        Total mass received from AGB and their progenitors|
PartType4        TotalMassFromSNII                       Total mass received from SNII and their progenitors|
PartType4        TotalMassFromSNIa                       Total mass received from SNIa|
PartType4        Velocity                                Co-moving velocities. Physical v_p = a dx/dt  = Velocities a to the power of1/2 U_V [cm/s]|
                                                          ^
PartType5        BH_AccretionLength                      BH smoothing length.|
PartType5        BH_CumlAccrMass                         Cumulative mass accreted by largest progenitor of this BH. Physical m = Mass h to the power of-1 U_M [g]|
PartType5        BH_CumlNumSeeds                         Cumulative number of BH seeds swallowed by this BH.|
PartType5        BH_Density                              Co-moving black hole densities. Physical rho = Densities h to the power of2 a to the power of-3 U_M U_L to the power of-3 [g/cm to the power of3]|
PartType5        BH_EnergyReservoir                      Black hole energy reservoir for thermal feedback.|
PartType5        BH_FormationTime                        Expansion factor a when BH particle was born|
PartType5        BH_Mass                                 BH mass. Physical m = Mass h to the power of-1 U_M [g]|
PartType5        BH_Mdot                                 BH accretion rate. Physical mdot = BH_Mdot h to the power of-1 U_M /U_T [g/s]|
PartType5        BH_MostMassiveProgenitorID              Unique ID of the most massive progenitor of this BH. At each merger event, the ID of the most massive of the two merging BHs is stored in this array.|
PartType5        BH_Pressure                             Black hole surrounding gas pressure. Physical P = Pressure h to the power of2 a to the power of(-3*GAMMA) U_M U_V to the power of2 U_L to the power of-3 [g cm to the power of-1 s to the power of-2]|
PartType5        BH_SoundSpeed                           Black hole surrounding gas sound speed. Physical c_snd = C_snd U_V [cm/s]|
PartType5        BH_SurroundingGasVel                    Velocity of the gas surrounding the BH (kernel weighted). Physical Velocity = Velocity a to the power of-1 U_M U_V to the power of [cm/s]|
PartType5        BH_TimeLastMerger                       Expansion factor a when BH particle last accreted an other BH. 0 if the particle as never accreted another BH.                                                       |
PartType5        BH_WeightedDensity                      Co-moving weighted black hole densities. Physical rho = Densities h to the power of2 a to the power of-3 U_M U_L to the power of-3 [g/cm to the power of3]|
PartType5        Coordinates                             Co-moving coordinates. Physical: r = a x = Coordinates h to the power of-1 a U_L [cm]|
PartType5        GroupNumber                             FoF group number particle is in|
PartType5        HostHalo_TVir_Mass                      Estimate of halo's virial temperature, calculated from the DM halo mass.   T_vir = (MEANMOLIONIZED * PROTONMASS / 3. / BOLTZMANN) * (G * m200 * H(z)) to the power of(2./3.) [K]|
PartType5        Mass                                    Particle mass. Physical m = Mass h to the power of-1 U_M [g]                                                                                                                     |
PartType5        ParticleIDs                             Unique particle identifier|
PartType5        SmoothingLength                         Co-moving smoothing length. Physical h = SmoothingLength h to the power of-1 a U_L [cm]|
PartType5        SubGroupNumber                          Subgroup number particle is in|
PartType5        Velocity                                Co-moving velocities. Physical v_p = a dx/dt  = Velocities a to the power of1/2 U_V [cm/s]|
============== ======================================== ==========================================================================================================================================================================================================
