import imp
from re import template
from urllib import response
from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader
from .forms import EmailInputForm
from .forms import UploadEmailAddressForm
# from . import verify_email_sockets
from .finalVer_check_email import CheckEmail
# import finalVer_check_email

# Create your views here.
def index(request):
    # template = loader.get_template('index.html')
    context = {}
    context['form'] = EmailInputForm()
    context['multipleEmailForm'] = UploadEmailAddressForm()


    if request.method == 'POST':
        # Runs when the form is submitted
        form = EmailInputForm(request.POST)

        email = form['email_address'].value()
        # print(email.as_text)
        print(f'\nThe Email address is {email}')

        verifyObj = CheckEmail()
        isExist = verifyObj.verify_email(email)

        context['results'] = f'{email} {isExist}'

        #return HttpResponse('Result page')
        return render(request, 'index.html', context)

    else:
        # context['form'] = GeeksForm()
        context['results'] = 'Result of Email Verification'

    return render(request, 'index.html', context)

