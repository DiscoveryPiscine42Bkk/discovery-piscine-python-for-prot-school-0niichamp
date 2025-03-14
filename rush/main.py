from checkmate import checkmate

def main(): #v จากบ้าน
    board = """\
.R...
.P...
..K..
.....\
"""
    checkmate(board)

if __name__ == "__main__":
    main()

# B = Bishop ตามเส้นเฉียง 
# R = Rook ตั้งหรือนอนเท่านั้น
# Q = Queen รอบๆจนสุดทุกทิศทาง
# P = Pawn เฉียงขึ้นเท่านั้น
    
# K = King ก็คิง(ศัตรูเป็นเพียงหนึ่งเดียว)