class Book:
	def __init__(self,bookname,price):
		self.bookname=bookname
		self.price=price
	def __str__(self):
		return "Name={0}, Price={1}".format(self.bookname,self.price)