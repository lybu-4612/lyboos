from email.message import EmailMessage
from django.shortcuts import redirect, render
from .forms import RegistrationForm
from .models import Account
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required 
from django.http import HttpResponse

#verification email
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding  import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage



'''def userauth(uemail, upassword):
    k= Account.objects.filter(email=uemail).count()
    if k:
        print('user')
        q=  Account.objects.all()
        print(q)
        if q.password == upassword:
            print('admin')
            return True
        
    else:
        return False'''
    
def register(request):
    
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phonenumber = form.cleaned_data['phonenumber']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split("@")[0]
            user = Account.objects.create_user(username=username, first_name=first_name, last_name=last_name,  email=email, password=password)
            user.phonenumber = phonenumber
            user.save()
            
            #useractivation
            
            current_site = get_current_site(request)
            mail_subject = 'Please Activate Your Account.'
            message = render_to_string('accounts/account_verification_email.html', {
                'user' : user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
                
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to =[to_email])
            send_email.send()
            
            messages.success(request, 'Registration successful.')
            return redirect('/accounts/login/?command-verification&email='+email)
    else:
        form = RegistrationForm
    context = {
        'form': form,
    }
    
    return render(request, 'accounts/register.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        email = request.POST['email']   
        password = request.POST['password']
        
        user = auth.authenticate( email =email,password =password,  )
        print(user)
        print(user.username)
        if user is not None :
            auth.login(request, user)
            messages.success(request, 'You Are Now logged in. ')
            return redirect('home')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')
    return render(request, 'accounts/login.html')
            
@login_required(login_url='login')
def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        messages.success(request, 'You are now logged out.')
        return redirect('login')
    else:
        return redirect('login')

def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk = uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None
        
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Your account has been successfully activated.')
        return redirect('login')
    else:
        messages.error(request, 'The activation link is invalid.')
        return redirect('register')

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def forgotPassword(request):
    if request.method == 'POST':
        email = request.POST['email']
        if Account.objects.filter(email=email).exists():
            user = Account.objects.get(email__exact=email)
            
            #Reset password
            current_site = get_current_site(request)
            mail_subject = 'Reset Your Password.'
            message = render_to_string('accounts/reset_ password_email.html', {
                'user' : user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
                
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to =[to_email])
            send_email.send()
            
            messages.success(request, 'Password reset link has been sent to your email.')
            return redirect('login')
            
        
        else:
            messages.error(request, 'Email does not exist.')
            return redirect('forgotPassword')
    return render(request, 'accounts/forgotPassword.html')

def resetpassword_validate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk = uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None
    
    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.success(request,'please reset your password')
        return redirect('resetPassword')
    else:
        messages.error(request,'This link has been expired.')
        return redirect('login')
    
def resetPassword(request):
    
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password == confirm_password:
            uid = request.session.get('uid')
            user = Account.objects.get(pk=uid)
            user.set_password(password) 
            user.save()
            messages.success(request, 'Password  reset successful.') 
            return redirect('login')
    
        else:
            messages.error(request, 'Password does not match.')
            return redirect('resetPassword')
    else:
        return render(request, 'accounts/resetPassword.html')

        


        


    

