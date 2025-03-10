from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .forms import RegisterForm,CustomLoginForm
from django.contrib.auth import login
from LifeLinkApp.models import Donor, Recipient, Client, OrganDonor, OrganRecipient


def index(request):
    return render(request, 'index.html')

def login_page(request):
    if request.method == 'POST':
        form = CustomLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('homepage')  # Redirect to the home page after successful login
    else:
        form = CustomLoginForm()

    return render(request, 'login.html',{'form':form})


def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful! Please log in.")
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'signup.html', {'form': form})


def contact_us(request):
    if request.method == 'POST':
        client_name = request.POST.get('client_name')
        client_email = request.POST.get('client_email')
        client_message = request.POST.get('client_message')

        client = Client(
            client_name = client_name,
            client_email = client_email,
            client_message = client_message,

        )
        client.save()
    return render(request,'index.html')

def view_clients(request):
    clients = Client.objects.all()
    return render(request,'view_clients.html',{'clients':clients})

@login_required(login_url='login')
def blood_donation(request):
    return render(request, 'blood_donation.html')


def donor_details(request):
    if request.method == 'POST':
        donor_name = request.POST['donor_name']
        donor_bloodGroup = request.POST['donor_bloodGroup']
        donor_contact= request.POST['donor_contact']
        donor_address=request.POST['donor_address']

        donor=Donor(
            donor_name=donor_name,
            donor_bloodGroup=donor_bloodGroup,
            donor_contact=donor_contact,
            donor_address=donor_address,


        )
        donor.save()


    return render(request,'donor_details.html')

def view_donors(request):
    donors=Donor.objects.all()
    return render(request,'view_donors.html',{'donors':donors})


def recipient_details(request):
    if request.method == 'POST':
        recipient_name = request.POST['recipient_name']
        recipient_bloodGroup = request.POST['recipient_bloodGroup']
        recipient_contact= request.POST['recipient_contact']
        recipient_address=request.POST['recipient_address']
        recipient_message=request.POST['recipient_message']


        recipient = Recipient(
            recipient_name=recipient_name,
            recipient_bloodGroup=recipient_bloodGroup,
            recipient_contact=recipient_contact,
            recipient_address=recipient_address,
            recipient_message=recipient_message,

        )
        recipient.save()


    return render(request,'recipient_details.html')

def view_recipients(request):
    recipients = Recipient.objects.all()
    return render(request,'view_recipients.html',{'recipients':recipients})

def organ_transplant(request):
    return render(request,'organ_transplant.html')

def organ_donors_details(request):
    if request.method =='POST':
        donor_name = request.POST['donor_name']
        donor_organType = request.POST['donor_organType']
        donor_contact = request.POST['donor_contact']
        donor_address = request.POST['donor_address']

        donor = OrganDonor(
            donor_name=donor_name,
            donor_organType=donor_organType,
            donor_contact=donor_contact,
            donor_address=donor_address,

        )
        donor.save()
    return render(request,'organ_donor_details.html')



def view_organ_donors(request):
    donors = OrganDonor.objects.all()
    return render(request,'view_organ_donors.html',{'donors':donors})


def organ_recipient_details(request):
    if request.method =='POST':
        recipient_name = request.POST['recipient_name']
        recipient_organType = request.POST['recipient_organType']
        recipient_contact = request.POST['recipient_contact']
        recipient_address = request.POST['recipient_address']
        recipient_message = request.POST['recipient_message']

        recipient = OrganRecipient(
            recipient_name=recipient_name,
            recipient_organType=recipient_organType,
            recipient_contact=recipient_contact,
            recipient_address=recipient_address,
            recipient_message = recipient_message

        )
        recipient.save()
    return render(request,'organ_recipient_details.html')


def view_organ_recipients(request):
    recipients =OrganRecipient.objects.all()
    return render('view_organ_recipients.html',{'recipients':recipients})




# Create your views here.
