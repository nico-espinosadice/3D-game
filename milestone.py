GlowScript 2.7 VPython
# Start.py
# Jacob van der Leeuw and Nico Espinosa Dice
# Final Project - VPython




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

# Cylinder (other control)
chaseObject1 = cylinder(pos = vector(8.5, 0, 4), size = 1.0*vector(1,1,1), color = color.orange)
chaseObject1.vel = vector(0,0,-5) #initial velocity for chaseObject1
# +++ End of TRACK CREATION +++

# +++ start of ANIMATION section ++

# Other constants
RATE = 30                # The number of times the while loop runs each second
dt = 1.0/(1.0*RATE)      # The time step each time through the while loop
scene.autoscale = False  # Avoids changing the view automatically
scene.forward = vector(0, -3, -2)  # Ask for a bird's-eye view of the scene...
# This is the "event loop" or "animation loop"
# Each pass through the loop will animate one step in time, dt
while gameplay:
    print("Ball Position =", ball.pos)
    print("Object Velocity =", chaseObject1.vel)
    print("Object Position =", chaseObject1.pos)
    #print("Wall Position =", O_wallS.pos)
    rate(RATE)   # maximum number of times per second the while loop runs

    # +++ Start of PHYSICS UPDATES -- update all positions here, every time step
    ball.pos = ball.pos + ball.vel*dt      # Update the ball's position
    # +++ End of PHYSICS UPDATES -- be sure new objects are updated appropriately!
    chaseObject1.pos = chaseObject1.pos + chaseObject1.vel*dt

    Chaseobj_collide(chaseObject1)
    corral_collide(ball)
    gameFin(ball, chaseObject1)
    

# +++ start of EVENT_HANDLING section -- separate functions for
#                                keypresses and mouse clicks...


def gameFin(ball, chaseObject1):
    if (abs(ball.pos.x - chaseObject1.pos.x) < 0.10) and (abs(ball.pos.z - chaseObject1.pos.z) < 0.10):
        print("You Win")
        gameplay = False

def keydown_fun(event):
    """This function is called each time a key is pressed."""
    global L
    ball.color = randcolor()
    key = event.key
    
    amt = 0.9            # "Strength" of the keypress's velocity changes
    
    if key == 'up' or key in 'wWiI':
        ball.vel = ball.vel + vector(0, 0, -amt)
    elif key == 'left' or key in 'aAjJ':
        ball.vel = ball.vel + vector(-amt, 0, 0)
    elif key == 'down' or key in 'sSkK':
        ball.vel = ball.vel + vector(0, 0, amt)
    elif key == 'right' or key in "dDlL":
        ball.vel = ball.vel + vector(amt, 0, 0)
    elif key in ' rR':
        ball.vel = ball.vel * 0.45 # Reset! via the spacebar
        
        
    #L.append(key)
    #print(L)
    #print("L =", L)
    #print("key:", key)  # Prints the key pressed -- caps only...
    """L.append(key)
    print(L)
    if L[-1] == 'up' and L[-2] == '':
        ball.vel = vector(0, 0, -amt)
    elif L[-1] == 'left' and L[-2] == 'left':
        ball.vel = vector(-amt, 0, 0)
    elif L[-1] == 'down' and L[-2] == 'down':
        ball.vel = vector(0, 0, amt)
    elif L[-1] == 'right' and L[-2] == 'right':
        ball.vel = vector(amt, 0, 0)
    elif L[-1] == 'up' and L[-2] == 'right' or L[-1] == 'right' and L[-2] == 'up':
        ball.vel = vector(amt/1.414, 0, amt/-1.414)
    elif L[-1] == 'up' and L[-2] == 'left' or L[-1] == 'left' and L[-2] == 'up':
        ball.vel = vector(amt/-1.414, 0, amt/-1.414)
    elif L[-1] == 'down' and L[-2] == 'right' or L[-1] == 'right' and L[-2] == 'down':
        ball.vel = vector(amt/1.414, 0, amt/1.414)
    elif L[-1] == 'down' and L[-2] == 'left' or L[-1] == 'left' and L[-2] == 'down':
        ball.vel = vector(amt/-1.414, 0, amt/1.414)
    elif key in ' rR':
        ball.vel = vector(0, 0, 0) # Reset! via the spacebar """
    
        
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

def Chaseobj_collide(chaseObject1):
    
        if (abs(chaseObject1.pos.z - O_wallN.pos.z) < 0.25 or (chaseObject1.pos.z <= -10)):  # Hit -- check for z
            
            chaseObject1.vel = vector(-5,0,0)
        
        if (abs(chaseObject1.pos.x - I_wallE2.pos.x) < 0.25):  # Hit -- check for z
            chaseObject1.vel = vector(0,0,5)

        if (abs(chaseObject1.pos.z - O_wallS.pos.z) < 0.25 or (chaseObject1.pos.z >= 10)):  # Hit -- check for z
            chaseObject1.vel = vector(-5,0,0)
        
        if (abs(chaseObject1.pos.x - I_wallC.pos.x) < 0.25):  # Hit -- check for z
            chaseObject1.vel = vector(0,0,-5)

        if (abs(chaseObject1.pos.x - I_wallW2.pos.x) < 0.25):  # Hit -- check for z
            chaseObject1.vel = vector(0,0,5)

        if (abs(chaseObject1.pos.x - I_wallW.pos.x) < 0.25):  # Hit -- check for z
            chaseObject1.vel = vector(0,0,-5)    

        if (abs(chaseObject1.pos.x - O_wallW.pos.x) < 0.25):  # Hit -- check for z
            chaseObject1.vel = vector(0,0,5)

        if (abs(chaseObject1.pos.x + 8.61) < 0.15) and (abs(chaseObject1.pos.z - 10 < 0.15)):
            gameplay = False
            print("You Lose!")
        # Reverse the z velocity 
        # if chaseObject1.pos.x == 5.88:
        #     chaseObject1.vel = vector(0,0,5)
        # if chaseObject1.pos.x == 1.70:
        #     chaseObject1.vel = vector(0,0,-5)
        # if chaseObject1.pos.x == -2.7:
        #     chaseObject1.vel = vector(0,0,5)
        # if chaseObject1.pos.x == -5.88:
        #     chaseObject1.vel = vector(0,0,-5)
        # if chaseObject1.pos.x == -9.3:
        #     chaseObject1.vel = vector(0,0,5)
        # elif chaseObject1.pos.z < -9 or chaseObject1.pos.z > 9:
        #     chaseObject1.vel = vector(-5, 0, 0)


# +++ Start of COLLISIONS -- check for collisions & do the "right" thing
def corral_collide(ball):
    """Corral collisions!
    Ball must have a .vel field and a .pos field. """
    # -- Outer walls --
    # If the ball hits O_wallE
    if (abs(ball.pos.x - O_wallE.pos.x) < 0.25) and (ball.pos.z >= -10) and (ball.pos.z <= 10):  # Hit -- check for z
        ball.vel.x *= -1.0 # Reverse the x velocity   

    # If the ball hits O_wallW
    if (abs(ball.pos.x - O_wallW.pos.x) < 0.25) and (ball.pos.z >= -8) and (ball.pos.z <= 10):  # Hit -- check for z
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
    
    if (ball.pos.x > 15 or ball.pos.x < -11.5) or (ball.pos.z < -11) or (ball.pos.z > 15):
        print("Oh no! You fell off!")
        ball.vel = vector(0, 0, 0)
        ball.pos = vector(9, 0, 9)