class client:
	def __init__(self,last_name,first_name,license_nb,birth_date,email):
		self._last_name = last_name
		self._first_name = first_name
		self._license_nb = license_nb
		self._birth_date = birth_date
		self._email = email
	
	def __str__(self):
		pass
	
	@property
	def last_name(self):
		return self._last_name
	
	@property
	def first_name(self):
		return self._first_name
	
	@property
	def license_nb(self):
		return self._license_nb
	
	@property
	def birth_date(self):
		return self._birth_date
	
	@property
	def email(self):
		return self._email
	
	@last_name.setter
	def last_name(self,value):
		if type(value)==str and len(value)>0:
			self._last_name = value
	
	@first_name.setter
	def first_name(self,value):
		if type(value)==str and len(value)>0:
			self._first_name = value
	
	@license_nb.setter
	def license_nb(self,value):
		if type(value)==str and len(value)>0:
			self._license_nb = value
	
	@birth_date.setter
	def birth_date(self,value):
		if type(value)==str and len(value)>0:
			self._birth_date = value
	
	@email.setter
	def email(self,value):
		if type(value)==str and len(value)>0:
			self._email = value