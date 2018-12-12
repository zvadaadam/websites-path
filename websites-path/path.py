import queue as q

from websites import get_all_links

class WebPath(object):

    def __init__(self):
        pass


    def get_shortest_path(self, from_url, to_url):

        return self.bfs(from_url, to_url)

    def bfs(self, from_node, to_node):

        open = q.Queue()

        closed = set()

        predecessors = {}

        open.put(from_node)

        while not open.empty():

            cur_node = open.get()

            print(f'{cur_node}, {to_node}')
            if cur_node == to_node:
                path = self.backtrace(predecessors, from_node, to_node)
                return path

            adj_nodes = get_all_links(cur_node)

            for adj_node in adj_nodes:

                if adj_node not in closed:

                    open.put(adj_node)

                    predecessors[adj_node] = cur_node

            closed.add(cur_node)

        return None

    def backtrace(self, predecessors, from_node, to_node):

        if from_node == to_node:
            return [from_node]

        pred = predecessors[to_node]

        path = self.backtrace(predecessors, from_node, pred)

        path.append(to_node)

        return path



if __name__ == '__main__':

    path = WebPath()

    print(path.get_shortest_path('https://fit.cvut.cz/', 'https://mit.edu/'))