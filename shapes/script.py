import shapes

def draw_shape(shape_name="box", character="x", line_breaks=True):
  shape = shapes.draw_shape(shape_name, character)
  if not line_breaks:
    print(shape[1:-1])
  else:
    print(shape)

# call draw_shape() with keyword arguments here:
def get_params():
  character = input("Enter character name \n > ")
  if character:
    shape_name = input("Enter shape type (box/triangle) \n > ")
  if shape_name:
    draw_shape(character, shape_name, line_breaks=False)

get_params()