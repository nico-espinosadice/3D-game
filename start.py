#
# game_starter.py
#
# Building an interaction with 3D graphics using python
#   Documentation: http://www.glowscript.org/docs/GlowScriptDocs/index.html
#   Examples:      http://www.glowscript.org/#/user/GlowScriptDemos/folder/Examples/
#

scene.bind('keydown', keydown_fun)     # Function for key presses
scene.bind('click', click_fun)         # Function for mouse clicks
scene.background = 0.8*vector(1, 1, 1) # Light gray (0.8 out of 1.0)
scene.width = 640                      # Make the 3D canvas larger
scene.height = 480


# +++ start of OBJECT_CREATION section
# These functions create "container" objects, called "compounds"

def make_alien(starting_position, starting_vel = vector(0, 0, 0)):
    """The lines below make a new "frame", which is a container with a
       local coordinate system.
       The arguments to make_alien allow for any initial starting position
       and initial starting velocity, with a default starting velocity
       of vector(0, 0, 0).

       Compounds can have any number of components.  Here are the
       alien's components:
    """
    alien_body = sphere(size = 1.0*vector(1, 1, 1), pos = vector(0, 0, 0), color = color.green)
    alien_eye1 = sphere(size = 0.3*vector(1, 1, 1), pos = .42*vector(.7, .5, .2), color = color.white)
    alien_eye2 = sphere(size = 0.3*vector(1, 1, 1), pos = .42*vector(.2, .5, .7), color = color.white)
    alien_hat = cylinder(pos = 0.42*vector(0, .9, -.2), axis = vector(.02, .2, -.02), size = vector(0.2, 0.7, 0.7), color = color.magenta)
    alien_objects = [alien_body, alien_eye1, alien_eye2, alien_hat]  # make a list to "fuse" with a compound
    # now, we create a compound -- we'll name it com_alien:
    com_alien = compound(alien_objects, pos = starting_position)
    com_alien.vel = starting_vel   # set the initial velocity
    return com_alien



# The ground is represented by a box (vpython's rectangular solid)
# http://www.glowscript.org/docs/GlowScriptDocs/box.html
ground = box(size = vector(20, 1, 20), pos = vector(0, -1, 0), color = .4*vector(1, 1, 1))

# Create two walls, also boxes
wallA = box(pos = vector(0, 0, -10), axis = vector(1, 0, 0), size = vector(20, 1, .2), color = vector(1.0, 0.7, 0.3)) # amber
wallB = box(pos = vector(-10, 0, 0), axis = vector(0, 0, 1), size = vector(20, 1, .2), color = color.blue)   # blue
wallC = box(pos = vector(0, 0, 10), axis = vector(1, 0, 0), size = vector(20, 1, .2), color = color.green) #green
wallD = box(pos = vector(10, 0, 0), axis = vector(0, 0, 1), size = vector(20, 1, .2), color = color.yellow) #yellow

# A ball that we will be able to control
ball = sphere(size = 1.0*vector(1, 1, 1), color = vector(0.8, 0.5, 0.0))   # ball is an object of class sphere
ball.vel = vector(0, 0, 0)     # this is its initial velocity

# We make two aliens using two calls to the make_alien function (from above)
alien = make_alien(starting_position = vector(6, 0, -6), starting_vel = vector(0, 0, -1))
alien2 = make_alien(starting_position = vector(-10, 5, -10))  # zero starting velocity

handle = cylinder(size=vec(1,.2,.2), color=vec(0.72,0.42,0))
head = box(size=vec(.2,.6,.2), pos=vec(1.1,0,0), color=color.gray(.6))
hammer = compound([handle, head])
hammer.axis = vec(1,1,0)
hammer.pos = vector(5, 0, 5)

ball2 = sphere(pos = vector(10, 0, 10), size = 3.0*vector(1, 1, 1), color = vector(0, 0, 1))   # ball is an object of class sphere
ball2.vel = vector(10, 0, 0)     # this is its initial velocity

ball3 = sphere(pos = vector(0, 0, -10), size = 3.0*vector(1, 1, 1), color = vector(1, 0, 0.0))   # ball is an object of class sphere
ball3.vel = vector(10, 0, 0)     # this is its initial velocity

ball4 = sphere(pos = vector(5, 0, 5), size = 3.0*vector(1, 1, 1), color = vector(0, 1, 0.0))   # ball is an object of class sphere
ball4.vel = vector(10, 0, 0)     # this is its initial velocity


# +++ end of OBJECT_CREATION section


# +++ start of ANIMATION section

# Other constants
RATE = 30                # The number of times the while loop runs each second
dt = 1.0/(1.0*RATE)      # The time step each time through the while loop
scene.autoscale = False  # Avoids changing the view automatically
scene.forward = vector(0, -3, -2)  # Ask for a bird's-eye view of the scene...

