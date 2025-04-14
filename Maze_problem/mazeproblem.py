### CEP_1 MAZE PROBLEM ##
### Azhar Ali ###
### 2021_MC_87 ###
from pyamaze import maze,COLOR,agent
from random import *
chromosome=100
row=12     #row and column shows the size of grid
column=17
goal=(1,1)   # The goal for agent is always (1,1)
m=maze(row,column)  
m.CreateMaze(theme=COLOR.light,loopPercent=200)
a=agent(m,shape='square',filled=True,footprints=True)
f=m.maze_map
# Define crossover function (single point crossover)
def crossover(parent1, parent2):
    crossover_point =choice([1,len(parent1)-1]) #randomly deciding the crossover point
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1,child2
# Define mutation function (random mutation)
def mutation(solution, mutation_rate):
    for i in range(len(solution)):
       if random()<mutation_rate: 
          solution[i] =choice(['W','N'])
    
    return solution
#This function have different path as child and this will check the feasibilty of child chromosome 
def solutionpath(m,f):
       obstacle=[]
       solpath=[]
       for i in m: #m is the where path direction are mentioned
            pathlist=[]
            obs=0
            r,c=row,column
            for j in i:
                  pathlist.append((r,c))
                  if j=='W':
                      if c==1:
                            r-=1
                            if f[(r,c)]['N']==0:
                              obs+=1
                      else:
                            
                            if f[(r,c)]['W']==0:
                                obs+=1
                            c-=1
                  elif j=='N':
                      if r==1:
                            c-=1
                            if f[(r,c)]['W']==0:
                              obs+=1
                      else:
                            if f[(r,c)]['N']==0:
                               obs+=1
                            r-=1
            obstacle.append(obs)   #obstacle of decided path         
            solpath.append(pathlist) #cooordinate cell of decided path
       return obstacle,solpath 
#This function is generating the random path population along with thier obstacle
def pathdecision(population,f):
      obstacle=[]
      path=[]
      i=0
      while i<population:
            r,c=row,column
            obs=0
            direction={}
            while True:
                  dir=0
                  dir=choice(['W','N'])
                  if dir=='W':
                        if c==1:
                              continue
                        else:
                          if f[(r,c)]['W']==0:
                                    obs+=1
                        direction[(r,c)]=dir
                        c-=1
                  elif dir=='N':  
                        if r==1:
                              continue
                        else:
                              if f[(r,c)]['N']==0:
                                    obs+=1
                              direction[(r,c)]=dir
                              r-=1
                  if (r,c)==goal:
                        break
            obstacle.append(obs)
            path.append(direction)
            i+=1
      return obstacle,path
j=0
while j<50000:
      obs,path=pathdecision(chromosome,f)
      c=[(obs[i],path[i]) for i in range(len(obs))]
      s=sorted(c, key=lambda x: x[0])
      if s[0][0]==0:               ##This condition is checking that is any path randomly generated
            l=list(s[0][1].keys()) # path give zero obstacle
            m.tracePath({a:l})
            m.run()
      #print(s)
      k=[]
      for i in range(len(s)): #k is taking out path dictionary 
        k.append(s[i][1])
      l=[list(d.values()) for d in k]  # l have  direction for agnet as list
      parent1=choice(l)
      parent2=choice(l)
      child1,child2=crossover(parent1,parent2)
      child1=mutation(child1,0.5)
      child2=mutation(child2,0.5)
      l.append(choice([child1,child2]))
      o,p=solutionpath(l,f)
      bestpath=p[sorted(o)[0]]
      o=sorted(o)
      print(f'iteration no.{j}')
      j+=1
      
      if o[0]==0:
            m.tracePath({a:bestpath})
            m.run()
            break
   
   
