import sys
import os

# Add the path to Blender's Python to sys.path (Blender 3.6 LTS)
blender_python_path = "/Applications/Blender.app/Contents/Resources/3.6/python/lib/python3.10"
sys.path.append(blender_python_path)

# Import bpy
import bpy

# Name
print("Abstract Art Generator by kennynahh and itsanantk")

# Accept the output path as a command-line argument (this is a CLI interface)
output_path = sys.argv[-1]

# Set the specific file name for rendering
specific_file_name = "output_image.png"
output_file_path = os.path.join(output_path, specific_file_name)
bpy.context.scene.render.filepath = output_file_path

# Clear scene
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()

# Asset import (all obj files)
obj_path = "assets/obj"
obj_files = [f for f in os.listdir(obj_path) if f.endswith('.obj')]
for obj_file in obj_files:
    obj_file_path = os.path.join(obj_path, obj_file)
    bpy.ops.import_scene.obj(filepath=obj_file_path)

# Render
bpy.ops.render.render(write_still=True)

# Complete
print(f"Rendering to {output_file_path} is complete.")
