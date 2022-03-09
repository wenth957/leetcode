# 有向加权图
graph = {}
graph['start'] = {}  # 用散列表来储存权重
graph['start']['a'] = 6
graph['start']['b'] = 2
graph['a'] = {}
graph['a']['fin'] = 1
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5
graph['fin'] = {}
print(graph)
# 储存路径消耗/开销
infinity = float('inf')
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity
# 储存父节点
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None
# 记录处理过的结点
processed = []


def find_lowest_cost_node(costs):
    '''当前开销中，开销最小的结点'''
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)
'''
 1 获取离起点最近的结点
 2 更新其邻居的开销
 3 如果邻居开销有更新，更新其父节点
 4 该节点标记为处理过
'''
print(f"父节点：{parents}")
print(f"开销：{costs}")
