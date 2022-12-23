from django.shortcuts import render, redirect        
from django.contrib.auth import authenticate, login, logout                    #Django authentication libraries     
from django.contrib.auth.forms import AuthenticationForm                       #Django Form for authentication

#define a function view called login_view that takes a request from user
def login_view(request):                                
   error_message = None                                               #error_message to None                              
   form = AuthenticationForm()                                        #form object with username and password fields   


   #when user hits "login" button, then POST request is generated
   if request.method == 'POST':                          
       form =AuthenticationForm(data=request.POST)                    #read the data sent by the form via POST request

       #check if form is valid
       if form.is_valid():                                
           username=form.cleaned_data.get('username')                 #read username
           password = form.cleaned_data.get('password')               #read password

           #use Django authenticate function to validate the user
           user=authenticate(username=username, password=password)
           if user is not None:                    
               login(request, user)                
               return redirect('/list')
       else:                                              
           error_message ='ooops.. something went wrong'             # in case of errorprint error message

   #prepare data to send from view to template
   context ={                                             
       'form': form,                                                 #send the form data
       'error_message': error_message                                #and the error_message
   }
   #load the login page using "context" information
   return render(request, 'auth/login.html', context) 

#define a function view called logout_view that takes a request from user
def logout_view(request):                                  
   logout(request)                                                   #the use pre-defined Django function to logout
   return render(request, 'auth/success.html')   