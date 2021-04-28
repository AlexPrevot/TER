# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 17:23:27 2021

@author: User
"""
from math import *
from Error import error

from random import seed
from random import randint

import random

import numpy as np



import myModule

import pylab

from Map import Map


#note : changer le deuxième for car complexité de n², on peut transformer en n
def crossOverPath5(nbrElementTab1,tabPath1, tabPath2):
    newTabPathCO=[]
    for i in range(nbrElementTab1):
        newTabPathCO.append(tabPath1[i])

    for i in range(np.size(tabPath2)):
        if tabPath2[i] not in newTabPathCO:
            newTabPathCO.append(tabPath2[i])

    return newTabPathCO


def crossOverPath3(nbr,path1, path2):
    child = []
    seen = []
    temp = [-1]*len(path1)
    miss = []
    
    l = len(path1)
    for i in range(0,l,2):
        if i < l:
            child.append(path1[i])
        if i+1 < l:
            child.append(path2[i+1])
    
    #find already seen value
    for i in range(len(temp)):
        if temp[child[i]] == -1:
            temp[child[i]] = i
        else:
            seen.append(i)
    
    for i in range(len(temp)):
        if temp[path2[i]] == -1:
            miss.append(path2[i])
    
    for i in range(len(seen)):
        child[seen[i]] = miss[i]
    
    return child


#note : sous forme n et non n^2
def singlePoint(nbr,path1, path2):
    #child from the cross_over
    child=path2.copy()
    #tab of already present values (but only their coordinates)
    seen=[]
    temp = [-1]*len(path1)
    #tab of missing value in the order of path2
    miss = []
    
    #copy piece of path1 in path2
    for i in range(nbr):
        child[i] = path1[i]

    #find already seen value
    for i in range(len(temp)):
        if temp[child[i]] == -1:
            temp[child[i]] = i
        else:
            seen.append(i)
    
    for i in range(len(temp)):
        if temp[path2[i]] == -1:
            miss.append(path2[i])
    
    for i in range(len(seen)):
        child[seen[i]] = miss[i]
    
    return child	


#cross over hasardeux
def crossOverPath2(path1, path2):
    #child from the cross_over
    child=path2.copy()
    #tab of already present values (but only their coordinates)
    seen=[]
    temp = [-1]*len(path1)
    #tab of missing value in the order of path2
    miss = []
    
    p1 = randint(0,len(path1))
    p2 = randint(0,len(path1))
    
    if (p1 > p2):
        tmp = p1
        p1 = p2
        p2 = tmp
        
    
    
    #copy piece of path1 in path2
    for i in range(p1,p2):
        child[i] = path1[i]

    #find already seen value
    for i in range(len(temp)):
        if temp[child[i]] == -1:
            temp[child[i]] = i
        else:
            seen.append(i)
    
    for i in range(len(temp)):
        if temp[path2[i]] == -1:
            miss.append(path2[i])
    
    for i in range(len(seen)):
        child[seen[i]] = miss[i]
    
    return child






           
def matriceUnion(mat1,mat2):
    #print("matrice union")
    #print("------------mat1")
    #print(mat1)
    #print("------------mat2")
    #print(mat2)
    final_mat = list(set(mat1) | set(mat2))
    return final_mat




#crossover ERO 
def matriceConversion(path1,path2):
    mat1 = [-1]*len(path1)
    mat2 = [-1]*len(path2)
    
    
    #mat3 = [-1]*len(path3)
    matFinal = []

    
    for i in range(len(path1)):
        if i== (len(path1))-1:
            mat1[path1[i]] = [path1[len(path1)-2],path1[0]]
            mat2[path2[i]] = [path2[len(path2)-2],path2[0]]
            
            #mat3[path3[i]] = [path3[len(path3)-2],path3[0]]
            
        else :
            mat1[path1[i]] = [path1[i-1],path1[i+1]]
            mat2[path2[i]] = [path2[i-1],path2[i+1]]
            
            #mat3[path3[i]] = [path3[i-1],path3[i+1]]
  
    for i in range(len(path1)):
        matFinal.append(matriceUnion(mat1[i], mat2[i]))
    
    return matFinal

#complexité n² voir si on peut faire mieux
def crossOverERO(parent1, parent2):
    k = []
    N = parent1[0]
    
    
    
    matrice = matriceConversion(parent1, parent2)
    
    #print(matrice)
    smallest = [1,2]
    while(len(k) < len(parent1)):
        
        #print(k)
        k.append(N)
        
        for i in matrice:
            if N in i:
                i.remove(N)
    
        if len(matrice[N]) != 0:
            #print("-----")
            #print(N)
            #print(matrice[N])
            #print(len(matrice[N]))
            smallest = [matrice[N][0],len(matrice)]
            
            for i in matrice[N]:
                if ((len(matrice[i]) < smallest[1]) and (len(matrice[i]) != 0)):
                    smallest[0] = i
                    smallest[1] = len(matrice[i])
        else:
            #print("-----else")
            #print(N)
            #print(matrice[N])
            #print(len(matrice[N]))
            m = len(parent1)
            for i in range(len(matrice)):
                if ((i not in k)):
                    #print("condition remplie")
                    smallest[0] = i #random.choice([x for x in range(m) if x not in k])
                    smallest[1] = len(matrice[i])
                    i = len(matrice) + 1            
        N = smallest[0]
        
    return k
        
        



    


























#force brute
def crossOverLoopBRUT(nbrPath, tab):
    crossedTabs = []
    iteration = 0
    for i in range(nbrPath - len(tab)):
        for j in range(i,len(tab)):
            if(iteration + len(tab) < nbrPath):                
                iteration += 1
                crossedTabs.append(
                                        crossOverPath2(tab[i],tab[j]))
            else:
                if crossedTabs:
                    return crossedTabs
                else:
                    error("Le cross_over ne s'est fait pas fait")
                
    return crossedTabs









#force brute
def crossOverLoopClassique(nbrPath, tab, Map):
    crossedTabs = []
    iteration = 0
    nbr = floor(0.5*len(tab[0]))
    for i in range(nbrPath - len(tab)):
        for j in range(i,len(tab)):
            if(iteration + len(tab) < nbrPath):                
                iteration += 1
                crossedTabs.append(
                                        singlePoint(nbr,tab[i],tab[j]))
            else:
                if crossedTabs:
                    return crossedTabs
                else:
                    error("Le cross_over ne s'est fait pas fait")
                
    return crossedTabs




def combinaisonPointSingulier(nbrPath, tab,Map):
    crossedTabs = []
    iteration = 0
    size = floor(len(tab[0])/2)
    for i in range(nbrPath - len(tab)):
         parent1 = tab[randint(0, len(tab)-1)]
         parent2 =tab[randint(0, len(tab)-1)]
         
         child = singlePoint(size,parent1, parent2)

   
        
         
         
         for j in range(len(child)):
            l = random.random()*100
            #print("---")
            #print(P)
            #print(l)
            if ( l < 2):
                #print("mutation")
                pos = randint(0,len(child)-1)
                swapPositions(child, j, pos)

         crossedTabs.append(child)    
         
    return crossedTabs

def RandomCrossMapping(nbrPath, tab,Map,p):
    crossedTabs = []
    iteration = 0
    for i in range(nbrPath - len(tab)):
         parent1 = tab[randint(0, len(tab)-1)]
         parent2 =tab[randint(0, len(tab)-1)]
         
         child1 = crossOverPath2(parent1, parent2)
         child2 = crossOverPath2(parent2, parent1)

         child = []
         if Map.pathLength(child1) < Map.pathLength(child2):
            child = child1
         else:
            child = child2
        
         
         
         for j in range(len(child)):
            l = random.random()*100
            #print("---")
            #print(P)
            #print(l)
            if ( l < p):
                #print("mutation")
                pos = randint(0,len(child)-1)
                swapPositions(child, j, pos)

         crossedTabs.append(child)    
         
    return crossedTabs





#par pair au hasard
def EdgeRecombination(nbrPath, tab,Map):
    crossedTabs = []
    iteration = 0
    for i in range(nbrPath - len(tab)):
         parent1 = tab[randint(0, len(tab)-1)]
         parent2 =tab[randint(0, len(tab)-1)]
         
         child = crossOverERO(parent1, parent2)
         
         
         for j in range(len(child)):
            l = random.random()*100
            #print("---")
            #print(P)
            #print(l)
            if (l < 2):
                #print("mutation")
                pos = randint(0,len(child)-1)
                swapPositions(child, j, pos)
                

         crossedTabs.append(child)

         
         
    return crossedTabs















#par random
def crossOverLoopRAND(nbrPath, tab):
    crossedTabs = []
    iteration = 0
    for i in range(len(tab)):
        if(randint(0,len(tab)) > i +3):
            for j in range(i,len(tab)):
                if(iteration + len(tab) < nbrPath):                
                    iteration += 1
                    crossedTabs.append(
                                        crossOverPath2(tab[i],tab[j]))
                else:
                    if crossedTabs:
                        return crossedTabs
                    else:
                        error("Le cross_over ne s'est fait pas fait")
    return crossedTabs
        


 
    



#mega mutation
def mutation(population,P, Map):
    mutant = []
    for i in population:
        for j in range(len(i)):
            l = random.random()*100

            if (100*P >= l):
                #print("mutation")
                pos = randint(0,len(i)-1)
                swapPositions(i, j, pos)
        mutant.append(i);
                

    return mutant


def mutationDynamique(Map,tabBestPath):
    average = 0
    minimum = Map.pathLength(tabBestPath[0])
        
    for i in tabBestPath:
        average += Map.pathLength(i)
        
    average = average/len(tabBestPath)
    
    p = (1 - ((average - minimum)/minimum))**5
    return p
    
    
def mutationStatique(Map,tabBestPath):
    return 0



    
    
    
def mutationReferentiel(population,P, Map):
    mutant = []
    best = Map.pathLength(population[0])
    prob = 0
    for i in population[1:]:
        prob = best/Map.pathLength(i)
        #print(prob)
        for j in range(len(i)):
            l = random.random()*100
            if (100*prob >= l):
                #print("mutation")
                pos = randint(0,len(i)-1)
                swapPositions(i, j, pos)
        mutant.append(i);
                

    return mutant        
    
    



#mega mutation
def mutationClassique(population,P, Map):
    mutant = []
    for i in population:
        for j in range(len(i)):
            l = random.random()*100
            #print("---")
            #print(P)
            #print(l)
            if (0.01 >= l):
                #print("mutation")
                pos = randint(0,len(i)-1)
                swapPositions(i, j, pos)
        mutant.append(i);
                

    return mutant












#mutation d'un chemin
def mutationPath(tabPath):
    element1 = randint(0 , len(tabPath)-1)
    element2 = randint(0 , len(tabPath)-1)
    swapPositions(tabPath, element1, element2)
    return tabPath



def mutationLoop(tab):
    for i in range(len(tab)):
        if randint(0,10) > 1:
            tab[i] = mutationPath(tab[i])
    return tab

# Swap function 
def swapPositions(tab, pos1, pos2):
    tab[pos1], tab[pos2] = tab[pos2], tab[pos1] 




#selection
def FUSS4(paths,nbr,props):
    final = []
    chunk = floor(len(paths)/10)
    s = nbr/len(paths)
    #prop = ceil(s*chunk)*2 #le x2 ici vient du fait qu'on prend que la moitié de tous les chunks
    prop = ceil(0.5*chunk)

    for i in range(5):
        for j in range(prop):
            final.append(paths[(chunk*i)+j][0])
        #l = random.sample(range(chunk*i, chunk*i + chunk),prop) #sans double essayer avec prob = 1/2
        #for i in l:
            #final.append(paths[i][0])
    
            
            
    #print("proportion")
    #print(prop)
    #print("taille")
    #print(len(final))
    return final

from bisect import bisect_left

#selection
def FUSSPonderer(paths,nbr,props):
    final = []
    chunks = len(paths)/10
   
        
    for i in range(nbr):
         index = random.choice(props)
         start = int(index*chunks)
         end = int((index+1)*chunks)
         l = []
         if index + 1 < 10:
             l = paths[start:end]
         else:
             l = paths[start:len(paths)-1]
         element = random.choice(l)
         final.append(element[0])
        
    return final

#ESSAYER LE FUSS CLASSIQUE SANS MUTATION
def FUSS(paths,nbr,props):
    final = []
    chunks = len(paths)/10
   
        
    for i in range(nbr):
        final.append(random.choice(paths)[0])
        
    return final

def hardSelector(paths,nbr,props):
    chosens = 0
    tab = []
    for i in range(len(paths)):
        if (chosens < nbr):
            if(randint(0,len(paths)) > i):
                chosens += 1
                tab.append(paths[i][0])
    return tab
        
def selectionBrute(paths,nbr,props):
    tab = []
    for i in range(nbr):
        tab.append(paths[i][0])
    return tab



def selectionPathGENITOR(nbrPath, Map, bestElementsSize):
    cityTab = Map.cities
    tabPath =[]
    tabBestPath =[]
    print("NOUVELLE SELECTION")
    import time
    start = time.process_time()
    
    
    
    
    props = []
    for i in range(40):
        props.append(0)
    
    for i in range(20):
        props.append(1)
    
    for i in range(10):
        props.append(2)
    
    for i in range(8):
        props.append(3)
        
    for i in range(7):
        props.append(4)
        
    for i in range(5):
        props.append(5)
    
    for i in range(4):
        props.append(6)
    
    for i in range(3):
        props.append(7)
        
    for i in range(2):
        props.append(8)
        
    for i in range(1):
        props.append(9)
    
    
    
    for m in range(10):
        tabPath.append([])
        for i in range(floor(nbrPath/10)):
                cityTab = Map.randomPath()
                tabPath[m].append([cityTab,Map.pathLength(cityTab)])
            
    
    generation = 0
    bestScore = float('inf')
    iteration = 0
    
    path = []
    
    arrayProb = []
    tabPath.sort(key=lambda x:x[1])
    tabBestPath = [-1]*10
    
    print("nbrPath : 10")
    print(nbrPath/10)
    print("bestElementsSize:10")
    print(bestElementsSize/10)
    while (iteration < 200):
        generation += 1
        for m in range(10):
    
            
            
            
            tabBestPath[m] = []
            
            
        
             
            tabBestPath[m] = FUSSPonderer(tabPath[m],floor(bestElementsSize/10),props)
            
   
            genCrossed = EdgeRecombination(floor(nbrPath/10), tabBestPath[m],Map)
    
            
            
            newSet = tabBestPath[m]
            
            
            
           
            genMutated = mutation(newSet,0,Map)
       
            
           
            tabBestPath[m] = genMutated + genCrossed
            
           
            
            tabPath[m] = []

            
            for i in tabBestPath[m]:
                tabPath[m].append([i,Map.pathLength(i)])
                
            tabPath[m].sort(key=lambda x:x[1])
            
            #print("taille de la pop numéro : ", m)
            #print(len(tabPath[m]))
        
        
        currBest = []
        currBestScore = float('inf')
        for m in range(10):
            if tabPath[m][0][1] < currBestScore:
                currBestScore = tabPath[m][0][1]
                currBest = tabPath[m][0][0].copy()
        
        
        #vérifier le meilleur de chaque sous pop(!) (!) (!)
        if currBestScore < bestScore:
            iteration = 0
            bestScore = currBestScore
            path = currBest.copy()
        else:
            iteration +=1
            
        if (generation % 200 == 0):
            element = []
            for p in range(floor(bestElementsSize/10)):
                element.append(randint(0,floor((nbrPath/10)-1)))
            
            for p in range(10):
                subpop = randint(0,9)
                
                for q in element:
                    mem = tabPath[p][q]
                    tabPath[p][q] = tabPath[subpop][q]
                    tabPath[subpop][q]= mem
                
            
        for p in range(10):
            tabPath[m].sort(key=lambda x:x[1])
    
    print("RESULTAT FINAL")
    print(path)
    print(bestScore)
    print("TEMPS")
    print(time.process_time() - start)
    print("Nombre de Generation : ")
    print(generation)
    return path
         
    
        
        
    




def selectionPath(nbrPath, Map, bestElementsSize):
    cityTab = Map.cities
    tabPath =[]
    tabBestPath =[]
    print("NOUVELLE SELECTION")
    import time
    start = time.process_time()
    
    
    
    
    props = []
    for i in range(40):
        props.append(0)
    
    for i in range(20):
        props.append(1)
    
    for i in range(10):
        props.append(2)
    
    for i in range(8):
        props.append(3)
        
    for i in range(7):
        props.append(4)
        
    for i in range(5):
        props.append(5)
    
    for i in range(4):
        props.append(6)
    
    for i in range(3):
        props.append(7)
        
    for i in range(2):
        props.append(8)
        
    for i in range(1):
        props.append(9)
    
    
    
    for i in range(nbrPath):
            cityTab = Map.randomPath()
            tabPath.append([cityTab,Map.pathLength(cityTab)])
            
    m = 0
    for j in tabPath:
        m += j[1]
    
    m = m/len(tabPath)
    print("moyenne de : " + str(m))
    
    generation = 0
    bestScore = float('inf')
    iteration = 0
    
    path = []
    """
    arrayProb = []
    tabPath.sort(key=lambda x:x[1])
    while (iteration < 200):
        generation += 1
        
        
        tabBestPath = []
        
        
        
        #RAPPEL faire la mutation APRES le crossover et la descendanse (!) (!)
        average = 0
        minimum = Map.pathLength(tabPath[0][0])
        
        for i in tabPath:
            average += Map.pathLength(i[0])
        
        average = average/len(tabPath)
    
        p = (1 - ((average - minimum)/minimum))
        
        #best = tabPath[0][0]

        
         
        tabBestPath = selectionBrute(tabPath,bestElementsSize,props)
        
       
        #p = 0
        
        
        genCrossed = EdgeRecombination(nbrPath, tabBestPath,Map)

        
        #print(len(genCrossed))
        newSet = tabBestPath
        
        
        
       
        genMutated = mutation(newSet,-1,Map)
   
        
       
        tabBestPath = genMutated + genCrossed
        #tabBestPath.append(best)
       
        
        tabPath = []
        
        
        
        
        for i in tabBestPath:
            tabPath.append([i,Map.pathLength(i)])
            
        tabPath.sort(key=lambda x:x[1])
        
        if tabPath[0][1] < bestScore:
            iteration = 0
            bestScore = tabPath[0][1]
            path = tabPath[0][0].copy()
        else:
            iteration +=1
        
        arrayProb.append(p*100)
        
    

    print("Taille population final")
    print(len(tabPath))
    #print("population")
    #for i in tabPath:
        #print(i)

    tabPath.sort(key=lambda x:x[1])
    print("RESULTAT FINAL")
    print(path)
    print(bestScore)
    print("TEMPS")
    print(time.process_time() - start)
    print("Nombre de Generation : ")
    print(generation)
    
    make_graph(generation, arrayProb, "lla", "lala")
    pylab.show()
    return path

    
    
    """
    print("RESULTAT FINAL")
    resultat = myModule.genalgo(Map.cities, nbrPath)
    print(resultat)
    print(Map.pathLength(resultat))
    print("TEMPS")
    print(time.process_time() - start)
    
    
    return resultat 







































#--------------------------------------------------------- POUR FAIRE DES GRAPHES




def selectionPath1(nbrPath,Map,bestElementsSize):
    print("JE FAIS DES GRAPHES")
    generation = 0
    bestScore = float('inf')
    iteration = 0
    
    tabPath = []
    
    for i in range(nbrPath):
            cityTab = Map.randomPath()
            tabPath.append([cityTab,Map.pathLength(cityTab)])
            
    m = 0
    for j in tabPath:
        m += j[1]
    
    m = m/len(tabPath)
    print("moyenne de : " + str(m))
    
    arrayP = []
    arrayG = []
    
    arrayS = []


    arrayERO = []
    arrayRC = []
    gen1 = 0
    gen2 = 0
    g1 = []
    g2 = []
    
    gen1 = algoGene(nbrPath,Map,tabPath,bestElementsSize,arrayERO,FUSS2,crossOverLoop1)
    print("fin 1")
    gen2 = algoGene(nbrPath,Map,tabPath,bestElementsSize,arrayRC,FUSS,crossOverLoop1)
    
    for i in range(gen1):
        g1.append(i)
        
    
    for i in range(gen2):
        g2.append(i)
    
    pylab.plot(g1, arrayERO, color= 'black' )
    pylab.plot(g2, arrayRC,color= 'red')
    pylab.show()
    
    print("generation ERO :")
    print(gen1)
    print("generation RCM :")
    print(gen2)
    
    
    print("score finale ERO:")
    print(arrayERO[-1])
    print("score finale RCM:")
    print(arrayRC[-1])



def mesurePerformance(nbrPath,Map1,bestElementsSize):
    
    #algoGene(nbrPath, Map,tabPath, bestElementsSize,array,mutator,selector,crossOver):
   
    pylab.figure(figsize=(20,10))
    n = 1
    
    count = 0
    arr = []
    nbrVilleMax = 60
    nbr = nbrVilleMax - 4
    
    pylab.grid()
    pylab.title("Croissance de la complexité")
    for i in range(4,nbrVilleMax):
        tabPath = []
        map2 = Map(i,500,0)
        for j in range(nbrPath):
            cityTab = map2.randomPath()
            tabPath.append([cityTab,map2.pathLength(cityTab)])
        newScore = []
        nbrGeneration = 0
        for j in range(n):
            nbrGeneration += algoGene(nbrPath, map2, tabPath, bestElementsSize, 
                                newScore,mutationNull,FUSS2, crossOverLoop)
            count += 1
            prop = (count/(nbr*n))*100
            print("proportion fait : " + str(prop))
        nbrGeneration = nbrGeneration / n
        arr.append(nbrGeneration)
        
    make_graph(nbr,arr,"courbe", "courbe")
    pylab.show()

def etudeGENITOR(nbrPath,Map,bestElementsSize):
    
    generation = 0
    bestScore = float('inf')
    iteration = 0
    
    tabPath = []
    
    for i in range(nbrPath):
            cityTab = Map.randomPath()
            tabPath.append([cityTab,Map.pathLength(cityTab)])
            
    m = 0
    for j in tabPath:
        m += j[1]
    
    m = m/len(tabPath)
    print("moyenne de : " + str(m))
    pylab.figure(figsize=(20,10))
    pylab.grid()
    n = 15


    
    n = 1
    count = 0
    for j in range(2):
        arr = []
        score = [0]
        for i in range(n):
            count += 1
            newScore = [] #mettre le nouveau score dedans et après l'intégrer dans currentScore
            
            if(j > 0):
                arr.append(algoGene2(nbrPath, Map, tabPath, bestElementsSize, 
                                            newScore,mutationStatique,FUSSPonderer,RandomCrossMapping))
            else:
                arr.append(algoGene(nbrPath, Map, tabPath, bestElementsSize, 
                                            newScore,mutationStatique,FUSSPonderer,RandomCrossMapping))
                    
            while len(score) < len(newScore):
                score.append(score[-1])
                            
            while len(score) > len(newScore):
                newScore.append(newScore[-1])
                          
            for k in range(len(score)):
                score[k] += newScore[k]
            
                       
            for k in range(len(score)):
                score[k] = score[k]/n
        
            
        c =1
        make_graph(len(score),score,c,"lala")
    pylab.show()
    print("fini")















def etude(nbrPath,Map,bestElementsSize):
    #ne pas oublier de supprimer le crossOverLoop1 que ne sert à rien
    #trieur = [hardSelector,crossOverLoop,crossOverLoopBrut,crossOverLoopRAND,FUSS]
    #combinateur = [singlePoint,crossOverERO,crossOverPath2] #ajouter le cycle cross over
    #mutateur = [mutation,mutationReferentiel,mutationClassique]
    """
    trieur = [selectionBrute, FUSSPonderer, FUSS]
    combinateur = [RandomCrossMapping,EdgeRecombination,combinaisonPointSingulier] #ajouter le cycle cross over
    mutateur = [mutationDynamique,mutationStatique]"""

    trieur = [selectionBrute]
    combinateur = [EdgeRecombination]
    mutateur = [mutationStatique]
    
    generation = 0
    bestScore = float('inf')
    iteration = 0
    
    tabPath = []
    
    for i in range(nbrPath):
            cityTab = Map.randomPath()
            tabPath.append([cityTab,Map.pathLength(cityTab)])
            
    m = 0
    for j in tabPath:
        m += j[1]
    
    m = m/len(tabPath)
    print("moyenne de : " + str(m))
    pylab.figure(figsize=(20,10))
    pylab.grid()
    n = 15
    total = n * len(trieur)*len(combinateur)*len(mutateur)
    count = 0
    c = 0
    
    for tri in trieur:
        for combi in combinateur:
            for mut in mutateur :
                arr = []
                score = [0] #faire la moyenne dessus
                
                for i in range(n):
                    count += 1
                    newScore = [] #mettre le nouveau score dedans et après l'intégrer dans currentScore
                    
                    
                    arr.append(algoGene(nbrPath, Map, tabPath, bestElementsSize, 
                                        newScore,mut,tri, combi))
                    

                    
                    while len(score) < len(newScore):
                        score.append(score[-1])
                        
                    while len(score) > len(newScore):
                        newScore.append(newScore[-1])
                      
                    for k in range(len(score)):
                        score[k] += newScore[k]
                    print("pourcentage de fait : ", (count/total)*100)
                   
                for k in range(len(score)):
                    score[k] = score[k]/n
                name = ""
                name += mut.__name__ + " "
                name += combi.__name__ + " "
                name += tri.__name__
                print(name)
                
                c = (c + 1)%4
                make_graph(len(score),score,c,name)
                #faire la moyenne de arr et après le plot
    pylab.legend(fontsize=15)
    pylab.xlabel("Nombre de génération")
    pylab.ylabel("Score du meilleur individu")
    pylab.show()
    #faire 10 simulations pour chaque possibilités
    #mettre les fonctions de crossover (pas les loop) en paramètre des crossoverloop


def make_graph(nbrGen,y,c,name):
    x = []
    for i in range(nbrGen):
        x.append(i)
        
    linestyles = ['-', '--', '-.', ':']
    pylab.plot(x, y,linestyle = linestyles[0])
    










def algoGene(nbrPath, Map,tabPath, bestElementsSize,array,mutator,selector,crossOver):
    cityTab = Map.cities
    tabBestPath =[]
    print("NOUVELLE SELECTION")
    
    nbrCity = len(cityTab)
    
    props = []
    for i in range(60):
        props.append(0)
    
    for i in range(9):
        props.append(1)
    
    for i in range(8):
        props.append(2)
    
    for i in range(7):
        props.append(3)
        
    for i in range(6):
        props.append(4)
        
    for i in range(5):
        props.append(5)
    
    for i in range(4):
        props.append(6)
    
    for i in range(3):
        props.append(7)
        
    for i in range(2):
        props.append(8)
        
    for i in range(1):
        props.append(9)

    generation = 0
    bestScore = float('inf')
    iteration = 0
    
    path = []
    
    while (iteration < 100):
        generation += 1
        
        
        tabBestPath = []
        
        
        
        
        
        best = tabPath[0][0]
         
        tabBestPath = selector(tabPath,bestElementsSize,props)
        
       #RAPPEL faire la mutation APRES le crossover et la descendanse (!) (!)
        average = 0
        minimum = Map.pathLength(tabBestPath[0])
        
        for i in tabBestPath:
            average += Map.pathLength(i)
        
        average = average/len(tabBestPath)
    
        #p = (1 - ((average - minimum)/minimum))**5
        p = mutator(Map,tabBestPath)
        
        
        genCrossed = crossOver(nbrPath, tabBestPath,Map)

        
        #print(len(genCrossed))
        newSet = tabBestPath[1:]
        
        
        
        
        genMutated = mutation(newSet,p,Map)
   
        
       
        tabBestPath = genMutated + genCrossed
        tabBestPath.append(best)
       
        
        tabPath = []
        
        
        
        for i in tabBestPath:
            tabPath.append([i,Map.pathLength(i)])
            
        tabPath.sort(key=lambda x:x[1])
        
        if tabPath[0][1] < bestScore:
            iteration = 0
            bestScore = tabPath[0][1]
            path = tabPath[0][0].copy()
        else:
            iteration +=1
        
        array.append(bestScore)
    
    return generation
    
        
    





def algoGene2(nbrPath, Map,tabPath, bestElementsSize,array,mutator,selector,crossOver):
    cityTab = Map.cities
    tabPath =[]
    tabBestPath =[]
    print("NOUVELLE SELECTION")
    import time
    start = time.process_time()
    
    nbrCity = len(cityTab)
    
    
    props = []
    for i in range(40):
        props.append(0)
    
    for i in range(20):
        props.append(1)
    
    for i in range(10):
        props.append(2)
    
    for i in range(8):
        props.append(3)
        
    for i in range(7):
        props.append(4)
        
    for i in range(5):
        props.append(5)
    
    for i in range(4):
        props.append(6)
    
    for i in range(3):
        props.append(7)
        
    for i in range(2):
        props.append(8)
        
    for i in range(1):
        props.append(9)
    
    k = 5
    
    for m in range(k):
        tabPath.append([])
        for i in range(floor(nbrPath/k)):
                cityTab = Map.randomPath()
                tabPath[m].append([cityTab,Map.pathLength(cityTab)])
            
    
    generation = 0
    bestScore = float('inf')
    iteration = 0
    
    path = []
    
    arrayProb = []
    tabPath.sort(key=lambda x:x[1])
    tabBestPath = [-1]*k
    
    while (iteration < 100):
        generation += 1
        for m in range(k):
    
            
            
            
            tabBestPath[m] = []
            
            
        
             
            tabBestPath[m] = FUSSPonderer(tabPath[m],floor(bestElementsSize/k),props)
            
   
            genCrossed = RandomCrossMapping(floor(nbrPath/k), tabBestPath[m],Map)
    
            
            
            newSet = tabBestPath[m]
            
            
            
           
            genMutated = mutation(newSet,0,Map)
       
            
           
            tabBestPath[m] = genMutated + genCrossed
            
           
            
            tabPath[m] = []

            
            for i in tabBestPath[m]:
                tabPath[m].append([i,Map.pathLength(i)])
                
            tabPath[m].sort(key=lambda x:x[1])
            
            #print("taille de la pop numéro : ", m)
            #print(len(tabPath[m]))
        
        
        currBest = []
        currBestScore = float('inf')
        for m in range(k):
            if tabPath[m][0][1] < currBestScore:
                currBestScore = tabPath[m][0][1]
                currBest = tabPath[m][0][0].copy()
        
        
        #vérifier le meilleur de chaque sous pop(!) (!) (!)
        if currBestScore < bestScore:
            iteration = 0
            bestScore = currBestScore
            path = currBest.copy()
        else:
            iteration +=1
        
        tmp = []
        
        for w in range(k):
            tmp.append([])
            for h in range(floor((bestElementsSize/k)/2)):
                tmp[w].append(tabPath[w][h])
            
        
        if(generation % 50 == 0):
            for p in range(k):
                if p+1 < k:
                    for i in range(floor((bestElementsSize/k)/2)):
                       tabPath[p+1][i] = tmp[p][i]
                else:
                    for i in range(floor((bestElementsSize/k)/2)):
                       tabPath[0][i] = tmp[p][i]
            
            for p in range(k):
                tabPath[m].sort(key=lambda x:x[1])
            
        array.append(bestScore)
    
    return generation
    




















    
    