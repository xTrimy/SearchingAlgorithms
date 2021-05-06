import graph as g
def ucs(goal, start):
    global graph, cost
    ans = []
    queue = []

    for i in range(len(goal)):
        ans.append(9999)  # ans = big value

    queue.append([0, start])

    # dict for visited
    visited = {}

    count = 0
    

    while (len(queue) > 0): # while not empty
        queue = sorted(queue)
        p = queue[-1] # last element in queue
        del queue[-1]
        p[0] *= -1
        
        if (p[1] in goal):
            # get the position
            index = goal.index(p[1])
            # if a new goal is reached
            if (ans[index] == 9999):
                count += 1
                
            # if the cost is less
            if (ans[index] > p[0]):
                ans[index] = p[0]
             
            # pop the element
            del queue[-1]

            queue = sorted(queue)
            if (count == len(goal)):
                return ans

        # check for the non visited nodes
        
        if (p[1] not in visited):
            for i in range(len(graph[p[1]])):
                # value is multiplied by -1 so that
                # least priority is at the top
                queue.append([(p[0] + graph[p[1]][i][1]) * -1, graph[p[1]][i][0]])
                # queue.append([(p[0] + cost[(p[1], graph[p[1]][i][1])]) * -1, graph[p[1]][i]])
        # mark as visited
        visited[p[1]] = 1
    

    return ans


if __name__ == '__main__':
    # g.chooseStart()
    # g.chooseGoal()
    start = g.start
    goal = [g.goal]

    # create the graph
    graph = g.graph

    cost = g.cost
    # goal state
    for i in cost:
        print(i, " =  ", cost[i])
    
    path = ucs(goal, start)

    print("Minimum cost from 0 to G is = ", path[0])

