from django.http import HttpResponse
from django.shortcuts import render
from pappu.models import BookModel
from . import book

def getbook(request):
	book = BookModel.objects.get(id="2")

	print(book)
	return HttpResponse(str(book))

def allbooks(request):
	books = BookModel.objects.all()
	for book in books:
		print(book)
	return HttpResponse(str(len(books)))
def addbook(request):
	# Creating an entry

	book = BookModel(
		bookname="Basic C", subject="C",
		price="300"
	)
	book.save()
	return HttpResponse("Inserted")


def mybook(request):
	b=book.Book("Basic C",150)
	data={"book":b}
	return render(request, "book.html", {'data': data})

def index(request):
	#b=book.Book()
	b=book.Book("",123)
	html = "<h1>The default view</h1>" + str(b)
	return HttpResponse(html)
def simpleurl(request):
    return HttpResponse("A very simple url ")
def logincheck(request):
	username=request.POST['username']
	password=request.POST['password']
	if username=="pappu" and password=="pass":
		request.session["username"]=username
		return protected(request)
	else:
		message="Invalid username or password"
	data ={'username' : username,'password':password,'message':message }
	return render(request,"dologin.html",{'data':data})

def dologin(request):
	data ={'username' : "",'password':"",'message':"Please Login" }
	return render(request,"dologin.html",{'data':data})
	
def protected(request):
	if request.session["username"]:
		message="welcome " + request.session["username"]
	else:
		message="Please login and come"
	data ={'message' : message }
	return render(request,"protected.html",{'data':data})
	
def showdata(request):
		try:
			l=[1,2,3,4]
			data={"data":l}
			return render(request,"datatemplate.html",{'data':data})
		except:
			l=[1,2,3,4]
			data={"data":l}
			return render(request,"datatemplate.html",{'data':data})

def suburl(request):
		try:
			print(request.POST.__contains__("n1"))
			print(request.POST.__contains__("n"))
			n1=request.POST["n1"]
			n2=request.POST.__getitem__("n2")
			sum=int(n1) - int(n2)
			data ={'sum' : sum,'n1':n1,'n2':n2 }
			return render(request,"subtemplate.html",{'data':data})
		except:
			data ={'sum' : 0,'n1':0,'n2':0 }
			return render(request,"subtemplate.html",{'data':data})
def multiply(request):
	try:
		n1=request.POST["n1"]
		n2=request.POST.__getitem__("n2")
		multiply=int(n1)*int(n2)
		data={'multiply':multiply,'n1':n1,'n2':n2}
		return render(request,"multiply.html",{'data':data})
	except:
		data ={'multiply' : 0,'n1':0,'n2':0 }
		return render(request,"multiply.html",{'data':data})


	return render(request,"multiply.html",{})
	
def setsession(request):
	request.session["name"]="popat"
	return HttpResponse("Session set");

def getsession(request):
	if request.session.get("name"):
		value=request.session.get("name")
		request.session.clear()
		return HttpResponse(value);
	return HttpResponse("Not found");


def calculator(request):
	return HttpResponse("Calculator");
def templateview(request):
	try:
		n1=request.POST["n1"]
		n2=request.POST.__getitem__("n2")
		sum=int(n1) + int(n2)
		data ={'sum' : sum,'n1':n1,'n2':n2 }
		return render(request,"addtemplate.html",{'data':data})
	except:
		data ={'sum' : 0,'n1':0,'n2':0 }
		return render(request,"addtemplate.html",{'data':data})


def testview(request):
	try:
		
		data ={'name' : "Champak",'address':"Pandepur"}
		return render(request,"test.html",{'data':data})
	except:
		data ={'name' : "Error"}
		return render(request,"test.html",{'data':data})
