def checkmate(board: str):
    board = board.split("\n")  # Split board into rows
    size = len(board)  # Determine board size


    king_pos = None
    for r in range(size):
        for c in range(size):
            if board[r][c] == 'K':
                king_pos = (r, c)
                break
        if king_pos:
            break

    if not king_pos:
        return  # No King found, return without output

    kx, ky = king_pos


    directions = {
        'R': [(0, 1), (0, -1), (1, 0), (-1, 0)],  # Rook directions
        'B': [(1, 1), (1, -1), (-1, 1), (-1, -1)],  # Bishop directions
        'Q': [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)],  # Queen directions
    }


    for piece, moves in directions.items():
        for dx, dy in moves:
            x, y = kx + dx, ky + dy
            while 0 <= x < size and 0 <= y < size:
                if board[x][y] == piece:
                    print("Success")
                    return
                elif board[x][y] != '.':  # Blocked by another piece
                    break
                x += dx
                y += dy


    for dx, dy in [(-1, -1), (-1, 1)]:  # Pawns attack diagonally
        x, y = kx + dx, ky + dy
        if 0 <= x < size and 0 <= y < size and board[x][y] == 'P':
            print("Success")
            return

    print("Fail")  # King is safe