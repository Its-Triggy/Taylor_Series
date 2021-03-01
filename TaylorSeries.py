from numpy import cos, sin, tan, exp, pi
import matplotlib.pyplot as plt

class TaylorSeries:

	def __init__(self, accuracy = 10):
		self.function = input("what is the function?  e.g. cos(x) : ")
		self.accuracy = min(accuracy, 7)
		self.domain = (-pi, pi)
		self.spacing = 0.003
	
	def getResult(self, x):
		self.coefs = self.getCoefs()
		total = 0
		for i in range(len(self.coefs)):
			total += self.coefs[i] * (x**i)
		return total
	
	def getPlotEstimate(self, n):
		self.coefs = self.getCoefs()
		
		x_lst = TaylorSeries.even_spacing(self.domain, self.spacing)
		y_lst = []
		for x in x_lst:
			y = 0
			for i in range(n):
				y += self.coefs[i] * (x**i)
			y_lst.append(y)
		return x_lst,y_lst
		
		coefs = self.getCoefs()
		total = 0
		for i in range(len(coefs)):
			total += coefs[i] * (x**i)
		return total
		
	def getCoefs(self):
		coefs = []
		x_lst, y_lst = self.getDataPoints()
		coef = y_lst[TaylorSeries.zeroArg(x_lst)]
		coefs.append(round(coef, 3))
		for i in range(2, self.accuracy):
			x_lst, y_lst = self.deriv(x_lst, y_lst)
			coef = y_lst[TaylorSeries.zeroArg(x_lst)] / TaylorSeries.factorial(i)
			coefs.append(round(coef, 3))		
		return coefs
		
	def getDataPoints(self):
		x_lst = TaylorSeries.even_spacing(self.domain, self.spacing)
		y_lst = []
		for x in x_lst: exec("y_lst.append(" + self.function + ")")
		return x_lst,y_lst
		
	def deriv(self, x_lst, y_lst): #function = "sin(x) + x^2"
		new_x_lst = x_lst[:-2]
		new_y_lst = []
		for i in range(len(x_lst)-2):
			dy = y_lst[i+1] - y_lst[i]
			dx = x_lst[i+1] - x_lst[i]
			new_y_lst.append(dy/dx)
		return new_x_lst, new_y_lst			
			
	def n_deriv(self, n):
		x_lst, y_lst = self.getDataPoints()
		for i in range(n):
			x_lst, y_lst = self.deriv(x_lst, y_lst)			
		return x_lst, y_lst			
		
	def even_spacing(domain, spacing):
		x = []
		i= domain[0]
		while i < domain[1]:
			x.append(i)
			i += spacing
		return x
		
	def zeroArg(lst): #Returns index with value closest to zero
		c_i = 9e999
		c_val = 9e999
		for i, val in enumerate(lst):
			if abs(val) < c_val:
				c_val = abs(val)
				c_i = i
		return c_i
	
	def abs(val):
		if val >= 0: return val
		else: return -val
	
	def factorial(n):
		total = 1
		for i in range(1,n):
			total *= i
		return total

ts = TaylorSeries()
coefs = ts.getCoefs()

x, y = ts.getDataPoints()

legend = [ts.function]
plt.plot(x, y)
for i in range(1,len(coefs)):
	x, y = ts.getPlotEstimate(i)
	plt.plot(x, y)
	legend.append("Estimate with " + str(i) + "coef(s)")

plt.legend(legend)
plt.show()


