def on_a_pressed():
    bubble.toss_bubble()
    mySprite.set_image(assets.image("""
        THROW
        """))
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_right_repeated():
    bubble.tilt_angle(bubble.Choice.RIGHT)
controller.right.on_event(ControllerButtonEvent.REPEATED, on_right_repeated)

def on_hit_wall(sprite, location):
    bubble.stick_to_wall(sprite, location)
    
    def on_after():
        mySprite.say_text("GAME OVER!!!!")
    timer.after(9000, on_after)
    
scene.on_hit_wall(SpriteKind.bubble, on_hit_wall)

def on_a_released():
    mySprite.set_image(assets.image("""
        CRY
        """))
    bubble.load_bubble()
controller.A.on_event(ControllerButtonEvent.RELEASED, on_a_released)

def on_left_repeated():
    bubble.tilt_angle(bubble.Choice.LEFT)
controller.left.on_event(ControllerButtonEvent.REPEATED, on_left_repeated)

mySprite: Sprite = None
bubble.create_board()
bubble.load_bubble()
mySprite = sprites.create(assets.image("""
    CRY
    """), SpriteKind.player)
mySprite.top = 102