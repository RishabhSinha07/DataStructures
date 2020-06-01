from collections import defaultdict

class  Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self,u,v):
        # unidirectional
        self.graph[u].append(v)

    def BFS(self, s):
        queue = []
        visited = [False]*len(self.graph)
        queue.append(s)
        visited[s] = True

        while queue:
            s = queue.pop(0)
            print(s,end = "")

            for val in self.graph[s]:
                if not visited[val]:
                    queue.append(val)
                    visited[val] = True

if __name__ == "__main__":
    g = Graph()
    g.add_edge(0,1)
    g.add_edge(0,2)
    g.add_edge(1,2)
    g.add_edge(2,0)
    g.add_edge(2,3)
    g.add_edge(3,3)

    # 0->1->2
    # 1->2
    # 2->0

    g.BFS(1)