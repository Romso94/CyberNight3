import sys
from socket import socket
import time

keyword = "CYBN"
def main():
    liste_movement = []

    dico_move_possible = {'U':'D',
                        'D': 'U',
                        'L':'R',
                        'R':'L'}
    sock = socket()
    # connection to hostname on the port.
    sock.connect(('10.242.0.1',10004))

    # Receive no more than 1024 bytes
    time.sleep(1)
    tm = sock.recv(8192)


    #recuperation des éléments reponse au nc
    temp = tm.decode('utf-8').split("\n")
    ligne1,ligne2,ligne3 = [],[],[]

    print(temp)

    for element in temp[5]:
        if element !=" ":
            ligne1.append(element)

    for element in temp[6]:
        if element !=" ":
            ligne2.append(element)

    for element in temp[7]:
        if element !=" ":
            ligne3.append(element)


    #construction du labyrinthe
    maze=[ligne1,
    ligne2,
    ligne3]



    print(ligne1)
    print(ligne2)
    print(ligne3)

    dico_voisin = create_dico()

    dico_voisin = check_voisin(dico_voisin,maze)

    dic_voisin = dico_voisin[1]

    # read_dico(dico_voisin)

    deplacement = moove_possibles(dic_voisin)

    
    sock.send(f"{deplacement}\n".encode())

   

    while True:
        maze = recupmaze(sock)
        print(maze)

        isdeplacement = check_voisin(dic_voisin,maze)

        if isdeplacement[0]==1:
            for element in isdeplacement[1]:
                deplace(maze,element,isdeplacement[1])
            



       
        



       
        

        
    

    
    

    # close the client socket
    sock.close()

def recupmaze(sock):

    tm = sock.recv(8196)
    tm = sock.recv(8196)



    
       
    temp = tm.decode('utf-8').split("\n")
    ligne1,ligne2,ligne3 = [],[],[]

    

    for element in temp[1]:
        if element !=" ":
            ligne1.append(element)

    for element in temp[2]:
        if element !=" ":
            ligne2.append(element)

    for element in temp[3]:
        if element !=" ":
            ligne3.append(element)


        #construction du labyrinthe
        maze=[ligne1,
        ligne2,
        ligne3]

    return maze

def deplace(maze,deplacement,dico,sock):

    if check_voisin(dico)[0]==0:
        return
    else:
        sock.send(f"{deplacement}\n".encode())
        return deplace(maze,deplacement,)
    pass

    


    



def create_dico():
    dico_voisins = {
        "bas":[0,'D'],
        "droite":[0,'R'],
        "haut":[0,'U'],
        "gauche":[0,'L'] 
        }
    return dico_voisins

def check_voisin(dico,maze):
    cpt = 0
    #check a gauche
    if maze[1][0] =='c':
        dico['gauche'][0] = 1

    #check a droite
    if maze[1][2] =='c':
        dico['droite'][0] = 1
    
    #check a bas
    if maze[2][1] =='c':
        dico['bas'][0] = 1

    #check a haut
    if maze[0][1] =='c':
        dico['haut'][0] = 1


    #check cul de sac
    if maze[0][1] =='w':
        cpt+=1

    if maze[1][0] =='w':
        cpt+=1

    if maze[1][2] =='w':
        cpt+=1
    if maze[2][1] =='w':
        cpt+=1

    if cpt == 3:
        return(0,dico)

    return (1,dico)


# def read_dico(dico):
    
#     print(f"Gauche : {dico['gauche']}")
#     print(f"Droite :{dico['droite']}")
#     print(f"Bas : {dico['bas']}")
#     print(f"Haut : {dico['haut']}")
    

def moove_possibles(dico_voisin):
    compteur = 0
    
    deplacement=[]
    for k in dico_voisin.items():
        if k[1][0]==1:
            compteur +=1
            deplacement.append(k[1][1])
    
    return deplacement
    
    



main()


    












    
   


