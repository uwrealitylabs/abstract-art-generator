import bpy
import sys

# Test
print("Abstract Art Generator by kennynahh and itsanantk")

# Accept the output path as a command-line argument (this is a CLI interface)
output_path = sys.argv[-1]
bpy.context.scene.render.filepath = output_path

# render
bpy.ops.render.render(write_still=True)

# complete
print("Rendering is complete.")