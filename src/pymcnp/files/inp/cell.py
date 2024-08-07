"""
'cell' contains the class representing INP cell cards.

Classes:
	Cell: Representation of INP cell cards.
"""


from enum import StrEnum
from typing import *
import collections
import re

from . import *
from .card import Card
from .errors import *
from ..types import *
from ..parser import *


class Cell(Card):
	"""
	'Cell' represents INP cell cards.

	Fields:
		number (int): Cell card number.
		material (int): Cell material number.
		density (int): Cell density value.
		geometry (str): Cell geometry specification.
		parameters (dict[float]): Cell parameter table.

	Methods:
		__init__: Initializes 'Cell'.
		from_mcnp: Generates cell card objects from INP.
		from_arguments: Generates cell card objects from arguments.
		to_mcnp: Generates INP from cell card objects.
		to_arguments: Generates dictionaries from cell card objects.
	"""

	class CellGeometry:
		"""
		'CellGeometry'
		"""


		def __init__(self):
			"""
			'__init__'
			"""
			
			self.str: str = None
			self.rpn: tuple[str] = None


		@classmethod
		def from_mcnp(cls, source: str) -> Self:
			"""
			'from_mcnp'
			"""

			geometry = cls()

			# Processing Source
			processed_source = re.sub(r"\n     ", '', source)

			# Running Shunting-Yard Algorithm 
			ops_stack = Deque([], INPValueError(INPValueError.Codes.INVALID_CELL_GEOMETRY))
			out_stack = Deque([], INPValueError(INPValueError.Codes.INVALID_CELL_GEOMETRY))
			inp_stack = re.findall(r"#|:| : |[()]| [()]|[()] | [()] | |[+-]?\d+", processed_source)
			OPERATIONS_ORDER = {'#': 0, ' ': 1, ':': 2}

			if ''.join(inp_stack) != processed_source:
				raise INPValueError(INPValueError.Codes.INVALID_CELL_GEOMETRY)

			for token in inp_stack:
				if re.match(r"[+-]?\d+", token):
					# Processing Surface Number

					value = cast_fortran_integer(token)
					if value is None or not (value != 0 and -99_999_999 <= value <= 99_999_999): raise INPValueError(INPValueError.Codes.INVALID_CELL_GEOMETRY)

					out_stack.pushr(token)

				elif re.match(r"#", token):
					# Processing Unary Operator
					ops_stack.pushr(token)

				elif re.match(r"([(]| [(]|[(] | [(] )", token):
					# Processing Left Parenthesis
					ops_stack.pushr('(')

				elif re.match(r"([)]| [)]|[)] | [)] )", token):
					# Processing Right Parenthesis
					while ops_stack.peekr() != '(':
						out_stack.pushr(ops_stack.popr())

					ops_stack.popr()

				elif re.match(r":| : | |: | :", token):
					# Processing Binary Operator
					token = token.strip() if token != ' ' else token
					
					while ops_stack and ops_stack.peekr() not in {'(', ')'} and OPERATIONS_ORDER[ops_stack.peekr()] >= OPERATIONS_ORDER[token]:
						out_stack.pushr(ops_stack.popr())
					
					ops_stack.pushr(token)

				else:
					# Unrecognized Character
					assert False

			while ops_stack:
				out_stack.pushr(ops_stack.popr())

			geometry.rpn = tuple(out_stack.deque)
			geometry.str = source

			return geometry


		def to_mcnp(self) -> str:
			"""
			'to_mcnp'
			"""

			return self.str


	class CellParameter:
		"""
		'CellParameter'
		"""


		class CellKeyword(StrEnum):
			"""
			'CellKeyword'
			"""


			IMP = 'imp'
			VOL = 'vol'
			PWT = 'pwt'
			EXT = 'ext'
			FCL = 'fcl'
			WWN = 'wwn'
			DXC = 'dxc'
			NONU = 'nonu'
			PD = 'pd'
			TMP = 'tmp'
			U = 'u'
			TRCL = 'trcl'
			LAT = 'lat'
			FILL = 'fill'
			ELPT = 'elpt'
			COSY = 'cosy'
			BFLCL = 'bflcl'
			UNC = 'unc'


			@classmethod
			def cast_cell_keyword(cls, string: str, hook: Callable[Self, bool] = lambda _: True) -> Self:
				"""
				'cast_cell_keyword'
				"""

				string = string.lower()

				if string.startswith("*"):
					string = string[:1]

				if string.startswith(('wwn', 'dxc')):
					if len(string) < 4 and cast_fortran_integer(tokens[:3]) is None:
						return None

					string = string[:3]
				elif string.startswith(('pd')):
					if len(string) < 3 and cast_fortran_integer(tokens[:2]) is None:
						return None

					string = string[:2]

				try:
					keyword = cls(string)

					if hook(keyword):
						return keyword
				except:
					pass

				return None


			def to_mcnp(self) -> str:
				"""
				'to_mcnp'
				"""

				return self.value


		def __init__(self):
			"""
			'__init__'
			"""

			self.keyword: CellKeyword = None
			self.designator: Designator = None
			self.value: any = None


		@classmethod
		def from_mcnp(cls, string: str):
			"""
			'from_mcnp'
			"""

			parameter = cls()

			tokens = Parser(string, r":|=", INPSyntaxError(INPSyntaxError.Codes.INCOMPLETE_CELL_PARAMETER))

			# Processing Keyword
			value = cls.CellKeyword.cast_cell_keyword(tokens.peekl())
			if value is None: raise INPValueError(INPValueError.Codes.INVALID_CELL_PARAMETER_KEYWORD)
			parameter.set_keyword(value)

			# Processing Value & Designator
			match parameter.keyword:
				case 'imp':
					parameter.__class__ = Cell.Importance

					# Processing Keyword
					tokens.popl()

					# Processing Value
					value = cast_fortran_integer(tokens.popr())
					parameter.set_value(value)

					# Processing Designator
					designator = Designator.cast_mcnp_designator(tokens.popr())
					parameter.set_designator(designator)

				case 'vol':
					parameter.__class__ = Cell.Volume

					# Processing Keyword
					tokens.popl()

					# Processing Value
					value = cast_fortran_real(tokens.popr())
					parameter.set_value(value)

				case 'pwt':
					parameter.__class__ = Cell.ProtonWeight

					# Processing Keyword
					tokens.popl()

					# Processing Value
					value = cast_fortran_real(tokens.popr())
					parameter.set_value(value)

				case 'ext':
					parameter.__class__ = Cell.ExponentialTransform

					# Processing Keyword
					tokens.popl()

					# Processing Value
					value = cast_fortran_integer(tokens.popr())
					parameter.set_value(value)

					# Processing Designator
					designator = Designator.cast_mcnp_designator(tokens.popr())
					parameter.set_designator(designator)

				case 'fcl':
					parameter.__class__ = Cell.ForcedCollision

					# Processing Keyword
					tokens.popl()

					# Processing Value
					value = cast_fortran_integer(tokens.popr())
					parameter.set_value(value)

					# Processing Designator
					designator = Designator.cast_mcnp_designator(tokens.popr())
					parameter.set_designator(designator)

				case 'wwn':
					parameter.__class__ = Cell.WeightWindowBounds

					# Processing Suffix/Keyword
					suffix = cast_fortran_integer(tokens.popl())[3:]
					parameter.set_suffix(suffix)

					# Processing Value
					value = cast_fortran_integer(tokens.popr())
					parameter.set_value(value)

					# Processing Designator
					designator = Designator.cast_mcnp_designator(tokens.popr())
					parameter.set_designator(designator)

				case 'dxc':
					parameter.__class__ = Cell.DxtranContribution

					# Processing Suffix/Keyword
					suffix = cast_fortran_integer(tokens.popl())[3:]
					parameter.set_suffix(suffix)

					# Processing Value
					value = cast_fortran_integer(tokens.popr())
					parameter.set_value(value)

					# Processing Designator
					designator = Designator.cast_mcnp_designator(tokens.popr())
					parameter.set_designator(designator)

				case 'nonu':
					parameter.__class__ = Cell.FissionTurnOff

					# Processing Keyword
					tokens.popl()

					# Processing Value
					value = cast_fortran_integer(tokens.popr())
					parameter.set_value(value)

				case 'pd':
					parameter.__class__ = Cell.DetectorContribution

					# Processing Keyword
					tokens.popl()

					# Processing Suffix/Keyword
					suffix = cast_fortran_integer(tokens.popl())[2:]
					parameter.set_suffix(suffix)

					# Processing Value
					value = cast_fortran_integer(tokens.popr())
					parameter.set_value(value)

				case 'tmp':
					parameter.__class__ = Cell.GasThermalTemperature

					# Processing Keyword
					tokens.popl()

					# Processing Suffix/Keyword
					suffix = cast_fortran_integer(tokens.popl())[2:]
					parameter.set_suffix(suffix)

					# Processing Value
					value = cast_fortran_real(tokens.popr())
					parameter.set_value(value)

				case 'u':
					parameter.__class__ = Cell.Universe

					# Processing Keyword
					tokens.popl()

					# Processing Value
					value = cast_fortran_integer(tokens.popr())
					parameter.set_value(value)

				case 'trcl':
					parameter.__class__ = Cell.CoordinateTransformation

					# Processing Keyword
					tokens.popl()

					# Processing Value
					value = cast_fortran_integer(tokens.popr())
					parameter.set_value(value)

				case 'lat':
					parameter.__class__ = Cell.Lattice

					# Processing Keyword
					tokens.popl()

					# Processing Value
					value = cast_fortran_integer(tokens.popr())
					parameter.set_value(value)				
				case 'fill':
					parameter.__class__ = Cell.Fill

					# Processing Keyword
					tokens.popl()

					# Processing Value
					value = cast_fortran_integer(tokens.popr())
					parameter.set_value(value)

					# Processing Designator
					designator = Designator.cast_mcnp_designator(tokens.popr())
					parameter.set_designator(designator)

				case 'elpt':
					parameter.__class__ = Cell.EnergyCutoff

					# Processing Keyword
					tokens.popl()

					# Processing Value
					value = cast_fortran_real(tokens.popr())
					parameter.set_value(value)

					# Processing Designator
					designator = Designator.cast_mcnp_designator(tokens.popr())
					parameter.set_designator(designator)

				case 'cosy':
					parameter.__class__ = Cell.Cosy

					# Processing Keyword
					tokens.popl()

					# Processing Value
					value = cast_fortran_integer(tokens.popr())
					parameter.set_value(value)

				case 'bflcl':
					parameter.__class__ = Cell.Bfield

					# Processing Keyword
					tokens.popl()

					# Processing Value
					value = cast_fortran_integer(tokens.popr())
					parameter.set_value(value)

				case 'unc':
					parameter.__class__ = Cell.UncolidedSecondaries

					# Processing Keyword
					tokens.popl()

					# Processing Value
					value = cast_fortran_integer(tokens.popr())
					parameter.set_value(value)

					# Processing Designator
					designator = Designator.cast_mcnp_designator(tokens.popr())
					parameter.set_designator(designator)

			# Checking for Remaining Tokens
			if tokens: raise INPSyntaxError(INPSyntaxError.Codes.EXCESSIVE_CELL_PARAMTER)

			return parameter


		def set_keyword(self, keyword: CellKeyword) -> None:
			"""
			'set_keyword'
			"""

			if keyword is None:
				INPValueError(INPValueError.Codes.INVALID_CELL_PARAMETER_KEYWORD)

			self.keyword = keyword


		def set_designator(self, designator: Designator) -> None:
			"""
			'set_designator'
			"""

			if designator is None or self.keyword not in {'n', 'q', 'p', 'e', 'f', '|', '!', 'u', '<', 'v', '>', 'h', 'g', 'l', 'b', '+', '_', '-', '~', 'x', 'c', 'y', 'w', 'o', '@', '/', '*', 'z', 'k', '?', '%', '^', 'd', 't', 's', 'a', '#'}:
				INPValueError(INPValueError.Codes.INVALID_CELL_PARAMETER_DESIGNATOR)


		def to_mcnp(self) -> str:
			"""
			'to_mcnp'
			"""

			# Processing Suffix
			suffix_str = self.suffix if hasattr(self, 'suffix') and self.suffix is not None else ''

			# Processing Designator
			designator_str = f":{','.join(self.designator)}" if hasattr(self, 'designator') and self.designator is not None else ''

			return f"{self.keyword}{suffix_str}{designator_str}={self.value}"


		def to_arguments(self) -> dict:
			"""
			'to_arguments'
			"""

			return {'keyword': self.keyword.to_mcnp(), 'suffix': self.suffix if hasattr(self.__class__, 'suffix') else None, 'designator': self.designator if hasattr(self.__class__, 'designator') else None, 'value': self.value}




	class Importance(CellParameter):
		"""
		'Importance' represents INP cell card particle importance parameters.

		Methods:
			__init__: Initalizes 'Importance'
			set_value: Sets INP cell card particle importance parameter values.
		"""


		def __init__ ():
			"""
			'__init__' initalizes 'Importance'
			"""

			super().__init__()

			self.importance: any = None
			self.designator: tuple[Designator] = None


		def set_value(self, value: any) -> None:
			"""
			'set_value' sets INP cell card particle importance parameter values.

			Parameters:
				importance (any): Cell particle importance.
			"""

			if value is not None and (value >= 0):
				self.importance = value
				self.value = value


		def set_designator(self, designator: tuple[Designator]) -> None:
			"""
			'set_designator' sets INP cell card particle importance parameter designator.	

			Parameters:
				designator (Designator): INP cell card parameter designator.
			"""		
			if designator is not None:
				self.designator = designator


	class Volume(CellParameter):
		"""
		'Volume' represents INP cell card volume parameters.

		Methods:
			__init__: Initalizes 'Volume'
			set_value: Sets INP cell card volume parameter values.
		"""


		def __init__ ():
			"""
			'__init__' initalizes 'Volume'
			"""

			super().__init__()

			self.volume: any = None


		def set_value(self, value: any) -> None:
			"""
			'set_value' sets INP cell card volume parameter values.

			Parameters:
				volume (any): Cell volume.
			"""

			if value is not None or not (value > 0):
				self.volume = value
				self.value = value


	class ProtonWeight(CellParameter):
		"""
		'ProtonWeight' represents INP cell card proton weight parameters.

		Methods:
			__init__: Initalizes 'ProtonWeight'
			set_value: Sets INP cell card proton weight parameter values.
		"""


		def __init__ ():
			"""
			'__init__' initalizes 'ProtonWeight'
			"""

			super().__init__()

			self.weight: any = None


		def set_value(self, value: any) -> None:
			"""
			'set_value' sets INP cell card proton weight parameter values.

			Parameters:
				weight (any): Cell collision-generated proton number/weight.
			"""

			if value is not None:
				self.weight = value
				self.value = value


	class ExponentialTransform(CellParameter):
		"""
		'ExponentialTransform' represents INP cell card exponential transformation parameters.

		Methods:
			__init__: Initalizes 'ExponentialTransform'
			set_value: Sets INP cell card exponential transformation parameter values.
		"""


		def __init__ ():
			"""
			'__init__' initalizes 'ExponentialTransform'
			"""

			super().__init__()

			self.stretch: any = None
			self.designator: Designator = None


		def set_value(self, value: any) -> None:
			"""
			'set_value' sets INP cell card exponential transformation parameter values.

			Parameters:
				stretch (any): Cell stretch specifier.
			"""

			if value is not None:
				self.stretch = value
				self.value = value


		def set_designator(self, designator: Designator) -> None:
			"""
			'set_designator' sets INP cell card exponential transformation parameter designator.		
			Parameters:
				designator (Designator): INP cell card parameter designator.
			"""		
			if designator is not None:
				self.designator = designator


	class ForcedCollision(CellParameter):
		"""
		'ForcedCollision' represents INP cell card forced-collision parameters.

		Methods:
			__init__: Initalizes 'ForcedCollision'
			set_value: Sets INP cell card forced-collision parameter values.
		"""


		def __init__ ():
			"""
			'__init__' initalizes 'ForcedCollision'
			"""

			super().__init__()

			self.control: any = None
			self.designator: Designator = None


		def set_value(self, value: any) -> None:
			"""
			'set_value' sets INP cell card forced-collision parameter values.

			Parameters:
				control (any): Cell forced-collision.
			"""

			if value is not None and (-1 <= value <= 1):
				self.control = value
				self.value = value


		def set_designator(self, designator: Designator) -> None:
			"""
			'set_designator' sets INP cell card forced-collision parameter designator.		
			Parameters:
				designator (Designator): INP cell card parameter designator.
			"""		
			if designator is not None:
				self.designator = designator


	class WeightWindowBounds(CellParameter):
		"""
		'WeightWindowBounds' represents INP cell card space-, time-, and energy-dependent weight window bound parameters.

		Methods:
			__init__: Initalizes 'WeightWindowBounds'
			set_value: Sets INP cell card space-, time-, and energy-dependent weight window bound parameter values.
		"""


		def __init__ ():
			"""
			'__init__' initalizes 'WeightWindowBounds'
			"""

			super().__init__()

			self.weight: any = None
			self.designator: Designator = None
			self.suffix: int = None


		def set_value(self, value: any) -> None:
			"""
			'set_value' sets INP cell card space-, time-, and energy-dependent weight window bound parameter values.

			Parameters:
				weight (any): Cell weight window bounds.
			"""

			if value is not None and (value == -1 or value >= 0):
				self.weight = value
				self.value = value


		def set_designator(self, designator: Designator) -> None:
			"""
			'set_designator' sets INP cell card space-, time-, and energy-dependent weight window bound parameter designator.		
			Parameters:
				designator (Designator): INP cell card parameter designator.
			"""		
			if designator is not None:
				self.designator = designator


		def set_suffix(self, suffix: int) -> None:
			"""
			'set_suffix' sets INP cell card space-, time-, and energy-dependent weight window bound parameter keyword suffix.		
			Parameters:
				suffix (int): INP cell card keyword suffix.
			"""		
			if suffix is not None:
				self.suffix = suffix


	class DxtranContribution(CellParameter):
		"""
		'DxtranContribution' represents INP cell card DXTRAN sphere contribution parameters.

		Methods:
			__init__: Initalizes 'DxtranContribution'
			set_value: Sets INP cell card DXTRAN sphere contribution parameter values.
		"""


		def __init__ ():
			"""
			'__init__' initalizes 'DxtranContribution'
			"""

			super().__init__()

			self.probability: any = None
			self.designator: Designator = None
			self.suffix: int = None


		def set_value(self, value: any) -> None:
			"""
			'set_value' sets INP cell card DXTRAN sphere contribution parameter values.

			Parameters:
				probability (any): Cell DXTRAN sphere contribution probability.
			"""

			if value is not None and (0 <= value <= 1):
				self.probability = value
				self.value = value


		def set_designator(self, designator: Designator) -> None:
			"""
			'set_designator' sets INP cell card DXTRAN sphere contribution parameter designator.		
			Parameters:
				designator (Designator): INP cell card parameter designator.
			"""		
			if designator is not None:
				self.designator = designator


		def set_suffix(self, suffix: int) -> None:
			"""
			'set_suffix' sets INP cell card DXTRAN sphere contribution parameter keyword suffix.		
			Parameters:
				suffix (int): INP cell card keyword suffix.
			"""		
			if suffix is not None:
				self.suffix = suffix


	class FissionTurnOff(CellParameter):
		"""
		'FissionTurnOff' represents INP cell card fission on/off parameters.

		Methods:
			__init__: Initalizes 'FissionTurnOff'
			set_value: Sets INP cell card fission on/off parameter values.
		"""


		def __init__ ():
			"""
			'__init__' initalizes 'FissionTurnOff'
			"""

			super().__init__()

			self.setting: any = None


		def set_value(self, value: any) -> None:
			"""
			'set_value' sets INP cell card fission on/off parameter values.

			Parameters:
				setting (any): Cell fission on/off setting.
			"""

			if value is not None and (value in {0, 1, 2}):
				self.setting = value
				self.value = value


	class DetectorContribution(CellParameter):
		"""
		'DetectorContribution' represents INP cell card point detector contribution parameters.

		Methods:
			__init__: Initalizes 'DetectorContribution'
			set_value: Sets INP cell card point detector contribution parameter values.
		"""


		def __init__ ():
			"""
			'__init__' initalizes 'DetectorContribution'
			"""

			super().__init__()

			self.probability: any = None
			self.suffix: int = None


		def set_value(self, value: any) -> None:
			"""
			'set_value' sets INP cell card point detector contribution parameter values.

			Parameters:
				probability (any): Cell point detector contribution probability.
			"""

			if value is not None and (0 <= value <= 1):
				self.probability = value
				self.value = value


		def set_suffix(self, suffix: int) -> None:
			"""
			'set_suffix' sets INP cell card point detector contribution parameter keyword suffix.		
			Parameters:
				suffix (int): INP cell card keyword suffix.
			"""		
			if suffix is not None:
				self.suffix = suffix


	class GasThermalTemperature(CellParameter):
		"""
		'GasThermalTemperature' represents INP cell card time-dependent thermal temperature parameters.

		Methods:
			__init__: Initalizes 'GasThermalTemperature'
			set_value: Sets INP cell card time-dependent thermal temperature parameter values.
		"""


		def __init__ ():
			"""
			'__init__' initalizes 'GasThermalTemperature'
			"""

			super().__init__()

			self.temperature: any = None
			self.suffix: int = None


		def set_value(self, value: any) -> None:
			"""
			'set_value' sets INP cell card time-dependent thermal temperature parameter values.

			Parameters:
				temperature (any): Cell temperature.
			"""

			if value is not None and (value >= 0):
				self.temperature = value
				self.value = value


		def set_suffix(self, suffix: int) -> None:
			"""
			'set_suffix' sets INP cell card time-dependent thermal temperature parameter keyword suffix.		
			Parameters:
				suffix (int): INP cell card keyword suffix.
			"""		
			if suffix is not None:
				self.suffix = suffix


	class Universe(CellParameter):
		"""
		'Universe' represents INP cell card universe parameters.

		Methods:
			__init__: Initalizes 'Universe'
			set_value: Sets INP cell card universe parameter values.
		"""


		def __init__ ():
			"""
			'__init__' initalizes 'Universe'
			"""

			super().__init__()

			self.number: any = None


		def set_value(self, value: any) -> None:
			"""
			'set_value' sets INP cell card universe parameter values.

			Parameters:
				number (any): Cell universe number.
			"""

			if value is not None and (0 <= value <= 99_999_999):
				self.number = value
				self.value = value


	class CoordinateTransformation(CellParameter):
		"""
		'CoordinateTransformation' represents INP cell card transformation parameters.

		Methods:
			__init__: Initalizes 'CoordinateTransformation'
			set_value: Sets INP cell card transformation parameter values.
		"""


		def __init__ ():
			"""
			'__init__' initalizes 'CoordinateTransformation'
			"""

			super().__init__()

			self.number: any = None


		def set_value(self, value: any) -> None:
			"""
			'set_value' sets INP cell card transformation parameter values.

			Parameters:
				number (any): Cell transformation number.
			"""

			if value is not None:
				self.number = value
				self.value = value


	class Lattice(CellParameter):
		"""
		'Lattice' represents INP cell card lattice shape parameters.

		Methods:
			__init__: Initalizes 'Lattice'
			set_value: Sets INP cell card lattice shape parameter values.
		"""


		def __init__ ():
			"""
			'__init__' initalizes 'Lattice'
			"""

			super().__init__()

			self.shape: any = None


		def set_value(self, value: any) -> None:
			"""
			'set_value' sets INP cell card lattice shape parameter values.

			Parameters:
				shape (any): Cell shape setting.
			"""

			if value is not None and (value in {1, 2}):
				self.shape = value
				self.value = value


	class Fill(CellParameter):
		"""
		'Fill' represents INP cell card filling universe parameters.

		Methods:
			__init__: Initalizes 'Fill'
			set_value: Sets INP cell card filling universe parameter values.
		"""


		def __init__ ():
			"""
			'__init__' initalizes 'Fill'
			"""

			super().__init__()

			self.number: any = None
			self.designator: Designator = None


		def set_value(self, value: any) -> None:
			"""
			'set_value' sets INP cell card filling universe parameter values.

			Parameters:
				number (any): Cell filling universe number.
			"""

			if value is not None and (0 <= number <= 99_999_999):
				self.number = value
				self.value = value


		def set_designator(self, designator: Designator) -> None:
			"""
			'set_designator' sets INP cell card filling universe parameter designator.		
			Parameters:
				designator (Designator): INP cell card parameter designator.
			"""		
			if designator is not None:
				self.designator = designator


	class EnergyCutoff(CellParameter):
		"""
		'EnergyCutoff' represents INP cell card lower energy cutoff parameters.

		Methods:
			__init__: Initalizes 'EnergyCutoff'
			set_value: Sets INP cell card lower energy cutoff parameter values.
		"""


		def __init__ ():
			"""
			'__init__' initalizes 'EnergyCutoff'
			"""

			super().__init__()

			self.cutoff: any = None
			self.designator: Designator = None


		def set_value(self, value: any) -> None:
			"""
			'set_value' sets INP cell card lower energy cutoff parameter values.

			Parameters:
				cutoff (any): Cell energy cutoff.
			"""

			if value is not None:
				self.cutoff = value
				self.value = value


		def set_designator(self, designator: Designator) -> None:
			"""
			'set_designator' sets INP cell card lower energy cutoff parameter designator.		
			Parameters:
				designator (Designator): INP cell card parameter designator.
			"""		
			if designator is not None:
				self.designator = designator


	class Cosy(CellParameter):
		"""
		'Cosy' represents INP cell card cosy map parameters.

		Methods:
			__init__: Initalizes 'Cosy'
			set_value: Sets INP cell card cosy map parameter values.
		"""


		def __init__ ():
			"""
			'__init__' initalizes 'Cosy'
			"""

			super().__init__()

			self.number: any = None


		def set_value(self, value: any) -> None:
			"""
			'set_value' sets INP cell card cosy map parameter values.

			Parameters:
				number (any): Cell cosy map number.
			"""

			if value is not None and (value >= 0):
				self.number = value
				self.value = value


	class Bfield(CellParameter):
		"""
		'Bfield' represents INP cell card magnetic/B field parameters.

		Methods:
			__init__: Initalizes 'Bfield'
			set_value: Sets INP cell card magnetic/B field parameter values.
		"""


		def __init__ ():
			"""
			'__init__' initalizes 'Bfield'
			"""

			super().__init__()

			self.number: any = None


		def set_value(self, value: any) -> None:
			"""
			'set_value' sets INP cell card magnetic/B field parameter values.

			Parameters:
				number (any): Cell magnetic field number.
			"""

			if value is not None and (value >= 0):
				self.number = value
				self.value = value


	class UncolidedSecondaries(CellParameter):
		"""
		'UncolidedSecondaries' represents INP cell card uncollided particle secondaries behavior parameters.

		Methods:
			__init__: Initalizes 'UncolidedSecondaries'
			set_value: Sets INP cell card uncollided particle secondaries behavior parameter values.
		"""


		def __init__ ():
			"""
			'__init__' initalizes 'UncolidedSecondaries'
			"""

			super().__init__()

			self.setting: any = None
			self.designator: Designator = None


		def set_value(self, value: any) -> None:
			"""
			'set_value' sets INP cell card uncollided particle secondaries behavior parameter values.

			Parameters:
				setting (any): Cell uncollided secondaries setting.
			"""

			if value is not None and (value in {0, 1}):
				self.setting = value
				self.value = value


		def set_designator(self, designator: Designator) -> None:
			"""
			'set_designator' sets INP cell card uncollided particle secondaries behavior parameter designator.		
			Parameters:
				designator (Designator): INP cell card parameter designator.
			"""		
			if designator is not None:
				self.designator = designator


	def __init__(self):
		"""
		'__init__' initializes 'Cell'.
		"""

		super().__init__()

		self.number: int = None
		self.mateiral: int = None
		self.density: float = None
		self.geometry: str = None
		self.parameters: tuple[CellParameter] = None


	def set_number(self, number: int) -> None:
		"""
		'set_number'
		"""

		if number is None or not (1 <= number <= 99_999_999): 
			raise INPValueError(INPValueError.Codes.INVALID_CELL_NUMBER)
		
		self.number = number
		self.id = number


	def set_material(self, material: int) -> None:
		"""
		'set_material'
		"""

		if material is None or not (0 <= material <= 99_999_999): 
			raise INPValueError(INPValueError.Codes.INVALID_CELL_MATERIAL)
		
		self.material = material


	def set_density(self, density: float) -> None:
		"""
		'set_density'
		"""

		if density is None or density == 0:
			raise INPValueError(INPValueError.Codes.INVALID_CELL_DENSITY)

		self.density = density


	def set_geometry(self, geometry: CellGeometry) -> None:
		"""
		'set_geometry'
		"""

		if geometry is None:
			raise INPValueError(INPValueERROR.Codes.INVALID_CELL_GEOMETRY)

		self.geometry = geometry


	def set_parameters(self, parameters: tuple[CellParameter]) -> None:
		"""
		'set_parameters'
		"""

		params = []

		for parameter in parameters:
			if parameter is None:
				raise INPValueError(INPValueERROR.Codes.INVALID_CELL_PARAMETER)

			params.append(parameter)

		self.parameters = tuple(params)


	@classmethod
	def from_mcnp(cls, card: str) -> Self:
		"""
		'from_mcnp' generates cell card objects from INP.

		Parameters:
			card (str): INP to parse.

		Returns:
			cell (Cell): Cell card object.
		"""

		cell = cls()
		### MUST GET PREPROCESSED STRING '  ' -> ' ' and strip.
		tokens = Parser(card, ' ', INPEOFError)

		# Processing Card Number	
		value = cast_fortran_integer(tokens.popl())
		cell.set_number(value)

		# Processing Material Number
		value = cast_fortran_integer(tokens.popl())
		cell.set_material(value)

		# Processing Material Density
		if cell.material != 0:
			value = cast_fortran_real(tokens.popl())
			cell.set_density(value)

		# Processing Parameters
		parameters = []

		entries = re.split(r":|=", tokens.peekr())
		value = cls.CellParameter.CellKeyword.cast_cell_keyword(entries[0])

		while value is not None:
			parameter = cls.CellParameter().from_mcnp(tokens.popr())
			parameters.append(parameter)

			entries = re.split(r":|=", tokens.peekr())
			value = cls.CellParameter.CellKeyword.cast_cell_keyword(entries[0])

		cell.set_parameters(tuple(parameters))

		# Processing Geometry
		cell.geometry = cls.CellGeometry().from_mcnp(' '.join(tokens.deque))
		
		return cell


	@classmethod
	def from_arguments(cls, number: int, material: int, geometry: CellGeometry, parameters: tuple[CellParameter] = tuple(), density: int = None) -> Self:
		"""
		'from_arguments' generates cell card objects from arguments.

		Parameters:
			number (int): Cell card number.
			material (int): Cell card material.
			density (int): Cell card density.
			geometry (str): Cell card geometry.
			parameters (dict[tuple[str, any]]): Cell card parameter table.

		Returns:
			cell (Cell): Call card object.
		"""

		cell = cls()

		cell.set_number(number)
		cell.set_material(material)
		cell.set_density(density)
		cell.set_geometry(geometry)
		cell.set_parameters(parameters)

		return cell


	def to_mcnp(self) -> str:
		"""
		'to_mcnp' generates INP from cell card objects.

		Returns:
			source (str): INP for cell card object.
		"""

		# Formatting Density
		density_str = f" {self.density}" if self.material else ''

		# Formatting Geometry
		geometry_str = self.geometry.to_mcnp()

		# Formatting Parameters
		parameters_str = ' '.join(param.to_mcnp() for param in self.parameters)
		
		return add_continuation_lines(f"{self.number} {self.material}{density_str} {geometry_str} {parameters_str}")


	def to_arguments(self) -> dict:
		"""
		'to_arguments' generates dictionary from cell card objects.

		Returns:
			arguments (dict): Dictionary for cell card object.
		"""

		return {'j': self.number, 'm': self.material, 'd': self.density, 'geom': self.geometry.to_mcnp(), 'params': [param.to_arguments() for param in self.parameters]}

