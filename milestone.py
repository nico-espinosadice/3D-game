GlowScript 2.7 VPython
# Start.py
# Jacob van der Leeuw and Nico Espinosa Dice
# Final Project - VPython
import math
scene.bind('keydown', keydown_fun)     # Function for key presses
scene.bind('click', click_fun)         # Function for mouse clicks
scene.background = 0.8*vector(1, 1, 1) # Light gray (0.8 out of 1.0)
scene.width = 640                      # Make the 3D canvas larger
scene.height = 480

# +++ start of TRACK CREATION +++
# Ground (represented by a box - vpython's rectangular solid)
ground = box(size = vector(20, 1, 20), pos = vector(0, -1, 0), color = .4*vector(1, 1, 1))
ground2 = box(size = vector(20, 1, 4), pos = vector(0, -1, 12), color = color.purple)

# Outer-most boundaries of the track
O_wallN = box(pos = vector(0, 0, -10), axis = vector(1, 0, 0), size = vector(20, 1, .2), color = color.red) # "North" wall - red
O_wallW = box(pos = vector(-10, 0, 0), axis = vector(0, 0, 1), size = vector(20, 1, .2), color = color.blue) # "West" wall - blue
O_wallS = box(pos = vector(0, 0, 10), axis = vector(1, 0, 0), size = vector(16, 1, .2), color = color.green) # "South" wall - green
O_wallE = box(pos = vector(10, 0, 0), axis = vector(0, 0, 1), size = vector(20, 1, .2), color = color.yellow) # "East" wall - yellow

# Inner walls of the track
#east walls
I_wallE = box(pos = vector(8, 0, 1), axis = vector(0, 0, 1), size = vector(18, 1, .2), color = color.black) # "East" wall - yellow
I_wallE2 = box(pos = vector(4, 0, -1), axis = vector(0, 0, 1), size = vector(18, 1, .2), color = color.yellow) # "East" wall - yellow

#center wall
I_wallC = box(pos = vector(0, 0, 1), axis = vector(0, 0, 1), size = vector(18, 1, .2), color = color.green) # "East" wall - yellow

#west walls
I_wallW = box(pos = vector(-8, 0, 1), axis = vector(0, 0, 1), size = vector(18, 1, .2), color = color.white) # "East" wall - yellow
I_wallW2 = box(pos = vector(-4, 0, -1), axis = vector(0, 0, 1), size = vector(18, 1, .2), color = color.red) # "East" wall - yellow

# Ball (user controls)
ball = sphere(pos = vector(9, 0, 9), size = 1.0*vector(1, 1, 1), color = vector(0.8, 0.5, 0.0))   # ball is an object of class sphere
ball.vel = vector(0, 0, 0)     # this is its initial velocity

# +++ End of TRACK CREATION +++

# +++ start of ANIMATION section ++

# Other constants
RATE = 30                # The number of times the while loop runs each second
dt = 1.0/(1.0*RATE)      # The time step each time through the while loop
scene.autoscale = False  # Avoids changing the view automatically
scene.forward = vector(0, -3, -2)  # Ask for a bird's-eye view of the scene...
# This is the "event loop" or "animation loop"
# Each pass through the loop will animate one step in time, dt
while True:
    rate(RATE)   # maximum number of times per second the while loop runs

    # +++ Start of PHYSICS UPDATES -- update all positions here, every time step
    ball.pos = ball.pos + ball.vel*dt      # Update the ball's position
    # +++ End of PHYSICS UPDATES -- be sure new objects are updated appropriately!
    
    corral_collide(ball)

# +++ start of EVENT_HANDLING section -- separate functions for
#                                keypresses and mouse clicks...

def keydown_fun(event):
    """This function is called each time a key is pressed."""
    ball.color = randcolor()
    key = key.get_pressed()
    key1 = key.get_pressed()
    ri = randint(0, 10)
    print("key:", key, ri)  # Prints the key pressed -- caps only...

    amt = 7.00             # "Strength" of the keypress's velocity changes
    L = [] 
    L += key1
    L += key2
    if L[0] == 'up' and L[1] == '':
        ball.vel = vector(0, 0, -amt)
    elif L[0] == 'left' and L[1] == '':
        ball.vel = vector(-amt, 0, 0)
    elif L[0] == 'down' and L[1] == '':
        ball.vel = vector(0, 0, amt)
    elif L[0] == 'right' and L[1] == '':
        ball.vel = vector(amt, 0, 0)
    elif L[0] == 'up' and L[1] == 'right':
        ball.vel = vector(amt/1.414, 0, amt/-1.414)
    elif L[0] == 'up' and L[1] == 'left':
        ball.vel = vector(amt/-1.414, 0, amt/-1.414)
    elif L[0] == 'down' and L[1] == 'right':
        ball.vel = vector(amt/1.414, 0, amt/1.414)
    elif L[0] == 'down' and L[1] == 'left':
        ball.vel = vector(amt/-1.414, 0, amt/1.414)
    elif key in ' rR':
        ball.vel = vector(0, 0, 0) # Reset! via the spacebar, " "

