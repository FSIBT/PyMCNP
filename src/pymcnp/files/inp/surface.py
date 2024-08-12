"""
'surface' contains the class representing surface cards.

'surface' packages the 'Surface' class, providing an importable interface
for surface cards.
"""


import numpy as np

import math
from typing import *
from enum import StrEnum

from .card import Card
from .._utils import parser
from .._utils import errors
from .._utils import types


class Surface(Card):
	"""
	'Surface' represents surface cards.

	'Surface' abstracts the surface card syntax element and it
	encapsulates all functionallity for parsing surface cards.

	Attributes:
		number: Surface card number.
		mnemonic: Surface card type identifier.
		transform: Surface card transformation number.
		periodic: Surface card periodic number.
		parameters: Surface parameter list based on mnemonic.
	"""


	class SurfaceMnemonic(StrEnum):
		"""
		'SurfaceMnemonic' represents surface card mnemoincs.

		'SurfaceMnemonic' functions as a data types for surface
		cards. It selects between 'Surface' subclasses. It 
		represents surface card mnemonics as abstract syntax elements.
		"""


		PLANEGENERAL = 'p'
		PLANENORMALX = 'px'
		PLANENORMALY = 'py'
		PLANENORMALZ = 'pz'
		SPHEREORIGIN = 'so'
		SPHEREGENERAL = 's'
		SPHERENORMALX = 'sx'
		SPHERENORMALY = 'sy'
		SPHERENORMALZ = 'sz'
		CYLINDERPARALLELX = 'c/x'
		CYLINDERPARALLELY = 'c/y'
		CYLINDERPARALLELZ = 'c/z'
		CYLINDERONX = 'cx'
		CYLINDERONY = 'cy'
		CYLINDERONZ = 'cz'
		CONEPARALLELX = 'k/x'
		CONEPARALLELY = 'k/y'
		CONEPARALLELZ = 'k/z'
		CONEONX = 'kx'
		CONEONY = 'ky'
		CONEONZ = 'kx'
		QUADRATICSPECIAL = 'sq'
		QUADRATICGENERAL = 'gq'
		TORUSPARALLELX = 'tx'
		TORUSPARALLELY = 'ty'
		TORUSPARALLELZ = 'tz'
		SURFACEX = 'x'
		SURFACEY = 'y'
		SURFACEZ = 'z'
		BOX = 'box'
		PARALLELEPIPED = 'rpp'
		SPHERE = 'sph'
		CYLINDERCIRCULAR = 'rcc'
		HEXAGONALPRISM = 'rhp'
		CYLINDERELLIPTICAL = 'rec'
		CONETRUNCATED = 'trc'
		ELLIPSOID = 'ell'
		WEDGE = 'wed'
		POLYHEDRON = 'arb'

		
		@classmethod
		def cast_surface_mnemonic(cls, string: str, hook: Callable[Self, bool] = lambda _: True) -> Self:
			"""
			'cast_surface_mnemonic' types casts from strings to surface mnemoincs.

			'cast_surface_mnemonic' creates surface mnemonic objects from
			strings. If the stirng is invalid or the hook returns false, it
			returns None.

			Returns:
				Cell parameter keyword from string.
			"""

			string = string.lower()

			try:
				keyword = cls(string)

				if hook(keyword):
					return keyword
			except:
				pass

			return None


	def __init__(self) -> Self:
		"""
		'__init__' initializes 'Surface'.
		"""

		super().__init__()

		self.number: int = None
		self.mnemonic: str = None
		self.is_white_boundary: bool = False
		self.is_reflecting: bool = False
		self.transform: int = None
		self.periodic: int = None
		self.parameters: dict[str, float] = {}


	def set_number(self, number: int):
		"""
		'set_number' sets surface card number.

		'set_number' checks numbers are greater than
		or equal to 1 and less than or equal to 99,999,999. 
		It raises errors if given None.

		Parameters:
			number: Surface card number.

		Raises:
			MCNPSemanticError: Invalid surface card number.
		"""

		if number is None or not (1 <= number <= 99_999_999): 
			raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_NUMBER)
		
		self.number = number
		self.id = number


	def set_mnemonic(self, mnemonic: SurfaceMnemonic):
		"""
		'set_mnemonic' sets surface card mnemoincs.

		'set_mnemonic' checks are valid. It raises errors
		if given None.

		Parameters:
			mnemonic: Surface card mnemonic.

		Raises:
			MCNPSemanticError: Invalid surface card mnemonic.
		"""

		if mnemonic is None: 
			raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_MNEMONIC)

		self.mnemonic = mnemonic


	def set_transform_periodic(self, transform_periodic: int):
		"""
		'set_transform_periodic' sets surface card transform/periodic numbers.

		'set_transform_periodic' checks are greater than or equal to -99,999,999
		and less than or equal to 999. It raises errors if given None.

		Parameters:
			transform_periodic: Surface card transform/periodic numbers.

		Raises:
			MCNPSemanticError: Invalid surface card transform/periodic numbers.
		"""

		if transform_periodic is None or not (-99_999_999 <= transform_periodic <= 999):
			raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_TRANSFORMPERIODIC)

		if transform_periodic < 0:
			self.periodic = transform_periodic
			self.transform = None
		elif transform_periodic > 0:
			self.periodic = None
			self.transform = transform_periodic
		elif transform_periodic == 0:
			self.periodic = None
			self.transform = None
		else:
			assert False


	@classmethod
	def from_mcnp(cls, source: str) -> Self:
		"""
		'from_mcnp' generates surface card objects from INP.

		'from_mcnp' constructs instances of 'Surface' from INP 
		strings, so it functions as a class constructor.

		Parameters:
			surface: INP to parse.

		Returns:
			Surface card object.

		Raises:
			MCNPSemanticError: Invalid surface card values.
			MCNPSyntaxError: Invalid surface card syntax.
		"""

		surface = cls()

		source = parser.Preprocessor.process_inp(source)
		tokens = parser.Parser(SyntaxError).from_string(source, ' ')
		
		# Processing Reflecting Prefix
		if tokens.peekl()[0] == '+':
			self.is_white_boundary = True
			tokens.pushl(tokens.popl()[1:])
		elif tokens.peekl()[0] == '*':
			self.is_reflecting_number = True
			tokens.pushl(tokens.popl()[1:])

		# Processing Card Number
		value = types.cast_fortran_integer(tokens.popl())
		surface.set_number(value)

		# Processing Transformation Number
		value = types.cast_fortran_integer(tokens.peekl())
		if value is not None:
			surface.set_transform_periodic(value)
			tokens.popl()

		# Processing Mnemonic
		value = cls.SurfaceMnemonic.cast_surface_mnemonic(tokens.popl()) 
		surface.set_mnemonic(value)

		# Processing Parameters
		match surface.mnemonic:
			case 'p':
				if len(tokens) not in {4, 9}: raise SyntaxError
				surface.__class__ = PlaneGeneral
				if len(tokens) == 4:
					surface.set_parameters_equation(*tokens.deque)
				elif len(tokens) == 9:
					surface.set_parameters_points(*tokens.deque)
				else:
					assert False
			case 'px':
				if len(tokens) != 1: raise SyntaxError
				surface.__class__ = PlaneNormalX
				surface.set_parameters(*tokens.deque)
			case 'py':
				if len(tokens) != 1: raise SyntaxError
				surface.__class__ = PlaneNormalY
				surface.set_parameters(*tokens.deque)
			case 'pz':
				if len(tokens) != 1: raise SyntaxError
				surface.__class__ = PlaneNormalZ
				surface.set_parameters(*tokens.deque)
			case 'so':
				if len(tokens) != 1: raise SyntaxError
				surface.__class__ = SphereOrigin
				surface.set_parameters(*tokens.deque)
			case 's':
				if len(tokens) != 4: raise SyntaxError
				surface.__class__ = SphereGeneral
				surface.set_parameters(*tokens.deque)
			case 'sx':
				if len(tokens) != 2: raise SyntaxError
				surface.__class__ = SphereNormalX
				surface.set_parameters(*tokens.deque)
			case 'sy':
				if len(tokens) != 2: raise SyntaxError
				surface.__class__ = SphereNormalY
				surface.set_parameters(*tokens.deque)
			case 'sz':
				if len(tokens) != 2: raise SyntaxError
				surface.__class__ = SphereNormalZ
				surface.set_parameters(*tokens.deque)
			case 'c/x':
				if len(tokens) != 3: raise SyntaxError
				surface.__class__ = CylinderParallelX
				surface.set_parameters(*tokens.deque)
			case 'c/y':
				if len(tokens) != 3: raise SyntaxError
				surface.__class__ = CylinderParallelY
				surface.set_parameters(*tokens.deque)
			case 'c/z':
				if len(tokens) != 3: raise SyntaxError
				surface.__class__ = CylinderParallelZ
				surface.set_parameters(*tokens.deque)
			case 'cx':
				if len(tokens) != 1: raise SyntaxError
				surface.__class__ = CylinderOnX
				surface.set_parameters(*tokens.deque)
			case 'cy':
				if len(tokens) != 1: raise SyntaxError
				surface.__class__ = CylinderOnY
				surface.set_parameters(*tokens.deque)
			case 'cz':
				if len(tokens) != 1: raise SyntaxError
				surface.__class__ = CylinderOnZ
				surface.set_parameters(*tokens.deque)
			case 'k/x':
				if len(tokens) != 5: raise SyntaxError
				surface.__class__ = ConeParallelX
				surface.set_parameters(*tokens.deque)
			case 'k/y':
				if len(tokens) != 5: raise SyntaxError
				surface.__class__ = ConeParallelY
				surface.set_parameters(*tokens.deque)
			case 'k/z':
				if len(tokens) != 5: raise SyntaxError
				surface.__class__ = ConeParallelZ
				surface.set_parameters(*tokens.deque)
			case 'kx':
				if len(tokens) != 3: raise SyntaxError
				surface.__class__ = ConeOnX
				surface.set_parameters(*tokens.deque)
			case 'ky':
				if len(tokens) != 3: raise SyntaxError
				surface.__class__ = ConeOnY
				surface.set_parameters(*tokens.deque)
			case 'kx':
				if len(tokens) != 3: raise SyntaxError
				surface.__class__ = ConeOnZ
				surface.set_parameters(*tokens.deque)
			case 'sq':
				if len(tokens) != 10: raise SyntaxError
				surface.__class__ = QuadraticSpecial
				surface.set_parameters(*tokens.deque)
			case 'gq':
				if len(tokens) != 10: raise SyntaxError
				surface.__class__ = QuadraticGeneral
				surface.set_parameters(*tokens.deque)
			case 'tx':
				if len(tokens) != 6: raise SyntaxError
				surface.__class__ = TorusParallelX
				surface.set_parameters(*tokens.deque)
			case 'ty':
				if len(tokens) != 6: raise SyntaxError
				surface.__class__ = TorusParallelY
				surface.set_parameters(*tokens.deque)
			case 'tz':
				if len(tokens) != 6: raise SyntaxError
				surface.__class__ = TorusParallelZ
				surface.set_parameters(*tokens.deque)
			case 'x':
				if len(tokens) not in {2, 4, 6}: raise SyntaxError
				surface.__class__ = SurfaceX
				surface.set_parameters(*(list(tokens.deque) + [None] * (6 - len(tokens))))
			case 'y':
				if len(tokens) not in {2, 4, 6}: raise SyntaxError
				surface.__class__ = SurfaceY
				surface.set_parameters(*(list(tokens.deque) + [None] * (6 - len(tokens))))
			case 'z':
				if len(tokens) not in {2, 4, 6}: raise SyntaxError
				surface.__class__ = SurfaceZ
				surface.set_parameters(*(list(tokens.deque) + [None] * (6 - len(tokens))))
			case 'box':
				if len(tokens) not in {12, 9}: raise SyntaxError
				surface.__class__ = Box
				surface.set_parameters(*(list(tokens.deque) + [None] * (12 - len(tokens))))
			case 'rpp':
				if len(tokens) != 6: raise SyntaxError
				surface.__class__ = Parallelepiped
				surface.set_parameters(*tokens.deque)
			case 'sph':
				if len(tokens) != 4: raise SyntaxError
				surface.__class__ = Sphere
				surface.set_parameters(*tokens.deque)
			case 'rcc':
				if len(tokens) != 7: raise SyntaxError
				surface.__class__ = CylinderCircular
				surface.set_parameters(*tokens.deque)
			case 'rhp' | 'hex':
				if len(tokens) not in {15, 9}: raise SyntaxError
				surface.__class__ = HexagonalPrism
				surface.set_parameters(*(list(tokens.deque) + [None] * (15 - len(tokens))))
			case 'rec':
				if len(tokens) not in {10, 12}: raise SyntaxError
				surface.__class__ = CylinderElliptical
				surface.set_parameters(*(list(tokens.deque) + [None] * (12 - len(tokens))))
			case 'trc':
				if len(tokens) != 8: raise SyntaxError
				surface.__class__ = ConeTruncated
				surface.set_parameters(*tokens.deque)
			case 'ell':
				if len(tokens) != 7: raise SyntaxError
				surface.__class__ = Ellipsoid
				surface.set_parameters(*tokens.deque)
			case 'wed':
				if len(tokens) != 12: raise SyntaxError
				surface.__class__ = Wedge
				surface.set_parameters(*tokens.deque)
			case 'arb':
				if len(tokens) != 30: raise SyntaxError
				surface.__class__ = Polyhedron
				surface.set_parameters(*tokens.deque)
			
		return surface


	def to_mcnp(self) -> str:
		"""
		'to_mcnp' generates from surface card objects.

		'to_mcnp' provides an MCNP endpoints for writing INP
		source strings.

		Returns:
			INP for surface card object.
		"""

		parameters_str = ' '.join([str(param) for _, param in self.parameters.items()])
		source = f"{self.number}{' ' + {self.transform} + ' ' if self.transform is not None else ' '}{self.mnemonic} {parameters_str}"

		return parser.Postprocessor.add_continuation_lines(source)


	def to_arguments(self) -> dict:
		"""
		'to_arguments' generates dictionary from surface card objects.

		'to_arguments' creates dictionaries whose keys are 
		attribute names, and whose values are attribute value.

		Returns:
			Dictionary for surface card object.
		"""

		return {'j': self.number, 'n': self.transform, 'A': self.mnemonic, 'list': self.parameters}


