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

def view_registrations(request):
    # Fetch all registrations from the database
    registrations = CourseRegistration.objects.all()

    # Render the template with the fetched data
    return render(request, 'view_data.html', {'registrations': registrations})

#edit function
def edit_registration(request, registration_id):
    registration = get_object_or_404(CourseRegistration, id=registration_id)

    if request.method == 'POST':
        registration.name = request.POST.get('name')
        registration.email = request.POST.get('email')
        registration.phone = request.POST.get('phone')

        if 'academic_documents' in request.FILES:
            academic_documents = request.FILES['academic_documents']
            registration.academic_documents = academic_documents

        registration.save()
        return redirect('view_registrations')

    return render(request, 'edit_registration.html', {'registration': registration})

#delete function
def delete_registration(request, registration_id):
    registration = get_object_or_404(CourseRegistration, id=registration_id)

    if request.method == 'POST':
        registration.delete()
        return redirect('view_registrations')
