controller.A.onEvent(ControllerButtonEvent.Pressed, function on_a_pressed() {
    bubble.tossBubble()
    mySprite.setImage(assets.image`
        THROW
        `)
})
controller.right.onEvent(ControllerButtonEvent.Repeated, function on_right_repeated() {
    bubble.tilt_angle(bubble.Choice.Right)
})
scene.onHitWall(SpriteKind.Bubble, function on_hit_wall(sprite: Sprite, location: tiles.Location) {
    bubble.stick_to_wall(sprite, location)
    timer.after(9000, function on_after() {
        mySprite.sayText("GAME OVER!!!!")
    })
})
controller.A.onEvent(ControllerButtonEvent.Released, function on_a_released() {
    mySprite.setImage(assets.image`
        CRY
        `)
    bubble.load_bubble()
})
controller.left.onEvent(ControllerButtonEvent.Repeated, function on_left_repeated() {
    bubble.tilt_angle(bubble.Choice.Left)
})
let mySprite : Sprite = null
bubble.createBoard()
bubble.load_bubble()
mySprite = sprites.create(assets.image`
    CRY
    `, SpriteKind.Player)
mySprite.top = 102