class PlaneGeneral(Surface):
	"""
	'PlaneGeneral' represents general planes surface cards.

	'PlaneGeneral' functions as a data subtype for 'Surface'. It
	represents cell card parameter as abstract syntax 
	elements.
	"""


	def __init__(self) -> Self:
		"""
		'__init__' initializes 'PlaneGeneral'.
		"""

		self.a: float = None
		self.b: float = None
		self.c: float = None
		self.d: float = None
		self.x1: float = None
		self.y1: float = None
		self.z1: float = None
		self.x2: float = None
		self.y2: float = None
		self.z2: float = None
		self.x3: float = None
		self.y3: float = None
		self.z3: float = None

		super().__init__()


	def set_parameters_equation(self, a: float, b: float, c: float, d: float) -> None:
		"""
		'set_parameters_equation' sets general planes parameters.

		'set_parameters_equation' checks parameter entries for the equation
		definition are valid floating points. It raises errors if given None.

		Parameters:
			a: Plane equation A coefficent.
			b: Plane equation B coefficent.
			c: Plane equation C coefficent.
			d: PLane equation D coefficent.
		"""

		value = types.cast_fortran_real(a)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.a = value
		self.parameters['a'] = value
		
		value = types.cast_fortran_real(b)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.b = value
		self.parameters['b'] = value

		value = types.cast_fortran_real(c)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.c = value
		self.parameters['c'] = value

		value = types.cast_fortran_real(d)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.d = value
		self.parameters['d'] = value


	def set_parameters_points(self, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float, x3: float, y3: float, z3: float) -> None:
		"""
		'set_parameters_points' sets general planes parameters.

		'set_parameters_points' checks parameter entries for the point
		definition are valid floating points. It raises errors if given None.

		Parameters:
			x1: Point #1 x component.
			y1: Point #1 y component.
			z1: Point #1 z component.
			x2: Point #2 x component.
			y2: Point #2 y component.
			z2: Point #2 z component.
			x3: Point #3 x component.
			y3: Point #3 y component.
			z3: Point #3 z component.
		"""
 
		value = types.cast_fortran_real(x1)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.x1 = value
		self.parameters['x1'] = value 

		value = types.cast_fortran_real(y1)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.y1 = value
		self.parameters['y1'] = value 

		value = types.cast_fortran_real(z1)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.z1 = value
		self.parameters['z1'] = value 

		value = types.cast_fortran_real(x2)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.x2 = value
		self.parameters['x2'] = value 

		value = types.cast_fortran_real(y2)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.y2 = value
		self.parameters['y2'] = value 

		value = types.cast_fortran_real(z2)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.z2 = value
		self.parameters['z2'] = value 

		value = types.cast_fortran_real(x3)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.x3 = value
		self.parameters['x3'] = value 

		value = types.cast_fortran_real(y3)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.y3 = value
		self.parameters['y3'] = value 

		value = types.cast_fortran_real(z3)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.z3 = value
		self.parameters['z3'] = value


class PlaneNormalX(Surface):
	"""
	'PlaneNormalX' represents planes normal to the x-axis surface cards.

	'PlaneNormalX' functions as a data subtype for 'Surface'. It
	represents cell card parameter as abstract syntax 
	elements.
	"""


	def __init__(self) -> Self:
		"""
		'__init__' initializes 'PlaneNormalX'.
		"""

		self.d: float = None

		super().__init__()


	def set_parameters(self, d: float) -> None:
		"""
		'set_parameters' sets planes normal to the x-axis parameters.

		'set_parameters' checks parameter entries are valid 
		floating points. It raises errors if given None.

		'set_parameters' checks entries are valid floats.

		'set_parameters' checks parameter entries are valid 
		floating points. It raises errors if given None.
		It raises None if given None on required entries.

		Parameters:
			d: Plane equation D coefficent.
		"""

		value = types.cast_fortran_real(d)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.d = value
		self.parameters['d'] = value


class PlaneNormalY(Surface):
	"""
	'PlaneNormalY' represents planes normal to the y-axis surface cards.

	'PlaneNormalY' functions as a data subtype for 'Surface'. It
	represents cell card parameter as abstract syntax 
	elements.
	"""


	def __init__(self) -> Self:
		"""
		'__init__' initializes 'PlaneNormalY'.
		"""

		self.d: float = None

		super().__init__()


	def set_parameters(self, d: float) -> None:
		"""
		'set_parameters' sets planes normal to the y-axis parameters.

		'set_parameters' checks parameter entries are valid 
		floating points. It raises errors if given None.

		'set_parameters' checks entries are valid floats.

		'set_parameters' checks parameter entries are valid 
		floating points. It raises errors if given None.
		It raises None if given None on required entries.

		Parameters:
			d: Plane equation D coefficent.
		"""

		value = types.cast_fortran_real(d)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.d = value
		self.parameters['d'] = value


class PlaneNormalZ(Surface):
	"""
	'PlaneNormalZ' represents planes normal to the z-axis surface cards.

	'PlaneNormalZ' functions as a data subtype for 'Surface'. It
	represents cell card parameter as abstract syntax 
	elements.
	"""


	def __init__(self) -> Self:
		"""
		'__init__' initializes 'PlaneNormalZ'.
		"""

		self.d: float = None

		super().__init__()


	def set_parameters(self, d: float) -> None:
		"""
		'set_parameters' sets planes normal to the z-axis parameters.

		'set_parameters' checks parameter entries are valid 
		floating points. It raises errors if given None.

		'set_parameters' checks entries are valid floats.

		'set_parameters' checks parameter entries are valid 
		floating points. It raises errors if given None.
		It raises None if given None on required entries.

		Parameters:
			d: Plane equation D coefficent.
		"""

		value = types.cast_fortran_real(d)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.d = value
		self.parameters['d'] = value


class SphereOrigin(Surface):
	"""
	'SphereOrigin' represents origin-centered spheres surface cards.

	'SphereOrigin' functions as a data subtype for 'Surface'. It
	represents cell card parameter as abstract syntax 
	elements.
	"""


	def __init__(self) -> Self:
		"""
		'__init__' initializes 'SphereOrigin'.
		"""

		self.r: float = None

		super().__init__()


	def set_parameters(self, r: float) -> None:
		"""
		'set_parameters' sets origin-centered spheres parameters.

		'set_parameters' checks parameter entries are valid 
		floating points. It raises errors if given None.

		Parameters:
			r: Sphere radius.
		"""

		value = types.cast_fortran_real(r)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.r = value
		self.parameters['r'] = value


	def to_cadquery(self, hasHeader: bool = False) -> str:
		"""
		'to_cadquery' generates cadquery from surface card objects.

		'to_cadquery' provides a Cadquery endpoints for writing Cadquery
		source strings and later displaying geometries.

		Parameters:
			hasHeader: Boolean to include cadquery header.

		Returns:
			Cadquery for surface card object.
		"""

		cadquery = 'import cadquery as cq\n\n' if hasHeader else ''

		cadquery += f"surface_{self.number} = cq.Workplane().sphere({self.parameters['r']})\n"

		return cadquery


class SphereGeneral(Surface):
	"""
	'SphereGeneral' represents general spheres surface cards.

	'SphereGeneral' functions as a data subtype for 'Surface'. It
	represents cell card parameter as abstract syntax 
	elements.
	"""


	def __init__(self) -> Self:
		"""
		'__init__' initializes 'SphereGeneral'.
		"""

		self.x: float = None
		self.y: float = None
		self.z: float = None
		self.r: float = None

		super().__init__()


	def set_parameters(self, x: float, y: float, z: float, r: float) -> None:
		"""
		'set_parameters' sets general spheres parameters.

		'set_parameters' checks parameter entries are valid 
		floating points. It raises errors if given None.

		Parameters:
			x: Sphere center x component.
			y: Sphere center y component.
			z: Sphere center z component.
			r: Sphere radius.
		"""

		value = types.cast_fortran_real(x)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.x = value
		self.parameters['x'] = value

		value = types.cast_fortran_real(y)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.y = value
		self.parameters['y'] = value

		value = types.cast_fortran_real(z)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.z = value
		self.parameters['z'] = value

		value = types.cast_fortran_real(r)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.r = value
		self.parameters['r'] = value


	def to_cadquery(self, hasHeader: bool = False) -> str:
		"""
		'to_cadquery' generates cadquery from surface card objects.

		'to_cadquery' provides a Cadquery endpoints for writing Cadquery
		source strings and later displaying geometries.

		Parameters:
			hasHeader: Boolean to include cadquery header.

		Returns:
			Cadquery for surface card object.
		"""

		cadquery = 'import cadquery as cq\n\n' if hasHeader else ''

		cadquery += f"surface_{self.number} = cq.Workplane().sphere({self.parameters['r']}).translate(({self.parameters['x']}, {self.parameters['y']}, {self.parameters['z']}))\n"

		return cadquery


class SphereNormalX(Surface):
	"""
	'SphereNormalX' represents spheres on x-axis surface cards.

	'SphereNormalX' functions as a data subtype for 'Surface'. It
	represents cell card parameter as abstract syntax 
	elements.
	"""


	def __init__(self) -> Self:
		"""
		'__init__' initializes 'SphereNormalX'.
		"""

		self.x: float = None
		self.r: float = None

		super().__init__()


	def set_parameters(self, x: float, r: float) -> None:
		"""
		'set_parameters' sets spheres on x-axis parameters.

		'set_parameters' checks parameter entries are valid 
		floating points. It raises errors if given None.

		Parameters:
			x: Sphere center x component.
			r: Sphere radius.
		"""

		value = types.cast_fortran_real(x)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.x = value
		self.parameters['x'] = value

		value = types.cast_fortran_real(r)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.r = value
		self.parameters['r'] = value


	def to_cadquery(self, hasHeader: bool = False) -> str:
		"""
		'to_cadquery' generates cadquery from surface card objects.

		'to_cadquery' provides a Cadquery endpoints for writing Cadquery
		source strings and later displaying geometries.

		Parameters:
			hasHeader: Boolean to include cadquery header.

		Returns:
			Cadquery for surface card object.
		"""

		cadquery = 'import cadquery as cq\n\n' if hasHeader else ''

		cadquery += f"surface_{self.number} = cq.Workplane().sphere({self.parameters['r']}).translate(({self.parameters['x']}, 0, 0))\n"

		return cadquery


