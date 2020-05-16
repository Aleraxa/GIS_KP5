import sys
import math
import networkx as nx
import matplotlib.pyplot as plt

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

    # wykonanie tych samyhc kroków dla pozostałych wierzchołków
    for x in range(2, n):
        lista_prim = list(G1.degree)
        minimum = min(G1.degree(), key=lambda x: x[1])
        element = lista_prim.pop(lista_prim.index(minimum))
        lista_wierzcholkow_posortowana.insert(0, element[0])
        G1.remove_node(minimum[0])
    lista_wierzcholkow_posortowana.insert(0, lista_prim[0][0])

    return lista_wierzcholkow_posortowana


if __name__ == "__main__":
    G = WczytajGraf()
    print("Krawedzie: ", G.edges)

    # obliczanie liczby krawędzi
    m = G.number_of_edges()

    # obliczanie liczby wierzcholkow
    n = G.number_of_nodes()

    print("Liczba krawedzi: ", m, "\nLiczba wierzcholkow: ", n)

    # stworzenie listy wierzchołków
    lista_wierzcholkow = list(G.nodes())

    # stworzenie listy stopni wierzchołków po przez listę słowników. Jeden słownik odpowiada jednemu wierzchołkowi
    # key: indeks wierzchołka, value: stopień wierzchołka
    # ////lista_stopni_prim = sorted(G.degree(), key=lambda kv: int(kv[0]))
    lista_stopni = list(G.degree())

    # ------------------------------------------------SmallestLast()
    lista_smallest_last = SmallestLast()

    # -----------------------------------------KolorujZachłannie()
    # TO DO

    # -------------------------------------------------Naiwny()
    # TO DO

    # stworzenie listy sąsiedztw
    slownik_sasiedztw = G.adj["3"]
    # G.adjacency()

    lista_sasiedztw = list(slownik_sasiedztw)

    print("lista sąsiedztw = ", lista_sasiedztw)
