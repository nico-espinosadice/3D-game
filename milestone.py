GlowScript 2.7 VPython
# Milestone.py
# Jacob van der Leeuw and Nico Espinosa Dice
# Final Project - VPython
# URL: http://www.glowscript.org/#/user/nespinosadice/folder/MyPrograms/program/Milestone

gameOver = False #changes to true if the user has caught all three chaseObjects
#or if the user has not caught all objects by the time
newLapPossible = False
newLapPossible_obj1 = True
newLapPossible_obj2 = True
newLapPossible_obj3 = True
lapCount = 1 # user starts on the first lap
lapLimit = 3
lapCount_obj1 = 1
lapCount_obj2 = 1
lapCount_obj3 = 1
points = 0
totalPointsPossible = 6 #1 point for slowest chaseObject, 2 for second chaseObject, and 3 for third chaseObject

easy_vel = [1, 3, 5] # creates velocity list for easier game
hard_vel = [3, 5, 7] # creates velocity list for more challenging game
game_difficulty = "easy" # sets default game_difficulty to easy

# +++ Start of SCENE SETUP +++ 
scene.bind('keydown', keydown_fun)     # Function for key presses
scene.background = 0.8*vector(1, 1, 1) # Light gray (0.8 out of 1.0)
scene.width = 640                      # Make the 3D canvas larger
scene.height = 480
# +++ End of SCENE SETUP +++ 

# +++ Start of TRACK CREATION +++
# Ground (represented by a box - vpython's rectangular solid)
ground = box(size = vector(20, 1, 20), pos = vector(0, -1, 0), color = .4*vector(1, 1, 1))
ground2 = box(size = vector(20, 1, 4), pos = vector(0, -1, 12), color = color.purple)

# Outer Walls
O_wallN = box(pos = vector(0, 0, -10), axis = vector(1, 0, 0), size = vector(20, 1, .2), color = color.blue) # "North" wall - red
O_wallW = box(pos = vector(-10, 0, 0), axis = vector(0, 0, 1), size = vector(20, 1, .2), color = color.blue) # "West" wall - blue
O_wallS = box(pos = vector(0, 0, 10), axis = vector(1, 0, 0), size = vector(16, 1, .2), color = color.yellow) # "South" wall - green
O_wallE = box(pos = vector(10, 0, 0), axis = vector(0, 0, 1), size = vector(20, 1, .2), color = color.blue) # "East" wall - yellow

# Inner Walls
# east walls
I_wallE = box(pos = vector(8, 0, 1), axis = vector(0, 0, 1), size = vector(18, 1, .2), color = color.red) # "East" wall - yellow
I_wallE2 = box(pos = vector(4, 0, -1), axis = vector(0, 0, 1), size = vector(18, 1, .2), color = color.green) # "East" wall - yellow

# center wall
I_wallC = box(pos = vector(0, 0, 1), axis = vector(0, 0, 1), size = vector(18, 1, .2), color = color.white) # "East" wall - yellow

# west walls
I_wallW = box(pos = vector(-8, 0, 1), axis = vector(0, 0, 1), size = vector(18, 1, .2), color = color.red) # "East" wall - yellow
I_wallW2 = box(pos = vector(-4, 0, -1), axis = vector(0, 0, 1), size = vector(18, 1, .2), color = color.green) # "East" wall - yellow
# +++ End of TRACK CREATION +++ 


# +++ Start of OBJECT CREATION +++ 
# Ball (user controls)
ball = sphere(pos = vector(9, 0, 9), size = 1.0*vector(1, 1, 1), color = vector(0.8, 0.5, 0.0))   # ball is an object of class sphere
ball.vel = vector(0, 0, 0)     # this is its initial velocity

# Chase Objects #1, 2, 3 (autonomous)
chaseObject1 = sphere(pos = vector(9.0, 0, -5.0), size = 0.5*vector(1,1,1), color = color.orange)
chaseObject2 = sphere(pos = vector(6.0, 0, 5.0), size = 0.5*vector(1,1,1), color = color.purple)
chaseObject3 = sphere(pos = vector(2.0, 0, 5.0), size = 0.5*vector(1,1,1), color = color.green)


# Obstacle 1 (moving object)
obstacle1 = box(pos = vector(-4, 0, 8.5), size = 0.5*vector(1, 1, 1), color = vector(1, 1, 1))   # ball is an object of class sphere
obstacle1.vel = vector(-5, 0, 0)     # this is its initial velocity