class SphereNormalY(Surface):
	"""
	'SphereNormalY' represents spheres on y-axis surface cards.

	'SphereNormalY' functions as a data subtype for 'Surface'. It
	represents cell card parameter as abstract syntax 
	elements.
	"""


	def __init__(self) -> Self:
		"""
		'__init__' initializes 'SphereNormalY'.
		"""

		self.y: float = None
		self.r: float = None

		super().__init__()


	def set_parameters(self, y: float, r: float) -> None:
		"""
		'set_parameters' sets spheres on y-axis parameters.

		'set_parameters' checks parameter entries are valid 
		floating points. It raises errors if given None.

		Parameters:
			y: Sphere center y component.
			r: Sphere radius.
		"""

		value = types.cast_fortran_real(y)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.y = value
		self.parameters['y'] = value

		value = types.cast_fortran_real(r)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.r = value
		self.parameters['r'] = value


	def to_cadquery(self, hasHeader: bool = False) -> str:
		"""
		'to_cadquery' generates cadquery from surface card objects.

		'to_cadquery' provides a Cadquery endpoints for writing Cadquery
		source strings and later displaying geometries.

		Parameters:
			hasHeader: Boolean to include cadquery header.

		Returns:
			Cadquery for surface card object.
		"""

		cadquery = 'import cadquery as cq\n\n' if hasHeader else ''
	
		cadquery += f"surface_{self.number} = cq.Workplane().sphere({self.parameters['r']}).translate((0, {self.parameters['y']}, 0))\n"

		return cadquery


class SphereNormalZ(Surface):
	"""
	'SphereNormalZ' represents spheres on z-axis surface cards.

	'SphereNormalZ' functions as a data subtype for 'Surface'. It
	represents cell card parameter as abstract syntax 
	elements.
	"""


	def __init__(self) -> Self:
		"""
		'__init__' initializes 'SphereNormalZ'.
		"""

		self.z: float = None
		self.r: float = None

		super().__init__()


	def set_parameters(self, z: float, r: float) -> None:
		"""
		'set_parameters' sets spheres on z-axis parameters.

		'set_parameters' checks parameter entries are valid 
		floating points. It raises errors if given None.

		Parameters:
			z: Sphere center z component.
			r: Sphere radius.
		"""

		value = types.cast_fortran_real(z)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.z = value
		self.parameters['z'] = value

		value = types.cast_fortran_real(r)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.r = value
		self.parameters['r'] = value


	def to_cadquery(self, hasHeader: bool = False) -> str:
		"""
		'to_cadquery' generates cadquery from surface card objects.

		'to_cadquery' provides a Cadquery endpoints for writing Cadquery
		source strings and later displaying geometries.

		Parameters:
			hasHeader: Boolean to include cadquery header.

		Returns:
			Cadquery for surface card object.
		"""

		cadquery = 'import cadquery as cq\n\n' if hasHeader else ''
		
		cadquery += f"surface_{self.number} = cq.Workplane().sphere({self.parameters['r']}).translate((0, 0, {self.parameters['z']}))\n"

		return cadquery


class CylinderParallelX(Surface):
	"""
	'CylinderParallelX' represents cylinders parallel to x-axis surface cards.

	'CylinderParallelX' functions as a data subtype for 'Surface'. It
	represents cell card parameter as abstract syntax 
	elements.
	"""


	def __init__(self) -> Self:
		"""
		'__init__' initializes 'CylinderParallelX'.
		"""

		self.y: float = None
		self.z: float = None
		self.r: float = None

		super().__init__()


	def set_parameters(self, y: float, z: float, r: float) -> None:
		"""
		'set_parameters' sets cylinders parallel to x-axis parameters.

		'set_parameters' checks parameter entries are valid 
		floating points. It raises errors if given None.

		Parameters:
			y: Cylinder center y component.
			z: Cylinder center z component.
			r: Cylinder radius.
		"""

		value = types.cast_fortran_real(y)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.y = value
		self.parameters['y'] = value

		value = types.cast_fortran_real(z)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.z = value
		self.parameters['z'] = value

		value = types.cast_fortran_real(r)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.r = value
		self.parameters['r'] = value


class CylinderParallelY(Surface):
	"""
	'CylinderParallelY' represents cylinders parallel to y-axis surface cards.

	'CylinderParallelY' functions as a data subtype for 'Surface'. It
	represents cell card parameter as abstract syntax 
	elements.
	"""


	def __init__(self) -> Self:
		"""
		'__init__' initializes 'CylinderParallelY'.
		"""

		self.x: float = None
		self.z: float = None
		self.r: float = None

		super().__init__()


	def set_parameters(self, x: float, z: float, r: float) -> None:
		"""
		'set_parameters' sets cylinders parallel to y-axis parameters.

		'set_parameters' checks parameter entries are valid 
		floating points. It raises errors if given None.

		Parameters:
			x: Cylinder center x component.
			z: Cylinder center z component.
			r: Cylinder radius.
		"""

		value = types.cast_fortran_real(x)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.x = value
		self.parameters['x'] = value

		value = types.cast_fortran_real(z)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.z = value
		self.parameters['z'] = value

		value = types.cast_fortran_real(r)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.r = value
		self.parameters['r'] = value


class CylinderParallelZ(Surface):
	"""
	'CylinderParallelZ' represents cylinders parallel to z-axis surface cards.

	'CylinderParallelZ' functions as a data subtype for 'Surface'. It
	represents cell card parameter as abstract syntax 
	elements.
	"""


	def __init__(self) -> Self:
		"""
		'__init__' initializes 'CylinderParallelZ'.
		"""

		self.x: float = None
		self.y: float = None
		self.r: float = None

		super().__init__()


	def set_parameters(self, x: float, y: float, r: float) -> None:
		"""
		'set_parameters' sets cylinders parallel to z-axis parameters.

		'set_parameters' checks parameter entries are valid 
		floating points. It raises errors if given None.

		Parameters:
			x: Cylinder center x component.
			y: Cylinder center y component.
			r: Cylinder radius.
		"""

		value = types.cast_fortran_real(x)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.x = value
		self.parameters['x'] = value

		value = types.cast_fortran_real(y)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.y = value
		self.parameters['y'] = value

		value = types.cast_fortran_real(r)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.r = value
		self.parameters['r'] = value


class CylinderOnX(Surface):
	"""
	'CylinderOnX' represents cylinders on x-axis surface cards.

	'CylinderOnX' functions as a data subtype for 'Surface'. It
	represents cell card parameter as abstract syntax 
	elements.
	"""


	def __init__(self) -> Self:
		"""
		'__init__' initializes 'CylinderOnX'.
		"""

		self.r: float = None

		super().__init__()


	def set_parameters(self, r: float) -> None:
		"""
		'set_parameters' sets cylinders on x-axis parameters.

		'set_parameters' checks parameter entries are valid 
		floating points. It raises errors if given None.

		Parameters:
			r: Cylinder radius.
		"""

		value = types.cast_fortran_real(r)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.r = value
		self.parameters['r'] = value


class CylinderOnY(Surface):
	"""
	'CylinderOnY' represents cylinders on y-axis surface cards.

	'CylinderOnY' functions as a data subtype for 'Surface'. It
	represents cell card parameter as abstract syntax 
	elements.
	"""


	def __init__(self) -> Self:
		"""
		'__init__' initializes 'CylinderOnY'.
		"""

		self.r: float = None

		super().__init__()


	def set_parameters(self, r: float) -> None:
		"""
		'set_parameters' sets cylinders on y-axis parameters.

		'set_parameters' checks parameter entries are valid 
		floating points. It raises errors if given None.

		Parameters:
			r: Cylinder radius.
		"""

		value = types.cast_fortran_real(r)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.r = value
		self.parameters['r'] = value


class CylinderOnZ(Surface):
	"""
	'CylinderOnZ' represents cylinders on z-axis surface cards.

	'CylinderOnZ' functions as a data subtype for 'Surface'. It
	represents cell card parameter as abstract syntax 
	elements.
	"""


	def __init__(self) -> Self:
		"""
		'__init__' initializes 'CylinderOnZ'.
		"""

		self.r: float = None

		super().__init__()


	def set_parameters(self, r: float) -> None:
		"""
		'set_parameters' sets cylinders on z-axis parameters.

		'set_parameters' checks parameter entries are valid 
		floating points. It raises errors if given None.

		Parameters:
			r: Cylinder radius.
		"""

		value = types.cast_fortran_real(r)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.r = value
		self.parameters['r'] = value


class ConeParallelX(Surface):
	"""
	'ConeParallelX' represents cones parallel to x-axis surface cards.

	'ConeParallelX' functions as a data subtype for 'Surface'. It
	represents cell card parameter as abstract syntax 
	elements.
	"""


	def __init__(self) -> Self:
		"""
		'__init__' initializes 'ConeParallelX'.
		"""

		self.x: float = None
		self.y: float = None
		self.z: float = None
		self.t_squared: float = None
		self.plusminus_1: float = None

		super().__init__()


	def set_parameters(self, x: float, y: float, z: float, t_squared: float, plusminus_1: float) -> None:
		"""
		'set_parameters' sets cones parallel to x-axis parameters.

		'set_parameters' checks parameter entries are valid 
		floating points. It raises errors if given None.

		Parameters:
			x: Cone center x component.
			y: Cone center y component.
			z: Cone center z component.
			t_squared: Cone t_squared coefficnet.
			plusminus_1: Cone sheet selector.
		"""

		value = types.cast_fortran_real(x)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.x = value
		self.parameters['x'] = value

		value = types.cast_fortran_real(y)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.y = value
		self.parameters['y'] = value

		value = types.cast_fortran_real(z)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.z = value
		self.parameters['z'] = value

		value = types.cast_fortran_real(t_squared)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.t_squared = value
		self.parameters['t_squared'] = value

		value = types.cast_fortran_real(plusminus_1)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.plusminus_1 = value
		self.parameters['plusminus_1'] = value


class ConeParallelY(Surface):
	"""
	'ConeParallelY' represents cones parallel to y-axis surface cards.

	'ConeParallelY' functions as a data subtype for 'Surface'. It
	represents cell card parameter as abstract syntax 
	elements.
	"""


	def __init__(self) -> Self:
		"""
		'__init__' initializes 'ConeParallelY'.
		"""

		self.x: float = None
		self.y: float = None
		self.z: float = None
		self.t_squared: float = None
		self.plusminus_1: float = None

		super().__init__()


	def set_parameters(self, x: float, y: float, z: float, t_squared: float, plusminus_1: float) -> None:
		"""
		'set_parameters' sets cones parallel to y-axis parameters.

		'set_parameters' checks parameter entries are valid 
		floating points. It raises errors if given None.

		Parameters:
			x: Cone center x component.
			y: Cone center y component.
			z: Cone center z component.
			t_squared: Cone t_squared coefficnet.
			plusminus_1: Cone sheet selector.
		"""

		value = types.cast_fortran_real(x)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.x = value
		self.parameters['x'] = value

		value = types.cast_fortran_real(y)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.y = value
		self.parameters['y'] = value

		value = types.cast_fortran_real(z)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.z = value
		self.parameters['z'] = value

		value = types.cast_fortran_real(t_squared)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.t_squared = value
		self.parameters['t_squared'] = value

		value = types.cast_fortran_real(plusminus_1)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.plusminus_1 = value
		self.parameters['plusminus_1'] = value


