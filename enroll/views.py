from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration   #modelform
from .models import User  #modelclass

# Create your views here.

#This function adds new item and shows all items...
def add_show(request):
    if request.method =='POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email= em, password= pw)
            reg.save()
            fm = StudentRegistration()  #for rendering blank form 

            
    else:
        fm = StudentRegistration()
        
    stud = User.objects.all()  #for showing data into dom

    return render(request, 'enroll/addandshow.html', {'form':fm, 'stu':stud})



#This function updates data ...
def update_data(request, id):
    # serving for POST request...
    if request.method == 'POST':
        up_data = User.objects.get(pk=id)  #getting data from dom form...
        fm = StudentRegistration(request.POST, instance=up_data)
        if fm.is_valid():
            fm.save()
    else:
        #serving for GET request...
        up_data = User.objects.get(pk=id)
        fm = StudentRegistration(instance=up_data)
    return render(request, 'enroll/updatestudent.html', {'form': fm})


# This function deletes the data form DB...
def delete_data(request, id):
    if request.method == 'POST':
        #for deleting all data use-->  User.objects.all()
        del_data = User.objects.get(pk=id)
        del_data.delete()
        return HttpResponseRedirect('/')