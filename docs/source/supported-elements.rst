Supported Syntax
================

A list of MCNP input files syntax that PyMCNP is currently supporting.

Parsing Support
---------------

===================================================================   =======
Syntax Element                                                        Support
===================================================================   =======
INP                                                                   Partial
INP.Cell                                                              Full
INP.Cell.Geometry                                                     Partial
INP.Cell.Option                                                       Full
INP.Cell.Option.Importance                                            Full
INP.Cell.Option.Volume                                                Full
INP.Cell.Option.Proton Weight                                         Full
INP.Cell.Option.Exponential Transformation                            Full
INP.Cell.Option.Forced Collision                                      Full
INP.Cell.Option.Weight Window Bounds                                  Full
INP.Cell.Option.Dxtran Contribution                                   Full
INP.Cell.Option.Fission Turnoff                                       Full
INP.Cell.Option.Detector Contribution                                 Full
INP.Cell.Option.Gas Thermal Temperature                               Full
INP.Cell.Option.Universe                                              Full
INP.Cell.Option.Coordinate Transformation                             Full
INP.Cell.Option.Lattice                                               Full
INP.Cell.Option.Fill                                                  Full
INP.Cell.Option.EnergyCutoff                                          Full
INP.Cell.Option.Cosy                                                  Full
INP.Cell.Option.Bfield                                                Full
INP.Cell.Option.Uncollided Secondaries                                Full
INP.Surface                                                           Full
INP.Surface.Plane                                                     Full
INP.Surface.Sphere (Centered at Origin)                               Full
INP.Surface.Sphere (General)                                          Full
INP.Surface.Sphere (Centered on x-axis)                               Full
INP.Surface.Sphere (Centered on y-axis)                               Full
INP.Surface.Sphere (Centered on z-axis)                               Full
INP.Surface.Cylinder (Parallel to x-axis)                             Full
INP.Surface.Cylinder (Parallel to y-axis)                             Full
INP.Surface.Cylinder (Parallel to z-axis)                             Full
INP.Surface.Cylinder (On x-axis)                                      Full
INP.Surface.Cylinder (On y-axis)                                      Full
INP.Surface.Cylinder (On z-axis)                                      Full
INP.Surface.Cone (Parallel to x-axis)                                 Full
INP.Surface.Cone (Parallel to y-axis)                                 Full
INP.Surface.Cone (Parallel to z-axis)                                 Full
INP.Surface.Cone (On x-axis)                                          Full
INP.Surface.Cone (On x-axis)                                          Full
INP.Surface.Cone (On x-axis)                                          Full
INP.Surface.Special Quadratic                                         Full
INP.Surface.General Quadratic                                         Full
INP.Surface.Torus (Parallel to x-axis)                                Full
INP.Surface.Torus (Parallel to y-axis)                                Full
INP.Surface.Torus (Parallel to z-axis)                                Full
INP.Surface.Axisymetric Surface (Symmetric about x-axis, 2 Entries)   Full
INP.Surface.Axisymetric Surface (Symmetric about y-axis, 2 Entries)   Full
INP.Surface.Axisymetric Surface (Symmetric about z-axis, 2 Entries)   Full
INP.Surface.Axisymetric Surface (Symmetric about x-axis, 4 Entries)   Full
INP.Surface.Axisymetric Surface (Symmetric about y-axis, 4 Entries)   Full
INP.Surface.Axisymetric Surface (Symmetric about z-axis, 4 Entries)   Full
INP.Surface.Axisymetric Surface (Symmetric about x-axis, 6 Entries)   Full
INP.Surface.Axisymetric Surface (Symmetric about y-axis, 6 Entries)   Full
INP.Surface.Axisymetric Surface (Symmetric about z-axis, 6 Entries)   Full
INP.Surface.Arbitrarily Orident Orthogonal Box (9 Entries)            Full
INP.Surface.Arbitrarily Orident Orthogonal Box (12 Entries)           Full
INP.Surface.Rectangular Parallelepiped                                Full
INP.Surface.Sphere                                                    Full
INP.Surface.Right Circular Cylinder                                   Full
INP.Surface.Right Hexagonal Prism                                     Full
INP.Surface.Right Elliptical Cylinder (10 Entries)                    Full
INP.Surface.Right Elliptical Cylinder (12 Entries)                    Full
INP.Surface.Truncated Right-Angle Cone                                Full
INP.Surface.Ellipsoid                                                 Full
INP.Surface.Wedge                                                     Full
INP.Surface.Arbitrary Polyhedron                                      Full
INP.Data                                                              Full
INP.Data.Cell Volume                                                  Full
INP.Data.Cell Area                                                    Full
INP.Data.Surface Coordinate Transformation                            Full
INP.Data.Cell Coordinate Transormation                                Full
INP.Data.Universe                                                     Full
INP.Data.Lattice                                                      Full
INP.Data.Fill                                                         Full
INP.Data.Stochastic Geometry                                          Full
INP.Data.ZAID Aliases for Deterministic Materials                     Full
INP.Data.Deterministic Adjoint Weight.Window Generator                Full
INP.Data.Embedded Geometry Specification                              Full
INP.Data.Embedded Elemental Edits Control                             Full
INP.Data.Embedded Elemental Edit Energy Bin Boundaries                Full
INP.Data.Embedded Elemental Edit Energy Bin Multipliers               Full
INP.Data.Embedded Elemental Edit Time Bin Boundaries                  Full
INP.Data.Embedded Elemental Edit Time Bin Multiplies                  Full
INP.Data.Material                                                     Full
INP.Data.Material Thermal Neutron Scattering                          Full
INP.Data.Material Nuclide Substitution                                Full
INP.Data.Photonuclear Nuclide Selector                                Full
INP.Data.On.The.Fly Doppler Broadening                                Full
INP.Data.Total Fission                                                Full
INP.Data.Fission Turnoff                                              Full
INP.Data.Atomic Weight                                                Full
INP.Data.Cross-Section File                                           Full
INP.Data.Material Void                                                Full
INP.Data.Multigroup Adjoint Transport Option                          None
INP.Data.Discrete.Reaction Cross Section                              None
INP.Data.Physics Options                                              None
INP.Data.Activation Control                                           None
INP.Data.Cutoffs                                                      None
INP.Data.Cell Cutoffs                                                 None
INP.Data.Free-Gas Thermal Temperature                                 None
INP.Data.Thermal Times                                                None
INP.Data.Lca                                                          None
INP.Data.Lcb                                                          None
INP.Data.Lcc                                                          None
INP.Data.Lea                                                          None
INP.Data.Leb                                                          None
INP.Data.Multiplicity Constants                                       None
INP.Data.Transport Options                                            None
INP.Data.Uncollided Secondaries                                       None
INP.Data.Cosyp                                                        None
INP.Data.Cosy                                                         None
INP.Data.BField                                                       None
INP.Data.Cell BField                                                  None
INP.Data.Gravitational Field                                          None
INP.Data.Source Definition                                            None
INP.Data.Source Information                                           None
INP.Data.Source Probability                                           None
INP.Data.Source Bias                                                  None
INP.Data.Dependent Source Distribution                                None
INP.Data.Source Comment                                               None
INP.Data.Surface Source Write                                         None
INP.Data.Surface Source Read                                          None
INP.Data.Criticality Source                                           None
INP.Data.Criticaliy Calculations Options                              None
INP.Data.Mesh for Shannon Entropy                                     None
INP.Data.Depletion/Burnup                                             None
INP.Data.Source                                                       None
INP.Data.Standard Tallies                                             None
INP.Data.Tally Comment                                                None
INP.Data.Tally Energy                                                 None
INP.Data.Tally Time                                                   None
INP.Data.Tally Cosine                                                 None
INP.Data.Print Hierarchy                                              None
INP.Data.Tally Muliplier                                              None
INP.Data.Dose Energy                                                  None
INP.Data.Dose Function                                                None
INP.Data.Energy Multiplier                                            None
INP.Data.Time Multiplier                                              None
INP.Data.Cosine Multiplier                                            None
INP.Data.Cell Flagging                                                None
INP.Data.Surface Falgging                                             None
INP.Data.Tally Segment                                                None
INP.Data.Segment Divisor                                              None
INP.Data.Special Tally                                                None
INP.Data.User-Supplied Subroutine                                     None
INP.Data.Special Treatments for Tallies                               None
INP.Data.Tally Fluctuation                                            None
INP.Data.Neutral-Particle Detector Contributions                      None
INP.Data.Tally Pertubations.Differential Operator                     None
INP.Data.Reactivity Pertubations.Adjoint Weighting                    None
INP.Data.Sensitivity Coefficents.Adjoint Weighting                    None
INP.Data.Superimposed Mesh Tally A                                    None
INP.Data.Superimposed Mesh Tally B                                    None
INP.Data.Lattice Soeed Takky Enhancement                              None
INP.Data.Cell Importance                                              None
INP.Data.Variance Reducation Control                                  None
INP.Data.Weight-Window Energies                                       None
INP.Data.Weight-Window Times                                          None
INP.Data.Weight-Window Bounds                                         None
INP.Data.Weight-Window Parameter                                      None
INP.Data.Weight-Window Generation                                     None
INP.Data.Weight-Window Generation Energies                            None
INP.Data.Weight-Window Generation Times                               None
INP.Data.Mesh for Weight-Window Generator                             None
INP.Data.Energy Splitting and Roulette                                None
INP.Data.Time SPlitting and ROulette                                  None
INP.Data.Exponential Transform                                        None
INP.Data.Vector Input                                                 None
INP.Data.Forced Collision                                             None
INP.Data.DXTRAN Sphere                                                None
INP.Data.Detector Diagnositcs                                         None
INP.Data.Detector Contribution                                        None
INP.Data.DXTRAN Contribution                                          None
INP.Data.Bremsstrahlung Biasing                                       None
INP.Data.Photo-Production Biasing                                     None
INP.Data.Secondary Particle Biasing                                   None
INP.Data.Photon Weight                                                None
INP.Data.History Cutoff                                               None
INP.Data.Computer Time Cutoff                                         None
INP.Data.Precision Cutoff                                             None
INP.Data.Output Print Tables                                          None
INP.Data.Negate Printing of Tallies                                   None
INP.Data.Print and Dump Cycle                                         None
INP.Data.Particle Track Output                                        None
INP.Data.Plot Tally While Problem is Running                          None
INP.Data.Create LAHET-Compatible Files                                None
INP.Data.Rabdin Bynber Generation                                     None
INP.Data.Debug                                                        None
INP.Data.Lost Particle Control                                        None
INP.Data.Integer Array                                                None
INP.Data.Floating-Point Array                                         None
INP.Data.Devlopers Placeholders                                       None
INP.Data.File Creation                                                None
PTRAC                                                                 Full
PTRAC.Header                                                          Full
PTRAC.Header.KOD VER LODDAT IDTM AID                                  Full
PTRAC.Header.AID                                                      Full
PTRAC.Header.V Line                                                   Full
PTRAC.Header.N Line                                                   Full
PTRAC.Header.L Line                                                   Full
PTRAC.History.I Line                                                  Full
PTRAC.History.J Line                                                  Full
PTRAC.History.P Line                                                  Full
===================================================================   =======