class ConeParallelZ(Surface):
	"""
	'ConeParallelZ' represents cones parallel to z-axis surface cards.

	'ConeParallelZ' functions as a data subtype for 'Surface'. It
	represents cell card parameter as abstract syntax 
	elements.
	"""


	def __init__(self) -> Self:
		"""
		'__init__' initializes 'ConeParallelZ'.
		"""

		self.x: float = None
		self.y: float = None
		self.z: float = None
		self.t_squared: float = None
		self.plusminus_1: float = None

		super().__init__()


	def set_parameters(self, x: float, y: float, z: float, t_squared: float, plusminus_1: float) -> None:
		"""
		'set_parameters' sets cones parallel to z-axis parameters.

		'set_parameters' checks parameter entries are valid 
		floating points. It raises errors if given None.

		Parameters:
			x: Cone center x component.
			y: Cone center y component.
			z: Cone center z component.
			t_squared: Cone t_squared coefficnet.
			plusminus_1: Cone sheet selector.
		"""

		value = types.cast_fortran_real(x)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.x = value
		self.parameters['x'] = value

		value = types.cast_fortran_real(y)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.y = value
		self.parameters['y'] = value

		value = types.cast_fortran_real(z)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.z = value
		self.parameters['z'] = value

		value = types.cast_fortran_real(t_squared)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.t_squared = value
		self.parameters['t_squared'] = value

		value = types.cast_fortran_real(plusminus_1)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.plusminus_1 = value
		self.parameters['plusminus_1'] = value


class ConeOnX(Surface):
	"""
	'ConeOnX' represents cones on x-axis surface cards.

	'ConeOnX' functions as a data subtype for 'Surface'. It
	represents cell card parameter as abstract syntax 
	elements.
	"""


	def __init__(self) -> Self:
		"""
		'__init__' initializes 'ConeOnX'.
		"""

		self.x: float = None
		self.t_squared: float = None
		self.plusminus_1: float = None

		super().__init__()


	def set_parameters(self, x: float, t_squared: float, plusminus_1: float) -> None:
		"""
		'set_parameters' sets cones on x-axis parameters.

		'set_parameters' checks parameter entries are valid 
		floating points. It raises errors if given None.

		Parameters:
			x: Cone center x component.
			t_squared: Cone t_squared coefficnet.
			plusminus_1: Cone sheet selector.
		"""

		value = types.cast_fortran_real(x)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.x = value
		self.parameters['x'] = value

		value = types.cast_fortran_real(t_squared)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.t_squared = value
		self.parameters['t_squared'] = value

		value = types.cast_fortran_real(plusminus_1)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.plusminus_1 = value
		self.parameters['plusminus_1'] = value


class ConeOnY(Surface):
	"""
	'ConeOnY' represents cones on y-axis surface cards.

	'ConeOnY' functions as a data subtype for 'Surface'. It
	represents cell card parameter as abstract syntax 
	elements.
	"""


	def __init__(self) -> Self:
		"""
		'__init__' initializes 'ConeOnY'.
		"""

		self.y: float = None
		self.t_squared: float = None
		self.plusminus_1: float = None

		super().__init__()


	def set_parameters(self, y: float, t_squared: float, plusminus_1: float) -> None:
		"""
		'set_parameters' sets cones on y-axis parameters.

		'set_parameters' checks parameter entries are valid 
		floating points. It raises errors if given None.

		Parameters:
			y: Cone center y component.
			t_squared: Cone t_squared coefficnet.
			plusminus_1: Cone sheet selector.
		"""

		value = types.cast_fortran_real(y)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.y = value
		self.parameters['y'] = value

		value = types.cast_fortran_real(t_squared)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.t_squared = value
		self.parameters['t_squared'] = value

		value = types.cast_fortran_real(plusminus_1)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.plusminus_1 = value
		self.parameters['plusminus_1'] = value


class ConeOnZ(Surface):
	"""
	'ConeOnZ' represents cones on z-axis surface cards.

	'ConeOnZ' functions as a data subtype for 'Surface'. It
	represents cell card parameter as abstract syntax 
	elements.
	"""


	def __init__(self) -> Self:
		"""
		'__init__' initializes 'ConeOnZ'.
		"""

		self.z: float = None
		self.t_squared: float = None
		self.plusminus_1: float = None

		super().__init__()


	def set_parameters(self, z: float, t_squared: float, plusminus_1: float) -> None:
		"""
		'set_parameters' sets cones on z-axis parameters.

		'set_parameters' checks parameter entries are valid 
		floating points. It raises errors if given None.

		Parameters:
			z: Cone center z component.
			t_squared: Cone t_squared coefficnet.
			plusminus_1: Cone sheet selector.
		"""

		value = types.cast_fortran_real(z)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.z = value
		self.parameters['z'] = value

		value = types.cast_fortran_real(t_squared)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.t_squared = value
		self.parameters['t_squared'] = value

		value = types.cast_fortran_real(plusminus_1)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.plusminus_1 = value
		self.parameters['plusminus_1'] = value


class QuadraticSpecial(Surface):
	"""
	'QuadraticSpecial' represents special quadratic not parallel to x-, y-, or z- axis surface cards.

	'QuadraticSpecial' functions as a data subtype for 'Surface'. It
	represents cell card parameter as abstract syntax 
	elements.
	"""


	def __init__(self) -> Self:
		"""
		'__init__' initializes 'QuadraticSpecial'.
		"""

		self.a: float = None
		self.b: float = None
		self.c: float = None
		self.d: float = None
		self.e: float = None
		self.f: float = None
		self.g: float = None
		self.x: float = None
		self.y: float = None
		self.z: float = None

		super().__init__()


	def set_parameters(self, a: float, b: float, c: float, d: float, e: float, f: float, g: float, x: float, y: float, z: float) -> None:
		"""
		'set_parameters' sets special quadratic not parallel to x-, y-, or z- axis parameters.

		'set_parameters' checks parameter entries are valid 
		floating points. It raises errors if given None.

		Parameters:
			a: Quadratic surface equation A coefficent.
			b: Quadratic surface equation B coefficent.
			c: Quadratic surface equation C coefficent.
			d: Quadratic surface equation D coefficent.
			e: Quadratic surface equation E coefficent.
			f: Quadratic surface equation F coefficent.
			g: Quadratic surface equation G coefficent.
			x: Quadratic center x component.
			y: Quadratic center y component.
			z: Quadratic center z component.
		"""

		value = types.cast_fortran_real(a)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.a = value
		self.parameters['a'] = value

		value = types.cast_fortran_real(b)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.b = value
		self.parameters['b'] = value

		value = types.cast_fortran_real(c)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.c = value
		self.parameters['c'] = value

		value = types.cast_fortran_real(d)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.d = value
		self.parameters['d'] = value

		value = types.cast_fortran_real(e)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.e = value
		self.parameters['e'] = value

		value = types.cast_fortran_real(f)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.f = value
		self.parameters['f'] = value

		value = types.cast_fortran_real(g)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.g = value
		self.parameters['g'] = value

		value = types.cast_fortran_real(x)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.x = value
		self.parameters['x'] = value

		value = types.cast_fortran_real(y)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.y = value
		self.parameters['y'] = value

		value = types.cast_fortran_real(z)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.z = value
		self.parameters['z'] = value


class QuadraticGeneral(Surface):
	"""
	'QuadraticGeneral' represents general quadratic parallel to x-, y-, or z- axis surface cards.

	'QuadraticGeneral' functions as a data subtype for 'Surface'. It
	represents cell card parameter as abstract syntax 
	elements.
	"""


	def __init__(self) -> Self:
		"""
		'__init__' initializes 'QuadraticGeneral'.
		"""

		self.a: float = None
		self.b: float = None
		self.c: float = None
		self.d: float = None
		self.e: float = None
		self.f: float = None
		self.g: float = None
		self.h: float = None
		self.j: float = None
		self.k: float = None

		super().__init__()


	def set_parameters(self, a: float, b: float, c: float, d: float, e: float, f: float, g: float, h: float, j: float, k: float) -> None:
		"""
		'set_parameters' sets general quadratic parallel to x-, y-, or z- axis parameters.

		'set_parameters' checks parameter entries are valid 
		floating points. It raises errors if given None.

		Parameters:
			a: Quadratic surface equation A coefficent.
			b: Quadratic surface equation B coefficent.
			c: Quadratic surface equation C coefficent.
			d: Quadratic surface equation D coefficent.
			e: Quadratic surface equation E coefficent.
			f: Quadratic surface equation F coefficent.
			g: Quadratic surface equation G coefficent.
			h: Quadratic surface equation H coefficent.
			j: Quadratic surface equation J coefficent.
			k: Quadratic surface equation K coefficent.
		"""

		value = types.cast_fortran_real(a)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.a = value
		self.parameters['a'] = value

		value = types.cast_fortran_real(b)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.b = value
		self.parameters['b'] = value

		value = types.cast_fortran_real(c)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.c = value
		self.parameters['c'] = value

		value = types.cast_fortran_real(d)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.d = value
		self.parameters['d'] = value

		value = types.cast_fortran_real(e)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.e = value
		self.parameters['e'] = value

		value = types.cast_fortran_real(f)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.f = value
		self.parameters['f'] = value

		value = types.cast_fortran_real(g)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.g = value
		self.parameters['g'] = value

		value = types.cast_fortran_real(h)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.h = value
		self.parameters['h'] = value

		value = types.cast_fortran_real(j)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.j = value
		self.parameters['j'] = value

		value = types.cast_fortran_real(k)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.k = value
		self.parameters['k'] = value


class TorusParallelX(Surface):
	"""
	'TorusParallelX' represents tori parallel to x-axis surface cards.

	'TorusParallelX' functions as a data subtype for 'Surface'. It
	represents cell card parameter as abstract syntax 
	elements.
	"""


	def __init__(self) -> Self:
		"""
		'__init__' initializes 'TorusParallelX'.
		"""

		self.x: float = None
		self.y: float = None
		self.z: float = None
		self.a: float = None
		self.b: float = None
		self.c: float = None

		super().__init__()


	def set_parameters(self, x: float, y: float, z: float, a: float, b: float, c: float) -> None:
		"""
		'set_parameters' sets tori parallel to x-axis parameters.

		'set_parameters' checks parameter entries are valid 
		floating points. It raises errors if given None.

		Parameters:
			x: Torus center x component.
			y: Torus center y component.
			z: Torus center z component.
			a: Quadratic surface equation A coefficent.
			b: Quadratic surface equation B coefficent.
			c: Quadratic surface equation C coefficent.
		"""

		value = types.cast_fortran_real(x)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.x = value
		self.parameters['x'] = value

		value = types.cast_fortran_real(y)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.y = value
		self.parameters['y'] = value

		value = types.cast_fortran_real(z)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.z = value
		self.parameters['z'] = value

		value = types.cast_fortran_real(a)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.a = value
		self.parameters['a'] = value

		value = types.cast_fortran_real(b)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.b = value
		self.parameters['b'] = value

		value = types.cast_fortran_real(c)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.c = value
		self.parameters['c'] = value


class TorusParallelY(Surface):
	"""
	'TorusParallelY' represents tori parallel to y-axis surface cards.

	'TorusParallelY' functions as a data subtype for 'Surface'. It
	represents cell card parameter as abstract syntax 
	elements.
	"""


	def __init__(self) -> Self:
		"""
		'__init__' initializes 'TorusParallelY'.
		"""

		self.x: float = None
		self.y: float = None
		self.z: float = None
		self.a: float = None
		self.b: float = None
		self.c: float = None

		super().__init__()


	def set_parameters(self, x: float, y: float, z: float, a: float, b: float, c: float) -> None:
		"""
		'set_parameters' sets tori parallel to y-axis parameters.

		'set_parameters' checks parameter entries are valid 
		floating points. It raises errors if given None.

		Parameters:
			x: Torus center x component.
			y: Torus center y component.
			z: Torus center z component.
			a: Quadratic surface equation A coefficent.
			b: Quadratic surface equation B coefficent.
			c: Quadratic surface equation C coefficent.
		"""

		value = types.cast_fortran_real(x)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.x = value
		self.parameters['x'] = value

		value = types.cast_fortran_real(y)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.y = value
		self.parameters['y'] = value

		value = types.cast_fortran_real(z)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.z = value
		self.parameters['z'] = value

		value = types.cast_fortran_real(a)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.a = value
		self.parameters['a'] = value

		value = types.cast_fortran_real(b)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.b = value
		self.parameters['b'] = value

		value = types.cast_fortran_real(c)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.c = value
		self.parameters['c'] = value


