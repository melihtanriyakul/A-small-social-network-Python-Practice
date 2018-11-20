import networkx as nx


def find_path(city, graph):
        if(G.neighbors(city)==""):
            print "City '"+city+"' has no reachable neighbour"
        else:
            print "'"+city+"'",":",G.neighbors(city)

G=nx.Graph()
in_file = "CN.txt"
myfile = open("CN.txt")
while (0==0):
        paths = myfile.readline();
        if(paths!=""):
            pathA = paths.split()
            a = pathA[0].split(":")
            pathz = pathA[1:len(pathA)]
            pathz.append(a[1])
            i=0
            for i in pathz:
                G.add_path([a[0],i])
        else: break

in_file = "commandsP2.txt"
myfile = open("commandsP2.txt")
paths=myfile.read();
pathsinputs=paths.split(",")
for i in pathsinputs:
    find_path(i,G)