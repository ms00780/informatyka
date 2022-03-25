import random

# funckja mająca na celu wylosowanie liczb


def randomize(n, m):  # n jest ilością liczb, m jest przedzialem
    liczby = []  # utworzenie pustej tablicy
    while len(liczby) < n:
        # dodanie losowej liczby w danym przedziale
        liczby.append(random.randint(1, m))
        # sprawdzanie czy ostatnia dodana liczba jest tylko raz -> indeks -1 przenosi do ostatniego elementu tablicy
        if (liczby.count(liczby[-1]) == 1):
            continue
        else:
            liczby.pop()  # jesli liczba sie powtarza, usuniecie ostatniego elementu
            continue
    return(liczby)
