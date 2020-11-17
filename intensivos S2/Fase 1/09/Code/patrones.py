def t(mundo, x, y):
    mundo[x+1][y] = 1
    mundo[x][y-1] = 1
    mundo[x+1][y-1] = 1
    mundo[x+2][y-1] = 1

def r_pentomino(mundo, x, y):
    mundo[x+1][y] = 1
    mundo[x+2][y] = 1
    mundo[x][y+1] = 1
    mundo[x+1][y+1] = 1
    mundo[x+1][y+2] = 1

def glider(mundo ,x, y):
    mundo[x+1][y] = 1
    mundo[x+2][y+1] = 1
    mundo[x][y+2] = 1
    mundo[x+1][y+2] = 1
    mundo[x+2][y+2] = 1

def blinker(mundo, x, y):
    mundo[x][y] = 1
    mundo[x][y-1] = 1
    mundo[x][y-2] = 1