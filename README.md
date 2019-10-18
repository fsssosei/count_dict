# count_dict

*This is a Python package for count dictionaries.*

*Welcome to complete the documentation.*

## Installation

Installation can be done through pip. You must have python version >= 3.6.

	pip install count_dict

## Usage

The statement to import the package:

	from count_dict_package import count_dict

or

	from count_dict_package import *
	
Example:

	>>> accumulated = count_dict()
	>>> accumulated['x'] += 9
	dict_items([('x', 9)])


	>>> accumulated = count_dict(10)
	>>> accumulated['x'] += 9
	>>> accumulated.items()
	dict_items([('x', 19)])


	>>> accumulated = defaultdict(count_dict)
	>>> accumulated['x']['y'] += 9
	>>> {'x': dict(accumulated['x'])}
	{'x': {'y': 9}}

