import random
import time
import sys

def main():
    while True:
        choice = input("\nWybierz co chcesz zrobic:\n\n1 - Powitanie.\n2 - Wyjdź\n3 - Minigra.\n4 - Kalkulator napiwku.\n5 - Kalkulator BMI\n6 - Sprawdź ile weekendów mogło Ci zostać w zyciu :(\n7 - Biletomat rollercoaster\n\nJeśli zauwazysz jakieś bugi, daj mi znać.\nBędę próbował to naprawić.\n\nWybór: ")
        if choice == "1":
            name = input("Podaj swoje imię: ")
            print(f"\nWitam Cię {name} w moim kodzie.\n")
            time.sleep(2)
        elif choice == "2":
            break
        elif choice =="3":
            minigra()
        elif choice =="4":
            kalkulatornapiwku()
        elif choice =="5":
            kalkulatorbmi()
        elif choice =="6":
            weekend()
        elif choice =="7":
            rollercoaster()
        
        else:
            print("NIE MA TAKIEJ OPCJI lub nie jest jeszcze napisany kod")
            time.sleep(5)
        
def minigra():
    number = random.randint(0,100)
    counter = 1
    try:
        numuser = int(input("\nWitaj w minigrze!\nZnajdź liczbę od 0 do 100.\nMasz 10 prób. Powodzenia!\n\nPodaj swoją liczbę: "))
    except ValueError:
        print("błąd")

    while counter != 10:
            if -1 < numuser < number:
                numuser = int(input(f"Za mało\nZostało Ci" + str(counter - 10) + " prób: "))
                counter += 1
            elif 101 > numuser > number:
                numuser = int(input(f"Za duzo\nZostało Ci" + str(counter - 10) + " prób: "))
                counter += 1
            elif numuser == number:
                print("!!!UDAŁO CI SIĘ!!!\n")
                time.sleep(2)
                break
            else:
                print("\nNie kombinuj.\n")
                time.sleep(2)
                break
    if counter == 10:
            print("Przegrałeś.")
            time.sleep(3)


def kalkulatornapiwku():
    bill = float(input("Witaj w kalkulatorze napiwku!\nPodaj wysokość rachunku: PLN "))
    percentage = int(input("Ile procent chcesz przeznaczyć na napiwek? "))
    people = int(input("Na ile osób ma być podzielony rachunek? "))
    sum = float((bill * percentage / 100 + bill) / people)
    print(f"\nKazdy powinien zapłacić: " + str(sum) + "zł.")
    time.sleep(5)

def kalkulatorbmi():
    print("Witam Cię! Skoro tu jesteś, chcesz sprawdzić swoje BMI.")
    height = float(input("Proszę bardzo. Podaj swój wzrost. np 1.75: "))
    time.sleep(0.3)
    weight = int(input("Teraz podaj swoją wagę: "))
    bmi = weight / height ** 2
    bmiint = int(bmi)

    time.sleep(0.3)
    print("\nTeraz mielę informacje które podałeś i kosmicznym algorytmem kalkuluję twoje BMI.\n")
    def animate_loading(duration=5):
        images = ["[    O]", "[>   O]", "[=>  O]", "[==> O]", "[8==>O]", "[==> O]", "[=>  O]", "[>   O]"]
        start_time = time.time()
        while time.time() - start_time < duration:
            for image in images:
                sys.stdout.write("\r" + "Ładowanie... " + image)
                sys.stdout.flush()
                time.sleep(0.1)

    animate_loading()
    print("\nMielenie informacji zakończone.")
    time.sleep(2)
    if bmi < 18.5:
        print("\nMasz niedowage.\n")
    elif bmi < 25:
        print("\nMasz normalną wagę.\n")
    elif bmi < 30:
        print("\nMasz lekką nadwagę.\n")
    elif bmi < 35:
        print("\nMasz nadwagę.\n")
    else:
        print("\nJesteś wykurwiście spasiony.\n")
    enter = input("Wciśnij enter by wyjść: ")
    if enter == "":
        print("Wracam...")
    else:
        print("Miałeś wcisnąć ENTER, ale niech Ci będzie ;)")
    time.sleep(3)

def weekend():
    print("Obliczymy razem na szybko ile zostało Ci weekendów w Twoim zyciu.\n")
    age = input("Wpisz swój wiek: ")
    if age.isalpha():
        print("Are you kiddin me? ;) Podaj cyfre.\n")
        time.sleep(3)
    else:
        ageint = int(age)
        if ageint <15 or ageint >100:
            print("Ni chuja nie masz tylu lat.\n")
            time.sleep(3)
        else:
            left = ageint * 90
            print(f"Zostało Ci {left} weekendów w Twoim zyciu.\n\nPrzykro mi :(")
            time.sleep(4)

def rollercoaster():
    totaltickets = 0
    while True:
        try:
            height = int(input("Musisz mieć ponad 120cm wzrostu by jechać kolejką\nPodaj swój wzrost w centymetrach: "))
        except ValueError:
            print("Błąd")
            continue
        bill = 0
        if height >= 120:
            try:
                age = int(input("Podaj swój wiek: "))
            except ValueError:
                print("Błąd")
                continue
            if age <= 12:
                print("Zapłać 12zł")
                bill = 12
            elif age < 18:
                print("Zapłać 18zł")
                bill = 18
            elif age >= 45 and age <=55:
                print("Wszystko jest ok. Mozesz jechac za darmo! :)")
            else:
                print("Zapłać 25zł")
                bill = 25

            photo = input('Czy chcesz dodatkowo zdjęcie za 3zł?\nWpisz "Y" jeśli tak, lub "N" jeśli nie: ')
            if photo == "Y":
                bill += 3
                totaltickets +=1
            else:
                totaltickets +=1
            yes = input("Czy chcesz kupić jeszcze więcej biletów? Y lub N: ")
            if yes != "Y":
                break
        else:
            print("Przykro mi, nie mozesz jechac.")
            return
    print(f"Kupiłeś łącznie {totaltickets} biletów.\nRazem do zapłaty: {bill}zł")




main()