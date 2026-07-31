from django.shortcuts import render
from .models import Trenery, Schedule, Contact, Training, Price, Direction
import requests
import os


def contact(request):
    contacts = Contact.objects.all()
    directions = Direction.objects.all()

    if request.method == "POST":

        training = Training.objects.create(
            name=request.POST["name"],
            phone=request.POST["phone"],
            naprav=request.POST["naprav"],
            description=request.POST["description"]
        )


        with open("applications.txt", "a", encoding="utf-8") as f:
            f.write(f"Имя: {training.name}\n")
            f.write(f"Телефон: {training.phone}\n")
            f.write(f"Направление: {training.naprav}\n")
            f.write(f"Комментарий: {training.description}\n")
            f.write("-" * 40 + "\n")



        TOKEN = os.getenv("BOT_TOKEN")
        CHAT_ID = os.getenv("CHAT_ID")


        text = (
            f"🥊 Новая заявка!\n\n"
            f"👤 Имя: {training.name}\n"
            f"📞 Телефон: {training.phone}\n"
            f"🥋 Направление: {training.naprav}\n"
            f"📝 Комментарий: {training.description}"
        )


        try:
            response = requests.post(
                f"https://api.telegram.org/bot{TOKEN}/sendMessage",
                data={
                    "chat_id":CHAT_ID,
                    "text": text
                },
                timeout=10
            )

            print("Telegram response:")
            print(response.text)


        except Exception as e:
            print("Telegram error:")
            print(e)



        return render(request, "success.html")



    return render(request, "contact.html", {
        "contacts": contacts,
        "directions": directions
    })



def trenery(request):

    trenerys = Trenery.objects.all()

    return render(request, "trenery.html", {
        "trenerys": trenerys
    })



def schedule(request):

    schedules = Schedule.objects.all()

    return render(request, "schedule.html", {
        "schedules": schedules
    })



def price(request):

    prices = Price.objects.all()

    return render(request, "price.html", {
        "prices": prices
    })



def basa(request):

    return render(request, "basa.html")



def home(request):

    return render(request, "home.html")