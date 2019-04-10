# definizione della classe Node
class Node(object):
    def __init__(self, id):
        self.sane = False
        self.visited = False
        self.id = id
        self.adjlist = []

    def __str__(self):
        return "id:"+str(self.id)+"\nsane:"+str(self.sane)+"\n"


# visita in profondità
def visit(node):
    if not node.visited and node.sane:
        # marca il nodo come visitato e lo restituisce al chiamante
        node.visited = True
        yield node
        # per ogni nodo connesso ad esso ricorre
        for adjnode in node.adjlist:
            # yield from serve per permettere l'utilizzo di yield durante le
            # ricorsioni
            yield from visit(adjnode)


# costruisce una foresta composta da liste di nodi connessi fra di loro
def buildforest(graph):
    forest = dict()
    for node in graph:
        if not node.visited and node.sane:
            # la foresta è costruita come un dizionario con key l'id del nodo
            # di partenza e value una lista dei nodi scoperti durante una
            # visita in profondità
            forest[node.id] = list(visit(node))
    return forest


# resetta i parametri visited e sano dei nodi
def resetgraph(graph):
    for node in graph:
        node.sane = False
        node.visited = False


# importa il grafo da file di testo
def buildgraph(filepath):
    graph = []
    i = 0
    with open(filepath, 'r') as f:
        # crea oggetti nodo in base al numero letto nella prima riga
        nnodes = f.readline()
        while(i < int(nnodes)):
            graph.append(Node(i))
            i += 1

        # costruzione della lista delle adiacenze
        i = 0
        for line in f:
            j = 0
            for connected in line.split(','):
                if connected == "1":
                    # l'adiacenza viene registrata tramite una lista di nodi
                    # all'interno di ogni nodo vengono inseriti solo i
                    # riferimenti ai nodi già presenti nella lista graph
                    graph[i].adjlist.append(graph[j])
                j += 1
            i += 1
    return graph


# generica funzione di lettura di un file dato un delimitatore come parametro
def readfile(filepath, delim):
    with open(filepath, 'r') as f:
        for line in f:
            yield line.split(delim)


########
# MAIN #
########
def main():
    # importa il grafo da txt
    graph = buildgraph('./src/inputmatrix3000.txt')

    # creazione del generatore di linee
    # ogni linea è generata in base al delimitatore '-'
    # quindi rappresenta i risultati di ogni simulazione
    simulations = readfile('./src/log.txt', '-')

    # ora cicliamo estraendo ogni simulazione in simu,
    # che sarà quindi una lista di stringhe
    for simulation in simulations:
        for simu in simulation:
            # splittiamo la simulazione in una lista di parole
            # (un elemento per ogni spazio)
            nodestates = str(simu).split()

            # mettiamo da parte il primo elemento della lista in quanto
            # rappresenta la probabilità alla quale è stata simulata
            # l'infezione
            p = nodestates.pop(0)

            # e cicliamo sul resto per determinare lo stato dei nodi
            for state in nodestates:
                graph[int(state)].sane = True

            # finito il setup del grafo
            # analizziamo per ottenere una lista delle lcc
            lcc = buildforest(graph)

            # la sfruttiamo per ottenere una lista di valori corrispondenti
            # alla grandezza di ogni lcc
            lccsizes = []
            for root, nodelist in lcc.items():
                lccsizes.append(len(nodelist))

            # e stampiamo a schermo il valore più alto
            maxitem = max(lccsizes)
            print(p, maxitem)

            # resettiamo per il prossimo ciclo
            resetgraph(graph)


if __name__ == "__main__":
    main()
