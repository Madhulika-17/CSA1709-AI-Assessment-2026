from queue import PriorityQueue

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

def heuristic(state):
    h = 0
    for i in range(9):
        if state[i] != 0:
            x1, y1 = divmod(i, 3)
            x2, y2 = divmod(state[i]-1, 3)
            h += abs(x1-x2) + abs(y1-y2)
    return h

def successors(state):
    moves = []
    i = state.index(0)
    r, c = divmod(i, 3)

    directions = [(-1,0),(1,0),(0,-1),(0,1)]

    for dr, dc in directions:
        nr, nc = r+dr, c+dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            ni = nr*3 + nc
            new = list(state)
            new[i], new[ni] = new[ni], new[i]
            moves.append(tuple(new))

    return moves

def solve(start):
    pq = PriorityQueue()
    pq.put((heuristic(start), 0, start, [start]))
    visited = set()

    while not pq.empty():
        f, g, state, path = pq.get()

        if state == goal:
            return path

        if state in visited:
            continue

        visited.add(state)

        for nxt in successors(state):
            if nxt not in visited:
                pq.put((g+1+heuristic(nxt), g+1, nxt, path+[nxt]))

    return None

start = (1, 2, 3,
         5, 6, 0,
         7, 8, 4)

solution = solve(start)

if solution:
    print("Solution Path:\n")
    for state in solution:
        for i in range(0, 9, 3):
            print(state[i], state[i+1], state[i+2])
        print()
else:
    print("No Solution")
