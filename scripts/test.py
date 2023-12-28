import bpy
# Test
print("Abstract Art Generator by kennynahh and itsanantk")

# Set the output path for the rendered image
bpy.context.scene.render.filepath = "//render_output.png"

# Render the scene
bpy.ops.render.render(write_still=True)
