from tkinter import *
import GUI
#####################################
import graph as g
import DFS

graph = g.graph
heuristic = g.heuristic
start = g.start
goal = g.goal

path, total_cost = DFS.run(graph, start, goal)

print("Path: " + str(path))
print("Total Cost:" + str(total_cost))

def run():
    GUI.GUIrun(start, goal, graph, heuristic, path,
               total_cost, startSelection, goalSelection)


root = Tk(className="DFS Algorithm")
startSelection = StringVar(root)
startSelection.set(g.start)  # default value

goalSelection = StringVar(root)
goalSelection.set(g.goal)  # default value

root.geometry("300x300")

theLabel = Label(root, text="DFS Algorithm")
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

