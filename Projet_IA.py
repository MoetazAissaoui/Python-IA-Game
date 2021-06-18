# Daoud Anas - Aissaoui Moetez - Barkewi Mohammed - 2CS4

from copy import deepcopy
import time

# ------------------------------------------------------------------
#                      Les fonctions de Bases 
# ------------------------------------------------------------------

etat_initial = [[1,2,3],[8,6,0],[7,5,4]]  #état initial
etat_final =[[1,2,3],[8,0,4],[7,6,5]]  #état final

# Comparer entre l'état courant et l'état final 

def estEtatFinal (t,tf):
  return t==tf

# Trouver les coordonnées des cases vides dans la matrice 

def position_case_vide(t):
    for row in range(len(t)):
        for col in range(len(t[row])):
            if t[row][col] == 0 : 
                return (row,col)

# Retourne la valeur de la case

def numero(t,x,y):
  return t[x][y]

# Permuter deux cases 

def permuter(t, pos, move):
    temp = deepcopy(t)
    i, j = pos  # ancienne position de vide
    x, y = move  # nouvelle position de vide
    temp[i][j], temp[x][y] = temp[x][y], temp[i][j]  # permutation avec python
    return temp

# Afficher la matrice

def affiche (t):
    for row in t:
      print('\t ++++++++++++')
      print('\t|',row[0],'|',row[1],'|',row[2],'|')
    print('\t +++++++++++++')

# Verifie si le mouvement est valide
# Si on fait un mouvement quel que soit sa direction il ne doit pas faire sortir la case au dehors de la matrice

def valid(x,y):
    return x>-1 and x<3 and y>-1 and y<3

# Retourne une ou plusieurs matrices selon la validité de transition

def transitions(t) :
  pos=position_case_vide(t)
  liste = []
  x = [1,0,-1,0]
  y = [0,1,0,-1]
  for i in range(4):
    if(valid(pos[0]+x[i],pos[1]+y[i])):
       liste.append([pos[0]+x[i],pos[1]+y[i]])
  derive=[]
  for i in liste :
    derive.append(permuter(t,pos,i))
  return derive

# Fonction Heuristique --> trouver combien de cases mal placés

def h(etat_initial,etat_final):
  nb=0
  for i in range(len(etat_initial)):
    for j in range(len(etat_initial[i])):
      if (etat_initial[i][j]!=etat_final[i][j])and (etat_initial[i][j]!=0):
        nb=nb+1
  return nb

# ------------------------------------------------------------------
#                      Algorithme A* 
# ------------------------------------------------------------------

trace= []
visited= []
success=False

def aetoile(s,goal):
  start = time.time()
  niveaux = 0
  free_nodes = []
  free_nodes.append(s)
  closed_nodes = []
  success = False
  while (free_nodes!=[]) and (not success) and (niveaux < 100):
    first_node = free_nodes[0]
    print()
    print (' \n-- Itération ', niveaux,': ')
    niveaux += 1
    affiche(first_node)
    free_nodes.remove(first_node)
    closed_nodes.append(first_node)
    generated_states = transitions(first_node)

    for s in generated_states:
      if s == goal:
        success = True
        print (' \n-- Itération ', niveaux,': ')
        affiche(s)
        goal_node = s
    free_nodes = free_nodes + generated_states
    free_nodes.sort(key = lambda el:(niveaux+h(el,goal)))

  if niveaux == 100:
    print("Recherche non conclussive")
  else:
    print(" Recherche fini aprés",niveaux," iterations .")
  print ('Temps pris pour exécution: %0.3fs' % (time.time()-start))

aetoile(etat_initial,etat_final)


def transitions(t) :
  pos=position_case_vide(t)
  liste = []
  x = [1,0,-1,0]
  y = [0,1,0,-1]
  for i in range(4):
    if(valid(pos[0]+x[i],pos[1]+y[i])):
       liste.append([pos[0]+x[i],pos[1]+y[i]])
  derive=[]
  for i in liste :
    derive.append(permuter(t,pos,i))
  return derive

# ------------------------------------------------------------------
#                      Algorithme BFS 
# ------------------------------------------------------------------

def bfs(node):
    global start 
    start= time.time()
    global success
    global tf
    global visited
    global trace 
    l = []
    l.append(node)
    while(len(l) != 0 and success==False):
        s=l.pop(0)
        trace.append(s)
        visited.append(s)
        if estEtatFinal(s,etat_final):
            success=True
        else:
            tab=transitions(s)
            for i in tab:
                if (i not in visited and success==False):
                    l.append(i)
bfs(etat_initial)
niveaux=0
for i in trace :
  print()
  print ('Itération:', niveaux,':')
  affiche(i)
  niveaux+=1
print("Résultat trouvée après ",niveaux-1," iterations .")
print ('Time spent: %0.2fs' % (time.time()-start))


def transitions(t) :
  pos=position_case_vide(t)
  liste = []
  x = [1,-1,0,0]
  y = [0,0,1,-1]
  for i in range(4):
    if(valid(pos[0]+x[i],pos[1]+y[i])):
       liste.append([pos[0]+x[i],pos[1]+y[i]])
  derive=[]
  for i in liste :
    derive.append(permuter(t,pos,i))
  return derive

# ------------------------------------------------------------------
#                      Algorithme DFS 
# ------------------------------------------------------------------

trace= []
visited= []
success= False
def dfs(node, etat):
  global start 
  start= time.time()
  global success
  if (success==False and node not in visited):
    trace.append(node)
    if estEtatFinal(node,etat):
      success=True
    visited.append(node)
    tab=transitions(node)
    for i in tab:
      if i not in visited and success==False:
         dfs(i,etat)
dfs(etat_initial,etat_final)
niveaux=0
for i in trace :
  print()
  print ('Itération:', niveaux,' : ')
  affiche(i)
  niveaux+=1
print("Résultat trouvée après",niveaux-1," iterations .")
print ('Temps dexecution: %0.2fs' % (time.time()-start))

# Daoud Anas - Aissaoui Moetez - Barkewi Mohammed - 2CS4