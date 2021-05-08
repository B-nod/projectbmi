from django.shortcuts import render, reverse, Http404, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from home.models import BmiMeasurement
from home.forms import BmiForm
from django.core.mail import send_mail
from django.template.loader import render_to_string

# Create your views here.

def bmi(request):
    return render(request, "base.html")


def bmiuserlist(request):
    userlist = BmiMeasurement.objects.all()
    context = {"userlist": userlist}
    return render(request, "bmiuserlist.html", context)

def bmiform(request):
     context = {}
     if request.POST:
        name = request.POST.get("name")
        weight = float(request.POST.get("weight"))
        height = float(request.POST.get("height"))

        bmi = (weight/(height**2))

        form = BmiForm(request.POST or None)
        if form.is_valid():
            # form.save()
            BmiMeasurement.objects.create(name=name, height=height, weight=weight, bmi=bmi)

   
        if bmi < 18:
            message = "Underweight. Eat a variety of foods that give you the nutrition that your body needs."
        elif bmi > 18 and bmi < 24.9:
            message = "Congratulation! Your weight is normal.Keep it up."
        elif bmi > 25 and bmi < 29.9:
            message = "Overweight. Avoid junk food and do exercise regularly."
        elif bmi > 30:
            message = "Obese. Consult with doctor, avoid junk food and increase physical activities."

        context = {'bmi':bmi}
        context["message"] = message 
   
     return render(request, "form.html", context)


def bmi_edit(request, id):
    # try:
    #     bmis = BmiMeasurement.objects.get(id=id)
    # except BmiMeasurement.DoesNotExist:
    #     raise Http404("No object found.")
    bmi = get_object_or_404(BmiMeasurement, id=id)
    form = BmiForm(request.POST or None, instance=bmi)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("home:bmiuserlist"))
    context = {"bmi": bmi}
    return render(request, "form.html", context)
    return HttpResponse(id)

def bmi_delete(request, id):
    bmi = get_object_or_404(BmiMeasurement, id=id)
    bmi.delete()
    return HttpResponseRedirect(reverse("home:bmiuserlist"))

def send_confirm_email(request):
    subject = "Test Subject"
    message = "Test Message"
    from_email = "herotamang245@gmail.com"
    recipient_list = [
                    "binodtamang245@gmail.com",
    ]
    context = {"name":"binod"}
    html_message = render_to_string("test.html", context)
    res = send_mail(subject, message, from_email, recipient_list, html_message=html_message)
    return HttpResponse(res)
