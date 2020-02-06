'''
count_dict - This is a count the dictionary package.
Copyright (C) 2019-2020  sosei

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

from collections import defaultdict

__all__ = ['count_dict']

class count_dict(defaultdict):
    '''
        count_dict() -> new empty count dictionary
        
        count_dict(integer) -> new empty dictionary that sets the starting point of counting
        
        >>> accumulated = count_dict()
        >>> accumulated['x'] += 9
        >>> accumulated.items()
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
    '''
    version = '1.1.0'
    
    def __set_initial_value(self):
        return self.initial_value
    
    def __init__(self, initial_value:int = 0):
        if not isinstance(initial_value, (int, float)):
            raise TypeError(f"must be 'int' or 'float', not '{initial_value.__class__.__name__}'")
        self.initial_value = initial_value
        self.default_factory = self.__set_initial_value
    
    def __call__(self):
        return count_dict(self.initial_value)
