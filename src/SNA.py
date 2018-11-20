import networkx as nx

def ADD_USER(newuser,existuser,graph):
    if(graph.has_node(newuser)==True):
        print("This user already exists!!")
    elif(graph.has_node(existuser)==False):
        print("There is no user named '"+existuser+"'")
    elif(graph.has_node(existuser) & graph.has_node(newuser)==False):
        G.add_edge(newuser,existuser)
        print("User '"+newuser+"' has been added and tied to '"+existuser+"' successfully")

def REMOVE_USER(existuser,graph):
    if(graph.has_node(existuser)==False):
        print("There is no user named '"+existuser+"'!!")
    elif(graph.has_node(existuser)==True):
        G.remove_node(existuser)
        print("User '"+existuser+"' and its all relations have been removed successfully.")

def ADD_RELATION(existuser1,existuser2,graph):
    if(graph.has_node(existuser1)==False):
        print("No user named '"+existuser1+"' or '"+existuser2+"' found!!")
    elif(graph.has_node(existuser2)==False):
        print("No user named '"+existuser1+"' or '"+existuser2+"' found!!")
    elif(graph.has_edge(existuser1,existuser2)==True):
        print("A relation between '"+existuser1+"' and '"+existuser2+"' already exists!!")
    else:
        G.add_edge(existuser1,existuser2)
        print("Relation between '"+existuser1+"' and '"+existuser2+"' has been added succesfully.")

def REMOVE_RELATION(existuser1,existuser2,graph):
    if(graph.has_node(existuser1)==False):
        print("No user named '"+existuser1+"' or '"+existuser2+"' found!!")
    elif(graph.has_node(existuser2)==False):
        print("No user named '"+existuser2+"' or '"+existuser1+"' found!!")
    elif(graph.has_edge(existuser1,existuser2)==False):
        print("No relation between '"+existuser1+"' and '"+existuser2+"' found!!")
    else:
        G.remove_edge(existuser1,existuser2)
        print("A relation between '"+existuser1+"' and '"+existuser2+"' has been removed successfully.")

G=nx.Graph()
in_file = "sn.txt"
myfile = open("sn.txt")
while (0==0):
        liste = myfile.readline();
        if(liste!=""):
            listA = liste.split()
            a = listA[0].split(":")
            listz = listA[1:len(listA)]
            listz.append(a[1])
            i=0
            for i in listz:
                G.add_edge(a[0],i)
        else: break
command_file="commandsP1.txt"
myfile=open("commandsP1.txt")
while (0==0):
    liste=myfile.readline();
    if(liste!=""):
        listinputs=liste.split()
        if(listinputs[0]=="AU"):
            if(len(listinputs)<3):
                print("Error: Wrong input type! for 'AU'!")
            else:
                ADD_USER(listinputs[1],listinputs[2],G)
        if(listinputs[0]=="RU"):
            if(len(listinputs)>2):
                print("Error: Wrong input type! for 'RU'!")
            elif(len(listinputs)<2):
                print("Error: Wrong input type! for 'RU'!")
            else:
                REMOVE_USER(listinputs[1],G)
        if(listinputs[0]=="AR"):
            if(len(listinputs)<3):
                print("Error: Wrong input type! for 'AR'!")
            else:
                ADD_RELATION(listinputs[1],listinputs[2],G)
        if(listinputs[0]=="RR"):
            if(len(listinputs)<3):
                print("Error: Wrong input type! for 'RR'!")
            else:
                REMOVE_RELATION(listinputs[1],listinputs[2],G)

    else: break
