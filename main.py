import sys
import math
import networkx as nx
import matplotlib as mpl
import matplotlib.pyplot as plt
from collections import Counter

# from .classic import empty_graph, path_graph, complete_graph

# Wczytanie grafu G z pliku input.txt
def WczytajGraf():
    # G = nx.star_graph(n)
    G = nx.Graph()
    plik = open("res/input.txt")
    for line in plik:
        x = line.split()
        G.add_edge(x[0], x[1])
    return G


def ZapiszGraf(G, plik):

    for krotka in G._node:
        print(str(krotka) + "  kolor: " + str(G.nodes[krotka]["kolor"]), file=plik)
    # print(G._node, file=plik)
    plik.close()
    return 0


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

        # jeśli wierzchołek nie ma sąsiadów to pokoloruj na pierwszy istniejący kolor
        if lista_sasiadow == []:
            G.nodes[v1]["kolor"] = 0
            break

        for sasiad in lista_sasiadow:
            if G.nodes[sasiad]["kolor"] > -1:
                tab[G.nodes[sasiad]["kolor"]] = "true"
            i = 0
            while tab[i] == "true":
                i += 1
            else:
                G.nodes[v1]["kolor"] = i

    return G


def PokazGraf(Graf, kolory, plik):
    # ----------------interpretacja graficzna pokolorowanego grafu
    print(kolory)
    low, *_, high = sorted(kolory)
    norm = mpl.colors.Normalize(vmin=low, vmax=high, clip=True)
    mapper = mpl.cm.ScalarMappable(norm=norm, cmap=plt.cm.get_cmap("Spectral"))

    print(Graf._node)
    plt.figure()

    nx.draw(
        Graf,
        pos=None,
        node_color=[mapper.to_rgba(i) for i in kolory],
        edgecolors="k",
        with_labels=True,
    )
    plt.savefig(plik)
    plt.show()
    return 0


def Naiwny():
    # słownik z parami 'wierzchołek': int(kolor)
    b = nx.get_node_attributes(G, "kolor")

    # stworzenie listy wartości kolorów do wyłuskania liczby ich wystąpień
    c = list(b.values())
    # PokazGraf(G, c, 'out/input.png')

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
        flaga = 0
        for n in lista:
            lista_sasiadow = list(G.adj[n])
            for sasiad in lista_sasiadow:
                if G.nodes[sasiad]["kolor"] == kolor_min:
                    break
            else:
                G.nodes[n]["kolor"] = kolor_min
                flaga = 1
                break

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


def Test(nr_testu):
    print("Test nr ", nr_testu)
    if nr_testu == 1:
        G = WczytajGraf()

    if nr_testu == 2:
        G = nx.complete_graph(30)
        plik = open("res/generated.txt", "wb")
        nx.write_edgelist(G, plik, data=False)
        plik.close()

    if nr_testu == 3:
        G = nx.fast_gnp_random_graph(8, 0.3)
        plik = open("res/generated.txt", "wb")
        nx.write_edgelist(G, plik, data=False)
        plik.close()

    if nr_testu == 4:
        G = nx.newman_watts_strogatz_graph(10, 3, 0.3)
        plik = open("res/generated.txt", "wb")
        nx.write_edgelist(G, plik, data=False)
        plik.close()

    return G


# def Zwroc_wierzcholki():
# return {n for n in G.nodes() if G.nodes(n).data("kolor") == colmax}

if __name__ == "__main__":
    G = Test(1)
    # G.add_node("1")

    # ustawienie domyślnego koloru '-1' dla wszystkich wierzchołków w grafie G. Kolor jest słownikiem.
    nx.set_node_attributes(G, -1, "kolor")

    # prezentacja grafu wejściowego z wierzchołkami o jednym kolorze
    PokazGraf(
        G, list(nx.get_node_attributes(G, "kolor").values()), "res/input_graph.png",
    )

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

    # -----------------------------------------KolorujZachłannie()
    G = KolorujZachłannie()

    PokazGraf(
        G,
        list(nx.get_node_attributes(G, "kolor").values()),
        "out/output_SmallestLast.png",
    )
    ZapiszGraf(G, open("out/output_SmallestLast.txt", "w"))

    # -------------------------------------------------Naiwny()
    G = Naiwny()

    PokazGraf(
        G,
        list(nx.get_node_attributes(G, "kolor").values()),
        "out/output_Naiwny_final.png",
    )
    ZapiszGraf(G, open("out/output_Naiwny_final.txt", "w"))
