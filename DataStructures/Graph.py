#We import the LinkedList Class we had already created
from LinkedList import LinkedList


class GraphNode:
    def __init__(self, data):
        self.data = data
        self.adjacent = []

    def addAdjacent(self, adjacent):
        self.adjacent.append(adjacent)

    def addAdjacents(self, adjacents):
        for adjacent in adjacents:
            self.adjacent.append(adjacent)

    def getAdjacents(self):
        return self.adjacent

    def addEdge(self, source, destination):
        s = self.getNodeDFS(source, set())
        d = self.getNodeDFS(destination, set())
        s.addAdjacent(d)

    def hasPathDFS(self, source, destination):
        s = self.getNodeDFS(source, set())
        return not s.getNodeDFS(destination, set()) is None

    def hasPathBFS(self, source, destination):
        s = self.getNodeDFS(source, set())
        return not s.getNodeBFS(destination) is None

    def addNode(self, source, destination):
        s = self.getNodeDFS(source, set())
        s.addAdjacent(GraphNode(destination))

    def getNodeDFS(self, data, checked):
        if not self.data in checked:
            if self.data == data:
                return self

            checked.add(self.data)
            for node in self.adjacent:
                checkedNode = node.getNodeDFS(data, checked)
                if not checkedNode is None:
                    return checkedNode

    def getNodeBFS(self, destination):
        nextToVisit = LinkedList()
        visited = set()
        nextToVisit.append(self)
        while not nextToVisit.head is None:
            node = nextToVisit.remove()
            if node.data == destination:
                return node

            if node.data in visited:
                continue

            visited.add(node.data)
            for child in node.getAdjacents():
                nextToVisit.append(child)

        return None


root = GraphNode(55)
root.addAdjacents([GraphNode(10), GraphNode(20), GraphNode(30)])
root.addNode(10, 50)
root.addEdge(20, 50)
print(root.hasPathDFS(20, 50))
print(root.hasPathBFS(10, 50))
print(root.hasPathDFS(20, 30))
print(root.hasPathBFS(20, 30))