obstacle2_1 = box(pos = vector(3.4, 0, 3), size = 0.3*vector(1, 1, 1), color = vector(1, 1, 1))   # ball is an object of class sphere
obstacle2_1.vel = vector(-2, 0, 0)

obstacle2_2= box(pos = vector(2.4, 0, 0), size = 0.3*vector(1, 1, 1), color = vector(1, 1, 1))   # ball is an object of class sphere
obstacle2_2.vel = vector(-2, 0, 0)

obstacle2_3 = box(pos = vector(1.4, 0, -3), size = 0.3*vector(1, 1, 1), color = vector(1, 1, 1))   # ball is an object of class sphere
obstacle2_3.vel = vector(-2, 0, 0)

obstacle2_4 = box(pos = vector(0.4, 0, -6), size = 0.3*vector(1, 1, 1), color = vector(1, 1, 1))   # ball is an object of class sphere
obstacle2_4.vel = vector(-2, 0, 0)

obstacle2_5 = box(pos = vector(0.4, 0, 6), size = 0.3*vector(1, 1, 1), color = vector(1, 1, 1))   # ball is an object of class sphere
obstacle2_5.vel = vector(-2, 0, 0)

# Speed Section
speedSection = box(size = vector(2, 0.0001, 5), pos = vector(-6, 0, 4), color = color.blue) # speed boost section on track
# +++ End of OBJECT CREATION ++


# +++ Start of ANIMATION +++
# Constants
RATE = 30                # The number of times the while loop runs each second
dt = 1.0/(1.0*RATE)      # The time step each time through the while loop
scene.autoscale = False  # Avoids changing the view automatically
scene.forward = vector(0, -3, -2)  # Ask for a bird's-eye view of the scene...
# +++ End of ANIMATION +++

# +++ Start of GAME EXPLANATION to user +++ 
print("Objective: Capture the runaway spheres!")
print("How: Use the arrow keys to move the ball through the track (while avoiding the obstacles)!")
print("Tip: Use the space bar to slow down before turns.")
print("Press the 'e' key to start an easy level or the 'h' key to begin the harder level.")
print()
print("Lap", lapCount, "out of", lapLimit)
# +++ End of GAME EXPLANATION to user +++ 

# +++ Start of GAME LOOP +++ 
scene.waitfor('keydown') # wait for keyboard key press
gameOver = False # Keeps track of whether the game is over

# +++ Setting ChaseObject Velocity +++
if game_difficulty == "easy":
    chaseObject1.vel = vector(0,0,-1) #initial velocity for chaseObj1
    chaseObject2.vel = vector(0,0,3) #initial velocity for chaseObj2
    chaseObject3.vel = vector(0,0,-5) #initial velocity for chaseObj3
else:
    chaseObject1.vel = vector(0,0,-3) #initial velocity for chaseObj1
    chaseObject2.vel = vector(0,0,5) #initial velocity for chaseObj2
    chaseObject3.vel = vector(0,0,-7) #initial velocity for chaseObj3
# +++ End of ChaseObject Velocity +++

