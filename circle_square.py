import pyglet
shapes = pyglet.shapes

window = pyglet.window.Window()

circle = shapes.Circle(100, 100, 50, color=(255, 0, 0))
square = shapes.Rectangle(window.width/2, window.height/2, 100, 100, color=(0, 255, 0))

@window.event
def on_draw():
  window.clear()

  circle.draw()
  square.draw()

  circle.x += 1
  square.y += 1

pyglet.app.run()
