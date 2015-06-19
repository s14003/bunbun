import pyglet
import resources

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480


window = pyglet.window.Window(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)

window = pyglet.window.Window()
sprite_batch = pyglet.graphics.Batch()
sam_sprites = []
sam0_speed_x = 0

sam_part = resources.sam.get_region(x=0,y=0,width=32,height=48)
sam_sprites.append(pyglet.sprite.Sprite(sam_part,x=200,y=200, batch= sprite_batch))



@window.event ##デコレートは上の変数名と同じ

def on_draw(): ##オーバーライドしている
    window.clear()
    sprite_batch.draw()

@window.event
def on_key_press(symbol,modifiers):
    from pyglet.window import key
    global sam0_speed_x
    if symbol == key.LEFT:
        sam0_speed_x -= 20
    elif symbol == key.RIGHT:
        sam0_speed_x += 20
    elif symbol == key.UP:
        sam_sprites[0].y += 20
    elif symbol == key.DOWN:
        sam_sprites[0].y -= 20
    elif symbol== key.SPACE:
        import random
        x = int(random.random() * WINDOW_WIDTH)
        y = int(random.random() * WINDOW_HEIGHT)
        sam_sprites.append(pyglet.sprite.Sprite(sam_part,x=x,y=y, batch=sprite_batch))


@window.event
def on_key_release(symbol,modifiers):
    global sam0_speed_x
    from pyglet.window import key
    if symbol == key.LEFT:
        sam0_speed_x += 20
    elif symbol == key.RIGHT:
        sam0_speed_x -= 20



def update(dt):##ただの関数
    sam_sprites[0].x += sam0_speed_x


if __name__ == '__main__':
    pyglet.clock.schedule_interval(update,1/30)
    pyglet.app.run()