while not gameOver: # Each pass through the loop will animate one step in time (dt)
    if isLapLimitExceded(lapCount): # Checks to see if the lapLimit has been reached
        lapLimitReached()
        continue # Skips over the iteration of the while loop if the lapLimit has been reached

    if isLapLimitExceded(lapCount_obj1): # Checks to see if the lapLimit has been reached
        endGame()
        continue # Skips over the iteration of the while loop if the lapLimit has been reached

    rate(RATE)   # maximum number of times per second the while loop runs

    # +++ Start of PHYSICS UPDATES +++
    # Update all positions here (every time step)
    ball.pos = ball.pos + ball.vel*dt # Update the ball's position
    chaseObject1.pos = chaseObject1.pos + chaseObject1.vel*dt # Update chaseObject1's position
    chaseObject2.pos = chaseObject2.pos + chaseObject2.vel*dt # Update chaseObject2's position
    chaseObject3.pos = chaseObject3.pos + chaseObject3.vel*dt # Update chaseObject3's position
    obstacle1.pos = obstacle1.pos + obstacle1.vel*dt # Update obstacle1's position
    obstacle2_1.pos = obstacle2_1.pos + obstacle2_1.vel*dt # Update obstacle2_1's position
    obstacle2_2.pos = obstacle2_2.pos + obstacle2_2.vel*dt # Update obstacle2_2's position
    obstacle2_3.pos = obstacle2_3.pos + obstacle2_3.vel*dt # Update obstacle2_3's position
    obstacle2_4.pos = obstacle2_4.pos + obstacle2_4.vel*dt # Update obstacle2_4's position
    obstacle2_5.pos = obstacle2_5.pos + obstacle2_5.vel*dt # Update obstacle2_5's position
    # +++ End of PHYSICS UPDATES +++
    
    # +++ Start of EVENT CHECKING +++ 
    # Ball
    corral_collide(ball) # Checks to see if ball has collided with something
    speedSectionCollide(ball) # Checks to see if ball is in speed section

    # Chase Object
    chaseObject1.vel = chaseObject_Path(chaseObject1) #updates the velocities of the chaseObjects
    chaseObject2.vel = chaseObject_Path(chaseObject2)
    chaseObject3.vel = chaseObject_Path(chaseObject3)
    
    # Obstacles
    obstacle1Collide(obstacle1) # Checks to see if obstacle1 has collided with something
    
    obstacle2_1.vel = obstacle2Collide(obstacle2_1) # Checks to see if obstacle2_1 has collided with something
    obstacle2_2.vel = obstacle2Collide(obstacle2_2) # Checks to see if obstacle2_2 has collided with something
    obstacle2_3.vel = obstacle2Collide(obstacle2_3) # Checks to see if obstacle2_3 has collided with something
    obstacle2_4.vel = obstacle2Collide(obstacle2_4) # Checks to see if obstacle2_4 has collided with something
    obstacle2_5.vel = obstacle2Collide(obstacle2_5) # Checks to see if obstacle2_5 has collided with something

    # New Lap
    newLapPossible = newLapPossible_Collide(ball, newLapPossible)
    newLapPossible_obj1 = newLapPossible_Collide(chaseObject1, newLapPossible_obj1)
    newLapPossible_obj2 = newLapPossible_Collide(chaseObject2, newLapPossible_obj2)
    newLapPossible_obj3 = newLapPossible_Collide(chaseObject3, newLapPossible_obj3)
    newLap_Collide(ball)
    lapCount_obj1 = newLap_Collide_chaseObject(1, chaseObject1, newLapPossible_obj1, lapCount_obj1)
    lapCount_obj2 = newLap_Collide_chaseObject(2, chaseObject2, newLapPossible_obj2, lapCount_obj2)
    lapCount_obj3 = newLap_Collide_chaseObject(3, chaseObject3, newLapPossible_obj3, lapCount_obj3)
     # +++ End of EVENT CHECKING +++ 


# +++ start of EVENT_HANDLING section +++
# Separate functions for keypresses and mouse clicks
def keydown_fun(event):
    """This function is called each time a key is pressed."""  
    global game_difficulty

    ball.color = randcolor() # Randomize ball's color every time a key is pressed
    key = event.key
    
    amt = 0.9 # "Strength" of the keypress's velocity changes
    
    # If up key is pressed, accelerate ball in the -Z direction
    if key == 'up' or key in 'wWiI':
        ball.vel = ball.vel + vector(0, 0, -amt)
    
    # If left key is pressed, accelerate ball in the -X direction
    elif key == 'left' or key in 'aAjJ':
        ball.vel = ball.vel + vector(-amt, 0, 0)
    
    # If down key is pressed, accelerate ball in the +Z direction
    elif key == 'down' or key in 'sSkK':
        ball.vel = ball.vel + vector(0, 0, amt)
    
    # If right key is pressed, accelerate ball in the +X direction
    elif key == 'right' or key in "dDlL":
        ball.vel = ball.vel + vector(amt, 0, 0)
    
    # If spacebar is pressed, reduce ball's velocity
    elif key in ' rR':
        ball.vel = ball.vel * 0.45
    
    elif key in 'hH':
        game_difficulty = "hard"
        print("Hard game selected")
    
    elif key in 'eE':
        game_difficulty = "easy"
        print("Easy game selected")

# +++ End of EVENT_HANDLING +++

# +++ Start of OTHER FUNCTIONS +++
def choice(L):
    """Implements Python's choice using the random() function."""
    LEN = len(L) # Get the length
    randomindex = int(LEN*random()) # Get a random index
    return L[randomindex] # Return that element

def getSpeed(vel):
    """ Gets the speed from an object's velocity (magnitude) """
    return sqrt((vel.x ** 2) + (vel.y ** 2) + (vel.z ** 2))

def randint(low, hi):
    """Implements Python's randint using the random() function.
       returns an int from low to hi _inclusive_ (so, it's not 100% Pythonic)
    """
    if hi < low:
        low, hi = hi, low               # Swap if out of order!
    LEN = int(hi) - int(low) + 1.       # Get the span and add 1
    randvalue = LEN*random() + int(low) # Get a random value
    return int(randvalue)               # Return the integer part of it

