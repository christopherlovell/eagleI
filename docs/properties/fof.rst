FOF arrays
**********

Group numbers begin at 1.  Spherical overdensities associated with a FOF group use the negative of the group number.  A particle can only be associated with one spherical overdensity.

The following arrays can be found in the FOF group files:

======= ======================================== ===========================================================================================================
Group   Array Name                               Description
======= ======================================== ===========================================================================================================
 FOF    BH_Mdot                                   Particle mass. Physical m = Mass h to the power of-1 U_M [g] | 
 FOF    BlackHoleMass                             Particle mass. Physical m = Mass h to the power of-1 U_M [g] | 
 FOF    CentreOfMass                              Co-moving coordinates. Physical: r = a x = Coordinates h to the power of-1 a U_L [cm] | 
 FOF    GroupLength                               Number of particles in this group | 
 FOF    GroupLengthType                           Number of particles in this group of a given type | 
 FOF    GroupMassType                             Particle mass. Physical m = Mass h to the power of-1 U_M [g] | 
 FOF    GroupOffset                               Offset of IDs of this group, starts at 0 | 
 FOF    GroupOffsetType                           Meaning of this variable has not yet been defined. | 
 FOF    Mass                                      Particle mass. Physical m = Mass h to the power of-1 U_M [g] | 
 FOF    NSF/AExpMaximumTemperature                Expansion factor a when particle had highest temperature | 
 FOF    NSF/ElementAbundances/Carbon               | 
 FOF    NSF/ElementAbundances/Helium               | 
 FOF    NSF/ElementAbundances/Hydrogen             | 
 FOF    NSF/ElementAbundances/Iron                 | 
 FOF    NSF/ElementAbundances/Magnesium            | 
 FOF    NSF/ElementAbundances/Neon                 | 
 FOF    NSF/ElementAbundances/Nitrogen             | 
 FOF    NSF/ElementAbundances/Oxygen               | 
 FOF    NSF/ElementAbundances/Silicon              | 
 FOF    NSF/Entropy                               Meaning of this variable has not yet been defined. | 
 FOF    NSF/Mass                                  Particle mass. Physical m = Mass h to the power of-1 U_M [g] | 
 FOF    NSF/MaximumTemperature                    Maximum temperature ever reached by a particle [K] | 
 FOF    NSF/Metallicity                           Mass fraction of elements heavier than Helium | 
 FOF    NSF/SmoothedElementAbundances/Carbon       | 
 FOF    NSF/SmoothedElementAbundances/Helium       | 
 FOF    NSF/SmoothedElementAbundances/Hydrogen     | 
 FOF    NSF/SmoothedElementAbundances/Iron         | 
 FOF    NSF/SmoothedElementAbundances/Magnesium    | 
 FOF    NSF/SmoothedElementAbundances/Neon         | 
 FOF    NSF/SmoothedElementAbundances/Nitrogen     | 
 FOF    NSF/SmoothedElementAbundances/Oxygen       | 
 FOF    NSF/SmoothedElementAbundances/Silicon      | 
 FOF    NSF/SmoothedIronMassFracFromSNIa          Smoothed mass from SNIa divided by particle mass. (Initial particle mass for stars) | 
 FOF    NSF/SmoothedMetallicity                   Smoothed mass fraction of elements heavier than Helium | 
 FOF    NSF/Temperature                           Meaning of this variable has not yet been defined. | 
 FOF    ParticleIDs                               Unique particle identifier | 
 FOF    SF/AExpMaximumTemperature                 Expansion factor a when particle had highest temperature | 
 FOF    SF/ElementAbundaces/Carbon                 | 
 FOF    SF/ElementAbundaces/Helium                 | 
 FOF    SF/ElementAbundaces/Hydrogen               | 
 FOF    SF/ElementAbundaces/Iron                   | 
 FOF    SF/ElementAbundaces/Magnesium              | 
 FOF    SF/ElementAbundaces/Neon                   | 
 FOF    SF/ElementAbundaces/Nitrogen               | 
 FOF    SF/ElementAbundaces/Oxygen                 | 
 FOF    SF/ElementAbundaces/Silicon                | 
 FOF    SF/Entropy                                Meaning of this variable has not yet been defined. | 
 FOF    SF/IronMassFracFromSNIa                   Iron mass from SNIa divided by particle mass. (Initial particle mass for stars) | 
 FOF    SF/Mass                                   Particle mass. Physical m = Mass h to the power of-1 U_M [g] | 
 FOF    SF/MaximumTemperature                     Maximum temperature ever reached by a particle [K] | 
 FOF    SF/Metallicity                            Mass fraction of elements heavier than Helium | 
 FOF    SF/SmoothedElementAbundances/Carbon        | 
 FOF    SF/SmoothedElementAbundances/Helium        | 
 FOF    SF/SmoothedElementAbundances/Hydrogen      | 
 FOF    SF/SmoothedElementAbundances/Iron          | 
 FOF    SF/SmoothedElementAbundances/Magnesium     | 
 FOF    SF/SmoothedElementAbundances/Neon          | 
 FOF    SF/SmoothedElementAbundances/Nitrogen      | 
 FOF    SF/SmoothedElementAbundances/Oxygen        | 
 FOF    SF/SmoothedElementAbundances/Silicon       | 
 FOF    SF/SmoothedIronMassFracFromSNIa           Smoothed mass from SNIa divided by particle mass. (Initial particle mass for stars) | 
 FOF    SF/SmoothedMetallicity                    Smoothed mass fraction of elements heavier than Helium | 
 FOF    SF/Temperature                            Meaning of this variable has not yet been defined. | 
 FOF    StarFormationRate                         Gas star formation rate in solar masses / yr | 
 FOF    Stars/AExpMaximumTemperature              Expansion factor a when particle had highest temperature | 
 FOF    Stars/ElementAbundances/Carbon             | 
 FOF    Stars/ElementAbundances/Helium             | 
 FOF    Stars/ElementAbundances/Hydrogen           | 
 FOF    Stars/ElementAbundances/Iron               | 
 FOF    Stars/ElementAbundances/Magnesium          | 
 FOF    Stars/ElementAbundances/Neon               | 
 FOF    Stars/ElementAbundances/Nitrogen           | 
 FOF    Stars/ElementAbundances/Oxygen             | 
 FOF    Stars/ElementAbundances/Silicon            | 
 FOF    Stars/InitialMass                         Star particle mass at formation time. Physical m = InitialMass h to the power of-1 U_M [g] | 
 FOF    Stars/InitialMassWeightedStellarAge       Expansion factor a when star particle was born | 
 FOF    Stars/IronMassFracFromSNIa                Iron mass from SNIa divided by particle mass. (Initial particle mass for stars) | 
 FOF    Stars/Mass                                Particle mass. Physical m = Mass h to the power of-1 U_M [g] | 
 FOF    Stars/MaximumTemperature                  Maximum temperature ever reached by a particle [K] | 
 FOF    Stars/Metallicity                         Mass fraction of elements heavier than Helium | 
 FOF    Stars/SmootheElementAbundances/Carbon      | 
 FOF    Stars/SmootheElementAbundances/Helium      | 
 FOF    Stars/SmootheElementAbundances/Hydrogen    | 
 FOF    Stars/SmootheElementAbundances/Iron        | 
 FOF    Stars/SmootheElementAbundances/Magnesium   | 
 FOF    Stars/SmootheElementAbundances/Neon        | 
 FOF    Stars/SmootheElementAbundances/Nitrogen    | 
 FOF    Stars/SmootheElementAbundances/Oxygen      | 
 FOF    Stars/SmootheElementAbundances/Silicon     | 
 FOF    Stars/SmoothedIronMassFracFromSNIa        Smoothed mass from SNIa divided by particle mass. (Initial particle mass for stars) | 
 FOF    Stars/SmoothedMetallicity                 Smoothed mass fraction of elements heavier than Helium | 
 FOF    Velocity                                  Co-moving velocities. Physical v_p = a dx/dt  = Velocities a to the power of1/2 U_V [cm/s]((A bug affects this quantity. The correct factor is a^-1 and not a^0.5)) | 
======= ======================================== ===========================================================================================================
