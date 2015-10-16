from browser import document, svg
import random

"""
def hello(ev):
	document['helloText'].clear()
	document['helloText'] <= 'Hello, world!'
	print('Hello, world!')
"""

def addTile(board):
    tiles = getNumFreeTiles(board)
    tile = random.randint(1, tiles)
    for x in range(0, 4):
        for y in range(0, 4):
            if(board[x][y] == 0):
                tile -= 1
            
            if(tile == 0):
                board[x][y] = 2
                return board

def getNumFreeTiles(board):
    tiles = 0
    for x in range(0, 4):
        for y in range(0, 4):
            if( board[x][y] == 0 ):
                tiles += 1
    return tiles

def updateBoard(board, direction):
    if(direction == "up"):
        for x in range(0, 4):
            board[x] = slide(board[x])
            board[x] = smash(board[x])
            board[x] = slide(board[x])
            
    elif(direction == "down"):
        for x in range(0, 4):
            rev = list(reversed(board[x]))
            rev = slide(rev)
            rev = smash(rev)
            rev = slide(rev)
            board[x] = list(reversed(rev))
            
    elif(direction == "left"):
        for y in range(0, 4):
            newValues = slide([ board[0][y], board[1][y], board[2][y], board[3][y] ])
            newValues = smash(newValues)
            newValues = slide(newValues)
            for x in range(0, 4):
                board[x][y] = newValues[x]
            
    elif(direction == "right"):
        for y in range(0, 4):
            newValues = slide([ board[3][y], board[2][y], board[1][y], board[0][y] ])
            newValues = smash(newValues)
            newValues = slide(newValues)
            for x in range(0, 4):
                board[x][y] = newValues[3-x]
    
    return board

#add tiles as appropriate
def smash(leest):
    for i in range(0, len(leest)-1):
        if(leest[i] == leest[i+1]):
            leest[i:i+2] = [leest[i] * 2, 0]
    return leest

#bring all the tiles together
def slide(leest):
    newleest = []
    for i in leest:
        if(i != 0):
            newleest.append(i)
    while(len(leest) > len(newleest)):
        newleest.append(0)
    return newleest

#should only be called once, when you first build the background
def drawBG():
    pane = document["background"]
    
    #pane.clear()
    
    panelSide = 620
    bg = svg.rect(x=0, y=0, rx=5, ry=5, width=panelSide, height=panelSide,
                  fill="#EEEEEE")
    pane <= bg
    
    halfWay = 300
    triangleHalfWidth = 30
    triangleTop = 5
    triangleBottom = 28
    upTriangle = svg.polygon(points = str(halfWay)+","+str(triangleTop)+" "+
                             str(halfWay+triangleHalfWidth)+","+str(triangleBottom)+" "+
                             str(halfWay-triangleHalfWidth)+","+str(triangleBottom),
                             fill = "blue", id="upButton")
    downTriangle = svg.polygon(points = str(halfWay)+","+str(panelSide-triangleTop)+" "+
                             str(halfWay+triangleHalfWidth)+","+str(panelSide-triangleBottom)+" "+
                             str(halfWay-triangleHalfWidth)+","+str(panelSide-triangleBottom),
                             fill = "blue", id="downButton")
    leftTriangle = svg.polygon(points = str(triangleTop)+","+str(halfWay)+" "+
                               str(triangleBottom)+","+str(halfWay+triangleHalfWidth)+" "+
                               str(triangleBottom)+","+str(halfWay-triangleHalfWidth),
                               fill="blue", id="leftButton")
    rightTriangle = svg.polygon(points = str(panelSide-triangleTop)+","+str(halfWay)+" "+
                                str(panelSide-triangleBottom)+","+str(halfWay+triangleHalfWidth)+" "+
                                str(panelSide-triangleBottom)+","+str(halfWay-triangleHalfWidth),
                                fill="blue", id="rightButton")
    
    pane <= upTriangle
    pane <= downTriangle
    pane <= leftTriangle
    pane <= rightTriangle
    

def drawBoard(tiles):
    margin = 20
    tileSide = 120
    border = 20
    panel = document["board"]
    panel.clear()
    
    panelSide = 620
    
    
    
    
    for x in range(0, 4):
        xpos = margin + (margin * x) + (tileSide * x) + border
        for y in range(0, 4):
            ypos = margin + (margin * y) + (tileSide * y) + border
            rect = svg.rect(x=xpos, y=ypos, rx="5", ry="5", width=tileSide,
                            height=tileSide, fill="#444444")
            panel <= rect
            if(tiles[x][y] != 0):
                textX = xpos + (tileSide/2)
                textY = ypos + (tileSide/2) + (margin/2)
                tile = svg.text(str(tiles[x][y]), x=textX, y=textY, font_size=40,
                                 text_anchor="middle", fill="white")
                panel <= tile

def goUp(ev):
    board = updateBoard(board, "up")
    addTile(board)
    drawBoard(board)
    #print("done!")

def goDown(ev):
    board = updateBoard(board, "down")
    addTile(board)
    drawBoard(board)
    #print("done!")

def goLeft(ev):
    board = updateBoard(board, "left")
    addTile(board)
    drawBoard(board)

def goRight(ev):
    board = updateBoard(board, "right")
    addTile(board)
    drawBoard(board)

board = [[0, 0, 2, 0], [0, 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
drawBG()
drawBoard(board)

document['upButton'].bind('click', goUp)
document['downButton'].bind('click', goDown)
document['leftButton'].bind('click', goLeft)
document['rightButton'].bind('click', goRight)