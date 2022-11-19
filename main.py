def turn_around():
    turn_left()
    turn_left()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def take_right_turn():
    if wall_in_front():
        return False
    else:
        move()
        turn_right()        
        return True
    
breached = False

while not breached:
    if at_goal():    
        breached = True
    else:
        if wall_on_right() and wall_in_front():
            turn_left()
        elif wall_on_right():
            move()
        #elif wall_in_front():
        else:
            turn_right()
            move()