# This is the "event loop" or "animation loop"
# Each pass through the loop will animate one step in time, dt
#
while True:

    rate(RATE)   # maximum number of times per second the while loop runs

    # +++ Start of PHYSICS UPDATES -- update all positions here, every time step

    alien.pos = alien.pos + alien.vel*dt   # Update the alien's position
    ball.pos = ball.pos + ball.vel*dt      # Update the ball's position
    ball2.pos = ball2.pos + ball2.vel*dt      # Update the ball's position
    ball3.pos = ball3.pos + ball3.vel*dt      # Update the ball's position
    ball4.pos = ball4.pos + ball4.vel*dt      # Update the ball's position

    # +++ End of PHYSICS UPDATES -- be sure new objects are updated appropriately!
    
    corral_collide(ball)
    
    corral_collide(alien)
    
    corral_collide(ball2)
    
    corral_collide(ball3)
    
    corral_collide(ball4)
    
    # If the ball collides with the alien, give the alien a vertical velocity
    if mag(ball.pos - alien.pos) < 1.0:
        print("YOU WIN!")
        alien.color = color.blue
        ball.color = color.blue
        ball2.color = color.blue
        ball3.color = color.blue
        ball4.color = color.blue
        wallA.color = color.blue
        wallB.color = color.blue
        wallC.color = color.blue
        wallD.color = color.blue
        hammer.color = color.blue
        alien.vel = vector(0, 1, 0)

    if mag(ball.pos - hammer.pos) < 1.0 or mag(ball.pos - ball2.pos) < 1.0 or mag(ball.pos - ball3.pos) < 1.0 or mag(ball.pos - ball4.pos) < 1.0:
        print("YOU LOSE!")
        alien.color = color.red
        ball.color = color.red
        ball2.color = color.red
        ball3.color = color.red
        ball4.color = color.red
        wallA.color = color.red
        wallB.color = color.red
        wallC.color = color.red
        wallD.color = color.red
        hammer.color = color.red
    
    # +++ End of COLLISIONS



# +++ start of EVENT_HANDLING section -- separate functions for
#                                keypresses and mouse clicks...

def keydown_fun(event):
    """This function is called each time a key is pressed."""
    ball.color = randcolor()
    key = event.key
    ri = randint(0, 10)
    print("key:", key, ri)  # Prints the key pressed -- caps only...

    amt = 0.42              # "Strength" of the keypress's velocity changes
    if key == 'up' or key in 'wWiI':
        ball.vel = ball.vel + vector(0, 0, -amt)
    elif key == 'left' or key in 'aAjJ':
        ball.vel = ball.vel + vector(-amt, 0, 0)
    elif key == 'down' or key in 'sSkK':
        ball.vel = ball.vel + vector(0, 0, amt)
    elif key == 'right' or key in "dDlL":
        ball.vel = ball.vel + vector(amt, 0, 0)
    elif key in ' rR':
        ball.vel = vector(0, 0, 0) # Reset! via the spacebar, " "
        ball.pos = vector(0, 0, 0)

def click_fun(event):
    """This function is called each time the mouse is clicked."""
    print("event is", event.event, event.which)

# +++ End of EVENT_HANDLING section



# +++ Other functions can go here...

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
    # If the ball hits wallA
    if ball.pos.z < wallA.pos.z:  # Hit -- check for z
        ball.pos.z = wallA.pos.z  # Bring back into bounds
        ball.vel.z *= -1.0        # Reverse the z velocity

    # If the ball hits wallB
    if ball.pos.x < wallB.pos.x:  # Hit -- check for x
        ball.pos.x = wallB.pos.x  # Bring back into bounds
        ball.vel.x *= -1.0        # Reverse the x velocity
        
    # If the ball hits wallC
    if ball.pos.z > wallC.pos.z:  # Hit -- check for z
        ball.pos.z = wallC.pos.z  # Bring back into bounds
        ball.vel.z *= -1.0        # Reverse the z velocity

    # If the ball hits wallB
    if ball.pos.x > wallD.pos.x:  # Hit -- check for x
        ball.pos.x = wallD.pos.x  # Bring back into bounds
        ball.vel.x *= -1.0        # Reverse the x velocity
    
    # If the alien ventures too far, restart randomly -- but only if it's
    # not moving vertically.
    #if mag(alien.pos) > 10 and alien.vel.y < 1:
        #alien.pos.x = choice([-6, 6])
        #alien.pos.z = choice([-6, 6])
        #alien.vel = 2*vector.random() # Library-supplied random vector
        #alien.vel.y = 0.0             # No vertical component of velocity
        
    