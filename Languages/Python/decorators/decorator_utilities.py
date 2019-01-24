#importing all dependencies
from multiprocessing import pool
import time
import logging

class utility_decorator(object):
	"""A class that logs multiple metrics and
	enables multiprocessing of a function"""
	
	def __init__(self, og_function):
		"""Assigns passed function to class variable og_function"""
		self.og_function = og_function
		
	def make_log(self, *args, **kwargs):
		"""Logs basic information about passed function such as; time to execute, name, arguments, datetime executed etc"""
		logging.basicConfig(filename= "{}.log".format(self.og_function.__name__), level=logging.INFO)
		
		#timing
		t1 =time.time()
		self.og_function(*args, **kwargs)
		t2 = time.time() - t1
		
		
		logging.info("Ran {} with Arguments: {} \n and keyword Arguments {} \nIt took {} to complete.".format(self.og_function.__name__, args, kwargs,t2))
		
	def __call__(self, *args, **kwargs):
		self.make_log(*args,**kwargs)
		print("log created, it can be found at {}.log".format(self.og_function.__name__))
	
	def __repr__(self):
		"""Sets printable name of instances to
		funtion_name-utility-decorated"""
		return "{}-utility-decorated".format(self.og_function.__name__)
		