class TorusParallelZ(Surface):
	"""
	'TorusParallelZ' represents tori parallel to z-axis surface cards.

	'TorusParallelZ' functions as a data subtype for 'Surface'. It
	represents cell card parameter as abstract syntax 
	elements.
	"""


	def __init__(self) -> Self:
		"""
		'__init__' initializes 'TorusParallelZ'.
		"""

		self.x: float = None
		self.y: float = None
		self.z: float = None
		self.a: float = None
		self.b: float = None
		self.c: float = None

		super().__init__()


	def set_parameters(self, x: float, y: float, z: float, a: float, b: float, c: float) -> None:
		"""
		'set_parameters' sets tori parallel to z-axis parameters.

		'set_parameters' checks parameter entries are valid 
		floating points. It raises errors if given None.

		Parameters:
			x: Torus center x component.
			y: Torus center y component.
			z: Torus center z component.
			a: Quadratic surface equation A coefficent.
			b: Quadratic surface equation B coefficent.
			c: Quadratic surface equation C coefficent.
		"""

		value = types.cast_fortran_real(x)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.x = value
		self.parameters['x'] = value

		value = types.cast_fortran_real(y)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.y = value
		self.parameters['y'] = value

		value = types.cast_fortran_real(z)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.z = value
		self.parameters['z'] = value

		value = types.cast_fortran_real(a)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.a = value
		self.parameters['a'] = value

		value = types.cast_fortran_real(b)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.b = value
		self.parameters['b'] = value

		value = types.cast_fortran_real(c)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.c = value
		self.parameters['c'] = value


class SurfaceX(Surface):
	"""
	'SurfaceX' represents point-defined surface symmetric about x-axis surface cards.

	'SurfaceX' functions as a data subtype for 'Surface'. It
	represents cell card parameter as abstract syntax 
	elements.
	"""


	def __init__(self) -> Self:
		"""
		'__init__' initializes 'SurfaceX'.
		"""

		self.x1: float = None
		self.r1: float = None
		self.x2: float = None
		self.r2: float = None
		self.x3: float = None
		self.r3: float = None

		super().__init__()


	def set_parameters(self, x1: float, r1: float, x2: float, r2: float, x3: float, r3: float) -> None:
		"""
		'set_parameters' sets point-defined surface symmetric about x-axis parameters.

		'set_parameters' checks parameter entries are valid 
		floating points. It raises errors if given None.

		Parameters:
			x1: Point #1 x component.
			r1: Point #1 modulus.
			x2: Point #2 x component.
			r2: Point #2 modulus.
			x3: Point #3 x component.
			r3: Point #3 modulus.
		"""

		value = types.cast_fortran_real(x1)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.x1 = value
		self.parameters['x1'] = value

		value = types.cast_fortran_real(r1)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.r1 = value
		self.parameters['r1'] = value

		if x2 is not None and r2 is not None:
			value = types.cast_fortran_real(x2)
			if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
			self.x2 = value
			self.parameters['x2'] = value

			value = types.cast_fortran_real(r2)
			if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
			self.r2 = value
			self.parameters['r2'] = value

			if x3 is not None and r3 is not None:
				value = types.cast_fortran_real(x3)
				if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
				self.x3 = value
				self.parameters['x3'] = value

				value = types.cast_fortran_real(r3)
				if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
				self.r3 = value
				self.parameters['r3'] = value


class SurfaceY(Surface):
	"""
	'SurfaceY' represents point-defined surface symmetric about x-axis surface cards.

	'SurfaceY' functions as a data subtype for 'Surface'. It
	represents cell card parameter as abstract syntax 
	elements.
	"""


	def __init__(self) -> Self:
		"""
		'__init__' initializes 'SurfaceY'.
		"""

		self.y1: float = None
		self.r1: float = None
		self.y2: float = None
		self.r2: float = None
		self.y3: float = None
		self.r3: float = None

		super().__init__()


	def set_parameters(self, y1: float, r1: float, y2: float, r2: float, y3: float, r3: float) -> None:
		"""
		'set_parameters' sets point-defined surface symmetric about x-axis parameters.

		'set_parameters' checks parameter entries are valid 
		floating points. It raises errors if given None.

		Parameters:
			y1: Point #1 x component.
			r1: Point #1 modulus.
			y2: Point #2 x component.
			r2: Point #2 modulus.
			y3: Point #3 x component.
			r3: Point #3 modulus.
		"""

		value = types.cast_fortran_real(y1)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.y1 = value
		self.parameters['y1'] = value

		value = types.cast_fortran_real(r1)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.r1 = value
		self.parameters['r1'] = value

		if y2 is not None and r2 is not None:
			value = types.cast_fortran_real(y2)
			if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
			self.y2 = value
			self.parameters['y2'] = value

			value = types.cast_fortran_real(r2)
			if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
			self.r2 = value
			self.parameters['r2'] = value

			if y3 is not None and r3 is not None:
				value = types.cast_fortran_real(y3)
				if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
				self.y3 = value
				self.parameters['y3'] = value

				value = types.cast_fortran_real(r3)
				if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
				self.r3 = value
				self.parameters['r3'] = value


class SurfaceZ(Surface):
	"""
	'SurfaceZ' represents point-defined surface symmetric about x-axis surface cards.

	'SurfaceZ' functions as a data subtype for 'Surface'. It
	represents cell card parameter as abstract syntax 
	elements.
	"""


	def __init__(self) -> Self:
		"""
		'__init__' initializes 'SurfaceZ'.
		"""

		self.z1: float = None
		self.r1: float = None
		self.z2: float = None
		self.r2: float = None
		self.z3: float = None
		self.r3: float = None

		super().__init__()


	def set_parameters(self, z1: float, r1: float, z2: float, r2: float, z3: float, r3: float) -> None:
		"""
		'set_parameters' sets point-defined surface symmetric about x-axis parameters.

		'set_parameters' checks parameter entries are valid 
		floating points. It raises errors if given None.

		Parameters:
			z1: Point #1 x component.
			r1: Point #1 modulus.
			z2: Point #2 x component.
			r2: Point #2 modulus.
			z3: Point #3 x component.
			r3: Point #3 modulus.
		"""

		value = types.cast_fortran_real(z1)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.z1 = value
		self.parameters['z1'] = value

		value = types.cast_fortran_real(r1)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.r1 = value
		self.parameters['r1'] = value

		if z2 is not None and r2 is not None:
			value = types.cast_fortran_real(z2)
			if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
			self.z2 = value
			self.parameters['z2'] = value

			value = types.cast_fortran_real(r2)
			if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
			self.r2 = value
			self.parameters['r2'] = value

			if z3 is not None and r3 is not None:
				value = types.cast_fortran_real(z3)
				if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
				self.z3 = value
				self.parameters['z3'] = value

				value = types.cast_fortran_real(r3)
				if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
				self.r3 = value
				self.parameters['r3'] = value


class PlanePoint(Surface):
	"""
	'PlanePoint' represents point-defined plane surface cards.

	'PlanePoint' functions as a data subtype for 'Surface'. It
	represents cell card parameter as abstract syntax 
	elements.
	"""


	def __init__(self) -> Self:
		"""
		'__init__' initializes 'PlanePoint'.
		"""

		self.x1: float = None
		self.y1: float = None
		self.z1: float = None
		self.x2: float = None
		self.y2: float = None
		self.z2: float = None
		self.x3: float = None
		self.y3: float = None
		self.z3: float = None

		super().__init__()


	def set_parameters(self, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float, x3: float, y3: float, z3: float) -> None:
		"""
		'set_parameters' sets point-defined plane parameters.

		'set_parameters' checks parameter entries are valid 
		floating points. It raises errors if given None.

		Parameters:
			x1: Point #1 x component.
			y1: Point #1 y component.
			z1: Point #1 z component.
			x2: Point #2 x component.
			y2: Point #2 y component.
			z2: Point #2 z component.
			x3: Point #3 x component.
			y3: Point #3 y component.
			z3: Point #3 z component.
		"""

		value = types.cast_fortran_real(x1)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.x1 = value
		self.parameters['x1'] = value

		value = types.cast_fortran_real(y1)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.y1 = value
		self.parameters['y1'] = value

		value = types.cast_fortran_real(z1)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.z1 = value
		self.parameters['z1'] = value

		value = types.cast_fortran_real(x2)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.x2 = value
		self.parameters['x2'] = value

		value = types.cast_fortran_real(y2)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.y2 = value
		self.parameters['y2'] = value

		value = types.cast_fortran_real(z2)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.z2 = value
		self.parameters['z2'] = value

		value = types.cast_fortran_real(x3)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.x3 = value
		self.parameters['x3'] = value

		value = types.cast_fortran_real(y3)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.y3 = value
		self.parameters['y3'] = value

		value = types.cast_fortran_real(z3)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.z3 = value
		self.parameters['z3'] = value


class Box(Surface):
	"""
	'Box'

	'Box' functions as a data subtype for 'Surface'. It
	represents cell card parameter as abstract syntax 
	elements.
	"""


	def __init__(self) -> Self:
		"""
		'__init__' initializes 'Box'.
		"""

		self.vx: float = None
		self.vy: float = None
		self.vz: float = None
		self.a1x: float = None
		self.a1y: float = None
		self.a1z: float = None
		self.a2x: float = None
		self.a2y: float = None
		self.a2z: float = None
		self.a3x: float = None
		self.a3y: float = None
		self.a3z: float = None

		super().__init__()


	def set_parameters(self, vx: float, vy: float, vz: float, a1x: float, a1y: float, a1z: float, a2x: float, a2y: float, a2z: float, a3x: float, a3y: float, a3z: float) -> None:
		"""
		'set_parameters' sets arbitrarily oriented orthogonal box parameters.

		'set_parameters' checks parameter entries are valid 
		floating points. It raises errors if given None.

		Parameters:
			vx: Macrobody center x component.
			vy: Macrobody center y component.
			vz: Macrobdoy center z component.
			a1x: 1st side vector from coordiante x component.
			a1y: 1st side vector from coordiante y component.
			a1z: 1st side vector from coordinate z compoennt.
			a2x: 2nd side vector from coordiante x component.
			a2y: 2nd side vector from coordiante y component.
			a2z: 2nd side vector from coordinate z compoennt.
			a3x: 3rd side vector from coordiante x component.
			a3y: 3rd side vector from coordiante y component.
			a3z: 3rd side vector from coordinate z compoennt.
		"""

		value = types.cast_fortran_real(vx)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.vx = value
		self.parameters['vx'] = value

		value = types.cast_fortran_real(vy)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.vy = value
		self.parameters['vy'] = value

		value = types.cast_fortran_real(vz)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.vz = value
		self.parameters['vz'] = value

		value = types.cast_fortran_real(a1x)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.a1x = value
		self.parameters['a1x'] = value

		value = types.cast_fortran_real(a1y)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.a1y = value
		self.parameters['a1y'] = value

		value = types.cast_fortran_real(a1z)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.a1z = value
		self.parameters['a1z'] = value

		value = types.cast_fortran_real(a2x)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.a2x = value
		self.parameters['a2x'] = value

		value = types.cast_fortran_real(a2y)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.a2y = value
		self.parameters['a2y'] = value

		value = types.cast_fortran_real(a2z)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.a2z = value
		self.parameters['a2z'] = value

		if a3x is not None and a3y is not None and a3z is not None:
			value = types.cast_fortran_real(a3x)
			if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
			self.a3x = value
			self.parameters['a3x'] = value

			value = types.cast_fortran_real(a3y)
			if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
			self.a3y = value
			self.parameters['a3y'] = value

			value = types.cast_fortran_real(a3z)
			if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
			self.a3z = value
			self.parameters['a3z'] = value


	def to_cadquery(self, hasHeader: bool = False) -> str:
		"""
		'to_cadquery' generates cadquery from surface card objects.

		'to_cadquery' provides a Cadquery endpoints for writing Cadquery
		source strings and later displaying geometries.

		Parameters:
			hasHeader: Boolean to include cadquery header.

		Returns:
			Cadquery for surface card object.
		"""

		cadquery = 'import cadquery as cq\n\n' if hasHeader else ''

		if len(self.parameters) != 9:
			length, width, height = np.linalg.norm([self.a1x, self.a1y, self.a1z]), np.linalg.norm([self.a2x, self.a2y, self.a2z]), np.linalg.norm([self.a3x, self.a3y, self.a3z])

			cadquery += f"surface_{self.number} = cq.Workplane().polyline([({self.vx}, {self.vy}, {self.vz}), ({self.vx + self.a1x}, {self.vy + self.a1y}, {self.vz + self.a1z}), ({self.vx + self.a2x + self.a1x}, {self.vy + self.a2y + self.a1y}, {self.vz + self.a2z + self.a1z}), ({self.vx + self.a2x}, {self.vy + self.a2y}, {self.vz + self.a2z})]).close().polyline([({self.vx + self.a3x}, {self.vy + self.a3y}, {self.vz + self.a3z}), ({self.vx + self.a1x + self.a3x}, {self.vy + self.a1y + self.a3y}, {self.vz + self.a1z + self.a3z}), ({self.vx + self.a2x + self.a1x + self.a3x}, {self.vy + self.a2y + self.a1y + self.a3y}, {self.vz + self.a2z + self.a1z + self.a3z}), ({self.vx + self.a2x + self.a3x}, {self.vy + self.a2y + self.a3y}, {self.vz + self.a2z + self.a3z})]).close().loft()\n"

		return cadquery


