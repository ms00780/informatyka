import randomize
import csv_writing

# funkcja odpowiedzialna za przetworzenie danych uzytkownika i wylosowanie liczb


def play(a):
    if(a == "1" or a == "lotto"):  # a jest zmienną wpisaną przez uzytkownika
        game = "Lotto"
        # wykorzystanie funkcji do wylosowania liczb
        wynik = randomize.randomize(6, 49)
        # wykorzystanie funkcji csv_writing w celu zanotowania danych w pliku csv
        csv_writing.csv_writing(game, wynik)
        print(game, wynik)  # ukazanie wyniku uzytkownikowi

    elif(a == "2" or a == "multi multi" or a == "multimulti"):  # analogicznie  to, co jest wyzej
        game = "Multi Multi"
        wynik = randomize.randomize(20, 80)
        csv_writing.csv_writing(game, wynik)
        print(game, wynik)

    elif(a == "3" or a == "eurojackpot" or a == "euro jackpot"):
        game = "Euro Jackpot"
        wynik = [randomize.randomize(5, 50), randomize.randomize(2, 12)]
        csv_writing.csv_writing(game, wynik)
        print(game, wynik)

    elif(a == "i" or a == "info"):
        with open('legenda.txt') as legenda:  # otworzenie pliku tekstowego z legendą
            opis_gry = legenda.read()
            print(opis_gry)

    else:  # przypadek, gdy uzytkownik wpisze cokolwiek innego
        game = "error"
        wynik = ""
        print("Źle uzupełnione dane, prosimy spróbować ponownie")
