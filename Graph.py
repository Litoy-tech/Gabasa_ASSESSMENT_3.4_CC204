from collections import deque


class Graph:
    def __init__(self, labels):
        self.labels = labels
        self.adj = [[] for _ in labels]  # adjacency list

    def add_edge(self, source, target):
        self.adj[source].append(target)  # directed edge

    # Breadth-First Search (level by level, uses a queue)
    def bfs(self, start):
        visited = [False] * len(self.labels)
        queue = deque()
        result = []

        visited[start] = True
        queue.append(start)

        while queue:
            current = queue.popleft()
            result.append(self.labels[current])

            for neighbor in self.adj[current]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

        return result

    # Depth-First Search (go deep first, uses recursion)
    def dfs(self, start):
        visited = [False] * len(self.labels)
        result = []
        self._dfs_visit(start, visited, result)
        return result

    def _dfs_visit(self, node, visited, result):
        visited[node] = True
        result.append(self.labels[node])

        for neighbor in self.adj[node]:
            if not visited[neighbor]:
                self._dfs_visit(neighbor, visited, result)


def build_graph():
    # index: 0=A0, 1=A1, 2=S, 3=B, 4=G, 5=A2
    g = Graph(["A", "A", "S", "B", "G", "A"])
    g.add_edge(0, 1)  # A0 -> A1
    g.add_edge(0, 2)  # A0 -> S
    g.add_edge(0, 3)  # A0 -> B
    g.add_edge(2, 4)  # S  -> G
    g.add_edge(4, 3)  # G  -> B
    g.add_edge(3, 5)  # B  -> A2
    return g


if __name__ == "__main__":
    print("GABASA, ANGELITO L.| BSIT 2B")
    input("Please press enter to continue...")
    graph = build_graph()

    print("\n------------------------------------")
    print("Graph Traversal (start at A0)")
    print("BFS:", " - ".join(graph.bfs(0)))
    print("DFS:", " - ".join(graph.dfs(0)))
    print("------------------------------------")