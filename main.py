import sys
import math
import networkx as nx
import matplotlib.pyplot as plt
from collections import Counter

# from .classic import empty_graph, path_graph, complete_graph

print("Rozpoczecie wczytywania pliku z grafem \n")

# Wczytanie grafu G z pliku input.txt
def WczytajGraf():
    # G = nx.star_graph(n)
    G = nx.Graph()
    plik = open("res/input.txt")
    for line in plik:
        x = line.split()
        G.add_edge(x[0], x[1])
    return G


# sortowanie wierzchołków metodą "najmniejszy na końcu"
def SmallestLast():
    lista_wierzcholkow_posortowana = []
    lista_prim = lista_stopni.copy()

    # wyszukanie wierzchołka o najmniejszym stopniu w grafie G
    minimum = min(G.degree(), key=lambda x: x[1])

    # włożenie wierzchołka o najmniejszym stopniu na początek listy
    element = lista_prim.pop(lista_prim.index(minimum))
    lista_wierzcholkow_posortowana.insert(0, element[0])

    # generowanie podgrafu G1 z G
    G1 = G.subgraph(G.nodes).copy()

    # usuwanie wierzchołka o minimalnym stopniu z grafu G1
    G1.remove_node(minimum[0])

    # wykonanie tych samych kroków dla pozostałych wierzchołków
    for _ in range(2, n):
        lista_prim = list(G1.degree)
        minimum = min(G1.degree(), key=lambda x: x[1])
        element = lista_prim.pop(lista_prim.index(minimum))
        lista_wierzcholkow_posortowana.insert(0, element[0])
        G1.remove_node(minimum[0])
    lista_wierzcholkow_posortowana.insert(0, lista_prim[0][0])

    return lista_wierzcholkow_posortowana


# kolorowanie zachłanne wierzchołków
def KolorujZachłannie():
    # nadanie koloru pierwszemu wierzchołkowi z listy
    v1 = lista_smallest_last[0]
    G.nodes[v1]["kolor"] = 0

    lista_sasiadow = list(G.adj[lista_smallest_last[0]])

    for j in range(1, n):
        tab = ["false"] * n
        v1 = lista_smallest_last[j]
        lista_sasiadow = list(G.adj[lista_smallest_last[j]])
        for sasiad in lista_sasiadow:
            if G.nodes[sasiad]["kolor"] > -1:
                tab[G.nodes[sasiad]["kolor"]] = "true"
            i = 0
            while tab[i] == "true":
                i += 1
            else:
                G.nodes[v1]["kolor"] = i

    return G


def PokazGraf(Graf, kolory):
    # ----------------interpretacja graficzna pokolorowanego grafu
    print(Graf._node)
    plt.figure()

    nx.draw(
        Graf,
        pos=None,
        node_color=kolory,
        vmin=0,
        vmax=4,
        edgecolors="k",
        cmap=plt.cm.get_cmap("rainbow"),
        with_labels=True,
    )

    plt.show()
    return 0


def Naiwny():
    # słownik z parami 'wierzchołek': int(kolor)
    b = nx.get_node_attributes(G, "kolor")
    # stworzenie listy wartości kolorów do wyłuskania liczby ich wystąpień
    c = list(b.values())
    # PokazGraf(G, c)

    # indeks w liście odpowiada numerowi koloru
    c.sort()
    # zliczenie wystąpień kolorów
    liczba_wystapien = list((Counter(c)).values())
    colmin = min(liczba_wystapien)
    colmax = max(liczba_wystapien)

    # pętla sprawdzająca warunek sprawiedliwego pokolorowania
    while colmax - colmin > 1:

        # kolor z najmn. i najw. liczbą wystąpień
        kolor_min = liczba_wystapien.index(colmin)
        kolor_max = liczba_wystapien.index(colmax)

        # zbiór wierzchołków o 'kolor' == kolor_max
        lista = [n for n in G.nodes() if G.nodes[n]["kolor"] == kolor_max]
        for n in lista:
            lista_sasiadow = list(G.adj[n])
            for sasiad in lista_sasiadow:
                if G.nodes[sasiad]["kolor"] == kolor_min:
                    break
            else:
                G.nodes[n]["kolor"] = kolor_min
                flaga = 1

        # nadanie nowego koloru gdy żaden wierzchołek z kolor_max nie zmienił koloru na kolor_min
        if flaga != 1:
            G.nodes[lista[0]]["kolor"] = max(c) + 1

        # aktualizacja
        b = nx.get_node_attributes(G, "kolor")
        c = list(b.values())
        c.sort()
        liczba_wystapien = list((Counter(c)).values())
        colmin = min(liczba_wystapien)
        colmax = max(liczba_wystapien)
    # -----------koniec pętli while
    return G


# def Zwroc_wierzcholki():
# return {n for n in G.nodes() if G.nodes(n).data("kolor") == colmax}

if __name__ == "__main__":
    G = WczytajGraf()
    print("Krawedzie: ", G.edges)

    PokazGraf(G, "#fbfdfe")
    # obliczanie liczby krawędzi
    m = G.number_of_edges()

    # obliczanie liczby wierzcholkow
    n = G.number_of_nodes()

    print("Liczba krawedzi: ", m, "\nLiczba wierzcholkow: ", n)

    # stworzenie listy wierzchołków
    lista_wierzcholkow = list(G.nodes())

    # stworzenie listy stopni wierzchołków po przez listę słowników. Jeden słownik/krotka odpowiada jednemu wierzchołkowi
    # key: indeks wierzchołka, value: stopień wierzchołka
    # ////lista_stopni_prim = sorted(G.degree(), key=lambda kv: int(kv[0]))
    lista_stopni = list(G.degree())

    # ------------------------------------------------SmallestLast()
    lista_smallest_last = SmallestLast()

    # ustawienie domyślnego koloru '-1' dla wszystkich wierzchołków w grafie G. Kolor jest słownikiem.
    nx.set_node_attributes(G, -1, "kolor")

    # -----------------------------------------KolorujZachłannie()
    G = KolorujZachłannie()

    print(G._node)
    PokazGraf(G, list(nx.get_node_attributes(G, "kolor").values()))

    # -------------------------------------------------Naiwny()
    G = Naiwny()

    print(G._node)
    PokazGraf(G, list(nx.get_node_attributes(G, "kolor").values()))
