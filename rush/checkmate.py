def checkmate(board: str):
    board = board.split("\n")  
    size = len(board)  
    row_length = len(board[0])
    for i, row in enumerate(board, start=1):
        if len(row) != row_length:
            print(f"Error: In line {i} don,t match with ({len(row)} letters)")
            return False
        
    
    king_positions = []
    for r in range(size):
        for c in range(size):
            if board[r][c] == 'K':
                king_positions.append((r, c))

   
    if len(king_positions) == 0:
        print("No King")
        return
    elif len(king_positions) > 1:
        print("Many King")
        return

    kx, ky = king_positions[0]

    
    directions = {
        'R': [(0, 1), (0, -1), (1, 0), (-1, 0)],  
        'B': [(1, 1), (1, -1), (-1, 1), (-1, -1)],  
        'Q': [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)],  
    }

    


    for piece, moves in directions.items():
        for dx, dy in moves:
            x, y = kx + dx, ky + dy
            while 0 <= x < size and 0 <= y < size:
                if board[x][y] == piece:
                    print("Success")
                    return
                elif board[x][y] != '.': 
                    break
                x += dx
                y += dy

    print("Fail")