def randcolor():
    """Returns a vector of (r, g, b) random from 0.0 to 1.0."""
    r = random(0.0, 1.0)
    g = random(0.0, 1.0)
    b = random(0.0, 1.0)
    return vector(r, g, b) # Returns 3 element color vector

def newLap():
    """ Adds 1 to lapCount """
    global lapCount
    lapCount += 1

def endGame():
    """ Ends game. Stops all object motion. Sets gameOver to True. """
    global gameOver
    global points
    gameOver = True
    ball.vel = vector(0, 0, 0)
    chaseObject1.vel = vector(0, 0, 0)
    chaseObject2.vel = vector(0, 0, 0)
    chaseObject3.vel = vector(0, 0, 0)
    obstacle1.vel = vector(0, 0, 0)
    obstacle2_1.vel = vector(0, 0, 0)

def isLapLimitExceded(lap):
    """ Checks to see if the ball is on the last lap """
    global lapLimit

    if lap > lapLimit:
        return True
    else:
        return False

def lapLimitReached():
    """ Checks to see if lapLimit is reached. If yes, ends game. """
    print("You have reached the lap limit!")
    endGame()
    print("You got", points, "out of", totalPointsPossible, "possible points.")
# +++ End of OTHER FUNCTIONS +++

# +++ Start of COLLISIONS +++
# Check for collisions and do the "right" thing
def chaseObject_Path(chaseObject):
    """ makes the chaseObjects move along a specified path through the track
    by checking where they are on the track"""
    # Top Right (right)
    if abs(chaseObject.pos.x - 9.0) < 0.2 and abs(chaseObject.pos.z + 8.5) < 0.2:
        if game_difficulty == "easy":
            if getSpeed(chaseObject.vel) == 1:
                chaseObject.vel = vector(-1,0,0)
            elif getSpeed(chaseObject.vel) == 3:
                chaseObject.vel = vector(-3, 0, 0)
            else:
                chaseObject.vel = vector(-5, 0, 0)
        else:
            if getSpeed(chaseObject.vel) == 3:
                chaseObject.vel = vector(-3,0,0)
            elif getSpeed(chaseObject.vel) == 5:
                chaseObject.vel = vector(-5, 0, 0)
            else:
                chaseObject.vel = vector(-7, 0, 0)
                
    # Top Right (left)
    if abs(chaseObject.pos.x - 6) < 0.2 and abs(chaseObject.pos.z + 8.5) < 0.2:
        if game_difficulty == "easy":
            if getSpeed(chaseObject.vel) == 1:
                chaseObject.vel = vector(0, 0, 1)
            elif getSpeed(chaseObject.vel) == 3:
                chaseObject.vel = vector(0, 0, 3)
            else:
                chaseObject.vel = vector(0, 0, 5)
        else:
            if getSpeed(chaseObject.vel) == 3:
                chaseObject.vel = vector(0, 0, 3)
            elif getSpeed(chaseObject.vel) == 5:
                chaseObject.vel = vector(0, 0, 5)
            else:
                chaseObject.vel = vector(0, 0, 7)

    # Bottom Right (right)
    if abs(chaseObject.pos.x - 6) < 0.2 and abs(chaseObject.pos.z - 8.5) < 0.2:
        if game_difficulty == "easy":
            if getSpeed(chaseObject.vel) == 1:
                chaseObject.vel = vector(-1, 0, 0)
            elif getSpeed(chaseObject.vel) == 3:
                chaseObject.vel = vector(-3, 0, 0)
            else:
                chaseObject.vel = vector(-5, 0, 0)
        else:
            if getSpeed(chaseObject.vel) == 3:
                chaseObject.vel = vector(-3, 0, 0)
            elif getSpeed(chaseObject.vel) == 5:
                chaseObject.vel = vector(-5, 0, 0)
            else:
                chaseObject.vel = vector(-7, 0, 0)
        
    # Bottom Right (left)
    if abs(chaseObject.pos.x - 2) < 0.2 and abs(chaseObject.pos.z - 8.5) < 0.2:
        if game_difficulty == "easy":
            if getSpeed(chaseObject.vel) == 1:
                chaseObject.vel = vector(0, 0, -1)
            elif getSpeed(chaseObject.vel) == 3:
                chaseObject.vel = vector(0, 0, -3)
            else:
                chaseObject.vel = vector(0, 0, -5)
        else:
            if getSpeed(chaseObject.vel) == 3:
                chaseObject.vel = vector(0, 0, -3)
            elif getSpeed(chaseObject.vel) == 5:
                chaseObject.vel = vector(0, 0, -5)
            else:
                chaseObject.vel = vector(0, 0, -7)
        
    # Top Middle (right)
    if chaseObject.pos.x > 1.8 and chaseObject.pos.x < 2.2 and abs(chaseObject.pos.z + 8.5) < 0.2:
        if game_difficulty == "easy":
            if getSpeed(chaseObject.vel) == 1:
                chaseObject.vel = vector(-1, 0, 0)
            elif getSpeed(chaseObject.vel) == 3:
                chaseObject.vel = vector(-3, 0, 0)
            else:
                chaseObject.vel = vector(-5, 0, 0)
        else:
            if getSpeed(chaseObject.vel) == 3:
                chaseObject.vel = vector(-3, 0, 0)
            elif getSpeed(chaseObject.vel) == 5:
                chaseObject.vel = vector(-5, 0, 0)
            else:
                chaseObject.vel = vector(-7, 0, 0)
        
    # Top Middle (left)
    if chaseObject.pos.x < -1.9 and chaseObject.pos.x > -2.1 and abs(chaseObject.pos.z + 8.5) < 0.2:
        if game_difficulty == "easy":
            if getSpeed(chaseObject.vel) == 1:
                chaseObject.vel = vector(0, 0, 1)
            elif getSpeed(chaseObject.vel) == 3:
                chaseObject.vel = vector(0, 0, 3)
            else:
                chaseObject.vel = vector(0, 0, 5)
        else:
            if getSpeed(chaseObject.vel) == 3:
                chaseObject.vel = vector(0, 0, 3)
            elif getSpeed(chaseObject.vel) == 5:
                chaseObject.vel = vector(0, 0, 5)
            else:
                chaseObject.vel = vector(0, 0, 7)
        
    # Bottom Left (right)
    if chaseObject.pos.x < -1.9 and chaseObject.pos.x > -2.1 and abs(chaseObject.pos.z - 8.5) < 0.2:
        if game_difficulty == "easy":
            if getSpeed(chaseObject.vel) == 1:
                chaseObject.vel = vector(-1, 0, 0)
            elif getSpeed(chaseObject.vel) == 3:
                chaseObject.vel = vector(-3, 0, 0)
            else:
                chaseObject.vel = vector(-5, 0, 0)
        else:
            if getSpeed(chaseObject.vel) == 3:
                chaseObject.vel = vector(-3, 0, 0)
            elif getSpeed(chaseObject.vel) == 5:
                chaseObject.vel = vector(-5, 0, 0)
            else:
                chaseObject.vel = vector(-7, 0, 0)
    
    # Bottom Left (left)
    if chaseObject.pos.x < -5.9 and chaseObject.pos.x > -6.1 and abs(chaseObject.pos.z - 8.5) < 0.2:
        if game_difficulty == "easy":
            if getSpeed(chaseObject.vel) == 1:
                chaseObject.vel = vector(0, 0, -1)
            elif getSpeed(chaseObject.vel) == 3:
                chaseObject.vel = vector(0, 0, -3)
            else:
                chaseObject.vel = vector(0, 0, -5)
        else:
            if getSpeed(chaseObject.vel) == 3:
                chaseObject.vel = vector(0, 0, -3)
            elif getSpeed(chaseObject.vel) == 5:
                chaseObject.vel = vector(0, 0, -5)
            else:
                chaseObject.vel = vector(0, 0, -7)
    
    # Top Left (right)
    if chaseObject.pos.x < -5.9 and chaseObject.pos.x > -6.1 and abs(chaseObject.pos.z + 8.5) < 0.2:
        if game_difficulty == "easy":
            if getSpeed(chaseObject.vel) == 1:
                chaseObject.vel = vector(-1, 0, 0)
            elif getSpeed(chaseObject.vel) == 3:
                chaseObject.vel = vector(-3, 0, 0)
            else:
                chaseObject.vel = vector(-5, 0, 0)
        else:
            if getSpeed(chaseObject.vel) == 3:
                chaseObject.vel = vector(-3, 0, 0)
            elif getSpeed(chaseObject.vel) == 5:
                chaseObject.vel = vector(-5, 0, 0)
            else:
                chaseObject.vel = vector(-7, 0, 0)

    # Top Left (left)
    if chaseObject.pos.x < -8.9 and chaseObject.pos.x > -9.1 and abs(chaseObject.pos.z + 8.5) < 0.2:
        if game_difficulty == "easy":
            if getSpeed(chaseObject.vel) == 1:
                chaseObject.vel = vector(0, 0, 1)
            elif getSpeed(chaseObject.vel) == 3:
                chaseObject.vel = vector(0, 0, 3)
            else:
                chaseObject.vel = vector(0, 0, 5)
        else:
            if getSpeed(chaseObject.vel) == 3:
                chaseObject.vel = vector(0, 0, 3)
            elif getSpeed(chaseObject.vel) == 5:
                chaseObject.vel = vector(0, 0, 5)
            else:
                chaseObject.vel = vector(0, 0, 7)
    
    # Bottom Left
    if chaseObject.pos.x < -8.9 and chaseObject.pos.x > -9.1 and abs(chaseObject.pos.z - 12) < 0.2:
        if game_difficulty == "easy":
            if getSpeed(chaseObject.vel) == 1:
                chaseObject.vel = vector(1, 0, 0)
            elif getSpeed(chaseObject.vel) == 3:
                chaseObject.vel = vector(3, 0, 0)
            else:
                chaseObject.vel = vector(5, 0, 0)
        else:
            if getSpeed(chaseObject.vel) == 3:
                chaseObject.vel = vector(3, 0, 0)
            elif getSpeed(chaseObject.vel) == 5:
                chaseObject.vel = vector(5, 0, 0)
            else:
                chaseObject.vel = vector(7, 0, 0)
    
    # Bottom Portion of Track
    if chaseObject.pos.x > 8.9 and chaseObject.pos.x < 9.1 and abs(chaseObject.pos.z - 12) < 0.2:
        if game_difficulty == "easy":
            if getSpeed(chaseObject.vel) == 1:
                chaseObject.vel = vector(0, 0, -1)
            elif getSpeed(chaseObject.vel) == 3:
                chaseObject.vel = vector(0, 0, -3)
            else:
                chaseObject.vel = vector(0, 0, -5)
        else:
            if getSpeed(chaseObject.vel) == 3:
                chaseObject.vel = vector(0, 0, -3)
            elif getSpeed(chaseObject.vel) == 3:
                chaseObject.vel = vector(0, 0, -5)
            else:
                chaseObject.vel = vector(0, 0, -7)
    
    return chaseObject.vel # Returns velocity