class Parallelepiped(Surface):
	"""
	'Parallelepiped' represents rectangular parallelepiped surface cards.

	'Parallelepiped' functions as a data subtype for 'Surface'. It
	represents cell card parameter as abstract syntax 
	elements.
	"""


	def __init__(self) -> Self:
		"""
		'__init__' initializes 'Parallelepiped'.
		"""

		self.xmin: float = None
		self.xmax: float = None
		self.ymin: float = None
		self.ymax: float = None
		self.zmin: float = None
		self.zmax: float = None

		super().__init__()


	def set_parameters(self, xmin: float, xmax: float, ymin: float, ymax: float, zmin: float, zmax: float) -> None:
		"""
		'set_parameters' sets rectangular parallelepiped parameters.

		'set_parameters' checks parameter entries are valid 
		floating points. It raises errors if given None.

		Parameters:
			xmin: Minimum x of locus range.
			xmax: Maximum x of locus range.
			ymin: Minimum y of locus range.
			ymax: Maximum y of locus range.
			zmin: Minimum z of locus range.
			zmax: Maximum z of locus range.
		"""

		value = types.cast_fortran_real(xmin)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.xmin = value
		self.parameters['xmin'] = value

		value = types.cast_fortran_real(xmax)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.xmax = value
		self.parameters['xmax'] = value

		value = types.cast_fortran_real(ymin)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.ymin = value
		self.parameters['ymin'] = value

		value = types.cast_fortran_real(ymax)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.ymax = value
		self.parameters['ymax'] = value

		value = types.cast_fortran_real(zmin)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.zmin = value
		self.parameters['zmin'] = value

		value = types.cast_fortran_real(zmax)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.zmax = value
		self.parameters['zmax'] = value


	def to_cadquery(self, hasHeader: bool = False) -> str:
		"""
		'to_cadquery' generates cadquery from surface card objects.

		'to_cadquery' provides a Cadquery endpoints for writing Cadquery
		source strings and later displaying geometries.

		Parameters:
			hasHeader: Boolean to include cadquery header.

		Returns:
			Cadquery for surface card object.
		"""

		cadquery = 'import cadquery as cq\n\n' if hasHeader else ''

		xmin, xmax, ymin, ymax, zmin, zmax = self.parameters['xmin'], self.parameters['xmax'], self.parameters['ymin'], self.parameters['ymax'], self.parameters['zmin'], self.parameters['zmax']
		xlen, ylen, zlen = math.fabs(xmax - xmin), math.fabs(ymax - ymin), math.fabs(zmax - zmin)

		cadquery += f"surface_{self.number} = cq.Workplane().box({xlen}, {ylen}, {zlen}).translate(({xmin + xlen / 2}, {ymin + ylen / 2}, {zmin + zlen / 2}))\n"

		return cadquery


class Sphere(Surface):
	"""
	'Sphere' represents sphere surface cards.

	'Sphere' functions as a data subtype for 'Surface'. It
	represents cell card parameter as abstract syntax 
	elements.
	"""


	def __init__(self) -> Self:
		"""
		'__init__' initializes 'Sphere'.
		"""

		self.vx: float = None
		self.vy: float = None
		self.vz: float = None
		self.r: float = None

		super().__init__()


	def set_parameters(self, vx: float, vy: float, vz: float, r: float) -> None:
		"""
		'set_parameters' sets sphere parameters.

		'set_parameters' checks parameter entries are valid 
		floating points. It raises errors if given None.

		Parameters:
			vx: Macrobody center x component.
			vy: Macrobody center y component.
			vz: Macrobody center z component.
			r: Sphere radius.
		"""

		value = types.cast_fortran_real(vx)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.vx = value
		self.parameters['vx'] = value

		value = types.cast_fortran_real(vy)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.vy = value
		self.parameters['vy'] = value

		value = types.cast_fortran_real(vz)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.vz = value
		self.parameters['vz'] = value

		value = types.cast_fortran_real(r)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.r = value
		self.parameters['r'] = value


	def to_cadquery(self, hasHeader: bool = False) -> str:
		"""
		'to_cadquery' generates cadquery from surface card objects.

		'to_cadquery' provides a Cadquery endpoints for writing Cadquery
		source strings and later displaying geometries.

		Parameters:
			hasHeader: Boolean to include cadquery header.

		Returns:
			Cadquery for surface card object.
		"""

		cadquery = 'import cadquery as cq\n\n' if hasHeader else ''

		vx, vy, vz = [self.vx, self.vy, self.vz]

		cadquery += f"surface_{self.number} = cq.Workplane().sphere({self.parameters['r']}).translate(({vx}, {vy}, {vz}))\n"

		return cadquery


class CylinderCircular(Surface):
	"""
	'CylinderCircular' represents right circular cylinder surface cards.

	'CylinderCircular' functions as a data subtype for 'Surface'. It
	represents cell card parameter as abstract syntax 
	elements.
	"""


	def __init__(self) -> Self:
		"""
		'__init__' initializes 'CylinderCircular'.
		"""

		self.vx: float = None
		self.vy: float = None
		self.vz: float = None
		self.hx: float = None
		self.hy: float = None
		self.hz: float = None
		self.r: float = None

		super().__init__()


	def set_parameters(self, vx: float, vy: float, vz: float, hx: float, hy: float, hz: float, r: float) -> None:
		"""
		'set_parameters' sets right circular cylinder parameters.

		'set_parameters' checks parameter entries are valid 
		floating points. It raises errors if given None.

		Parameters:
			vx: Macrobody center x component.
			vy: Macrobody center y component.
			vz: Macrobody center z component.
			hx: Macrobody height vector x component.
			hy: Macrobody height vector y component.
			hz: Macrobody height vector z component.
			r: Right circular cylinder radius.
		"""

		value = types.cast_fortran_real(vx)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.vx = value
		self.parameters['vx'] = value

		value = types.cast_fortran_real(vy)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.vy = value
		self.parameters['vy'] = value

		value = types.cast_fortran_real(vz)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.vz = value
		self.parameters['vz'] = value

		value = types.cast_fortran_real(hx)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.hx = value
		self.parameters['hx'] = value

		value = types.cast_fortran_real(hy)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.hy = value
		self.parameters['hy'] = value

		value = types.cast_fortran_real(hz)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.hz = value
		self.parameters['hz'] = value

		value = types.cast_fortran_real(r)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.r = value
		self.parameters['r'] = value


	def to_cadquery(self, hasHeader: bool = False) -> str:
		"""
		'to_cadquery' generates cadquery from surface card objects.

		'to_cadquery' provides a Cadquery endpoints for writing Cadquery
		source strings and later displaying geometries.

		Parameters:
			hasHeader: Boolean to include cadquery header.

		Returns:
			Cadquery for surface card object.
		"""

		cadquery = 'import cadquery as cq\n\n' if hasHeader else ''

		height = np.linalg.norm([self.parameters['hx'], self.parameters['hy'], self.parameters['hz']])
		ax, ay, az = np.cross([0, 0, 1], [self.parameters['hx'], self.parameters['hy'], self.parameters['hz']])
		angle = np.arccos(self.hz / np.linalg.norm([self.parameters['hx'], self.parameters['hy'], self.parameters['hz']])) * 180 / math.pi

		if self.hx == 0 and self.hy == 0 and self.hz / self.hz == 1:
			cadquery += f"surface_{self.number} = cq.Workplane().cylinder({height}, {self.parameters['r']}).translate(({self.vx}, {self.vy}, {self.vz + height / 2}))\n"
		else:	
			cadquery += f"surface_{self.number} = cq.Workplane().cylinder({height}, {self.parameters['r']}).translate(({self.vx}, {self.vy}, {self.vz + height / 2})).rotate(({self.vx - self.ax}, {self.vy - self.ay}, {self.vz - self.az}), ({self.vx + self.ax}, {vy + self.ay}, {self.vz + self.az}), {angle})\n"

		return cadquery


class HexagonalPrism(Surface):
	"""
	'HexagonalPrism' represents right hexagonal prism surface cards.

	'HexagonalPrism' functions as a data subtype for 'Surface'. It
	represents cell card parameter as abstract syntax 
	elements.
	"""


	def __init__(self) -> Self:
		"""
		'__init__' initializes 'HexagonalPrism'.
		"""

		self.vx: float = None
		self.vy: float = None
		self.vz: float = None
		self.hx: float = None
		self.hy: float = None
		self.hz: float = None
		self.r1: float = None
		self.r2: float = None
		self.r3: float = None
		self.s1: float = None
		self.s2: float = None
		self.s3: float = None
		self.t1: float = None
		self.t2: float = None
		self.t3: float = None

		super().__init__()


	def set_parameters(self, vx: float, vy: float, vz: float, hx: float, hy: float, hz: float, r1: float, r2: float, r3: float, s1: float, s2: float , s3: float, t1: float, t2: float, t3: float) -> None:
		"""
		'set_parameters' sets right hexagonal prism parameters.

		'set_parameters' checks parameter entries are valid 
		floating points. It raises errors if given None.

		Parameters:
			vx: Macrobody center x component.
			vy: Macrobody center y component.
			vz: Macrobody center z component.
			hx: Macrobody height vector x component.
			hy: Macrobody height vector y component.
			hz: Macrobody height vector z component.
			r1: Vector from center to facet #1.
			r2: Vector from center to facet #1.
			r3: Vector from center to facet #1.
			s1: Vector from center to facet #2.
			s2: Vector from center to facet #2.
			s3: Vector from center to facet #2.
			t1: Vector from center to facet #3.
			t2: Vector from center to facet #3.
			t3: Vector from center to facet #3.
		"""

		value = types.cast_fortran_real(vx)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.vx = value
		self.parameters['vx'] = value

		value = types.cast_fortran_real(vy)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.vy = value
		self.parameters['vy'] = value

		value = types.cast_fortran_real(vz)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.vz = value
		self.parameters['vz'] = value

		value = types.cast_fortran_real(hx)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.hx = value
		self.parameters['hx'] = value

		value = types.cast_fortran_real(hy)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.hy = value
		self.parameters['hy'] = value

		value = types.cast_fortran_real(hz)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.hz = value
		self.parameters['hz'] = value

		value = types.cast_fortran_real(r1)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.r1 = value
		self.parameters['r1'] = value

		value = types.cast_fortran_real(r2)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.r2 = value
		self.parameters['r2'] = value

		value = types.cast_fortran_real(r3)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.r3 = value
		self.parameters['r3'] = value

		if s1 is not None and s2 is not None and s3 is not None and t1 is not None and t2 is not None and t3 is not None:
			value = types.cast_fortran_real(s1)
			if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
			self.s1 = value
			self.parameters['s1'] = value

			value = types.cast_fortran_real(s2)
			if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
			self.s2 = value
			self.parameters['s2'] = value

			value = types.cast_fortran_real(s3)
			if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
			self.s3 = value
			self.parameters['s3'] = value

			value = types.cast_fortran_real(t1)
			if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
			self.t1 = value
			self.parameters['t1'] = value

			value = types.cast_fortran_real(t2)
			if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
			self.t2 = value
			self.parameters['t2'] = value

			value = types.cast_fortran_real(t3)
			if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
			self.t3 = value
			self.parameters['t3'] = value


	def to_cadquery(self, hasHeader: bool = False) -> str:
		"""
		'to_cadquery' generates cadquery from surface card objects.

		'to_cadquery' provides a Cadquery endpoints for writing Cadquery
		source strings and later displaying geometries.

		Parameters:
			hasHeader: Boolean to include cadquery header.

		Returns:
			Cadquery for surface card object.
		"""

		cadquery = 'import cadquery as cq\n\n' if hasHeader else ''

		if len(self.parameters.items()) == 9:
			height = np.linalg.norm([self.hx, self.hy, self.hz])
			apothem = np.linalg.norm([self.r1, self.r2, self.r3]) * 2 / math.sqrt(3)
			ax, ay, az = np.cross([0, 0, 1], [self.hx, self.hy, self.hz])
			angle = np.arccos(self.hz / np.linalg.norm([self.hx, self.hy, self.hz])) * 180 / math.pi
			if self.hx == 0 and self.hy == 0 and self.hz / self.hz == 1:
				cadquery += f"surface_{self.number} = cq.Workplane().sketch().regularPolygon({apothem}, 6).finalize().extrude({height}).translate(({self.vx}, {self.vy}, {self.vz}))\n"
			else:
				cadquery += f"surface_{self.number} = cq.Workplane().sketch().regularPolygon({apothem}, 6).finalize().extrude({height}).translate(({self.vx}, {self.vy}, {self.vz})).rotate(({self.vx - ax}, {self.vy - ay}, {self.vz - az}), ({self.vx + ax}, {self.vy + ay}, {self.vz + az}), {angle})\n"
		else:
			pass

		return cadquery


