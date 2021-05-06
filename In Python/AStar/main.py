__author__ = "Mohamed Ashraf"

from tkinter import *
import graph as g
import AStar
import GUI

graph = g.graph
heuristic = g.heuristic
start = g.start
goal = g.goal
cost = g.cost
visited_nodes, path, total_costs = AStar.run(graph, heuristic, cost, g.start,g.goal)

print("Path: " + str(path))
print("Total Cost: " + str(total_costs[0]))


def run():
    GUI.GUIrun(start, goal, graph, heuristic, path,
               total_costs, cost, startSelection, goalSelection)
    

root = Tk(className="A* Algorithm")
startSelection = StringVar(root)
startSelection.set(g.start)  # default value

goalSelection = StringVar(root)
goalSelection.set(g.goal)  # default value

root.geometry("300x300")

theLabel = Label(root, text="A* Algorithm")
theLabel.pack()

theLabel = Label(root, text="Start:")
theLabel.pack()
w = OptionMenu(root, startSelection, *list(g.graph.keys()))
w.pack()
theLabel = Label(root, text="Goal:")
theLabel.pack()
w = OptionMenu(root, goalSelection, *list(g.graph.keys()))
w.pack()

button = Button(root, text="Go!", command=run)
button.pack()


root.mainloop()
