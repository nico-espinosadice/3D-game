GlowScript 2.7 VPython
# Milestone.py
# Jacob van der Leeuw and Nico Espinosa Dice
# Final Project - VPython

gameOver = False
newLapPossible = False
lapCount = 1
lapLimit = 3
points = 0
totalPointsPossible = 6

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

# Chase Object #1 (autonomous)
chaseObject1 = sphere(pos = vector(9.0, 0, -5.0), size = 0.5*vector(1,1,1), color = color.orange)
chaseObject1.vel = vector(0,0,-5) #initial velocity for chaseObj

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
speedSection = box(size = vector(2, 0.0001, 5), pos = vector(-6, 0, 4), color = color.blue)
# +++ End of OBJECT CREATION ++


# +++ Start of ANIMATION +++
# Constants
RATE = 30                # The number of times the while loop runs each second
dt = 1.0/(1.0*RATE)      # The time step each time through the while loop
scene.autoscale = False  # Avoids changing the view automatically
scene.forward = vector(0, -3, -2)  # Ask for a bird's-eye view of the scene...
# +++ End of ANIMATION +++

# +++ Start of GAME EXPLANATION to user +++ 
print("Objective: Capture the runaway cylinder.")
print("How: Use the arrow keys to mvoe the ball through the track (while avoiding the obstacles)!")
print("Tip: use the space bar to slow down before turns.")
print("Hurry! The ball is getting away!")
print("Press a key to begin.")
# +++ End of GAME EXPLANATION to user +++ 

# +++ Start of GAME LOOP +++ 
scene.waitfor('keydown') # wait for keyboard key press
gameOver = False # Keeps track of whether the game is over

while not gameOver: # Each pass through the loop will animate one step in time (dt)
    print(ball.pos)
    lapLimitReached(lapCount)

    rate(RATE)   # maximum number of times per second the while loop runs

    # +++ Start of PHYSICS UPDATES +++
    # Update all positions here (every time step)
    ball.pos = ball.pos + ball.vel*dt # Update the ball's position
    chaseObject1.pos = chaseObject1.pos + chaseObject1.vel*dt # Update chaseObject1's position
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
    chaseObject_Path(chaseObject1) # Checks to see if chaseObject has collided with something (keeps chaseObject on correct path)

    # Obstacles
    obstacle1Collide(obstacle1) # Checks to see if obstacle1 has collided with something
    
    obstacle2_1.vel = obstacle2Collide(obstacle2_1) # Checks to see if obstacle2_1 has collided with something
    obstacle2_2.vel = obstacle2Collide(obstacle2_2) # Checks to see if obstacle2_2 has collided with something
    obstacle2_3.vel = obstacle2Collide(obstacle2_3) # Checks to see if obstacle2_3 has collided with something
    obstacle2_4.vel = obstacle2Collide(obstacle2_4) # Checks to see if obstacle2_4 has collided with something
    obstacle2_5.vel = obstacle2Collide(obstacle2_5) # Checks to see if obstacle2_5 has collided with something

    # New Lap
    newLapPossible_Collide(ball)
    newLap_Collide(ball)
     # +++ End of EVENT CHECKING +++ 


# +++ start of EVENT_HANDLING section +++
# Separate functions for keypresses and mouse clicks
def keydown_fun(event):
    """This function is called each time a key is pressed."""    
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
# +++ End of EVENT_HANDLING +++

# +++ Start of OTHER FUNCTIONS +++
def choice(L):
    """Implements Python's choice using the random() function."""
    LEN = len(L) # Get the length
    randomindex = int(LEN*random()) # Get a random index
    return L[randomindex] # Return that element

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
    gameOver = True
    ball.vel = vector(0, 0, 0)
    chaseObject1.vel = vector(0, 0, 0)
    obstacle1.vel = vector(0, 0, 0)
    obstacle2_1.vel = vector(0, 0, 0)

def lapLimitReached(lapCount):
    """ Checks to see if lapLimit is reached. If yes, ends game. """
    global lapLimit

    if lapCount > lapLimit:
        endGame()
        print("You have reached your lap limit!")
        print("Game over. You lose!")
# +++ End of OTHER FUNCTIONS +++