class CylinderElliptical(Surface):
	"""
	'CylinderElliptical' represents right elliptical cylinder surface cards.

	'CylinderElliptical' functions as a data subtype for 'Surface'. It
	represents cell card parameter as abstract syntax 
	elements.
	"""


	def __init__(self) -> Self:
		"""
		'__init__' initializes 'CylinderElliptical'.
		"""

		self.vx: float = None
		self.vy: float = None
		self.vz: float = None
		self.hx: float = None
		self.hy: float = None
		self.hz: float = None
		self.v1x: float = None
		self.v1y: float = None
		self.v1z: float = None

		super().__init__()


	def set_parameters(self, vx: float, vy: float, vz: float, hx: float, hy: float, hz: float, v1x: float, v1y: float, v1z: float, v2x: float, v2y: float, v2z: float) -> None:
		"""
		'set_parameters' sets right elliptical cylinder parameters.

		'set_parameters' checks parameter entries are valid 
		floating points. It raises errors if given None.

		Parameters:
			vx: Macrobody center x component.
			vy: Macrobody center y component.
			vz: Macrobody center z component.
			hx: Macrobody height vector x component.
			hy: Macrobody height vector y component.
			hz: Macrobody height vector z component.
			v1x: Macrobody vector #1 x component.
			v1y: Macrobody vector #1 y component.
			v1z: Macrobody vector #1 z component.
			v2x: Macrobody vector #2 x component.
			v2y: Macrobody vector #2 y component.
			v2z: Macrobody vector #2 z component.
		"""

		if vx is not None:
			value = types.cast_fortran_real(vx)
			if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
			self.vx = value
			self.parameters['vx'] = value

		if vy is not None:
			value = types.cast_fortran_real(vy)
			if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
			self.vy = value
			self.parameters['vy'] = value

		if vz is not None:
			value = types.cast_fortran_real(vz)
			if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
			self.vz = value
			self.parameters['vz'] = value

		if hx is not None:
			value = types.cast_fortran_real(hx)
			if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
			self.hx = value
			self.parameters['hx'] = value

		if hy is not None:
			value = types.cast_fortran_real(hy)
			if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
			self.hy = value
			self.parameters['hy'] = value

		if hz is not None:
			value = types.cast_fortran_real(hz)
			if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
			self.hz = value
			self.parameters['hz'] = value

		if v1x is not None:
			value = types.cast_fortran_real(v1x)
			if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
			self.v1x = value
			self.parameters['v1x'] = value

		if v1y is not None:
			value = types.cast_fortran_real(v1y)
			if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
			self.v1y = value
			self.parameters['v1y'] = value

		if v1z is not None:
			value = types.cast_fortran_real(v1z)
			if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
			self.v1z = value
			self.parameters['v1z'] = value

		if v2x is not None:
			value = types.cast_fortran_real(v2x)
			if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
			self.v2x = value
			self.parameters['v2x'] = value

		if v2y is not None:
			value = types.cast_fortran_real(v2y)
			if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
			self.v2y = value
			self.parameters['v2y'] = value

		if v2z is not None:
			value = types.cast_fortran_real(v2z)
			if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
			self.v2z = value
			self.parameters['v2z'] = value


	def to_cadquery(self, hasHeader: bool = False) -> str:
		"""
		'to_cadquery' generates cadquery from surface card objects.

		'to_cadquery' provides a Cadquery endpoints for writing Cadquery
		source strings and later displaying geometries.

		Parameters:
			hasHeader: Boolean to include cadquery header.

		Returns:
			Cadquery for surface card object.
		"""

		cadquery = 'import cadquery as cq\n\n' if hasHeader else ''

		vx, vy, vz = [self.vx, self.vy, self.vz]
		hx, hy, hz = [self.hx, self.hy, self.hz]
		v1x, v1y, v1z = [self.v1x, self.v1y, self.v1z]
		v2x, v2y, v2z = [self.v2x, self.v2y, self.v2z]
		height = np.linalg.norm([self.hx, self.hy, self.hz])
		ax, ay, az = np.cross([0, 0, 1], [self.hx, self.hy, self.hz])
		angle = np.arccos(hz / np.linalg.norm([self.hx, self.hy, self.hz])) * 180 / math.pi

		if hx == 0 and hy == 0 and hz / hz == 1:
			cadquery += f"surface_{self.number} = cq.Workplane().ellipse({np.linalg.norm([self.v1x, self.v1y, self.v1z])}, {np.linalg.norm([self.v2x, self.v2y, self.v2z])}).extrude({height}).translate(({vx}, {vy}, {vz}))\n"
		else:
			cadquery += f"surface_{self.number} = cq.Workplane().ellipse({np.linalg.norm([self.v1x, self.v1y, self.v1z])}, {np.linalg.norm([self.v2x, self.v2y, self.v2z])}).extrude({height}).translate(({vx}, {vy}, {vz})).rotate(({vx - ax}, {vy - ay}, {vz - az}), ({vx + ax}, {vy + ay}, {vz + az}), {angle})\n"

		return cadquery


class ConeTruncated(Surface):
	"""
	'ConeTruncated' represents truncated right-angle cone surface cards.

	'ConeTruncated' functions as a data subtype for 'Surface'. It
	represents cell card parameter as abstract syntax 
	elements.
	"""


	def __init__(self) -> Self:
		"""
		'__init__' initializes 'ConeTruncated'.
		"""

		self.vx: float = None
		self.vy: float = None
		self.vz: float = None
		self.hx: float = None
		self.hy: float = None
		self.hz: float = None
		self.r1: float = None
		self.r2: float = None

		super().__init__()


	def set_parameters(self, vx: float, vy: float, vz: float, hx: float, hy: float, hz: float, r1: float, r2: float) -> None:
		"""
		'set_parameters' sets truncated right-angle cone parameters.

		'set_parameters' checks parameter entries are valid 
		floating points. It raises errors if given None.

		Parameters:
			vx: Macrobody center x component.
			vy: Macrobody center y component.
			vz: Macrobody center z component.
			hx: Macrobody height vector x component.
			hy: Macrobody height vector y component.
			hz: Macrobody height vector z component.
			r1: Lower cone base radius.
			r2: Upper cone base radius.
		"""

		value = types.cast_fortran_real(vx)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.vx = value
		self.parameters['vx'] = value

		value = types.cast_fortran_real(vy)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.vy = value
		self.parameters['vy'] = value

		value = types.cast_fortran_real(vz)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.vz = value
		self.parameters['vz'] = value

		value = types.cast_fortran_real(hx)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.hx = value
		self.parameters['hx'] = value

		value = types.cast_fortran_real(hy)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.hy = value
		self.parameters['hy'] = value

		value = types.cast_fortran_real(hz)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.hz = value
		self.parameters['hz'] = value

		value = types.cast_fortran_real(r1)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.r1 = value
		self.parameters['r1'] = value

		value = types.cast_fortran_real(r2)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.r2 = value
		self.parameters['r2'] = value


	def to_cadquery(self, hasHeader: bool = False) -> str:
		"""
		'to_cadquery' generates cadquery from surface card objects.

		'to_cadquery' provides a Cadquery endpoints for writing Cadquery
		source strings and later displaying geometries.

		Parameters:
			hasHeader: Boolean to include cadquery header.

		Returns:
			Cadquery for surface card object.
		"""

		cadquery = 'import cadquery as cq\n\n' if hasHeader else ''

		vx, vy, vz = [self.vx, self.vy, self.vz]
		hx, hy, hz = [self.hx, self.hy, self.hz]
		r1 = self.parameters['r1']
		r2 = self.parameters['r2']
		ax, ay, az = np.cross([0, 0, 1], [self.hx, self.hy, self.hz])
		angle = np.arccos(hz / np.linalg.norm([self.hx, self.hy, self.hz])) * 180 / math.pi

		if hx == 0 and hy == 0 and hz / hz == 1:
			cadquery += f"surface_{self.number} = cq.Workplane().circle({self.parameters['r1']}).workplane(offset={np.linalg.norm([self.hx, self.hy, self.hz])}).circle({self.parameters['r2']}).loft().translate(({vx}, {vy}, {vz}))\n"
		else:
			cadquery += f"surface_{self.number} = cq.Workplane().circle({self.parameters['r1']}).workplane(offset={np.linalg.norm([self.hx, self.hy, self.hz])}).circle({self.parameters['r2']}).loft().translate(({vx}, {vy}, {vz})).rotate(({vx - ax}, {vy - ay}, {vz - az}), ({vx + ax}, {vy + ay}, {vz + az}), {angle})\n"
				
		return cadquery


class Ellipsoid(Surface):
	"""
	'Ellipsoid' represents ellipsoid surface cards.

	'Ellipsoid' functions as a data subtype for 'Surface'. It
	represents cell card parameter as abstract syntax 
	elements.
	"""


	def __init__(self) -> Self:
		"""
		'__init__' initializes 'Ellipsoid'.
		"""

		self.v1x: float = None
		self.v1y: float = None
		self.v1z: float = None
		self.v2x: float = None
		self.v2y: float = None
		self.v2z: float = None
		self.rm: float = None

		super().__init__()


	def set_parameters(self, v1x: float, v1y: float, v1z: float, v2x: float, v2y: float, v2z: float, rm: float) -> None:
		"""
		'set_parameters' sets ellipsoid parameters.

		'set_parameters' checks parameter entries are valid 
		floating points. It raises errors if given None.

		Parameters:
			v1x: Macrobody vector #1 x component.
			v1y: Macrobody vector #1 y component.
			v1z: Macrobody vector #1 z component.
			v2x: Macrobody vector #2 x component.
			v2y: Macrobody vector #2 y component.
			v2z: Macrobody vector #2 z component.
			rm: Minor/major radius length.
		"""

		value = types.cast_fortran_real(v1x)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.v1x = value
		self.parameters['v1x'] = value

		value = types.cast_fortran_real(v1y)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.v1y = value
		self.parameters['v1y'] = value

		value = types.cast_fortran_real(v1z)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.v1z = value
		self.parameters['v1z'] = value

		value = types.cast_fortran_real(v2x)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.v2x = value
		self.parameters['v2x'] = value

		value = types.cast_fortran_real(v2y)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.v2y = value
		self.parameters['v2y'] = value

		value = types.cast_fortran_real(v2z)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.v2z = value
		self.parameters['v2z'] = value

		value = types.cast_fortran_real(rm)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.rm = value
		self.parameters['rm'] = value


	def to_cadquery(self, hasHeader: bool = False) -> str:
		"""
		'to_cadquery' generates cadquery from surface card objects.

		'to_cadquery' provides a Cadquery endpoints for writing Cadquery
		source strings and later displaying geometries.

		Parameters:
			hasHeader: Boolean to include cadquery header.

		Returns:
			Cadquery for surface card object.
		"""

		cadquery = 'import cadquery as cq\n\n' if hasHeader else ''

		if self.parameters['rm'] > 0:
			a = self.parameters['rm']
			b = math.sqrt(self.parameters['rm'] ** 2 - (np.linalg.norm([self.v2x, self.v2y, self.v2z] - [self.v1x, self.v1y, self.v1z]) / 2) ** 2)
			vx, vy, vz = ([self.v2x, self.v2y, self.v2z] - [self.v1x, self.v1y, self.v1z]) / 2 + [self.v1x, self.v1y, self.v1z]
			ax, ay, az = np.cross([0, 1, 0], [self.v2x, self.v2y, self.v2z] - [self.v1x, self.v1y, self.v1z])
			angle = np.arccos([self.v2x, self.v2y, self.v2z][1] / np.linalg.norm([self.v2x, self.v2y, self.v2z])) * 180 / math.pi
			cadquery += f"surface_{self.number} = cq.Workplane().ellipseArc({b}, {a}, -90, 90).close().revolve(axisStart=(0, -{a}, 0), axisEnd=(0, {a}, 0)).translate(({vx}, {vy - a}, {vz})).rotate(({vx - ax}, {vy - ay}, {vz - az}), ({vx + ax}, {vy + ay}, {vz + az}), {angle})\n"
		elif self.parameters['rm'] < 0:
			a = np.linalg.norm([self.v2x, self.v2y, self.v2z])
			b = math.fabs(self.parameters['rm'])
			vx, vy, vz = [self.v1x, self.v1y, self.v1z]
			ax, ay, az = np.cross([0, 1, 0], [self.v2x, self.v2y, self.v2z])
			angle = np.arccos([self.v2x, self.v2y, self.v2z][1] / np.linalg.norm([self.v2x, self.v2y, self.v2z])) * 180 / math.pi
			cadquery += f"surface_{self.number} = cq.Workplane().ellipseArc({b}, {a}, -90, 90).close().revolve(axisStart=(0, -{a}, 0), axisEnd=(0, {a}, 0)).translate(({vx}, {vy - a}, {vz})).rotate(({vx - ax}, {vy - ay}, {vz - az}), ({vx + ax}, {vy + ay}, {vz + az}), {angle})\n"

		return cadquery


