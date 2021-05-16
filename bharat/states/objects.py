# bharat\states\objects.py

import datetime


class Date(datetime.date):
	"""
	Overrides datetime.date object's __repr__ method

	Only purpose is the nice representation of a date
	"""

	def __new__(self, date_str):
		# The date is stored as YYYY-MM-DD in the JSON file
		return datetime.date.__new__(self, *map(int, date_str.split('-')))

	def __repr__(self) -> str:
		return self.strftime('%d-%m-%Y')


class State:
	"""
	State class:
	================
	A state has the following attributes:
		- abbr				: State code (string)
		- code				: GST code (integer)
		- capital			: Capital(s) [comma separated if multiple]
		- iso31662in			: ISO31662IN code (string)
		- is_UT				: True if the state is a union territory else False
		- name				: Name of state
		- post_zone			: Postal zone (integer)
		- statehood_date		: Date of statehood (date object)
		- website			: State's website
		- zone				: Geographical zone (string)
	"""

	abbr: str
	capital: str
	code: int
	iso31662in: str
	is_UT: bool
	name: str
	post_zone: int
	statehood_date: Date
	website: str
	zone: str

	def __init__(self, **kwargs):
		self.__dict__.update(kwargs)

	def __repr__(self) -> str:
		if self.is_UT:
			return f"<Union Territory:{self.name}>"
		else:
			return f"<State:{self.name}>"

	def __str__(self) -> str:
		return self.name
