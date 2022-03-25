import csv
from time import localtime, strftime

# funkcja przeznaczona do zamieszcania danych w pliku csv


def csv_writing(game, liczby):
    # zmienna ktorej nadajemy wartosc czasu w momencie uruchomienia funkcji csv_writing
    data = strftime("%d/%m/%Y %H:%M", localtime())
    with open('lottery.csv', 'a') as wyniki:
        category = ['data_godzina_systemowa',
                    'rodzaj_gry',
                    'wylosowane_liczby']
        writer = csv.DictWriter(wyniki, fieldnames=category, delimiter='|')

        writer.writerow({'data_godzina_systemowa': data,
                        'rodzaj_gry': game,
                         'wylosowane_liczby': liczby})
