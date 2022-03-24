import csv

def csv_create():
    with open('lottery.csv', 'w') as wyniki:
        category = ['data_godzina_systemowa',
                    'rodzaj_gry', 
                    'wylosowane_liczby']
        writer = csv.DictWriter(wyniki, fieldnames=category, delimiter='|')

        writer.writeheader()