def corral_collide(ball):    
    """This is what happens when the ball collides with a wall/it bounces
    off of walls """
    global gameOver 
    global points
    global totalPointsPossible
    global lapCount

    # -- Outer walls --
    # If the ball hits O_wallE
    if (abs(ball.pos.x - O_wallE.pos.x) < 0.25) and (ball.pos.z >= -10) and (ball.pos.z <= 10):  # Hit -- check for z
        ball.vel.x *= -1.0 # Reverse the x velocity   

    # If the ball hits O_wallW
    if ball.pos.x < -9.5 and ball.pos.z > -10 and ball.pos.z <= 10:  # Hit -- check for z
        ball.vel.x *= -1.0 # Reverse the x velocity   
        
    # If the ball hits O_wallN
    if (abs(ball.pos.z - O_wallN.pos.z) < 0.25) and (ball.pos.x >= -10) and (ball.pos.x <= 10):  # Hit -- check for z
        ball.vel.z *= -1.0 # Reverse the z velocity

    # If the ball hits O_wallS
    if (abs(ball.pos.z - O_wallS.pos.z) < 0.25) and (ball.pos.x >= -8) and (ball.pos.x <= 8):  # Hit -- check for z
        ball.vel.z *= -1.0 # Reverse the z velocity   
    
    # -- Inner Walls --
    # If the ball hits I_wallE
    if (abs(ball.pos.x - I_wallE.pos.x) < 0.25) and (ball.pos.z >= -8) and (ball.pos.z <= 10):  # Hit -- check for z
        ball.vel.x *= -1.0 # Reverse the x velocity    
     
    # If the ball hits I_wallE2
    if (abs(ball.pos.x - I_wallE2.pos.x) < 0.25) and (ball.pos.z >= -10) and (ball.pos.z <= 8):  # Hit -- check for z
        ball.vel.x *= -1.0 # Reverse the x velocity       
    
    # If the ball hits I_wallC
    if (abs(ball.pos.x - I_wallC.pos.x) < 0.25) and (ball.pos.z >= -8) and (ball.pos.z <= 10):  # Hit -- check for z
        ball.vel.x *= -1.0 # Reverse the x velocity       
    
    # If the ball hits I_wallW2
    if (abs(ball.pos.x - I_wallW2.pos.x) < 0.25) and (ball.pos.z >= -10) and (ball.pos.z <= 8):  # Hit -- check for z
        ball.vel.x *= -1.0 # Reverse the x velocity       
    
    # If the ball hits I_wallW
    if (abs(ball.pos.x - I_wallW.pos.x) < 0.25) and (ball.pos.z >= -8) and (ball.pos.z <= 10):  # Hit -- check for z
        ball.vel.x *= -1.0
    
    # -- Obstacles --
    # If the ball collides with obstacle1
    if abs(ball.pos.x - obstacle1.pos.x) < 0.4 and abs(ball.pos.y - obstacle1.pos.y) < 0.4 and abs(ball.pos.z - obstacle1.pos.z) < 0.4:
        print("Oh no! You've hit the obstacle! Press the spacebar or risk falling off the track!")
        old_x_vel = ball.vel.x
        ball.vel.x = ball.vel.z
        ball.vel.z = old_x_vel
        ball.vel = 2 * ball.vel
   
    # - Obstacle 2's -
    # ball's velocity is slowed
    # If the ball collides with obstacle2_1
    if abs(ball.pos.x - obstacle2_1.pos.x) < 0.3 and abs(ball.pos.y - obstacle2_1.pos.y) < 0.3 and abs(ball.pos.z - obstacle2_1.pos.z) < 0.3:
        ball.vel = 0.2 * ball.vel
    
    # If the ball collides with obstacle2_2
    if abs(ball.pos.x - obstacle2_2.pos.x) < 0.3 and abs(ball.pos.y - obstacle2_2.pos.y) < 0.3 and abs(ball.pos.z - obstacle2_2.pos.z) < 0.3:
        ball.vel = 0.2 * ball.vel
    
    # If the ball collides with obstacle2_3
    if abs(ball.pos.x - obstacle2_3.pos.x) < 0.3 and abs(ball.pos.y - obstacle2_3.pos.y) < 0.3 and abs(ball.pos.z - obstacle2_3.pos.z) < 0.3:
        ball.vel = 0.2 * ball.vel
    
    # If the ball collides with obstacle2_4
    if abs(ball.pos.x - obstacle2_4.pos.x) < 0.3 and abs(ball.pos.y - obstacle2_4.pos.y) < 0.3 and abs(ball.pos.z - obstacle2_4.pos.z) < 0.3:
        ball.vel = 0.2 * ball.vel
    
    # If the ball collides with obstacle2_5
    if abs(ball.pos.x - obstacle2_5.pos.x) < 0.3 and abs(ball.pos.y - obstacle2_5.pos.y) < 0.3 and abs(ball.pos.z - obstacle2_5.pos.z) < 0.3:
        ball.vel = 0.2 * ball.vel
    
    # - chaseObjects - 
    # If the ball collides with chaseObject1
    # chaseObjects become invisible when they are caught

    # Ball reaches the first chaseObject
    if abs(ball.pos.x - chaseObject1.pos.x) < 0.4 and abs(ball.pos.y - chaseObject1.pos.y) < 0.4 and abs(ball.pos.z - chaseObject1.pos.z) < 0.4:
        points += 1
        if points != totalPointsPossible:  # If the user has NOT captured all of the spheres
            print("Congratulations! You captured the first runaway sphere! You have", points, "out of", totalPointsPossible, "possible points.")
            chaseObject1.vel = vector(0,0,0)
            chaseObject1.pos = vector(15, 15, 15)
            chaseObject1.visible = False
        else: # If the user HAS captured all the spheres
            print("Congratulations! You captured all the runaway spheres!")
            endGame()

    # Ball reaches the second chaseObject
    if abs(ball.pos.x - chaseObject2.pos.x) < 0.4 and abs(ball.pos.y - chaseObject2.pos.y) < 0.4 and abs(ball.pos.z - chaseObject2.pos.z) < 0.4:
        points += 2
        if points != totalPointsPossible:  # If the user has NOT captured all of the spheres
            print("Congratulations! You captured the second runaway sphere! You have", points, "out of", totalPointsPossible, "possible points.")
            chaseObject2.vel = vector(0,0,0)
            chaseObject2.pos = vector(15, 15, 15)
            chaseObject2.visible = False
        else: # If the user HAS captured all the spheres
            print("Congratulations! You captured all the runaway spheres!")
            endGame()

    # Ball reaches the third chaseObject
    if abs(ball.pos.x - chaseObject3.pos.x) < 0.4 and abs(ball.pos.y - chaseObject3.pos.y) < 0.4 and abs(ball.pos.z - chaseObject3.pos.z) < 0.4:
        points += 3
        if points != totalPointsPossible: # If the user has NOT captured all of the spheres
            print("Congratulations! You captured the third runaway sphere! You have", points, "out of", totalPointsPossible, "possible points.")
            chaseObject3.vel = vector(0,0,0)
            chaseObject3.pos = vector(15, 15, 15)
            chaseObject3.visible = False
        else: # If the user HAS captured all the spheres
            print("Congratulations! You captured all the runaway spheres!")
            endGame() # Ends the game

    # -- Miscellaneous -- 
    # If the ball "falls off" track, place it back at the start of the lap
    if (ball.pos.x > 15 or ball.pos.x < -11.5) or (ball.pos.z < -11) or (ball.pos.z > 15):
        print("Oh no! You fell off the track!")
        ball.vel = vector(0, 0, 0)
        ball.pos = vector(9, 0, 9)
        
        newLap() # Adds a new lap

        if isLapLimitExceded(lapCount): # Checks to see if the lapLimit has been exceded
            lapLimitReached()
        else:
            print("Lap", lapCount, "out of", lapLimit) # Notifies user of the current lap they are on