Visualization Support
^^^^^^^^^^^^^^^^^^^^^

===================================================================   =======
Syntax Element                                                        Support
===================================================================   =======
INP.Surface.Plane (General)                                           None
INP.Surface.Plane (Normal to x-axis)                                  None
INP.Surface.Plane (Normal to y-axis)                                  None
INP.Surface.Plane (Normal to z-axis)                                  None
INP.Surface.Sphere (Centered at Origin)                               Full
INP.Surface.Sphere (General)                                          Full
INP.Surface.Sphere (Centered on x-axis)                               Full
INP.Surface.Sphere (Centered on y-axis)                               Full
INP.Surface.Sphere (Centered on z-axis)                               Full
INP.Surface.Cylinder (Parallel to x-axis)                             None
INP.Surface.Cylinder (Parallel to y-axis)                             None
INP.Surface.Cylinder (Parallel to z-axis)                             None
INP.Surface.Cylinder (On x-axis)                                      None
INP.Surface.Cylinder (On y-axis)                                      None
INP.Surface.Cylinder (On z-axis)                                      None
INP.Surface.Cone (Parallel to x-axis)                                 None
INP.Surface.Cone (Parallel to y-axis)                                 None
INP.Surface.Cone (Parallel to z-axis)                                 None
INP.Surface.Cone (On x-axis)                                          None
INP.Surface.Cone (On x-axis)                                          None
INP.Surface.Cone (On x-axis)                                          None
INP.Surface.Special Quadratic                                         None
INP.Surface.General Quadratic                                         None
INP.Surface.Torus (Parallel to x-axis)                                None
INP.Surface.Torus (Parallel to y-axis)                                None
INP.Surface.Torus (Parallel to z-axis)                                None
INP.Surface.Axisymetric Surface (Symmetric about x-axis, 2 Entries)   None
INP.Surface.Axisymetric Surface (Symmetric about y-axis, 2 Entries)   None
INP.Surface.Axisymetric Surface (Symmetric about z-axis, 2 Entries)   None
INP.Surface.Axisymetric Surface (Symmetric about x-axis, 4 Entries)   None
INP.Surface.Axisymetric Surface (Symmetric about y-axis, 4 Entries)   None
INP.Surface.Axisymetric Surface (Symmetric about z-axis, 4 Entries)   None
INP.Surface.Axisymetric Surface (Symmetric about x-axis, 6 Entries)   None
INP.Surface.Axisymetric Surface (Symmetric about y-axis, 6 Entries)   None
INP.Surface.Axisymetric Surface (Symmetric about z-axis, 6 Entries)   None
INP.Surface.Arbitrarily Orident Orthogonal Box (9 Entries)            Full
INP.Surface.Arbitrarily Orident Orthogonal Box (12 Entries)           Full
INP.Surface.Rectangular Parallelepiped                                Full
INP.Surface.Sphere                                                    Full
INP.Surface.Right Circular Cylinder                                   Full
INP.Surface.Right Hexagonal Prism                                     Full
INP.Surface.Right Elliptical Cylinder (10 Entries)                    None
INP.Surface.Right Elliptical Cylinder (12 Entries)                    Full
INP.Surface.Truncated Right.Angle Cone                                Full
INP.Surface.Ellipsoid                                                 Full
INP.Surface.Wedge                                                     Full
INP.Surface.Arbitrary Polyhedron                                      Full
===================================================================   =======
