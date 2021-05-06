def run(graph, heuristic, cost, start, goal):
    start_cost = heuristic[start]
    closed = []
    opened = [[start, start_cost]]
    while True:
        fn = [i[1] for i in opened]
        smallest_index = fn.index(min(fn))
        node = opened[smallest_index][0]
        closed.append(opened[smallest_index])
        print("Unvisited:"+str(opened))
        print("Current Node:"+str(node))
        print("Visited: "+str(closed))
        print("")
        del opened[smallest_index]
        if closed[-1][0] == goal:
            break
        for item in graph[node]:
            if item[0] in [closed_item[0] for closed_item in closed]:
                continue
            cost.update({item[0]: cost[node] + item[1]})
            fn_node = cost[node] + heuristic[item[0]] + item[1]
            temp = [item[0], fn_node]
            opened.append(temp)
    trace_node = goal
    optimal_sequence = [goal]
    for i in range(len(closed)-2,-1,-1):
        check_node = closed[i][0]

        if trace_node in [children[0] for children in graph[check_node]]:
            children_costs = [temp[1] for temp in graph[check_node]]
            children_nodes = [temp[0] for temp in graph[check_node]]

            if cost[check_node] + children_costs[children_nodes.index(trace_node)] == cost[trace_node]:
                optimal_sequence.append(check_node)
                trace_node = check_node

    optimal_sequence.reverse()
    return closed, optimal_sequence
