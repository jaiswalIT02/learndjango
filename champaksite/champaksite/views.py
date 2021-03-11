from django.http import HttpResponse
from django.shortcuts import render
from pappu.models import BookModel
from pappu.models import Bankaccount
from . import book



def getbook(request):
	book = BookModel.objects.get(id="2")

	print(book)
	return HttpResponse(str(book))

def getaccount(request):
	name=Bankaccount.objects.get(id="2")

	print(name)
	return HttpResponse(str(name))


def innbook(request):
	data={"bookname":"","subject":"","price":""}
	return render(request,"book.html",{'data':data})

def inbook(request):
	if(not request.POST):
		data={"bookname":"","subject":"","price":""}
		return render(request,"book.html",{'data':data})

	option=request.POST["option"]
	if option=="clear":
		data={"bookname":"","subject":"","price":""}
		return render(request,"book.html",{'data':data})
		
	bookname=request.POST["bookname"]
	subject=request.POST["subject"]
	price=request.POST["price"]
	print(bookname,subject,price)
	books=BookModel(
	bookname=bookname,
	subject=subject,
	price=price
	)
	books.save()
	data={"bookname":bookname,"subject":subject,"price":price}
	return render(request,"book.html",{'data':data})
	
def allaccounts(request):
	Name=Bankaccount.objects.all()
	for account in Name:
		print(Name)
	return HttpResponse(str(len(Name)))

def addaccount(request):
	bname="New Basic C"
	book = BookModel(
		bookname=bname, subject="C",
		price="300"
	)
	book.save()
	data={"account":""}
	return render(request,"bank.html",{"data":data})

def newaccount(request):
    
    data={}
    return render(request,"bank.html",{'data':data})



def addedaccount(request):
	#name=request.GET["name"]
	#balance=request.GET["balance"]
	account=Bankaccount.Bankaccount

	#account.save(name,balance)

	data={"account":""}
	return render(request,"bank.html",{"data":data})


def allbooks(request):
	books = BookModel.objects.all()
	for book in books:
		print(book.bookname,book.subject,book.price)
	return HttpResponse(str(len(books)))

def addbook(request):
	# Creating an entry
	bname="Basic C"
	book = BookModel(
		bookname=bname, subject="C",
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



def sumsub(request):
    if (request.GET):
        a=int(request.GET['n1'])
        b=int(request.GET['n2'])
        option=request.GET['option']
    else:
        a=0
        b=0
        option="Add"
    if option=="Add":
        result=a+b
    if option=="Sub":
        result=a-b
    result=str(result)
    
    data={"n1":a,"n2":b,"result":result}

    return render(request,'sumsub.html',{"data":data})