def speedSectionCollide(ball):
    """ball reaches the speed boost section of the track; increase the 
    ball's velocity"""
    if ball.pos.x > -7 and ball.pos.x < -5 and ball.pos.z > 1 and ball.pos.z < 6:
        ball.vel = ball.vel * 1.1
        print("SPEED BOOST!")

def obstacle1Collide(obstacle1):
    """obstacle1 collides with the walls"""
    if obstacle1.pos.x < -7.6:
        obstacle1.vel = vector(5,0,0)
        
    if obstacle1.pos.x > -0.5:
        obstacle1.vel = vector(-1, 0, 0)

def obstacle2Collide(obstacle):
    """obstacle2s ollide with the walls"""
    if obstacle.pos.x > 3.5:
        obstacle.vel = vector(-2,0,0)

    if obstacle.pos.x < 0.5: 
        obstacle.vel = vector(10,0,0)
    
    return obstacle.vel
    
def newLap_Collide(ball):
    """ Checks to see if the ball passes through the "start" of the track. If yes, then adds 1 to lapCount. """
    global lapCount
    global newLapPossible

    if newLapPossible == True:
        if ball.pos.x > 8 and ball.pos.x < 10 and ball.pos.z > 9.5 and ball.pos.z < 10.3:
            newLap()
            if isLapLimitExceded(lapCount):
                lapLimitReached()
            else:
                print("Lap", lapCount, "out of", lapLimit)
                newLapPossible = False

