import unittest

# Up, down, left, right
NEIGHBOURS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(E, A, start):
    # Set starting coordinate as the new front
    new_front = [start]
    E[start[0]][start[1]] = 1

    # Add all unexplored neighbours of the current front to the new front
    # Mark added neighbours as explored tiles
    # Do until there are unexplored neighbours
    while len(new_front) > 0:
        front = new_front
        #print(front)
        new_front = []
        for i, j in front:
            for x, y in NEIGHBOURS:
                #print(f'Search neighbour: {i+x} {j+y}')
                # Check border, explored and color)
                if (i+x >= 0 and i+x < len(A) and
                    j+y >= 0 and j+y < len(A[0]) and
                    A[i+x][j+y] == A[i][j] and
                    E[i+x][j+y] == 0):
                    #print(f'Valid neighbour: {i+x} {j+y}')
                    # Add neighbor tile to new front
                    new_front.append((i+x, j+y))
                    # Mark as explored
                    E[i+x][j+y] = 1

    return
            

def solution(A):
    # Make an A-shaped matrix to store explored tiles
    E = [[0]*len(A[0]) for i in range(len(A))]

    # Count countries
    countries = 0

    # Walk through each tile
    for i in range(len(A)):
        for j in range(len(A[0])):
            # Check if tile has been marked as explored yet
            #print(f'Current Tile: {i} {j}')
            if E[i][j] == 0:
                #print(f'New country at: {i} {j}')
                # If it hasn't, a new country has been found
                countries += 1
                # Start a breadth-first search and mark all tiles as the same country
                bfs(E, A, (i, j))

            #print(i, j, countries)

    return countries
