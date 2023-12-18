import sys
from BestFirst_A20464521 import BestFirst
from AStar_A20464521 import AStar
from NormalBest import NormalBest

def main():
    srch = BestFirst()
    srchStar = AStar()
    
    # CSV Files that are going to be used 
    drivingInfo = "driving.csv"
    straightInfo = "straightline.csv"
    
    # Get argument values
    if len(sys.argv) == 3:
        initial = sys.argv[1]
        goal = sys.argv[2]
    else:
        print('ERROR: Not enough or too many input arguments.')
        exit()
    
    print('Petkov, Kamen, A20464521 solution: \n',
        'Initial state: ', initial,
        'Goal State: ', goal,
        '\n\n')

    
    # call GBFS 
    if(srch.calculateTime(initial, goal, drivingInfo, straightInfo) != None):
        print('Greedy Best First Search: \n',
            'Solution path: ', *srch.solutionPath, sep = " ")
        print(
            '\n',
            'Number of states on a path: ', len(srch.solutionPath),
            '\n',
            'Number of expanded nodes: ', srch.expanedNodes, 
            '\n',
            'Path cost: ', srch.totalCost,
            '\n',
            'Execution time: ', srch.start_time,
            '\n')   
        
    else:
        print('Solution path: FAILURE: NO PATH FOUND\n', 
        'Number of states on a path: 0\n',
        'Path cost: 0\n', srch.totalCost,
        'Execution time: ', srch.start_time, '\n')
        
    # counter = 0
    # for i in range(10):
    #     srchStar = AStar()
    #     srchStar.calculateTime(initial, goal, drivingInfo, straightInfo)
    #     print(srchStar.start_time)
    #     counter += srchStar.start_time
    # print('\n')
    # print(counter/10)
    # print('\n')
    
    # call A* Search
    if(srchStar.calculateTime(initial, goal, drivingInfo, straightInfo) != None):
        print('A* Search: \n',
            'Solution path: ', *srchStar.solutionPath, sep = " ")
        print(
            '\n',
            'Number of states on a path: ', len(srchStar.solutionPath),
            '\n',
            'Number of expanded nodes: ', srchStar.expanedNodes, 
            '\n',
            'Path cost: ', srchStar.totalCost,
            '\n',
            'Execution time: ', srchStar.start_time,
            '\n')   

    else:
        print('Solution path: FAILURE: NO PATH FOUND\n', 
        'Number of states on a path: 0\n',
        'Path cost: 0\n', srchStar.totalCost,
        'Execution time: ', srchStar.start_time , '\n')
        
    # counter2 = 0
    # for i in range(10):
    #     srch = BestFirst()
    #     srch.calculateTime(initial, goal, drivingInfo, straightInfo)
    #     print(srch.start_time)
    #     counter2 += srch.start_time
    # print('\n')
    # print(counter2/10)
    # print('\n')
        
if __name__ == "__main__":
    main()


