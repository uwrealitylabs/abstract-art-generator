import sys

# Add the path to Blender's Python to sys.path
blender_python_path = "/Applications/Blender.app/Contents/Resources/3.6/python/lib/python3.10"
sys.path.append(blender_python_path)

# Import bpy
import bpy

# Now bpy should be recognized

# Test
print("Abstract Art Generator by kennynahh and itsanantk")

# Accept the output path as a command-line argument (this is a CLI interface)
output_path = sys.argv[-1]
bpy.context.scene.render.filepath = output_path

# render
bpy.ops.render.render(write_still=True)

# complete
print("Rendering is complete.")

# run the CLI script using:
# blender -b art.blend -P scripts/render.py
# this is assuming you have cd'd into the project file directory