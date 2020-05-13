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


if __name__ == "__main__":
    G = WczytajGraf()
    print("Krawedzie: ", G.edges)

    # obliczanie liczby krawędzi
    m = G.number_of_edges()

    # obliczanie liczby wierzcholkow
    n = G.number_of_nodes()

    print("Liczba krawedzi: ", m, "\nLiczba wierzcholkow: ", n)

    # stworzenie listy sąsiedztw
    slownik_sasiedztw = G.adj["3"]
    # G.adjacency()

    lista_sasiedztw = list(slownik_sasiedztw)

    print("lista sąsiedztw = ", lista_sasiedztw)
