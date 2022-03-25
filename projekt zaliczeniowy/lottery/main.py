import randomize
import csv_writing
import csv_create
import game

# utworzenie pustego pliku csv przy pomocy funkcji z pliku csv_create.py
csv_create.csv_create()

print(
    "\n Totolotek \n\nProszę wybrać jedną z opcji \nAby zobaczyć legendę, wpisz: [i/info] \nAby wyjść, wpisz: [n/end]")

a = "start"  # utworzenie zmiennej a. W tym miejscu z niej nie korzystamy, ale potrzebna jest do uruchomienia pętli while

while a != "end":
    a = input(
        "\n  1.   Lotto \n  2.   Multi Multi \n  3.   Euro Jackpot\n\nWybieram: ")
    a = a.lower()  # zamiana zmiennej wpisanej przez uzytkownika na male litery/cyfry
    if(a == "n" or a == "nie" or a == "no" or a == "end"):
        break

    # zatwierdzenie kontynuacji
    yn = input("Czy na pewno chcesz kontynuować? \n(T/N) ")
    yn = yn.lower()  # zmiana zmiennej wpisanej na male litery

    if(yn == "n" or yn == "nie" or yn == "no" or yn == "end"):
        break  # wyjscie z petli w przypadku checi zakonczenia programu przez uzytkowmnika

    game.play(a)  # wywolanie funkcji play
    yn = input("\n Powrócić do menu? \n(T/N) ")
    yn = yn.lower()
    if(yn == "n" or yn == "nie" or yn == "no" or yn == "end"):
        break  # wyjscie z petli w przypadku checi zakonczenia programu przez uzytkowmnika

print("\nDziękujemy za grę i zapraszamy do ponownego udziału!\n")
