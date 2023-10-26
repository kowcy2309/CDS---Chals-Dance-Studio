from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from datetime import datetime
from django.shortcuts import render, get_object_or_404
from .models import Student
from django.shortcuts import redirect


def admission(request):
    return render(request, 'danceapp/admission.html')

def admin1 (request):
    return render(request, 'danceapp/admin.html')

def aboutus (request):
    return render(request, 'danceapp/aboutus.html')

def profile (request):
    return render(request, 'danceapp/profile.html')

def gallery (request):
    return render(request, 'danceapp/gallery.html')

def sp(request):
    return render(request, 'danceapp/sp.html')

def insertuser(request):
    if request.method == 'POST':
        vuusername = request.POST.get('tusername')
        vuparentsname = request.POST.get('tparentsname')
        vuage = request.POST.get('tage')
        vuemail = request.POST.get('temail')
        vuaddress = request.POST.get('taddress')
        vupincode = request.POST.get('tpincode')
        vucontactnumber = request.POST.get('tcontactnumber')
        vunationality = request.POST.get('tnationality')
        vudate = request.POST.get('tdate')  # Get date as a string

        if not vucontactnumber:
            return HttpResponse("Contact Number is required. Please fill in the field.")

       

        user = Student(
            uusername=vuusername,
            uparentsname=vuparentsname,
            uage=vuage,
            uemail=vuemail,
            uaddress=vuaddress,
            upincode=vupincode,
            ucontactnumber=vucontactnumber,
            unationality=vunationality,
            udate=vudate,
        )

        user.save()

        

    return render(request, 'danceapp/admission.html')

# ...

def edit_user(request, user_id):
    user_profile = get_object_or_404(Student, pk=user_id)

    if request.method == 'POST':
        user_profile.uusername = request.POST['uusername']
        user_profile.uparentsname = request.POST['uparentsname']
        user_profile.uage = request.POST['uage']
        user_profile.uemail = request.POST['uemail']
        user_profile.uaddress = request.POST['uaddress']
        user_profile.upincode = request.POST['upincode']
        user_profile.ucontactnumber = request.POST['ucontactnumber']
        user_profile.unationality = request.POST['unationality']
        user_profile.udate = request.POST['udate']  # Get date as a string

       

        user_profile.save()

        return redirect('emt')

    return render(request, 'danceapp/update_user.html', {'user_profile': user_profile})








def emt(request):
    key=Student.objects.all()
    return render(request,'danceapp/emt.html',{'data':key})

def get_secret_credentials(request):
    secret_username = "Soosai09"
    secret_password = "Soosai@1"
    

    return JsonResponse({
        'secret_username': secret_username,
        'secret_password': secret_password
    })

# ...

def edit_user(request, user_id):
    user_profile = get_object_or_404(Student, pk=user_id)

    if request.method == 'POST':
        user_profile.uusername = request.POST['uusername']
        user_profile.uparentsname = request.POST['uparentsname']
        user_profile.uage = request.POST['uage']
        user_profile.uemail = request.POST['uemail']
        user_profile.uaddress = request.POST['uaddress']
        user_profile.upincode = request.POST['upincode']
        user_profile.ucontactnumber = request.POST['ucontactnumber']
        user_profile.unationality = request.POST['unationality']
        user_profile.udate = request.POST['udate']  # Get date as a string


        user_profile.save()

        return redirect('emt')

    return render(request, 'danceapp/update_user.html', {'user_profile': user_profile})


def delete_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)

    if request.method == 'POST':
        if request.POST.get('confirm_delete'):
            student.delete()
            return redirect('emt')  

    return render(request, 'danceapp/delete_student.html', {'student': student})


def logout_view(request):
    return render(request, 'danceapp/admin.html')