class Wedge(Surface):
	"""
	'Wedge' represents wedge surface card.

	'Wedge' functions as a data subtype for 'Cell'. It
	represents cell card parameter as abstract syntax 
	elements.
	"""


	def __init__(self) -> Self:
		"""
		'__init__' initializes 'Wedge'.
		"""

		self.vx: float = None
		self.vy: float = None
		self.vz: float = None
		self.v1x: float = None
		self.v1y: float = None
		self.v1z: float = None
		self.v2x: float = None
		self.v2y: float = None
		self.v2z: float = None
		self.v3x: float = None
		self.v3y: float = None
		self.v3z: float = None

		super().__init__()


	def set_parameters(self, vx: float, vy: float, vz: float, v1x: float, v1y: float, v1z: float, v2x: float, v2y: float, v2z: float, v3x: float, v3y: float, v3z: float) -> None:
		"""
		'set_parameters' sets wedge parameters.

		'set_parameters' checks parameter entries are valid 
		floating points. It raises errors if given None.

		Parameters:
			vx: Macrobody center x component.
			vy: Macrobody center y component.
			vz: Macrobdoy center z component.
			v1x: Macrobody vector #1 x component.
			v1y: Macrobody vector #1 y component.
			v1z: Macrobody vector #1 z component.
			v2x: Macrobody vector #2 x component.
			v2y: Macrobody vector #2 y component.
			v2z: Macrobody vector #2 z component.
			v3x: Macrobody vector #3 x component.
			v3y: Macrobody vector #3 y component.
			v3z: Macrobody vector #3 z component.
		"""

		value = types.cast_fortran_real(vx)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.vx = value
		self.parameters['vx'] = value

		value = types.cast_fortran_real(vy)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.vy = value
		self.parameters['vy'] = value

		value = types.cast_fortran_real(vz)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.vz = value
		self.parameters['vz'] = value

		value = types.cast_fortran_real(v1x)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.v1x = value
		self.parameters['v1x'] = value

		value = types.cast_fortran_real(v1y)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.v1y = value
		self.parameters['v1y'] = value

		value = types.cast_fortran_real(v1z)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.v1z = value
		self.parameters['v1z'] = value

		value = types.cast_fortran_real(v2x)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.v2x = value
		self.parameters['v2x'] = value

		value = types.cast_fortran_real(v2y)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.v2y = value
		self.parameters['v2y'] = value

		value = types.cast_fortran_real(v2z)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.v2z = value
		self.parameters['v2z'] = value

		value = types.cast_fortran_real(v3x)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.v3x = value
		self.parameters['v3x'] = value

		value = types.cast_fortran_real(v3y)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.v3y = value
		self.parameters['v3y'] = value

		value = types.cast_fortran_real(v3z)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.v3z = value
		self.parameters['v3z'] = value


	def to_cadquery(self, hasHeader: bool = False) -> str:
		"""
		'to_cadquery' generates cadquery from surface card objects.

		'to_cadquery' provides a Cadquery endpoints for writing Cadquery
		source strings and later displaying geometries.

		Parameters:
			hasHeader: Boolean to include cadquery header.

		Returns:
			Cadquery for surface card object.
		"""

		cadquery = 'import cadquery as cq\n\n' if hasHeader else ''

		vx, vy, vz = [self.vx, self.vy, self.vz]
		v1x, v1y, v1z = [self.v1x, self.v1y, self.v1z]
		v2x, v2y, v2z = [self.v2x, self.v2y, self.v2z]
		v3x, v3y, v3z = [self.v3x, self.v3y, self.v3z]

		cadquery += f"surface_{self.number} = cq.Workplane().polyline([({v1x}, {v1y}, {v1z}), (0, 0, 0), ({v2x}, {v2y}, {v2z})]).close().polyline([({v1x + v3x}, {v1y + v3y}, {v1z + v3z}), ({v3x}, {v3y}, {v3z}), ({v2x + v3x}, {v2y + v3y}, {v2z + v3z})]).close().loft().translate(({vx}, {vy}, {vz}))\n"

		return cadquery


class Polyhedron(Surface):
	"""
	'Polyhedron' represents arbitrary polyhedron surface cards.

	'Polyhedron' functions as a data subtype for 'Surface'. It
	represents cell card parameter as abstract syntax 
	elements.
	"""


	def __init__(self) -> Self:
		"""
		'__init__' initializes 'Polyhedron'.
		"""

		self.ax: float = None
		self.ay: float = None
		self.az: float = None
		self.bx: float = None
		self.by: float = None
		self.bz: float = None
		self.cx: float = None
		self.cy: float = None
		self.cz: float = None
		self.dx: float = None
		self.dy: float = None
		self.dz: float = None
		self.ex: float = None
		self.ey: float = None
		self.ez: float = None
		self.fx: float = None
		self.fy: float = None
		self.fz: float = None
		self.gx: float = None
		self.gy: float = None
		self.gz: float = None
		self.hx: float = None
		self.hy: float = None
		self.hz: float = None
		self.n1: float = None
		self.n2: float = None
		self.n3: float = None
		self.n4: float = None
		self.n5: float = None
		self.n6: float = None

		super().__init__()


	def set_parameters(self, ax: float, ay: float, az: float, bx: float, by: float, bz: float, cx: float, cy: float, cz: float, dx: float, dy: float, dz: float, ex: float, ey: float, ez: float, fx: float, fy: float, fz: float, gx: float, gy: float, gz: float, hx: float, hy: float, hz: float, n1: float, n2: float, n3: float, n4: float, n5: float, n6: float) -> None:
		"""
		'set_parameters' sets arbitrary polyhedron parameters.

		'set_parameters' checks parameter entries are valid 
		floating points. It raises errors if given None.

		Parameters:
			ax: Coordnate #1 x component.
			ay: Coordnate #1 y component.
			az: Coordnate #1 z component.
			bx: Coordnate #2 x component.
			by: Coordnate #2 y component.
			bz: Coordnate #2 z component.
			cx: Coordnate #3 x component.
			cy: Coordnate #3 y component.
			cz: Coordnate #3 z component.
			dx: Coordnate #4 x component.
			dy: Coordnate #4 y component.
			dz: Coordnate #4 z component.
			ex: Coordnate #5 x component.
			ey: Coordnate #5 y component.
			ez: Coordnate #5 z component.
			fx: Coordnate #6 x component.
			fy: Coordnate #6 y component.
			fz: Coordnate #6 z component.
			gx: Coordnate #7 x component.
			gy: Coordnate #7 y component.
			gz: Coordnate #7 z component.
			hx: Coordnate #8 x component.
			hy: Coordnate #8 y component.
			hz: Coordnate #8 z component.
			n1: Corresponding corners specifier #1.
			n2: Corresponding corners specifier #2.
			n3: Corresponding corners specifier #3.
			n4: Corresponding corners specifier #4.
			n5: Corresponding corners specifier #5.
			n6: Corresponding corners specifier #6.
		"""

		value = types.cast_fortran_real(ax)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.ax = value
		self.parameters['ax'] = value

		value = types.cast_fortran_real(ay)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.ay = value
		self.parameters['ay'] = value

		value = types.cast_fortran_real(az)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.az = value
		self.parameters['az'] = value

		value = types.cast_fortran_real(bx)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.bx = value
		self.parameters['bx'] = value

		value = types.cast_fortran_real(by)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.by = value
		self.parameters['by'] = value

		value = types.cast_fortran_real(bz)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.bz = value
		self.parameters['bz'] = value

		value = types.cast_fortran_real(cx)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.cx = value
		self.parameters['cx'] = value

		value = types.cast_fortran_real(cy)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.cy = value
		self.parameters['cy'] = value

		value = types.cast_fortran_real(cz)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.cz = value
		self.parameters['cz'] = value

		value = types.cast_fortran_real(dx)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.dx = value
		self.parameters['dx'] = value

		value = types.cast_fortran_real(dy)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.dy = value
		self.parameters['dy'] = value

		value = types.cast_fortran_real(dz)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.dz = value
		self.parameters['dz'] = value

		value = types.cast_fortran_real(ex)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.ex = value
		self.parameters['ex'] = value

		value = types.cast_fortran_real(ey)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.ey = value
		self.parameters['ey'] = value

		value = types.cast_fortran_real(ez)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.ez = value
		self.parameters['ez'] = value

		value = types.cast_fortran_real(fx)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.fx = value
		self.parameters['fx'] = value

		value = types.cast_fortran_real(fy)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.fy = value
		self.parameters['fy'] = value

		value = types.cast_fortran_real(fz)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.fz = value
		self.parameters['fz'] = value

		value = types.cast_fortran_real(gx)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.gx = value
		self.parameters['gx'] = value

		value = types.cast_fortran_real(gy)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.gy = value
		self.parameters['gy'] = value

		value = types.cast_fortran_real(gz)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.gz = value
		self.parameters['gz'] = value

		value = types.cast_fortran_real(hx)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.hx = value
		self.parameters['hx'] = value

		value = types.cast_fortran_real(hy)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.hy = value
		self.parameters['hy'] = value

		value = types.cast_fortran_real(hz)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.hz = value
		self.parameters['hz'] = value

		value = types.cast_fortran_real(n1)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.n1 = value
		self.parameters['n1'] = value

		value = types.cast_fortran_real(n2)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.n2 = value
		self.parameters['n2'] = value

		value = types.cast_fortran_real(n3)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.n3 = value
		self.parameters['n3'] = value

		value = types.cast_fortran_real(n4)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.n4 = value
		self.parameters['n4'] = value

		value = types.cast_fortran_real(n5)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.n5 = value
		self.parameters['n5'] = value

		value = types.cast_fortran_real(n6)
		if value is None: raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)
		self.n6 = value
		self.parameters['n6'] = value


	def to_cadquery(self, hasHeader: bool = False) -> str:
		"""
		'to_cadquery' generates cadquery from surface card objects.

		'to_cadquery' provides a Cadquery endpoints for writing Cadquery
		source strings and later displaying geometries.

		Parameters:
			hasHeader: Boolean to include cadquery header.

		Returns:
			Cadquery for surface card object.
		"""

		cadquery = 'import cadquery as cq\n\n' if hasHeader else ''
		
		return cadquery

