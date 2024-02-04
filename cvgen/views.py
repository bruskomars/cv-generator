from django.shortcuts import render, redirect
from .models import Profile

# Create your views here.
def home(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        summary = request.POST.get('summary')

        university1 = request.POST.get('university1')
        university_qualification1 = request.POST.get('university_qualification1')
        university_address1 = request.POST.get('university_address1')
        university_date1 = request.POST.get('university_date1')

        university2 = request.POST.get('university2')
        university_qualification2 = request.POST.get('university_qualification2')
        university_address2 = request.POST.get('university_address2')
        university_date2 = request.POST.get('university_date2')

        previous_work1 = request.POST.get('previous_work1')
        previous_work1_pos = request.POST.get('previous_work1_pos')
        previous_work1_loc = request.POST.get('previous_work1_loc')
        previous_work1_date = request.POST.get('previous_work1_date')
        previous_work1_role = request.POST.get('previous_work1_role')

        previous_work2 = request.POST.get('previous_work2')
        previous_work2_pos = request.POST.get('previous_work2_pos')
        previous_work2_loc = request.POST.get('previous_work2_loc')
        previous_work2_date = request.POST.get('previous_work2_date')
        previous_work2_role = request.POST.get('previous_work2_role')

        skill1 = request.POST.get('skill1')
        skill2 = request.POST.get('skill2')
        skill3 = request.POST.get('skill3')
        skill4 = request.POST.get('skill4')

        project1 = request.POST.get('project1')
        project1_desc = request.POST.get('project1_desc')
        project2 = request.POST.get('project2')
        project2_desc = request.POST.get('project2_desc')

        interests = request.POST.get('interests')

        profile = Profile(
            first_name=fname,
            last_name=lname,
            email=email,
            phone=phone,
            summary=summary,
            university1=university1,
            university_qualification1=university_qualification1,
            university_address1=university_address1,
            university_date1=university_date1,
            university2=university2,
            university_qualification2=university_qualification2,
            university_address2=university_address2,
            university_date2=university_date2,

            previous_work1=previous_work1,
            previous_work1_pos=previous_work1_pos,
            previous_work1_loc=previous_work1_loc,
            previous_work1_date=previous_work1_date,
            previous_work1_role=previous_work1_role,
            previous_work2=previous_work2,
            previous_work2_pos=previous_work2_pos,
            previous_work2_loc=previous_work2_loc,
            previous_work2_date=previous_work2_date,
            previous_work2_role=previous_work2_role,

            skill1=skill1,
            skill2=skill2,
            skill3=skill3,
            skill4=skill4,

            project1=project1,
            project1_desc=project1_desc,
            project2=project2,
            project2_desc=project2_desc,

            interests=interests,

        )

        profile.save()
        context = {'profile': profile}

        return render(request, 'cvgen/cv.html', context)

    return render(request, 'cvgen/home.html')

def cv_generator(request):
    return render(request, 'cvgen/cv.html')
