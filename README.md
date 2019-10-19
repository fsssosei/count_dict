# count_dict

[![Build Status](https://scrutinizer-ci.com/g/fsssosei/count_dict/badges/build.png?b=master)](https://scrutinizer-ci.com/g/fsssosei/count_dict/build-status/master)
[![Code Intelligence Status](https://scrutinizer-ci.com/g/fsssosei/count_dict/badges/code-intelligence.svg?b=master)](https://scrutinizer-ci.com/code-intelligence)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/fsssosei/count_dict.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/fsssosei/count_dict/context:python)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/bf34f8d12be84b4492a5a3709df0aae5)](https://www.codacy.com/manual/fsssosei/count_dict?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=fsssosei/count_dict&amp;utm_campaign=Badge_Grade)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/fsssosei/count_dict/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/fsssosei/count_dict/?branch=master)

*This is a Python package for count dictionaries.*

*Welcome to complete the documentation.*

## Installation

Installation can be done through pip. You must have python version >= 3.6.

	pip install count-dict

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


	>>> accumulated = defaultdict(count_dict(10))
	>>> accumulated['x']['y'] += 9
	>>> {'x': dict(accumulated['x'])}
	{'x': {'y': 19}}
