import sys
import os
import bpy
import random
import math

# Detect operating system
is_windows = sys.platform == "win32"
is_macos = sys.platform == "darwin"

# Example paths for Blender 3.6 LTS
if is_windows:
    blender_python_path = r"C:\Program Files\Blender Foundation\Blender 3.6\3.6\python\lib\python3.10"
elif is_macos:
    blender_python_path = "/Applications/Blender.app/Contents/Resources/3.6/python/lib/python3.10"
else:
    # Add more cases for other operating systems if needed
    raise ValueError("Unsupported operating system")

# Add the path to Blender's Python to sys.path
sys.path.append(blender_python_path)

# Name
print("Abstract Art Generator by kennynahh and itsanantk")

# Prompt the user to choose the rendering engine
render_engine_choice = input("Choose rendering engine ('C' or 'E' for Cycles or Eevee): ").strip().upper()

# Validate the user input and set the rendering engine accordingly (case-insensitive)
if render_engine_choice in ['C', 'CYCLES']:
    bpy.context.scene.render.engine = 'CYCLES'
elif render_engine_choice in ['E', 'EEVEE']:
    bpy.context.scene.render.engine = 'BLENDER_EEVEE'
else:
    print("Invalid choice. Defaulting to Eevee.")
    bpy.context.scene.render.engine = 'BLENDER_EEVEE'


# Accept the output path as a command-line argument (this is a CLI interface)
output_path = sys.argv[-1]
bpy.context.scene.render.filepath = output_path

# Clear scene
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()

# Find the outline size of parent class
def findBoundingBoxDimensions(parent):
    min_x = 99e99
    max_x = 0
    min_y = 99e99
    max_y = 0
    min_z = 99e99
    max_z = 0
    for child in parent.children:
        min_x = min(min_x, (child.location.x-child.dimensions.x/2))
        max_x = max(max_x, (child.location.x+child.dimensions.x/2))
        min_y = min(min_y, (child.location.y-child.dimensions.z/2))
        max_y = max(max_y, (child.location.y+child.dimensions.z/2))
        min_z = min(min_z, (child.location.z-child.dimensions.y/2))
        max_z = max(max_z, (child.location.z+child.dimensions.y/2))
    x = max_x-min_x
    y = max_y-min_y
    z = max_z-min_z
    
    return (x, y, z)


# Asset import (all obj files)
obj_path = "assets/obj"
obj_files = [f for f in os.listdir(obj_path) if f.endswith('.obj')]
x = 0
# Set random sizes and positions for imported objects
old_objects = []
new_objects = []
locations = []
dimensions = []
for obj_file in obj_files:

    # Debuging purposes only
    #if x <= 3:
    #    x += 1
    #    continue

    old_objects = list(bpy.data.objects)

    obj_file_path = os.path.join(obj_path, obj_file)
    bpy.ops.import_scene.obj(filepath=obj_file_path)
    
    new_objects = list(set(bpy.data.objects) - set(old_objects))    
    
    parent_object = bpy.data.objects.new("GroupParent", None)

    # Loop through all new objects
    for imported_object in new_objects:
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='BOUNDS')
        imported_object.parent = parent_object

    bbd = list(findBoundingBoxDimensions(parent_object))

    # Scale objects to proportioinality
    size = 1.5
    #scale_factor = size / (bbd[0]+bbd[1]+bbd[2]/3)  # Adjust this value as needed
    scale_factor = size / (max(bbd))  # Adjust this value as needed
    parent_object.scale = (scale_factor, scale_factor, scale_factor)
    bbd[0]*=scale_factor
    bbd[1]*=scale_factor
    bbd[2]*=scale_factor
    
    """
    # Set random scale (size) for the object
    scale_factor = random.uniform(0.1, 1.0)
    imported_object.scale = (scale_factor, scale_factor, scale_factor)
    """

    # Set random position for the object
    location_range = 3.5
    colliding = False
    searching = True
    while searching:
        parent_object.location = (
            random.uniform(-location_range, location_range),
            random.uniform(0, 0),
            random.uniform(-location_range/1.5, location_range/4)
        )
        colliding = False
        for i in range(len(locations)):
            # Check x collision
            if parent_object.location.x + bbd[0]/2 >= locations[i][0] - dimensions[i][0]/2 and parent_object.location.x - bbd[0] <= locations[i][0] + dimensions[i][0]/2:
                    # Check y collision
                    if parent_object.location.z + bbd[1]/2 >= locations[i][2] - dimensions[i][1]/2 and parent_object.location.z - bbd[1]/2 <= locations[i][2] + dimensions[i][1]/2 :
                        #if parent_object.location.y + bbd[2]/2 >= locations[i][1] - dimensions[i][2]/2 and parent_object.location.y - bbd[2]/2 <= locations[i][1] + dimensions[i][2]/2 :
                            colliding = True


        if not colliding:
            locations.append(parent_object.location)
            dimensions.append(bbd)
            searching = False
            print("found")
        
camera = bpy.data.objects["Camera"]
camera.location = (0, -10, 3)
c = (70, 0, 0)
pi = math.pi
scene = bpy.data.scenes["Scene"]
scene.camera.rotation_euler[0] = c[0] * (pi / 180.0)
scene.camera.rotation_euler[1] = c[1] * (pi / 180.0)
scene.camera.rotation_euler[2] = c[2] * (pi / 180.0)
            

bpy.context.active_object.scale= (50, 50, 50)

# Render
bpy.ops.render.render(write_still=True)

# Complete
print("Rendering is complete.")

# Run using the following CLI line while cd'd into the abstract-art-generator file (or open a terminal there):
# blender -b art.blend -P scripts/render.py