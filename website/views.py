from django.shortcuts import render
from django.core.mail import send_mail #imports django email system

# Create your views here.
def home(request):
	return render(request, 'home.html', {})

def contact(request):
#{} is a context dictionary and allow to pass data from the back to the front end
	if  request.method == "POST":
		message_name = request.POST['message-name'] 
		message_email = request.POST['message-email']
		message = request.POST['message']

		#Send mail function
		send_mail(
			message_name, # subject
			message, # message
			message_email, # from email
			['eacigliutti@gmail.com'], # to email
			fail_silently=False,
			)
		return render(request, 'contact', {'message_name':message_name})    
	else:

		return render(request, 'contact', {})

