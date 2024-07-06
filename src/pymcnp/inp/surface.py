"""
'surface' contains the class representing INP surface cards.

Classes:
	Surface: Representation of INP surface cards.
"""


from typing import *
import collections
import math

import numpy as np

from .card import Card
from .errors import *
from . import *


class Surface(Card):
	"""
	'Surface' represents INP surface cards.

	Fields:
		number (int): Surface card number.
		mnemonic (str): Surface card type identifier.
		transform (int): Surface card transformation number.
		periodic (int): Surface card periodic number.
		parameters (dict[str, Union[float, Type[np.ndarray]]]): Surface parameter list based on mnemonic.

	Methods:
		__init__: Initializes 'Surface'.
		from_mcnp: Generates surface card objects from INP.
		from_arguments: Generates surface card objects from arguments.
		to_mcnp: Generates INP from surface card objects.
		to_arguments: Generetes lists from surface card objects.
	"""


	PARAMETER_SYNTAX = {
		'p4': [('a', 'float'), ('B', 'float'), ('C', 'float'), ('D', 'float')],
		'px': [('D', 'float')],
		'py': [('D', 'float')],
		'pz': [('D', 'float')],
		'so': [('r', 'float')],
		's': [('x', 'float'), ('y', 'float'), ('z', 'float'), ('r', 'float')],
		'sx': [('x', 'float'), ('r', 'float')],
		'sy': [('y', 'float'), ('r', 'float')],
		'sz': [('z', 'float'), ('r', 'float')],
		'c/y': [('x', 'float'), ('z', 'float'), ('r', 'float')],
		'c/z': [('x', 'float'), ('y', 'float'), ('r', 'float')],
		'cx': [('r', 'float')],
		'cy': [('r', 'float')],
		'cz': [('r', 'float')],
		'k/x': [('x', 'float'), ('y', 'float'), ('z', 'float'), ('t^2', 'float'), ('+-1' , 'float')],
		'k/y': [('x', 'float'), ('y', 'float'), ('z', 'float'), ('t^2', 'float'), ('+-1' , 'float')],
		'k/z': [('x', 'float'), ('y', 'float'), ('z', 'float'), ('t^2', 'float'), ('+-1' , 'float')],
		'kx': [('x', 'float'), ('t^2', 'float'), ('+-1', 'float')],
		'ky': [('y', 'float'), ('t^2', 'float'), ('+-1', 'float')],
		'kz': [('z', 'float'), ('t^2', 'float'), ('+-1', 'float')],
		'sq': [('A', 'float'), ('B', 'float'), ('C', 'float'), ('D', 'float'), ('E', 'float'), ('F', 'float'), ('G', 'float'), ('x', 'float'), ('y', 'float'), ('z', 'float')],
		'gq': [('A', 'float'), ('B', 'float'), ('C', 'float'), ('D', 'float'), ('E', 'float'), ('F', 'float'), ('G', 'float'), ('H', 'float'), ('J', 'float'), ('K', 'float')],
		'tx': [('x', 'float'), ('y', 'float'), ('z', 'float'), ('A', 'float'), ('B', 'float'), ('C', 'float')],
		'ty': [('x', 'float'), ('y', 'float'), ('z', 'float'), ('A', 'float'), ('B', 'float'), ('C', 'float')],
		'tz': [('x', 'float'), ('y', 'float'), ('z', 'float'), ('A', 'float'), ('B', 'float'), ('C', 'float')],
		'x2': [('xr1', '2darray')],
		'y2': [('yr1', '2darray')],
		'z2': [('zr1', '2darray')],
		'x4': [('xr1', '2darray'), ('xr2', '2darray')],
		'y4': [('yr1', '2darray'), ('yr2', '2darray')],
		'z4': [('zr1', '2darray'), ('zr2', '2darray')],
		'x6': [('xr1', '2darray'), ('xr2', '2darray'), ('xr3', '2darray')],
		'y6': [('yr1', '2darray'), ('yr2', '2darray'), ('yr3', '2darray')],
		'z6': [('zr1', '2darray'), ('zr2', '2darray'), ('zr3', '2darray')],
		'p9': [('xyz1' '3darray'), ('xyz2', '3darray'), ('xyz3', '3darray')],
		'box': [('v', '3darray'), ('a1', '3darray'), ('a2', '3darray'), ('a3', '3darray')],
		'rpp': [('xmin', 'float'), ('xmax', 'float'), ('ymin', 'float'), ('ymax', 'float'), ('zmin', 'float'), ('zmax', 'float')],
		'sph': [('v', '3darray'), ('r', 'float')],
		'rcc': [('v', '3darray'), ('h', '3darray'), ('r', 'float')],
		'rhp9': [('v', '3darray'), ('h', '3darray'), ('r', '3darray')],
		'hex9': [('v', '3darray'), ('h', '3darray'), ('r', '3darray')],
		'rhp15': [('v', '3darray'), ('h', '3darray'), ('r', '3darray'), ('s', '3darray'), ('t', '3darray')],
		'hex15': [('v', '3darray'), ('h', '3darray'), ('r', '3darray'), ('s', '3darray'), ('t', '3darray')],
		'rec10': [('v', '3darray'), ('h', '3darray'), ('v1', '3darray'), ('r', 'float')],
		'rec12': [('v', '3darray'), ('h', '3darray'), ('v1', '3darray'), ('v2', '3darray')],
		'trc': [('v', '3darray'), ('h', '3darray'), ('r1', 'float'), ('r2', 'float')],
		'ell': [('v1', '3darray'), ('v2', '3darray'), ('rm', 'float')],
		'wed': [('v', '3darray'), ('v1', '3darray'), ('v2', '3darray'), ('v3', '3darray')],
		'arb': [('a', '3darray'), ('b', '3darray'), ('c', '3darray'), ('d', '3darray'), ('e', '3darray'), ('f', '3darray'), ('g', '3darray'), ('h', '3darray'), ('n', '6darray')]
	}


	def __init__(self):
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
		self.parameters: dict[str, Union[Type[np.ndarray], float]] = {}


	def set_number(self, number = None):
		if not is_integer(number): raise INPValueError
		number = int(number)

		if 1 > number or number > 99_999_999: raise INPValueError;
		self.number = number


	def set_mnemonic(self, mnemonic = None):
		if not is_mnemonic(mnemonic): raise INPValueError
		self.mnemonic = mnemonic


	def set_transform_periodic(self, transform_periodic):
		if not is_integer(transform_periodic): raise INPValueError
		periodic = int(transform_periodic)

		if transform_periodic < 0:
			self.periodic = transform_periodic
			self.transform = None
		elif transform_periodic > 0:
			self.periodic = None
			self.transform = transform_periodic
		else:
			self.periodic = None
			self.transform = None


	@classmethod
	def from_mcnp(cls, card: str) -> Self:
		"""
		'from_mcnp' generates surface card objects from INP.

		Parameters:
			source (str): INP to parse.

		Returns:
			surface (Surface): Surface card object.
		"""

		surface = cls()

		entries = Deque(card.lower().split(' '))
		if not entries: raise SyntaxError
		entry = entries.popleft()
		
		# Processing Reflecting Prefix
		if entry[0] == '+':
			self.is_white_boundary = True
			entry = entry[1:]
		elif entry[0] == '*':
			self.is_reflecting_number = True
			entry = entry[1:]

		# Processing Card Number
		surface.set_number(entry)
		surface.id = surface.number

		if not entries: raise SyntaxError
		entry = entries.popleft()

		# Processing Transformation Number
		if is_integer(entry):
			surface.set_transfrom_periodic(entry)

			if not entries: raise SyntaxError
			entry = entries.popleft()

		# Processing Mnemonic
		surface.set_mnemonic(entry)

		# Processing Parameters
		match surface.mnemonic:
			case 'so':
				if len(entries) != 1: raise INPSyntaxError(surface.mnemonic)
				surface.__class__ = SphereOrigin
				surface.set_parameters(*entries)
			case _:
				match surface.mnemonic:
					case 'p':
						if len(entires) not in [4, 9]: raise SyntaxError
						syntax_key = surface.mnemonic + str(len(entries))
					case 'x' | 'y' | 'z':
						if len(entires) not in [2, 4, 6]: raise SyntaxError
						syntax_key = surface.mnemonic + str(len(entries))
					case 'rec':
						if len(entries) not in [10, 12]: raise SyntaxError
						syntax_key = surface.mnemonic + str(len(entries))
					case 'hex' | 'rhp':
						if len(entries) not in [9, 15]: raise SyntaxError
						syntax_key = surface.mnemonic + str(len(entries))
					case _:
						syntax_key = surface.mnemonic

				for name, type_literal in surface.PARAMETER_SYNTAX[syntax_key]:
					match type_literal:
						case 'float':
							if len(entries) < 1: raise SyntaxError

							entry = entries.popleft()
							if not is_real(entry): raise ValueError

							surface.parameters[name] = float(entry)
						case '2darray':
							if len(entries) < 2: raise SyntaxError

							entry0 = entries.popleft()
							entry1 = entries.popleft()
							if not is_real(entry0): raise ValueError
							if not is_real(entry1): raise ValueError

							surface.parameters[name] = np.array([float(entry0), float(entry1)])
						case '3darray':
							if len(entries) < 3: raise SyntaxError

							entry0 = entries.popleft()
							entry1 = entries.popleft()
							entry2 = entries.popleft()
							if not is_real(entry0): raise ValueError
							if not is_real(entry1): raise ValueError
							if not is_real(entry2): raise ValueError

							surface.parameters[name] = np.array([float(entry0), float(entry1), float(entry2)])
						case '6darray':
							if len(entries) < 6: raise SyntaxError

							entry0 = entries.popleft()
							entry1 = entries.popleft()
							entry2 = entries.popleft()
							entry3 = entries.popleft()
							entry4 = entries.popleft()
							entry5 = entries.popleft()
							if not is_real(entry0): raise ValueError
							if not is_real(entry1): raise ValueError
							if not is_real(entry2): raise ValueError
							if not is_real(entry3): raise ValueError
							if not is_real(entry4): raise ValueError
							if not is_real(entry5): raise ValueError

							surface.parameters[name] = np.array([entry0, entry1, entry2, entry3, entry4, entry5])


		return surface
					
		
	@classmethod
	def from_arguments(cls, number: int, mnemonic: str, *parameters, transform_periodic: int = None) -> Self:
		"""
		'from_arguments' generates surface card objects from arguments.

		Arguments:
			number (int): Surface card number.
			mnemonic (str): Surface card mnemonic.
			transform (int): Surface card transformation number.
			parameters (dict[str, Union[Type[np.ndarray], float]]): Surface card parameters.

		Returns:
			surface (Surface): Surface card object.
		"""

		surface = cls()

		# Processing Card Number
		surface.set_number(number)
		surface.id = surface.number

		# Processing Transformation Number
		if transform_periodic >= 0:
			surface.set_transfrom(transform_periodic)
		else:
			surface.set_periodic(transform_periodic)

		# Processing Mnemonic
		surface.set_mnemonic(mnemonic)

		# Processing Parameters
		if set([spec[0] for spec in surface.PARAMETER_SYNTAX[surface.mnemonic]]) != set(parameters.keys()): raise SyntaxError

		for name, type_literal in surface.PARAMETER_SYNTAX[surface.mnemonic]:
			match type_literal:
				case 'float':
					if not is_real(parameters[name]): raise ValueError
				case '3darray':
					if len(parameters[name]) < 3: raise SyntaxError

		surface.parameters = parameters

		return surface


	def to_mcnp(self) -> str:
		"""
		'to_mcnp' generates INP from surface card objects.

		Returns:
			source (str): INP for surface card object.
		"""

		if not is_integer(self.number, lambda i : 1 <= i and i <= 99_999_999): raise ValueError
		if not is_mnemonic(self.mnemonic): raise SyntaxError

		parameters_str = ' '.join([str(parameter) if isinstance(parameter, float) or isinstance(parameter, int) else ' '.join(str(entry) for entry in list(parameter)) for _, parameter in self.parameters.items()])
		source = f"{self.number}{' ' + {self.transform} + ' ' if self.transform is not None else ' '}{self.mnemonic} {parameters_str}"

		return add_continuation_lines(source)


	def to_arguments(self) -> dict:
		"""
		'to_arguments' generates dictionaries from surface card objects.

		Returns:
			arguments (dict): Dictionary for surface card objectd.
		"""

		return {'j': self.number, 'n': self.transform, 'A': self.mnemonic, 'list': self.parameters}


	def to_cadquery(self, hasHeader: Optional[bool] = False) -> str:
		"""
		'to_cadquery' generates cadquery from surface card objects.

		Parameters:
			hasHeader (bool): Boolean to include cadquery header.

		Returns:
			cadquery (str): Cadquery for surface card object.
		"""

		cadquery = 'import cadquery as cq\n\n' if hasHeader else ''

		match self.mnemonic:
			# def to_cadquery(self, hasHeader: Optional[bool] = False) -> str:
			# return ('import cadquery as cq\n\n' if hasHeader else '') + f"surface_{self.number} = cq.Workplane().sphere({self.parameters['r']})\n"
			case "so":
				cadquery += f"surface_{self.number} = cq.Workplane().sphere({self.parameters['r']})\n"	
			case "s":
				cadquery += f"surface_{self.number} = cq.Workplane().sphere({self.parameters['r']}).translate(({self.parameters['x']}, {self.parameters['y']}, {self.parameters['z']}))\n"

			case "sx":
				cadquery += f"surface_{self.number} = cq.Workplane().sphere({self.parameters['r']}).translate(({self.parameters['x']}, 0, 0))\n"

			case "sy":
				cadquery += f"surface_{self.number} = cq.Workplane().sphere({self.parameters['r']}).translate((0, {self.parameters['y']}, 0))\n"

			case "sz":
				cadquery += f"surface_{self.number} = cq.Workplane().sphere({self.parameters['r']}).translate((0, 0, {self.parameters['z']}))\n"

			case "box":
				length, width, height = np.linalg.norm(self.parameters['a1']), np.linalg.norm(self.parameters['a2']), np.linalg.norm(self.parameters['a3'])
				vx, vy, vz, a1x, a1y, a1z, a2x, a2y, a2z, a3x, a3y, a3z = *self.parameters['v'], *self.parameters['a1'], *self.parameters['a2'], *self.parameters['a3']

				cadquery += f"surface_{self.number} = cq.Workplane().polyline([({vx}, {vy}, {vz}), ({vx + a1x}, {vy + a1y}, {vz + a1z}), ({vx + a2x + a1x}, {vy + a2y + a1y}, {vz + a2z + a1z}), ({vx + a2x}, {vy + a2y}, {vz + a2z})]).close().polyline([({vx + a3x}, {vy + a3y}, {vz + a3z}), ({vx + a1x + a3x}, {vy + a1y + a3y}, {vz + a1z + a3z}), ({vx + a2x + a1x + a3x}, {vy + a2y + a1y + a3y}, {vz + a2z + a1z + a3z}), ({vx + a2x + a3x}, {vy + a2y + a3y}, {vz + a2z + a3z})]).close().loft()\n"

			case "rpp":
				xmin, xmax, ymin, ymax, zmin, zmax = self.parameters['xmin'], self.parameters['xmax'], self.parameters['ymin'], self.parameters['ymax'], self.parameters['zmin'], self.parameters['zmax']
				xlen, ylen, zlen = math.fabs(xmax - xmin), math.fabs(ymax - ymin), math.fabs(zmax - zmin)

				cadquery += f"surface_{self.number} = cq.Workplane().box({xlen}, {ylen}, {zlen}).translate(({xmin + xlen / 2}, {ymin + ylen / 2}, {zmin + zlen / 2}))\n"

			case "sph":
				vx, vy, vz = self.parameters['v']

				cadquery += f"surface_{self.number} = cq.Workplane().sphere({self.parameters['r']}).translate(({vx}, {vy}, {vz}))\n"

			case "rcc":
				vx, vy, vz = self.parameters['v']
				hx, hy, hz = self.parameters['h']
				height = np.linalg.norm(self.parameters['h'])
				ax, ay, az = np.cross([0, 0, 1], self.parameters['h'])
				angle = np.arccos(hz / np.linalg.norm(self.parameters['h'])) * 180 / math.pi

				if hx == 0 and hy == 0 and hz / hz == 1:
					cadquery += f"surface_{self.number} = cq.Workplane().cylinder({height}, {self.parameters['r']}).translate(({vx}, {vy}, {vz + height / 2}))\n"
				else:	
					cadquery += f"surface_{self.number} = cq.Workplane().cylinder({height}, {self.parameters['r']}).translate(({vx}, {vy}, {vz + height / 2})).rotate(({vx - ax}, {vy - ay}, {vz - az}), ({vx + ax}, {vy + ay}, {vz + az}), {angle})\n"
			
			case "hex" | "rhp":
				if len(self.parameters.items()) == 3:
					vx, vy, vz = self.parameters['v']
					hx, hy, hz = self.parameters['h']
					height = np.linalg.norm(self.parameters['h'])
					apothem = np.linalg.norm(self.parameters['r']) * 2 / math.sqrt(3)
					ax, ay, az = np.cross([0, 0, 1], self.parameters['h'])
					angle = np.arccos(hz / np.linalg.norm(self.parameters['h'])) * 180 / math.pi

					if hx == 0 and hy == 0 and hz / hz == 1:
						cadquery += f"surface_{self.number} = cq.Workplane().sketch().regularPolygon({apothem}, 6).finalize().extrude({height}).translate(({vx}, {vy}, {vz}))\n"
					else:
						cadquery += f"surface_{self.number} = cq.Workplane().sketch().regularPolygon({apothem}, 6).finalize().extrude({height}).translate(({vx}, {vy}, {vz})).rotate(({vx - ax}, {vy - ay}, {vz - az}), ({vx + ax}, {vy + ay}, {vz + az}), {angle})\n"
				else:
					pass

			case "rec":
				vx, vy, vz = self.parameters['v']
				hx, hy, hz = self.parameters['h']
				v1x, v1y, v1z = self.parameters['v1']
				v2x, v2y, v2z = self.parameters['v2']
				height = np.linalg.norm(self.parameters['h'])
				ax, ay, az = np.cross([0, 0, 1], self.parameters['h'])
				angle = np.arccos(hz / np.linalg.norm(self.parameters['h'])) * 180 / math.pi

				if hx == 0 and hy == 0 and hz / hz == 1:
					cadquery += f"surface_{self.number} = cq.Workplane().ellipse({np.linalg.norm(self.parameters['v1'])}, {np.linalg.norm(self.parameters['v2'])}).extrude({height}).translate(({vx}, {vy}, {vz}))\n"
				else:
					cadquery += f"surface_{self.number} = cq.Workplane().ellipse({np.linalg.norm(self.parameters['v1'])}, {np.linalg.norm(self.parameters['v2'])}).extrude({height}).translate(({vx}, {vy}, {vz})).rotate(({vx - ax}, {vy - ay}, {vz - az}), ({vx + ax}, {vy + ay}, {vz + az}), {angle})\n"

			case "trc":
				vx, vy, vz = self.parameters['v']
				hx, hy, hz = self.parameters['h']
				r1 = self.parameters['r1']
				r2 = self.parameters['r2']
				ax, ay, az = np.cross([0, 0, 1], self.parameters['h'])
				angle = np.arccos(hz / np.linalg.norm(self.parameters['h'])) * 180 / math.pi

				if hx == 0 and hy == 0 and hz / hz == 1:
					cadquery += f"surface_{self.number} = cq.Workplane().circle({self.parameters['r1']}).workplane(offset={np.linalg.norm(self.parameters['h'])}).circle({self.parameters['r2']}).loft().translate(({vx}, {vy}, {vz}))\n"
				else:
					cadquery += f"surface_{self.number} = cq.Workplane().circle({self.parameters['r1']}).workplane(offset={np.linalg.norm(self.parameters['h'])}).circle({self.parameters['r2']}).loft().translate(({vx}, {vy}, {vz})).rotate(({vx - ax}, {vy - ay}, {vz - az}), ({vx + ax}, {vy + ay}, {vz + az}), {angle})\n"
			
			case "ell":
				if self.parameters['rm'] > 0:
					a = self.parameters['rm']
					b = math.sqrt(self.parameters['rm'] ** 2 - (np.linalg.norm(self.parameters['v2'] - self.parameters['v1']) / 2) ** 2)
					vx, vy, vz = (self.parameters['v2'] - self.parameters['v1']) / 2 + self.parameters['v1']
					ax, ay, az = np.cross([0, 1, 0], self.parameters['v2'] - self.parameters['v1'])
					angle = np.arccos(self.parameters['v2'][1] / np.linalg.norm(self.parameters['v2'])) * 180 / math.pi

					cadquery += f"surface_{self.number} = cq.Workplane().ellipseArc({b}, {a}, -90, 90).close().revolve(axisStart=(0, -{a}, 0), axisEnd=(0, {a}, 0)).translate(({vx}, {vy - a}, {vz})).rotate(({vx - ax}, {vy - ay}, {vz - az}), ({vx + ax}, {vy + ay}, {vz + az}), {angle})\n"

				else:
					a = np.linalg.norm(self.parameters['v2'])
					b = math.fabs(self.parameters['rm'])
					vx, vy, vz = self.parameters['v1']
					ax, ay, az = np.cross([0, 1, 0], self.parameters['v2'])
					angle = np.arccos(self.parameters['v2'][1] / np.linalg.norm(self.parameters['v2'])) * 180 / math.pi

					cadquery += f"surface_{self.number} = cq.Workplane().ellipseArc({b}, {a}, -90, 90).close().revolve(axisStart=(0, -{a}, 0), axisEnd=(0, {a}, 0)).translate(({vx}, {vy - a}, {vz})).rotate(({vx - ax}, {vy - ay}, {vz - az}), ({vx + ax}, {vy + ay}, {vz + az}), {angle})\n"

			case "wed":
				vx, vy, vz = self.parameters['v']
				v1x, v1y, v1z = self.parameters['v1']
				v2x, v2y, v2z = self.parameters['v2']
				v3x, v3y, v3z = self.parameters['v3']

				cadquery += f"surface_{self.number} = cq.Workplane().polyline([({v1x}, {v1y}, {v1z}), (0, 0, 0), ({v2x}, {v2y}, {v2z})]).close().polyline([({v1x + v3x}, {v1y + v3y}, {v1z + v3z}), ({v3x}, {v3y}, {v3z}), ({v2x + v3x}, {v2y + v3y}, {v2z + v3z})]).close().loft().translate(({vx}, {vy}, {vz}))\n"

			case "arb":
				pass


		return cadquery


class SphereOrigin(Surface):
	"""
	'SphereOrigin' represents origin-centered sphere INP surface cards.

	Methods:
		__init__: Initializes 'SphereOrigin'.
		set_parameters: Sets origin-centered sphere parameters.
	"""


	def __init__(self):
		"""
		'__init__' initializes 'SphereOrigin'.
		"""

		self.radius: float = None

		super().__init__()


	def set_parameters(self, radius = None):
		"""
		'set_parameters' sets origin-centered sphere parameters.

		Parameters:
			radius: origin-centered sphere radius.
		"""

		if radius is not None:
			if not is_real(radius): raise INPValueError
			value = float(radius)
			self.radius = value
			self.parameters['r'] = value
		else:
			self.radius = None
