"""

You'll have to simulate the video game's character selection screen 
behaviour, more specifically the selection grid.

	Input

The list of game characters in a 2x6 grid;
the initial position of the selection cursor (top-left is (0,0));
a list of moves of the selection cursor (which are up, down, left, right).

	Output

The list of characters who have been hovered by the selection cursor
after all the moves.

Selection cursor is circular horizontally but not vertically!

As you might remember from the game, the selection cursor rotates
horizontally but not vertically; that means that if I'm in the leftmost
and I try to go left again I'll get to the rightmost (examples: from
Ryu to Vega, from Ken to M.Bison) and vice versa from rightmost to
leftmost.

Instead, if I try to go further up from the upmost or further down from
the downmost, I'll just stay where I am located.

"""

fighters = [
	["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"],
	["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"]
	]


def street_fighter_selection(fighters, initial_position, moves):
    
    x = 0
    y = 0
    
    fighterList = []
     
    for move in moves:
        if move == 'up' and x == 1:
            x -= 1
        elif move == 'down' and x != 1:
            x += 1            
        elif move == 'right' and y == 5:
            y = 0
        elif move == 'right' and y != 5:
            y += 1            
        elif move == 'left' and y == 0:
            y = 5
        elif move == 'left' and y != 0:
            y -= 1
                
        fighterList.append(fighters[x][y])
            
    return fighterList
      
"""
Optimal solution

def street_fighter_selection(fighters, initial_position, moves):
    y, x = initial_position
    hovered_fighters = []
    for move in moves:
        dy, dx = MOVES[move]
        y += dy
        if not 0 <= y < len(fighters):
            y -= dy
        x = (x + dx) % len(fighters[y])
        hovered_fighters.append(fighters[y][x])
    return hovered_fighters
"""
