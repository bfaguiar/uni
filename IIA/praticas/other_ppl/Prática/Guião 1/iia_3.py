
class Sum:
	def __init__(self, f1, f2):
		self.f1=f1
		self.f2=f2

	def __str__(self):
		return "Sum of "+str(self.f1)+" and "+str(self.f2)

	def eval(self, x=1):
		return self.f1.eval(x)+self.f2.eval(x)

	def simplificar(self):
		s1 = self.f1.simplificar()
		s2 = self.f2.simplificar()
		if isinstance(s1,Const) and isinstance(s2, Const):
			return Const(s1.val+s2.val)
		if isinstance(s1,Const) and s1.val==0:
			return s2.simplificar()
		if isinstance(s2,Const) and s2.val==0:
			return s1.simplificar()
		return Sum(s1, s2)

	def derivative(self):
		s1 = self.f1.simplificar()
		s2 = self.f2.simplificar()

		if isinstance(s1,Var) and isinstance(s2,Var):
			return Const(s1.val+s2.val)
		if isinstance(s1,Var):
			return Const(s1.val)
		if isinstance(s2,Var):
			return Const(s2.val)

		return Sum(s1.derivative(),s2.derivative())


class Var:
	def __init__(self, val=1):
		self.val=val
	
	def __str__(self):
		return "Var with value "+str(self.val)

	def eval(self, x=1):
		return self.val*x

	def simplificar(self):
		return self

	def derivative(self):
		return Const(self.val)


class Product:
	def __init__(self, f1, f2):
		self.f1=f1
		self.f2=f2
	
	def __str__(self):
		return "Product of "+str(self.f1)+" and "+str(self.f2)

	def eval(self, x=1):
		return self.f1.eval(x)*self.f2.eval(x)

	def simplificar(self):
		s1 = self.f1.simplificar()
		s2 = self.f2.simplificar()
		if isinstance(s1,Const) and isinstance(s2, Const):
			return Const(s1.val*s2.val)
		if isinstance(s1,Const) and s1.val==0:
			return Const(0)
		if isinstance(s2,Const) and s2.val==0:
			return Const(0)
		if isinstance(s1,Const) and s1.val==1:
			return s2 
		if isinstance(s2,Const) and s2.val==1:
			return s1
		return Product(s1, s2)

	def derivative(self):
		s1 = self.f1.simplificar()
		s2 = self.f2.simplificar()

		if isinstance(s1,Var) and isinstance(s2,Var):
			return Var(s1.val*s2.val*2)
		if isinstance(s1,Var) or isinstance(s2,Var):
			return Product(s1.eval(),s2.eval())

		return Const(0)


class Const:
	def __init__(self, val):
		self.val=val
	
	def __str__(self):
		return "Constant with value "+str(self.val)

	def eval(self,x=1):
		return self.val

	def simplificar(self):
		return self
	def derivative(self):
		return Const(0)

print(Sum(Product(Const(2),Const(1)),Var(1)))
print(Sum(Product(Const(2),Const(1)),Var(1)).eval())
print(Sum(Product(Const(2),Const(1)),Var(1)).simplificar())
print(Product(Product(Const(4),Const(1)),Var(3)).eval(2))
print(Product(Product(Const(4),Const(1)),Var(3)).derivative())
print(Product(Var(2),Var(3)).derivative())
print(Sum(Var(2),Const(1)).derivative())


print(Const(73).derivative())
print(Const(73).eval(5))

print(Var(1).eval(5))
print(Var(3).derivative())

print(Sum(Const(3),Product(Const(4),Const(7))))
print(Sum(Const(3),Product(Const(4),Const(7))).derivative())

print(Sum(Product(Const(2),Var(1)),Const(1)).derivative())
print(Sum(Const(2),Product(Var(1),Sum(Var(1),Const(1)))).derivative())