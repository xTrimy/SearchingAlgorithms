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
                queue.append([(p[0] + cost[(p[1], graph[p[1]][i])]) * -1, graph[p[1]][i]])

        # mark as visited
        visited[p[1]] = 1

    return ans


if __name__ == '__main__':
    # create the graph
    graph = [[] for i in range(8)]
    cost = {}

    graph[0].append(1)
    graph[0].append(3)
    graph[3].append(1)
    graph[3].append(6)
    graph[3].append(4)
    graph[1].append(6)
    graph[4].append(2)
    graph[4].append(5)
    graph[2].append(1)
    graph[5].append(2)
    graph[5].append(6)
    graph[6].append(4)

    cost[(0, 1)] = 2
    cost[(0, 3)] = 5
    cost[(1, 6)] = 1
    cost[(3, 1)] = 5
    cost[(3, 6)] = 6
    cost[(3, 4)] = 2
    cost[(2, 1)] = 4
    cost[(4, 2)] = 4
    cost[(4, 5)] = 3
    cost[(5, 2)] = 6
    cost[(5, 6)] = 3
    cost[(6, 4)] = 7
    # goal state
    for i in cost:
        print(i, " =  ", cost[i])

    goal = []

    goal.append(6)

    answer = ucs(goal, 0)

    print("Minimum cost from 0 to G is = ", answer[0])
    print(graph)

