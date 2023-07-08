import pyglet

window = pyglet.window.Window()

label = pyglet.text.Label(
  'Hello, world',
  font_name='Times New Roman',
  font_size=36,
  x=window.width//2, y=window.height//2,
  anchor_x='center', anchor_y='center')

label2 = pyglet.text.Label(
  '你好世界！',
  font_name='Arial',
  font_size=48,
  x=100, y=400)

@window.event
def on_draw():
  window.clear()
  label.draw()
  label2.draw()

pyglet.app.run()
