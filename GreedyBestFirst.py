import sys
import pandas as pd 
import pdb
import time

class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        
class LinkedList:
    def __init__(self):
        self.head = None

class BestFirst:
    # constructor
    def __init__(self):
        self.reached = {}
        self.frontier = {}
        self.totalCost = 0
        self.solutionPath = []
        self.expanedNodes = 0
        self.start_time = 0

    def best_first_search(self, initState, finalState, drivingInfo, straightInfo):
        # we need closed and open list
        # closed list --> keeps track of visited nodes
        # open list --> keeps track of nodes yet to be visited
        # the initial node contains the name of the initial state
        
        
        initial = ''
        goal = ''
        datacheck = pd.read_csv(drivingInfo, usecols = ['STATE'])
        # if initial state or goal state don't exist, don't search shortest path
        for i in range(len(datacheck['STATE'].values)):
            if(datacheck['STATE'].values[i] == initState):
                initial = initState
                
        for i in range(len(datacheck['STATE'].values)):
            if(datacheck['STATE'].values[i] == finalState):
                goal = finalState
        
        if (initial == '' or goal == ''):
            return None
        
        # initialize frontier and reached lists with the initial state
        data = pd.read_csv(drivingInfo, usecols = ['STATE', initial])
        data2 = pd.read_csv(straightInfo, usecols = ['STATE', initial])
        for i in range(len(data[initial].values)):
            if(data2['STATE'].values[i] == goal): 
                # if the name of the state matches the name of the goal
                # add the distance to frontier
                # add the node to reached
                self.frontier.update({initial: data2[initial].values[i]})
                self.reached.update({initial: [None, data2[initial].values[i]]})
        
        # this linked list will be used to follow the jumps on the frontier
        curr = LinkedList()
        curr.head = Node(initial)
        
        while len(self.frontier) > 0:
            # find min cost for path
            # here I could use a priority queue
            # this could be seen as a priority queue since it still finds the min cost state and pops it
            currmin = float('inf')
            stateMin = ''
            for state in self.frontier:
                if self.frontier[state] < currmin:
                    currmin = self.frontier[state]
                    stateMin = state
            
           
            
            self.frontier.pop(stateMin) # get rid of the value 
            
            # attach the state with lowest cost from the frontier to the linked list as a new node   
            if(curr.head.value != stateMin):
                temp = curr.head
                curr.head = Node(stateMin)
                curr.head.parent = temp
            
            # if we've reached the goal state, call countTotalCost to do the stats
            # and return the reached goal state    
            if curr.head.value == goal:
                self.countTotalCost(initial, goal, drivingInfo) 
                return curr.head.value
            
            # expand from the last state with min cost    
            self.expand(curr.head.value, goal, drivingInfo, straightInfo)
            # increment value of expanded states by 1 for each state that we expanded
            self.expanedNodes += 1
            
        # if final node wasn't reached, return None     
        return None

    def expand(self, currName, goal, drivingInfo, straightInfo):
        # Use the data from the csv files
        data = pd.read_csv(drivingInfo, usecols = ['STATE', currName])
        data2 = pd.read_csv(straightInfo, usecols = ['STATE', goal])
        
        # find all of the neighboring states of the currName node, which is the current minimum cost state
        for i in range(len(data[currName].values)):
            if(int(data[currName].values[i]) != -1 and data['STATE'].values[i] != currName):         
                # if the expanded states are not reached, add them to the frontier and to the reached    
                if(data['STATE'].values[i] not in self.reached):
                    self.reached.update({data2['STATE'].values[i]: [currName , data2[goal].values[i]]})
                    self.frontier.update({data2['STATE'].values[i]: data2[goal].values[i]})
                    
                # if the current expanded state is in reached but its current total cost is lower than the one
                # we have in the reached list, swap their values
                # i.e. put the new cost and change the parent of this state/node
                elif(data['STATE'].values[i] in self.reached) and (data2[goal].values[i] < self.reached[data['STATE'].values[i]][1]):
                    self.reached[data['STATE'].values[i]][1] = data2[goal].values[i]
                    self.reached[data['STATE'].values[i]][0] = currName
                    self.frontier.update({data2['STATE'].values[i]: data2[goal].values[i]})
    
    # function for the statistics            
    def countTotalCost(self, initial, goal, drivingInfo):
        last = goal
        while(self.reached[last][0] != None):
            data = pd.read_csv(drivingInfo, usecols = ['STATE', last])
            for i in range(len(data[last].values)):
                if(data['STATE'].values[i] == self.reached[last][0]):
                    # add the cost of the parent node to curr node;
                    # I do this to calculate total cost
                    self.totalCost += data[last].values[i]
            # append the state to the solution path
            self.solutionPath.append(last)
            # move onto next node/state
            last = self.reached[last][0]
        
        # add the last node/state to solution path
        self.solutionPath.append(initial)
        # reverse it so it can be in the correct order (from initial to goal state)
        self.solutionPath.reverse()
    
    # here I could have used other function but this one works;
    # it returns the time it takes for aStar to start and finish 
    def calculateTime(self, initial, goal, drivingInfo, straightInfo):
        self.start_time = time.time()
        a = self.best_first_search(initial, goal, drivingInfo, straightInfo)
        self.start_time = time.time() - self.start_time
        if(a == None):
            return None
        else:
            return a