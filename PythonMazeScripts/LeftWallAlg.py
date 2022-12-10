def RCW():
    global dire
    k = list(dire.keys())
    v = list(dire.values())
    v_rotated = [v[-1]] + v[:-1]

    dire = dict(zip(k, v_rotated))


def RCCW():
    global dire
    k = list(dire.keys())
    v = list(dire.values())
    v_rotated = v[1:] + [v[0]]
    dire = dict(zip(k, v_rotated))


def moveForward(cell):
    if dire['forward'] == 'E':
        return (cell[0], cell[1] + 1), 'E'
    if dire['forward'] == 'W':
        return (cell[0], cell[1] - 1), 'W'
    if dire['forward'] == 'N':
        return (cell[0]-1, cell[1]), 'N'
    if dire['forward'] == 'S':
        return (cell[0]+1, cell[1]), 'S'


def wallMover(m):
    global dire
    dire = {'forward': 'N', 'left': 'W', 'back': 'S', 'right': 'E'}
    currCell = (m.rows, m.cols)
    path = ''

    while True:
        if currCell == (1, 1):
            break
        if m.maze_map[currCell][dire['left']] == 0:
            if m.maze_map[currCell][dire['forward']] == 0:
                RCW()
            else:
                currCell, d = moveForward(currCell)
                path += d
        else:
            RCCW()
            currCell, d = moveForward(currCell)
            path += d
    return path


if __name__ == '__main__':
    print("x")

    loadMaze = False

    from pyamaze import maze, agent

    if loadMaze:
        Maze = maze(20, 20)
        Maze.CreateMaze(loadMaze='maze.csv', loopPercent=50)

        a = agent(Maze, footprints=True)
        path = wallMover(Maze)
        Maze.tracePath({a: path})

        Maze.run()
        print(Maze.maze_map)
    else:
        Maze = maze(20, 20)
        Maze.CreateMaze(loopPercent=50)

        a = agent(Maze, footprints=True)
        path = wallMover(Maze)
        Maze.tracePath({a: path})

        Maze.run()
        print(Maze.maze_map)