def newLap_Collide_chaseObject(object_number, object, newLapPossible, lap):
    """ Checks to see if the ball passes through the "start" of the track. If yes, then adds 1 to lapCount. """
    global newLapPossible_obj1
    global newLapPossible_obj2
    global newLapPossible_obj3
    
    if newLapPossible == True:
        if object.pos.x > 8 and object.pos.x < 10 and object.pos.z > 9.5 and object.pos.z < 10.3:
            lap += 1
            if isLapLimitExceded(lap):
                print("Sphere", object_number, "reached 3 laps.")
                if object_number == 1:
                    chaseObject1.vel = vector(0,0,0)
                    chaseObject1.pos = vector(15, 15, 15)
                    chaseObject1.visible = False
                    newLapPossible_obj1 = False
                elif object_number == 2:
                    chaseObject2.vel = vector(0,0,0)
                    chaseObject2.pos = vector(15, 15, 15)
                    chaseObject2.visible = False
                    newLapPossible_obj2 = False
                else:
                    chaseObject3.vel = vector(0,0,0)
                    chaseObject3.pos = vector(15, 15, 15)
                    chaseObject3.visible = False
                    newLapPossible_obj3 = False
            else:
                if object_number == 1:
                    newLapPossible_obj1 = False
                elif object_number == 2:
                    newLapPossible_obj2 = False
                else:
                    newLapPossible_obj3 = False
    return lap

def newLapPossible_Collide(object, newLapPossible):
    """ Checks to see if the ball has passed the spot that makes a new lap possible """
    if object.pos.x > 8 and object.pos.x < 10 and object.pos.z > 4 and object.pos.z < 5:
        newLapPossible = True
    return newLapPossible
# +++ End of COLLISIONS +++