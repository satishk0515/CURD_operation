from django.shortcuts import render,redirect,HttpResponseRedirect
from .forms import studentregistration
from .models import user

# Create your views here.


def add_show(request):
    form= studentregistration()
    if request.method =='POST':
        form= studentregistration(request.POST)
        if form.is_valid():
            nm=form.cleaned_data['Name']
            em=form.cleaned_data['Email']
            pw=form.cleaned_data['Password']
            reg=user(Name=nm, Email=em, Password=pw)
            reg.save()
        form= studentregistration()

    else:
        form=studentregistration()
    stud =user.objects.all()
            # return redirect('added')

    return render( request , 'app/addandshow.html',{'form':form, 'stu':stud})




def update_data(request, id):
    if request.method =='POST':
        pi = user.objects.get(pk=id)
        form = studentregistration(request.POST, instance=pi)
        if form.is_valid():
            form.save()
    else:
        pi = user.objects.get(pk=id)
        form = studentregistration(instance=pi)
    return render(request, 'app/updatestudent.html',{'form':form})




def delete_data(request,id):
    if request.method =='POST':
        pi =user.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
