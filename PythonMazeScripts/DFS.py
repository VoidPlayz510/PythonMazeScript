import unittest

from pyamaze import maze, agent, COLOR


def DFS(m):
    """Creates a starting cell and an end cell and asks the maze obj to traverse the maze based on a
    preference of direction. Then will return the maze map to be loaded or saved."""
    # define variables
    currentCell = (0, 0)
    start = (m.rows, m.cols)
    explored = [start]
    frontier = [start]
    dfsPath = {}

    if start is None:
        start = (m.rows, m.cols)

    # found finish line
    while len(frontier) > 0:
        currentCell = frontier.pop()
        if currentCell == (1, 1):
            break
        # when following direction, move based on if allowed to go in an allocated way
        # using 'ESNW' as the directions of East, then South, then North and West.
        # This can be changed to such as 'WNSE' to have the maze traversed around the right sides

        for direction in 'WNSE':
            if m.maze_map[currentCell][direction]:
                if direction == 'E':
                    childCell = (currentCell[0], currentCell[1] + 1)
                elif direction == 'W':
                    childCell = (currentCell[0], currentCell[1] - 1)
                elif direction == 'S':
                    childCell = (currentCell[0] + 1, currentCell[1])
                elif direction == 'N':
                    childCell = (currentCell[0] - 1, currentCell[1])
                if childCell in explored:
                    continue
                explored.append(childCell)
                frontier.append(childCell)
                dfsPath[childCell] = currentCell
    fwdPath = {}
    cell = (1, 1)
    while cell != start:
        fwdPath[dfsPath[cell]] = cell
        cell = dfsPath[cell]
    return fwdPath


if __name__ == '__main__':
    # run a standard 20, 20 maze or run the maze in the file
    loadMaze = True

    if not loadMaze:
        m = maze(20, 20)
        m.CreateMaze(saveMaze=True)
        path = DFS(m)
        a = agent(m, footprints=True)
        m.tracePath({a: path}, delay=100, showMarked=True, kill=True)

        m.run()
    if loadMaze:
        m = maze()
        m.CreateMaze(loadMaze='maze.csv')
        path = DFS(m)
        a = agent(m, footprints=True)
        m.tracePath({a: path}, delay=100, showMarked=True, kill=True)

        m.run()


class TestPositionsMaze(unittest.TestCase):
    def test_startPos(self):
        """This test will ensure that the maze obj has started where it was expected to and compares the start variable
        with the start position of the object."""
        m = maze(5, 5)
        start = (m.rows, m.cols)

        m.CreateMaze(saveMaze=True)
        path = DFS(m)
        a = agent(m, footprints=True)
        self.assertEqual(a.position, start)
        print('start ' f'{start}', 'position' f'{a.position}')
        # m.tracePath({a: path}, delay=100, showMarked=True, kill=True)
        # Test maze


    def test_endPos(self):
        """This test like before however will now test for the end position of the maze and see if the obj
        has successfully traversed the maze. It will then return the end position of the maze and the maze obj."""
        m = maze(5, 5)
        end = (1, 1)

        m.CreateMaze(saveMaze=True)
        path = DFS(m)
        a = agent(m, footprints=True)
        m.tracePath({a: path}, delay=100, showMarked=True, kill=False)
        m.run()
        self.assertEqual(a.position, end)
        print(m.path)
        print('end ' f'{end}', 'position' f'{a.position}')

        # Test maze