def keyup_fun(event):
    "This function is called each time a key is not pressed"
        

def click_fun(event):
    """This function is called each time the mouse is clicked."""
    print("event is", event.event, event.which)

# +++ End of EVENT_HANDLING section

# +++ Start of OTHER FUNCTIONS +++
def choice(L):
    """Implements Python's choice using the random() function."""
    LEN = len(L)              # Get the length
    randomindex = int(LEN*random())  # Get a random index
    return L[randomindex]     # Return that element

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
    return vector(r, g, b)       # A color is a three-element vector

# +++ Start of COLLISIONS -- check for collisions & do the "right" thing
def corral_collide(ball):
    """Corral collisions!
    Ball must have a .vel field and a .pos field. """
    # -- Outer walls --
    # If the ball hits O_wallN
    if ball.pos.z < O_wallN.pos.z:  # Hit -- check for z
        ball.pos.z = O_wallN.pos.z  # Bring back into bounds
        ball.vel.z *= -1.0  
        O_wallN.color = randcolor()      # Reverse the z velocity

    # If the ball hits O_wallW
    if ball.pos.x < O_wallW.pos.x:  # Hit -- check for x
        ball.pos.x = O_wallW.pos.x  # Bring back into bounds
        ball.vel.x *= -1.0 
        O_wallW.color = randcolor()       # Reverse the x velocity
        
    # If the ball hits O_wallS
    if ball.pos.z > O_wallS.pos.z:  # Hit -- check for z
        ball.pos.z = O_wallS.pos.z  # Bring back into bounds
        ball.vel.z *= -1.0  
        O_wallS.color = randcolor()      # Reverse the z velocity

    # If the ball hits O_wallE
    if ball.pos.x > O_wallE.pos.x:  # Hit -- check for x
        ball.pos.x = O_wallE.pos.x  # Bring back into bounds
        ball.vel.x *= -1.0   
        O_wallE.color = randcolor()     # Reverse the x velocity
    
    # -- Inner Walls --
    # If the ball hits I_wallN
    if (abs(ball.pos.x - I_wallE.pos.x) < 0.10) and (ball.pos.z > (I_wallE.pos.z - 9)) and (ball.pos.z < (I_wallE.pos.z + 10)):  # Hit -- check for z
        ball.vel.x *= -1.0 # Reverse the z velocity  
        I_wallE.color = randcolor()

     
    # If the ball hits I_wallN
    if (abs(ball.pos.x - I_wallE2.pos.x) < 0.10) and (ball.pos.z > (I_wallE2.pos.z - 10)) and (ball.pos.z < (I_wallE2.pos.z + 9)):  # Hit -- check for z
        ball.vel.x *= -1.0 # Reverse the z velocity      
        I_wallE2.color = randcolor() 
    
    # If the ball hits I_wallN
    if (abs(ball.pos.x - I_wallC.pos.x) < 0.10) and (ball.pos.z > (I_wallC.pos.z - 9)) and (ball.pos.z < (I_wallC.pos.z + 10)):  # Hit -- check for z
        ball.vel.x *= -1.0 # Reverse the z velocity   
        I_wallC.color = randcolor()    
    
    # If the ball hits I_wallN
    if (abs(ball.pos.x - I_wallW2.pos.x) < 0.10) and (ball.pos.z > (I_wallW2.pos.z - 10)) and (ball.pos.z < (I_wallW2.pos.z + 9)):  # Hit -- check for z
        ball.vel.x *= -1.0 # Reverse the z velocity       
        I_wallW2.color = randcolor()

    # If the ball hits I_wallN
    if (abs(ball.pos.x - I_wallW.pos.x) < 0.25) and (ball.pos.z > (I_wallW.pos.z - 9)) and (ball.pos.z < (I_wallW.pos.z + 10)):  # Hit -- check for z
        ball.vel.x *= -1.0 # Reverse the z velocity     
        I_wallW.color = randcolor()  