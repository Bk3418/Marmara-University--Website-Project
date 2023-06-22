from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Home,About,Furnitures,Testimonial,Car,Rezervation
from .forms import CarForm,ContactForm,RezervationForm,TestimonialForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail





def index(request):
    Homes = Home.objects.all()
    return render(request, 'index.html',{'Homes': Homes})
def about(request):
    abouts = About.objects.all()
    return render(request, 'About.html',{'abouts': abouts})

def furnitures(request):
    furnituress = Furnitures.objects.all()
    return render(request, 'furnitures.html',{'furnituress': furnituress})
def testimonial(request):
    form = Testimonial.objects.filter(user=request.user)
    return render(request, 'testimonial.html',{'form': form})
def yorum(request):
   if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            form=form.save(commit=False)
            form.user=request.user
            form.save()
        return redirect('Testimonial')
   else:
        form = TestimonialForm()
        return render(request, 'yorumekle.html', {'form': form})
def aracekle(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form=form.save(commit=False)
            form.user=request.user
            form.save()
        return redirect('araclarim')
    else:
        form = CarForm()
        return render(request, 'aracekle.html', {'form': form})
def araclarim(request):
    form = Car.objects.filter(user=request.user)
    return render(request, 'araclarim.html',{'form': form})

def contact(request):
    if request.method =='POST':
            print('hello')
            form = ContactForm(request.POST)
            if form.is_valid():
                name =request.POST.get('name','')
                email = request.POST.get('email','')
                mesaj = request.POST.get('mesaj','')
                print('hello')
                send_mail(name,mesaj,email,['bugrakocaoglu1905@gmail.com'])
                messages.success(request, 'Mesajınız başarıyla gönderildi!')
                return redirect('Contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def rezervation(request):
    if request.method == 'POST':
        form = RezervationForm(request.POST)
        if form.is_valid():
            form=form.save(commit=False)
            form.user=request.user
            form.save()
        return redirect('rezervasyonlarim')
    else:
        form = RezervationForm()
        return render(request, 'rezervation.html', {'form': form})
def rezervasyonlarim(request):
    form = Rezervation.objects.filter(user=request.user)
    return render(request, 'rezervasyonlarim.html',{'form': form})
    


# Create your views here.
