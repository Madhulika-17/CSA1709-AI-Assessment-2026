from collections import deque

def water_jug():
    visited = set()
    queue = deque()

    start = (0, 0)
    goal = 2

    queue.append((start, [start]))
    visited.add(start)

    while queue:
        (a, b), path = queue.popleft()

        if a == goal or b == goal:
            return path

        next_states = [
            (4, b),                      # Fill 4L jug
            (a, 3),                      # Fill 3L jug
            (0, b),                      # Empty 4L jug
            (a, 0),                      # Empty 3L jug
            (max(0, a-(3-b)), min(3, b+a)),  # Pour 4L -> 3L
            (min(4, a+b), max(0, b-(4-a)))   # Pour 3L -> 4L
        ]

        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append((state, path + [state]))

path = water_jug()

print("Solution:")
for state in path:
    print(state)