# +++ Start of COLLISIONS +++
# Check for collisions and do the "right" thing
def chaseObject_Path(chaseObject1):

        # Top Right (right)
        if abs(chaseObject1.pos.x - 9.0) < 0.2 and abs(chaseObject1.pos.z + 8.5) < 0.2:
            chaseObject1.vel = vector(-5,0,0)
        
        # Top Right (left)
        if abs(chaseObject1.pos.x - 6) < 0.2 and abs(chaseObject1.pos.z + 8.5) < 0.2:
            chaseObject1.vel = vector(0,0,5)

        # Bottom Right (right)
        if abs(chaseObject1.pos.x - 6) < 0.2 and abs(chaseObject1.pos.z - 8.5) < 0.2:
            chaseObject1.vel = vector(-5,0,0)
        
        # Bottom Right (left)
        if abs(chaseObject1.pos.x - 2) < 0.2 and abs(chaseObject1.pos.z - 8.5) < 0.2:
            chaseObject1.vel = vector(0,0,-5)
        
        # Top Middle (right)
        if chaseObject1.pos.x > 1.8 and chaseObject1.pos.x < 2.2 and abs(chaseObject1.pos.z + 8.5) < 0.2:
            chaseObject1.vel = vector(-5, 0, 0)
        
        # Top Middle (left)
        if chaseObject1.pos.x < -1.9 and chaseObject1.pos.x > -2.1 and abs(chaseObject1.pos.z + 8.5) < 0.2:
            chaseObject1.vel = vector(0,0,5)
        
        # Bottom Left (right)
        if chaseObject1.pos.x < -1.9 and chaseObject1.pos.x > -2.1 and abs(chaseObject1.pos.z - 8.5) < 0.2:
            chaseObject1.vel = vector(-5,0,0)
        
        # Bottom Left (left)
        if chaseObject1.pos.x < -5.9 and chaseObject1.pos.x > -6.1 and abs(chaseObject1.pos.z - 8.5) < 0.2:
            chaseObject1.vel = vector(0,0,-5)
        
        # Top Left (right)
        if chaseObject1.pos.x < -5.9 and chaseObject1.pos.x > -6.1 and abs(chaseObject1.pos.z + 8.5) < 0.2:
            chaseObject1.vel = vector(-5,0,0)
    
        # Top Left (left)
        if chaseObject1.pos.x < -8.9 and chaseObject1.pos.x > -9.1 and abs(chaseObject1.pos.z + 8.5) < 0.2:
            chaseObject1.vel = vector(0,0,5)
        
        # Bottom Left
        if chaseObject1.pos.x < -8.9 and chaseObject1.pos.x > -9.1 and abs(chaseObject1.pos.z - 12) < 0.2:
            chaseObject1.vel = vector(5,0,0)
        
        # Bottom Portion of Track
        if chaseObject1.pos.x > 8.9 and chaseObject1.pos.x < 9.1 and abs(chaseObject1.pos.z - 12) < 0.2:
            chaseObject1.vel = vector(0,0,-5)

def corral_collide(ball):
    """Corral collisions!
    Ball must have a .vel field and a .pos field. """
    global gameOver 

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
    if abs(ball.pos.x - chaseObject1.pos.x) < 0.4 and abs(ball.pos.y - chaseObject1.pos.y) < 0.4 and abs(ball.pos.z - chaseObject1.pos.z) < 0.4:
        global points, totalPointsPossible
        endGame()
        print("You captured a runaway ball! You have", points, "(out of)", totalPointsPossible, "so far!")
    
    # -- Miscellaneous -- 
    # If the ball "falls off" track
    if (ball.pos.x > 15 or ball.pos.x < -11.5) or (ball.pos.z < -11) or (ball.pos.z > 15):
        print("Oh no! You fell off the track!")
        ball.vel = vector(0, 0, 0)
        ball.pos = vector(9, 0, 9)
        newLap()

def speedSectionCollide(ball):
    if ball.pos.x > -7 and ball.pos.x < -5 and ball.pos.z > 1 and ball.pos.z < 6:
        ball.vel = ball.vel * 1.1
        print("SPEED BOOST!")

def obstacle1Collide(obstacle1):
    if obstacle1.pos.x < -7.6:
        obstacle1.vel = vector(5,0,0)
        
    if obstacle1.pos.x > -0.5:
        obstacle1.vel = vector(-1, 0, 0)

def obstacle2Collide(obstacle):
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
            print("Lap:", lapCount)
            newLapPossible = False

def newLapPossible_Collide(ball):
    """ Checks to see if the ball has passed the spot that makes a new lap possible """
    global newLapPossible
    if ball.pos.x > 8 and ball.pos.x < 10 and ball.pos.z > 4 and ball.pos.z < 5:
        newLapPossible = True
# +++ End of COLLISIONS +++