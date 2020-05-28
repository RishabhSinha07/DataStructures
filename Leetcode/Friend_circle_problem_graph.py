from collections import defaultdict


class Solution:

    def get_graph(self, M, Nrows, Ncols):
        graph = defaultdict(list)
        for i in range(Nrows):
            for j in range(Ncols):
                if M[i][j]:
                    graph[i].append(j)
        return graph

    def dfs(self, i, graph, visited):
        visited[i] = True
        vertices = graph[i]
        for val in vertices:
            if not visited[val]:
                self.dfs(val, graph, visited)

    def findCircleNum(self, M) -> int:
        Nrows, Ncols, count = len(M), len(M), 0
        visited = [False] * Nrows
        graph = self.get_graph(M, Nrows, Ncols)
        for i in range(len(graph)):
            if not visited[i]:
                self.dfs(i, graph, visited)
                count += 1
        return count
