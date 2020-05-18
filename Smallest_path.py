from lab1_utilities import *


def get_installations_from_file(file_name):

    file = open(file_name, "r")
    line = file.readline()
    line = file.readline()

    
    final = []
    while line != '':
        
        line = line.split('\t')
        final.append(line)


        door = None
        name = line[0]
        ward = line[2]
        ward = int(ward)
        position = (line[6], line[7])
        if line[-1] == 'INDOORS':
            door = True
        elif line[-1] == 'OUTDOORS':
            door = False
        
        piece = Installation(name, ward, position, door)
        print(piece)
        return piece
    '''
                             
        final.append(piece)
        
        print(piece)
        line = file.readline()
    return final
     '''   

def euclidean_distance(position1, position2):
    for char in position1:
        if str(char) in 'naNA':
            return 'insufficient data for distance calculation'
    for char in position2:
        if str(char) in 'naNA':
            return 'insufficient data for distance calculation'

    inner = ((position1[0] - position2[0])**2) + ((position1[1] - position1[0])**2)                
    return inner**(1/2)



def get_adjacency_mtx(installations):
    
    matrix=[]
    for installation in installations:
        inner=[]
        for element in installations:
            
            if element.ward == element.ward():
                inner.append(0)
                
            if abs(installtion.ward()-element.ward()) == 1:
                d = euclidean_distance(installation.position, element.position)
                
                if installation.indoor == True and element.indoor == True:
                    inner.append(d*1.5)
                
                elif installation.indoor == False and element.indoor == False:
                    inner.append(d)
                  
        matrix.append(inner)
    return matrix

def make_graph(installations): 
    
    ins = []
    for x in installations: 
        ins.append(x.name)
        
    giraffe = Graph(ins, get_adjacency_mtx(installations))
    return giraffe  

def shortest_path(installation1, installation2, graph):
    pass