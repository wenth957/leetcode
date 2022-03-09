from collections import deque


'''实现图'''

graph = {}

graph["you"] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['jonny'] = []
graph['thom'] = []


def person_is_seller(name):
    return name[-1] == "m"


def search(name):
    search_queue = deque()
    search_queue += graph[name]  # 将图添加到队列中
    searched = []  # 记录查找过的

    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(f"{person} is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                # 二度关系中寻找
                searched.append(person)
    return False


search('you')
