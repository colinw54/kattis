
#board is a string of length 12

uniqueStates = {}
def dp(board):
    if board in uniqueStates:
        return uniqueStates[board]
    
    moves = []
    for i in range(10):
        #If the window contains 2 pebbles and a space, add to moves
        window = board[i:i+3]
        if window == "oo-":
            moves.append(board[0:i] + "--o" + board[i+3:])
        elif window == "-oo":
            moves.append(board[0:i] + "o--" + board[i+3:])

    if not moves:
        count = board.count("o")
        uniqueStates[board] = count
        return count 
    else: 
        count = min([dp(move) for move in moves])
        uniqueStates[board] = count
        return count
    
test = dp("oooooooooo-o")
print(test)