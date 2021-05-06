

start = 'Arad'
goal = 'Bucharest'

graph = {
    'Arad': [['Zerind', 75], ['Timisoara', 118], ['Sibiu', 140]],
    'Zerind': [['Arad', 75], ['Oradea', 71]],
    'Timisoara': [['Arad', 118], ['Lugoj', 111]],
    'Lugoj': [['Timisoara', 111], ['Mehadia', 70]],
    'Sibiu': [['Oradea',151], ['Arad',140],['Fagaras',99], ['RimnicuVilcea',80]],
    'RimnicuVilcea': [['Craiova', 146],  ['Pitesti', 97], ['Sibiu', 80]],
    'Oradea': [['Zerind',71], ['Sibiu',151]],
    'Mehadia': [['Lugoj',70], ['Dobreta',75]],
    'Craiova': [['Dobreta',120], ['RimnicuVilcea',146], ['Pitesti',138]],
    'Pitesti': [['RimnicuVilcea', 97], ['Craiova', 138], ['Pitesti', 101]],
    'Fagaras': [['Bucharest', 211], ['Sibiu',99]],
    'Dobreta': [['Craiova', 120], ['Mehadia',75]],
    'Bucharest': [['Pitesti', 101], ['Giurgiu', 90], ['Fagaras', 211]],
    'Giurgiu': [['Bucharest', 90]]
}

heuristic = {'Arad': 366, 'Bucharest': 0, 'Craiova': 160, 'Dobreta': 242, 'Zerind': 374, 'Timisoara': 326, 'Lugoj': 244, 'Sibiu':253,
             'RimnicuVilcea': 193, 'Oradea': 380, 'Mehadia': 241, 'Pitesti': 98, 'Fagaras': 178, 'Giurgiu': 77}
cost = {start: 0}
def chooseStart():
    global start, cost
    start = input('Enter start node from the list:')
    cost = {start: 0}

def chooseGoal():
    global goal
    goal = input('Enter goal node from the list:')

def run():
    for k , v in heuristic.items():
        print(k)

    chooseStart()
    chooseGoal()
