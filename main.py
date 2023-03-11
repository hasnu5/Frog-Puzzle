from collections import deque

dictionary1 = []
dictionary_1 = []

def PossibleMoves(node):
    possiblemoves = []
    length = len(node)
    index = 0
    while index < length:
        num = char(node[index])
        if(num == 1):
            hop = index + 2
            slide = index + 1
        elif(num == -1):
            hop = index - 2
            slide = index - 1
        if (num != 0):
            if (not ((hop < 0) or (hop >= len(node)))):
                if (node[hop] == ' '):
                    newmove = list(node)
                    newmove[index] = ' '
                    newmove[hop] = node[index]
                    possiblemoves.append(newmove)
            if (not ((slide < 0) or (slide >= len(node)))):
                if (node[slide] == ' '):
                    newmove = list(node)
                    newmove[index] = ' '
                    newmove[slide] = node[index]
                    possiblemoves.append(newmove)

        index = index + 1
    return possiblemoves

def BFS(nodestart, nodeend):
    numeric(nodestart)
    visited = []
    queue = deque()
    queue.append([nodestart])

    while queue:

        allmoves = queue.popleft()
        node = allmoves[-1]
        if node not in visited:
            moves = PossibleMoves(node)

            for move in moves:
                winmoves = list(allmoves)
                winmoves.append(move)
                queue.append(winmoves)

                if move == nodeend:
                    return winmoves

            visited.append(node)

    return "We can't win this game"

def DFS(start, end):

    numeric(start)
    visited = []

    stack = deque()
    stack.append([start])

    while stack:

        allmoves = stack.pop()

        node = allmoves[-1]
        if node not in visited:
            moves = PossibleMoves(node)

            for move in moves:
                winmoves = list(allmoves)
                winmoves.append(move)
                stack.append(winmoves)

                if move == end:
                    return winmoves

            visited.append(node)

    return "We can't win this game"

def DLS(start, end, maxDepth, moves, explored):

    moves.append(start)
    if start == end:
        print(list(moves))
        return True


    if maxDepth <= 0:
        return False

    if start not in explored:
        explored.append(start)
        for i in PossibleMoves(start):
            if (DLS(i, end, maxDepth - 1, moves, explored)):
                return True
            moves.pop()


    return False

def IDS(start, end):
    x = -1
    y = 0
    i = 0
    numeric(start)
    moves = deque()
    explored = []
    while x < y:
        moves.clear()
        explored.clear()
        if (DLS(start, end, i, moves, explored)):
            return True
        i = i + 1

    return False

def numeric(start):
    i = 0
    while i < len(start):
        if(i < (len(start)/2)-0.5):
            dictionary1.append(start[i])
        if(i > (len(start)/2)):
            dictionary_1.append(start[i])
        i = i + 1

def char(char):
    if char in dictionary1:
        return 1
    elif char in dictionary_1:
        return -1
    else:
        return 0

start = ['A', 'B', 'C', ' ','X', 'Y', 'Z']
end = ['X', 'Y', 'Z', ' ', 'A', 'B', 'C']

print('For DFS', DFS(start, end))
print('For BFS', BFS(start, end))
print('For IDS')
IDS(start, end)
