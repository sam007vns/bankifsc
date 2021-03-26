from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import BankNames, Data
from django.contrib.auth.models import auth, User
from django.contrib import auth
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import random
import urllib.parse


def home(request):
	context={}
	context['Bank']=BankNames.objects.all()
	context['process1'] = True
	for x in context['Bank']:
		y=x.name.split(" ")
		y="_".join(y)
		setattr(x,"bankurl",y)
	return render(request,"home.html",context)

def select_bank(request,select_bank_):
	context={}
	context['bankurl'] = select_bank_
	select_bank_=select_bank_.replace("_"," ")
	context['bank'] = select_bank_
	try:
		state_list=Data.objects.filter(name=select_bank_)
		if len(state_list) == 0:
			messages.add_message(request,messages.WARNING,"Bank Does Not Exist")
			return redirect("home")
	except Exception:
		messages.add_message(request,messages.WARNING,"Bank Does Not Exist")
		return redirect("home")
	context['process2'] =True
	final_list=[]
	for dupli in state_list:
		count=0
		for name_s in final_list:
			count+=1
			final_count = len(final_list)
			if name_s.adr4 == dupli.adr4:
				break
			if final_count == count:
				final_list.append(dupli)
				break
		if len(final_list) == 0:
			final_list.append(dupli)
	context['state'] = final_list
	for x in context['state']:
		y=x.adr4.split(" ")
		y="_".join(y)
		setattr(x,"stateurl",y)

	return render(request,"home.html",context)
def select_state(request,select_bank_,select_state_):
	context={}
	context['process3'] = True
	context['bankurl'] = select_bank_
	context['stateurl'] = select_state_
	select_state_=select_state_.replace("_"," ")
	select_bank_ = select_bank_.replace("_"," ")
	context['state'] = select_state_
	context['bank'] = select_bank_
	try:
		city_list = Data.objects.filter(name=select_bank_,adr4=select_state_)
		if len(city_list) == 0:
			messages.add_message(request,messages.WARNING,"Bank Does Not Exist")
			return redirect("home")
	except Exception:
		messages.add_message(request,messages.WARNING,"Bank Does Not Exist")
		return redirect("home")
	final_list=[]
	for dupli in city_list:
		count=0
		for name_s in final_list:
			count+=1
			final_count = len(final_list)
			if name_s.adr3 == dupli.adr3:
				break
			if final_count == count:
				final_list.append(dupli)
				break
		if len(final_list) == 0:
			final_list.append(dupli)
	context['city'] = final_list
	for x in context['city']:
		y=x.adr3.split(" ")
		y="_".join(y)
		setattr(x,"cityurl",y)
	return render(request,"home.html",context)
def select_city(request,select_bank_,select_state_,select_city_):
	context={}
	context['process4'] = True
	context['bankurl'] = select_bank_
	context['stateurl'] = select_state_
	context['cityurl'] = select_city_
	select_bank_=select_bank_.replace("_"," ")
	select_state_ = select_state_.replace("_"," ")
	select_city_ = select_city_.replace("_"," ")
	context['state']=select_state_
	context['city'] = select_city_
	context['bank'] = select_bank_
	try:
		branch_list = Data.objects.filter(name=select_bank_,adr4=select_state_,adr3=select_city_)
		if len(branch_list) == 0:
			messages.add_message(request,messages.WARNING,"Bank Does Not Exist")
			return redirect("home")
	except Exception:
		messages.add_message(request,messages.WARNING,"Bank Does Not Exist")
		return redirect("home")
	final_list=[]
	for dupli in branch_list:
		count=0
		for name_s in final_list:
			count+=1
			final_count = len(final_list)
			if name_s.adr1 == dupli.adr1:
				break
			if final_count == count:
				final_list.append(dupli)
				break
		if len(final_list) == 0:
			final_list.append(dupli)
	context['branch'] = final_list
	for x in context['branch']:
		y=x.adr1.split(" ")
		y="_".join(y)
		setattr(x,"branchurl",y)
	return render(request,"home.html",context)
def branch(request,select_bank_,select_state_,select_city_,branch_):
	context={}
	context['process5'] = True
	context['bankurl'] = select_bank_
	context['stateurl'] = select_state_
	context['cityurl'] = select_city_
	context['branchurl'] = branch_
	select_bank_=select_bank_.replace("_"," ")
	select_state_ = select_state_.replace("_"," ")
	select_city_ = select_city_.replace("_"," ")
	branch_=branch_.replace("_"," ")
	context['city'] = select_city_
	context['bank'] = select_bank_
	context['state'] = select_state_
	context['branch'] = branch_
	try:
		context['bank_details'] = Data.objects.get(name__icontains=select_bank_,adr4__icontains=select_state_,adr3__icontains=select_city_,adr1__icontains=branch_)
	except Exception:
		try:
			context['bank_details'] = context['bank_details'] = Data.objects.get(name=select_bank_,adr4=select_state_,adr3=select_city_,adr1=branch_)
		except Exception:
			messages.add_message(request,messages.WARNING,"Bank Does Not Exist")
			return redirect("home")
	return render(request,"home.html",context)

