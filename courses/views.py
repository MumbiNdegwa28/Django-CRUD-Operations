from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .models import CourseRegistration


# Create your views here.
def home(request):
    return render(request, 'index.html')
def courses(request):
    return render(request, 'courses.html')


def register_course(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        academic_documents = request.FILES.get('academicDocuments')

        if academic_documents is None:
            return render(request, 'register_course.html', {'error': 'Please upload a valid document.'})

        # Save the uploaded file
        fs = FileSystemStorage()
        filename = fs.save(academic_documents.name, academic_documents)

        # Save data to the database
        CourseRegistration.objects.create(
            name=name,
            email=email,
            phone=phone,
            academic_documents=filename
        )

        return render(request, 'registration_success.html')

    return render(request, 'register_course.html')