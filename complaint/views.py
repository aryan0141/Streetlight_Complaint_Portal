from django.http import HttpResponse
from django.shortcuts import render, redirect
from csv import*
#from django.contrib.auth.decorators import login_required
from prettytable import PrettyTable
import datetime
from django.core.mail import send_mail

#import matplotlib
#import pandas as pd

def index(request):
	#return HttpResponse("First app")
	return render(request,'index.html')
def form(request):
	
	return render(request,'form.html')

def submits(request):
	lenght=0
	fname=request.POST.get('fname','default')
	lname=request.POST.get('lname','default')
	email=request.POST.get('email','default')
	plotno=request.POST.get('plotno','default')
	city=request.POST.get('city','default')
	state=request.POST.get('state','default')
	pincode=request.POST.get('pincode','default')
	streetlightcode=request.POST.get('streetlightcode','default')
	problem=request.POST.get('problem','default')
	
	with open('data2.csv', 'r') as read_obj:
		csv_reader = reader(read_obj)
		for row in csv_reader:
			lenght+=1
	
	citizen_data = [lenght,fname, lname,email,plotno,city,state,pincode,streetlightcode,problem,datetime.datetime.now()]
	
	with open('data.csv', 'a', newline='') as write_obj:
		csv_writer = writer(write_obj)
		csv_writer.writerow(citizen_data)
	with open('data2.csv', 'a', newline='') as write_obj:
		csv_writer = writer(write_obj)
		csv_writer.writerow(citizen_data)

	#Subject of the mail...
	sub="Vivid Lightnings"
	
	#Body of the mail...
	if problem=="Any Other":
		body= f"Dear {fname},\nYour complaint of Street Light(No.{streetlightcode}) is being registered with us.\nYour problem will solved in next 48 hours.Your complaing Id is XH56{lenght}.\n\nThanks for choosing us..."
	else:
		body= f"Dear {fname},\nYour complaint of Street Light(No.{streetlightcode}) is being registered with us.\nYour problem will solved in next 48 hours.Your complaing Id is XH56{lenght}.\nProblem- Street Light {problem}\n\nThanks for choosing us..."
	#send_mail(sub,body,'Your email address',[email],fail_silently=False)
	
	return render(request,'submission.html')
	
def login(request):
	if request.method == "POST":
		return render(request, 'admins.html')
	return render(request,'login.html')

def admins(request):
	value=request.POST.get('value','default')
	submit=request.POST.get('submit','default')
	print('button:',submit)
	print('text:',value)

	if value!='default':
		input2=open('data2.csv', 'r')
		input = open('data.csv', 'r')
		output = open('data.csv','a',newline='')
		write = writer(output)
		i=0
		for row in reader(input):
			try:
				if row[0]!=value:
					
					if i==0:
						x = open('data.csv', 'w')
						y = writer(x)
						
						x.close()
						i=1
					write.writerow(row)
			except:
				pass
		for row in reader(input2):
			try:
				if row[0]==value:
					
					sub='Vivid Lightnings'
					body=f"Dear {row[1]},\nYour complaint of street light(No.{row[8]}) has been resolved by our technicians.\nThanks for choosing us..."			
					#send_mail(sub,body,'Your email address',[row[3]],fail_silently=False)
					
					
			except:
				pass
		input2.close()
		input.close()
		output.close()
				


	x=PrettyTable(['Id','Fname','Lname','Email','Plot No.','City','State','Pincode','SL No.','Problem','Date/Time'])
	y=PrettyTable(['Id','Fname','Lname','Email','Plot No.','City','State','Pincode','SL No.','Problem','Date/Time'])
	with open('data.csv', 'r') as read_obj:
		csv_reader = reader(read_obj)
		for row in csv_reader:
			
			try:
				x.add_row(row)
			except:
				pass
	html_code=x.get_html_string()
	html_file=open('complaint/static/complaint/data.html', 'w')
	html_file=html_file.write(html_code)
	
	with open('data2.csv', 'r') as read_obj:
		csv_reader = reader(read_obj)
		for row in csv_reader:
			
			try:
				y.add_row(row)
			except:
				pass
	html_code1=y.get_html_string()
	html_file1=open('complaint/static/complaint/data2.html', 'w')
	html_file1=html_file1.write(html_code1)
	
	return render(request,'admins.html')
	# return redirect(request, 'admins.html')
	

def about(request):
	return render(request,'about.html')












