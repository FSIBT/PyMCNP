# PYMCNP

PYMCNP enables research with Monte Carlo N-Particle (MCNP) simulations. It parses MCNP files, creates MCNP geometry visualization, and runs MCNP in parallel. PYMCNP provides a Python API for MCNP input and output files and a command line interface for interacting with MCNP and MCNP files.

## Description

### MCNP Parsing

PYMCNP enables MCNP INP, PTRAC, MESHTAL, and MCTAL parsing thorough the `pymcnp.files` submodule's `from_mcnp()` and `from_mcnp_file()` entrypoints, providing imperative interfaces for declarative MCNP files.

#### Support

* INP Files: <b style="color: gold;">Partial</b>
	* Cell Cards (Standard): <b style="color: gold;">Partial</b>
	* Cell Cards (Like-But): <b style="color: red;">None</b>
		* Cell Geometry: <b style="color: gold;">Partial</b> (Macrobody facets not supported)
		* Cell Parameters: <b style="color: gold;">Partial</b>
			* Importance (Card Format): <b style="color: limegreen;">Full</b>
			* Volume (Card Format): <b style="color: limegreen;">Full</b>
			* ProtonWeight (Card Format): <b style="color: limegreen;">Full</b>
			* ExponentialTransform (Card Format): <b style="color: limegreen;">Full</b>
			* ForcedCollision (Card Format): <b style="color: limegreen;">Full</b>
			* WeightWindowBounds (Card Format): <b style="color: gold;">Partial</b> (Alternate form not supported)
			* DxtranContribution (Card Format): <b style="color: limegreen;">Full</b>
			* FissionTurnOff (Card Format): <b style="color: limegreen;">Full</b>
			* DetectorContribution (Card Format): <b style="color: limegreen;">Full</b>
			* GasThermalTemperature (Card Format): <b style="color: gold;">Partial</b> (Alternate form not supported)
			* Universe (Card Format): <b style="color: limegreen;">Full</b>
			* CoordinateTransformation (Card Format): <b style="color: limegreen;">Full</b>
			* Lattice (Card Format): <b style="color: limegreen;">Full</b>
			* Fill (Card Format): <b style="color: gold;">Partial</b>
				* Fill (Form #1): <b style="color: gold;">Partial</b> (Optional transformation number not supported)
				* Fill (Form #2): <b style="color: red;">None</b>
			* EnergyCutoff (Card Format): <b style="color: limegreen;">Full</b>
			* Cosy (Card Format): <b style="color: limegreen;">Full</b>
			* Bfield (Card Format): <b style="color: limegreen;">Full</b>:
			* UncolidedSecondaries (Card Format): <b style="color: limegreen;">Full</b>
	* Surface Cards: <b style="color: limegreen;">Full</b>
		* Equation-Defined Surfaces: <b style="color: limegreen;">Full</b>
			* Plane (General): <b style="color: limegreen;">Full</b>
			* Plane (Normal to x-axis): <b style="color: limegreen;">Full</b>
			* Plane (Normal to y-axis): <b style="color: limegreen;">Full</b>
			* Plane (Normal to z-axis): <b style="color: limegreen;">Full</b>
			* Sphere (Centered at Origin): <b style="color: limegreen;">Full</b>
			* Sphere (General): <b style="color: limegreen;">Full</b>
			* Sphere (Centered on x-axis): <b style="color: limegreen;">Full</b>
			* Sphere (Centered on y-axis): <b style="color: limegreen;">Full</b>
			* Sphere (Centered on z-axis): <b style="color: limegreen;">Full</b>
			* Cylinder (Parallel to x-axis): <b style="color: limegreen;">Full</b>
			* Cylinder (Parallel to y-axis): <b style="color: limegreen;">Full</b>
			* Cylinder (Parallel to z-axis): <b style="color: limegreen;">Full</b>
			* Cylinder (On x-axis): <b style="color: limegreen;">Full</b>
			* Cylinder (On y-axis): <b style="color: limegreen;">Full</b>
			* Cylinder (On z-axis): <b style="color: limegreen;">Full</b>
			* Cone (Parallel to x-axis): <b style="color: limegreen;">Full</b>
			* Cone (Parallel to y-axis): <b style="color: limegreen;">Full</b>
			* Cone (Parallel to z-axis): <b style="color: limegreen;">Full</b>
			* Cone (On x-axis): <b style="color: limegreen;">Full</b>
			* Cone (On x-axis): <b style="color: limegreen;">Full</b>
			* Cone (On x-axis): <b style="color: limegreen;">Full</b>
			* Special Quadratic: <b style="color: limegreen;">Full</b>
			* General Quadratic: <b style="color: limegreen;">Full</b>
			* Torus (Parallel to x-axis): <b style="color: limegreen;">Full</b>
			* Torus (Parallel to y-axis): <b style="color: limegreen;">Full</b>
			* Torus (Parallel to z-axis): <b style="color: limegreen;">Full</b>
		* Point-Defined Surface:
			* Axisymmetric Surfaces (Symmetric about x-axis): <b style="color: limegreen;">Full</b>
				* Axisymetric Surface (Symmetric about x-axis, 2 Entries): <b style="color: limegreen;">Full</b>
				* Axisymetric Surface (Symmetric about y-axis, 4 Entries): <b style="color: limegreen;">Full</b>
				* Axisymetric Surface (Symmetric about z-axis, 6 Entries): <b style="color: limegreen;">Full</b>
			* Axisymmetric Surfaces (Symmetric about y-axis): <b style="color: limegreen;">Full</b>
				* Axisymetric Surface (Symmetric about x-axis, 2 Entries): <b style="color: limegreen;">Full</b>
				* Axisymetric Surface (Symmetric about y-axis, 4 Entries): <b style="color: limegreen;">Full</b>
				* Axisymetric Surface (Symmetric about z-axis, 6 Entries): <b style="color: limegreen;">Full</b>
			* Axisymmetric Surfaces (Symmetric about z-axis): <b style="color: limegreen;">Full</b>
				* Axisymetric Surface (Symmetric about x-axis, 2 Entries): <b style="color: limegreen;">Full</b>
				* Axisymetric Surface (Symmetric about y-axis, 4 Entries): <b style="color: limegreen;">Full</b>
				* Axisymetric Surface (Symmetric about z-axis, 6 Entries): <b style="color: limegreen;">Full</b>
			* General Plane: <b style="color: limegreen;">Full</b>
		* Macrobodies: <b style="color: limegreen;">Full</b>
			* Arbitrarily Orident Orthogonal Box: <b style="color: limegreen;">Full</b>
			* Rectangular Parallelepiped: <b style="color: limegreen;">Full</b>
			* Sphere: <b style="color: limegreen;">Full</b>
			* Right Circular Cylinder: <b style="color: limegreen;">Full</b>
			* Right Hexagonal Prism: <b style="color: limegreen;">Full</b>
			* Right Elliptical Cylinder: <b style="color: limegreen;">Full</b>
				* Right Elliptical Cylinder (10 Entries): <b style="color: limegreen;">Full</b>
				* Right Elliptical Cylinder (12 Entries): <b style="color: limegreen;">Full</b>
			* Truncated Right-Angle Cone: <b style="color: limegreen;">Full</b>
			* Ellipsoid: <b style="color: limegreen;">Full</b>
			* Wedge: <b style="color: limegreen;">Full</b>
			* Arbitrary Polyhedron: <b style="color: limegreen;">Full</b>
	* Data Cards: <b style="color: red;">None</b>
		* Cell Volume:: <b style="color: red;">None</b>
		* Cell Area:: <b style="color: red;">None</b>
		* Surface Coordinate Transformation: <b style="color: red;">None</b>
		* Cell Coordinate Transormation: <b style="color: red;">None</b>
		* Universe: <b style="color: red;">None</b>
		* Lattice: <b style="color: red;">None</b>
		* Fill: <b style="color: red;">None</b>
		* Stochastic Geometry: <b style="color: red;">None</b>
		* ZAID Aliases for Deterministic Materials: <b style="color: red;">None</b>
		* Deterministic Adjoint Weight-Window Generator: <b style="color: red;">None</b>
		* Embedded Geometry Specification : <b style="color: red;">None</b>
		* Embedded Elemental Edits Control: <b style="color: red;">None</b>
		* Embedded Elemental Edit Energy Bin Boundaries: <b style="color: red;">None</b>
		* Embedded Elemental Edit Energy Bin Multipliers: <b style="color: red;">None</b>
		* Embedded Elemental Edit Time Bin Boundaries: <b style="color: red;">None</b>
		* Embedded Elemental Edit Time Bin Multiplies: <b style="color: red;">None</b>
		* Material: <b style="color: red;">None</b>
		* Material Thermal Neutron Scattering: <b style="color: red;">None</b>
		* Material Nuclide Substitution: <b style="color: red;">None</b>
		* Photonuclear Nuclide Selector: <b style="color: red;">None</b>
		* On-The-Fly Doppler Broadening: <b style="color: red;">None</b>
		* Total Fission: <b style="color: red;">None</b>
		* Fission Turnoff: <b style="color: red;">None</b>
		* Atomic Weight: <b style="color: red;">None</b>
		* Cross-Section File: <b style="color: red;">None</b>
		* Material Void: <b style="color: red;">None</b>
		* Multigroup Adjoint Transport Option: <b style="color: red;">None</b>
		* Discrete-Reaction Cross Section: <b style="color: red;">None</b>
		* Physics Options: <b style="color: red;">None</b>
		* Activation Control: <b style="color: red;">None</b>
		* Cutoffs: <b style="color: red;">None</b>
		* Cell Cutoffs: <b style="color: red;">None</b>
		* Free-Gas Thermal Temperature: <b style="color: red;">None</b>
		* Thermal Times: <b style="color: red;">None</b>
		* Lca: <b style="color: red;">None</b>
		* Lcb: <b style="color: red;">None</b>
		* Lcc: <b style="color: red;">None</b>
		* Lea: <b style="color: red;">None</b>
		* Leb: <b style="color: red;">None</b>
		* Multiplicity Constants: <b style="color: red;">None</b>
		* Transport Options : <b style="color: red;">None</b>
		* Uncollided Secondaries: <b style="color: red;">None</b>
		* Cosyp: <b style="color: red;">None</b>
		* Cosy: <b style="color: red;">None</b>
		* BField: <b style="color: red;">None</b>
		* Cell BField: <b style="color: red;">None</b>
		* Gravitational Field: <b style="color: red;">None</b>
		* Source Definition: <b style="color: red;">None</b>
		* Source Information: <b style="color: red;">None</b>
		* Source Probability: <b style="color: red;">None</b>
		* Source Bias: <b style="color: red;">None</b>
		* Dependent Source Distribution: <b style="color: red;">None</b>
		* Source Comment: <b style="color: red;">None</b>
		* Surface Source Write: <b style="color: red;">None</b>
		* Surface Source Read: <b style="color: red;">None</b>
		* Criticality Source: <b style="color: red;">None</b>
		* Criticaliy Calculations Options=: <b style="color: red;">None</b>
		* Mesh for Shannon Entropy: <b style="color: red;">None</b>
		* Depletion/Burnup: <b style="color: red;">None</b>
		* Source: <b style="color: red;">None</b>
		* Standard Tallies: <b style="color: red;">None</b>
		* Tally Comment: <b style="color: red;">None</b>
		* Tally Energy: <b style="color: red;">None</b>
		* Tally Time: <b style="color: red;">None</b>
		* Tally Cosine: <b style="color: red;">None</b>
		* Print Hierarchy: <b style="color: red;">None</b>
		* Tally Muliplier: <b style="color: red;">None</b>
		* Dose Energy: <b style="color: red;">None</b>
		* Dose Function: <b style="color: red;">None</b>
		* Energy Multiplier: <b style="color: red;">None</b>
		* Time Multiplier: <b style="color: red;">None</b>
		* Cosine Multiplier: <b style="color: red;">None</b>
		* Cell Flagging: <b style="color: red;">None</b>
		* Surface Falgging: <b style="color: red;">None</b>
		* Tally Segment: <b style="color: red;">None</b>
		* Segment Divisor: <b style="color: red;">None</b>
		* Special Tally: <b style="color: red;">None</b>
		* User-Supplied Subroutine: <b style="color: red;">None</b>
		* Special Treatments for Tallies: <b style="color: red;">None</b>
		* Tally Fluctuation: <b style="color: red;">None</b>
		* Neutral-Particle Detector Contributions: <b style="color: red;">None</b>
		* Tally Pertubations-Differential Operator: <b style="color: red;">None</b>
		* Reactivity Pertubations-Adjoint Weighting: <b style="color: red;">None</b>
		* Sensitivity Coefficents-Adjoint Weighting: <b style="color: red;">None</b>
		* Superimposed Mesh Tally A: <b style="color: red;">None</b>
		* Superimposed Mesh Tally B: <b style="color: red;">None</b>
		* Lattice Soeed Takky Enhancement: <b style="color: red;">None</b>
		* Cell Importance: <b style="color: red;">None</b>
		* Variance Reducation Control: <b style="color: red;">None</b>
		* Weight-Window Energies: <b style="color: red;">None</b>
		* Weight-Window Times: <b style="color: red;">None</b>
		* Weight-Window Bounds: <b style="color: red;">None</b>
		* Weight-Window Parameter: <b style="color: red;">None</b>
		* Weight-Window Generation: <b style="color: red;">None</b>
		* Weight-Window Generation Energies: <b style="color: red;">None</b>
		* Weight-Window Generation Times: <b style="color: red;">None</b>
		* Mesh for Weight-Window Generator: <b style="color: red;">None</b>
		* Energy Splitting and Roulette: <b style="color: red;">None</b>
		* Time SPlitting and ROulette: <b style="color: red;">None</b>
		* Exponential Transform: <b style="color: red;">None</b>
		* Vector Input: <b style="color: red;">None</b>
		* Forced Collision: <b style="color: red;">None</b>
		* DXTRAN Sphere: <b style="color: red;">None</b>
		* Detector Diagnositcs: <b style="color: red;">None</b>
		* Detector Contribution: <b style="color: red;">None</b>
		* DXTRAN Contribution: <b style="color: red;">None</b>
		* Bremsstrahlung Biasing: <b style="color: red;">None</b>
		* Photo-Production Biasing: <b style="color: red;">None</b>
		* Secondary Particle Biasing: <b style="color: red;">None</b>
		* Photon Weight: <b style="color: red;">None</b>
		* History Cutoff: <b style="color: red;">None</b>
		* Computer Time Cutoff: <b style="color: red;">None</b>
		* Precision Cutoff: <b style="color: red;">None</b>
		* Output Print Tables: <b style="color: red;">None</b>
		* Negate Printing of Tallies: <b style="color: red;">None</b>
		* Print and Dump Cycle: <b style="color: red;">None</b>
		* Particle Track Output: <b style="color: red;">None</b>
		* Plot Tally While Problem is Running: <b style="color: red;">None</b>
		* Create LAHET-Compatible Files: <b style="color: red;">None</b>
		* Rabdin Bynber Generation: <b style="color: red;">None</b>
		* Debug: <b style="color: red;">None</b>
		* Lost Particle Control: <b style="color: red;">None</b>
		* Integer Array: <b style="color: red;">None</b>
		* Floating-Point Array: <b style="color: red;">None</b>
		* Devlopers Placeholders: <b style="color: red;">None</b>
		* File Creation: <b style="color: red;">None</b>

### Cadquery Visualization

PYMCNP enables MCNP surface geometry visualization through the `to_cadquery()` and `to_cadquery_file()` endpoints in the `pymcnp.files` submodule.

#### Support

Currently, PYMCNP only generates cadquery for bounded surfaces.

* Equation-Defined Surfaces: <b style="color: gold;">Partial</b>
	* Plane: <b style="color: red;">None</b>
	* Sphere: <b style="color: limegreen;">Full</b>
	* Cylinder: <b style="color: red;">None</b>
	* Cone: <b style="color: red;">None</b>
	* Special Quadratic: <b style="color: red;">None</b>
	* General Quadratic: <b style="color: red;">None</b>
	* Torus: <b style="color: red;">None</b>
* Point-Defined Surfaces: <b style="color: red;">None</b>
	* Axisymetric Surface: <b style="color: red;">None</b>
		* Axisymetric Surface (2 Entries): <b style="color: red;">None</b>
		* Axisymetric Surface (4 Entries): <b style="color: red;">None</b>
		* Axisymetric Surface (6 Entries): <b style="color: red;">None</b>
	* General Plane: <b style="color: red;">None</b>
* Macrobodies: <b style="color: gold;">Partial</b>	
	* Arbitrarily Orident Orthogonal Box: <b style="color: gold;">Partial</b>
		* Arbitrarily Orident Orthogonal Box (9 Entires): <b style="color: red;">None</b>
		* Arbitrarily Orident Orthogonal Box (12 Entries): <b style="color: limegreen;">Full</b>
	* Rectangular Parallelepiped: <b style="color: limegreen;">Full</b>
	* Sphere: <b style="color: limegreen;">Full</b>
	* Right Circular Cylinder: <b style="color: limegreen;">Full</b>
	* Right Hexagonal Prism: <b style="color: gold;">Partial</b>
		* Right Hexagonal Prism (9 Entires): <b style="color: red;">None</b>
		* Right Hexagonal Prism (15 Entries): <b style="color: limegreen;">Full</b>
	* Right Elliptical Cylinder: <b style="color: limegreen;">Full</b>
		* Right Elliptical Cylinder (10 Entries): <b style="color: limegreen;">Full</b>
		* Right Elliptical Cylinder (12 Entries): <b style="color: limegreen;">Full</b>
	* Truncated Right-Angle Cone: <b style="color: limegreen;">Full</b>
	* Ellipsoid: <b style="color: limegreen;">Full</b>
	* Wedge: <b style="color: limegreen;">Full</b>
	* Arbitrary Polyhedron: <b style="color: limegreen;">Full</b>

## Installation

### PYMCNP

To install PYMCNP (1) download PYMCNP from [Github](https://github.com/mauricioAyllon/MCNP-tools/tree/master/src/mcnptools), and (2) run the following command inside pymcnp.

```
pip install -e .
```
