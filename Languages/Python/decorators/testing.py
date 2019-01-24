import random
from decorator_utilities import utility_decorator
import time


@utility_decorator
def do_math(x):
	time.sleep(1.25)
	print(random.randint(1000,1000000)//random.randint(1000,100000))
	print(x*random.randint(10000,10000000))
	return "done"
	
if __name__ == '__main__':
	g = do_math
	print(g)
	print(g(11))