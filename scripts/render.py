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
"""
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
"""

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
        print(scale_factor, child, child.dimensions, child.location)
        if len(parent.children) > 1:
            min_x = min(min_x, ((child.location.x-(child.dimensions.x/2))*scale_factor))
            max_x = max(max_x, ((child.location.x+(child.dimensions.x/2))*scale_factor))
            min_y = min(min_y, ((child.location.z-(child.dimensions.y/2))*scale_factor))
            max_y = max(max_y, ((child.location.z+(child.dimensions.y/2))*scale_factor))
            min_z = min(min_z, ((child.location.y-(child.dimensions.z/2))*scale_factor))
            max_z = max(max_z, ((child.location.y+(child.dimensions.z/2))*scale_factor))
        else:
            min_x = min(min_x, ((0-(child.dimensions.x/2))*scale_factor))
            max_x = max(max_x, ((0+(child.dimensions.x/2))*scale_factor))
            min_y = min(min_y, ((0-(child.dimensions.y/2))*scale_factor))
            max_y = max(max_y, ((0+(child.dimensions.y/2))*scale_factor))
            min_z = min(min_z, ((0-(child.dimensions.z/2))*scale_factor))
            max_z = max(max_z, ((0+(child.dimensions.z/2))*scale_factor))
            print(max_x,min_x,max_y,min_y,max_z,min_z)
    x = max_x-min_x
    y = max_y-min_y
    z = max_z-min_z
    
    return (x, y, z)

# Find the global location of parent class
def findBoundingBoxLocation(parent):
    min_x = 99e99
    max_x = 0
    min_y = 99e99
    max_y = 0
    min_z = 99e99
    max_z = 0
    for child in parent.children:
        if len(parent.children) > 1:
            min_x = min(min_x, ((child.location.x-(child.dimensions.x/2))*scale_factor))
            max_x = max(max_x, ((child.location.x+(child.dimensions.x/2))*scale_factor))
            min_y = min(min_y, ((child.location.y-(child.dimensions.z/2))*scale_factor))
            max_y = max(max_y, ((child.location.y+(child.dimensions.z/2))*scale_factor))
            min_z = min(min_z, ((child.location.z-(child.dimensions.y/2))*scale_factor))
            max_z = max(max_z, ((child.location.z+(child.dimensions.y/2))*scale_factor))
        else:
            min_x = min(min_x, (((child.dimensions.x/2))*scale_factor))
            max_x = max(max_x, (((child.dimensions.x/2))*scale_factor))
            min_y = min(min_y, (((child.dimensions.z/2))*scale_factor))
            max_y = max(max_y, (((child.dimensions.z/2))*scale_factor))
            min_z = min(min_z, (((child.dimensions.y/2))*scale_factor))
            max_z = max(max_z, (((child.dimensions.y/2))*scale_factor))
        print(parent.location, parent.children, child, parent.location, child.location*scale_factor, child.dimensions*scale_factor, scale_factor)
    x = parent.location.x + (max_x+min_x)/2
    y = parent.location.y + (max_y+min_y)/2
    z = parent.location.z + (max_z+min_z)/2
    print(x,y,z)
    return (x, y, z)

"""
# Find the offset of parent class
def findBoundingBoxOffset(parent):
    min_x = 99e99
    max_x = 0
    min_y = 99e99
    max_y = 0
    min_z = 99e99
    max_z = 0
    for child in parent.children:
        min_x = min(min_x, (child.location.x-((child.dimensions.x/2)*scale_factor)))
        max_x = max(max_x, (child.location.x+((child.dimensions.x/2)*scale_factor)))
        min_y = min(min_y, (child.location.y-((child.dimensions.z/2)*scale_factor)))
        max_y = max(max_y, (child.location.y+((child.dimensions.z/2)*scale_factor)))
        min_z = min(min_z, (child.location.z-((child.dimensions.y/2)*scale_factor)))
        max_z = max(max_z, (child.location.z+((child.dimensions.y/2)*scale_factor)))
    x = (max_x+min_x)/2
    y = (max_y+min_y)/2
    z = (max_z+min_z)/2
    
    return (x, y, z)
"""


# Asset import (all obj files)
obj_path = "assets/obj"
obj_files = [f for f in os.listdir(obj_path) if f.endswith('.obj')]
x = 0
# Set random sizes and positions for imported objects
old_objects = []
new_objects = []
locations = []
dimensions = []
parents = []
for obj_file in obj_files:
    scale_factor = 1
    # Debuging purposes only
    
    if x != 0:
        x += 1
        #continue
    x+=1
    

    old_objects = list(bpy.data.objects)

    obj_file_path = os.path.join(obj_path, obj_file)
    bpy.ops.import_scene.obj(filepath=obj_file_path)
    
    new_objects = list(set(bpy.data.objects) - set(old_objects))    
    
    parent_object = bpy.data.objects.new("GroupParent", None)
    print(new_objects, obj_file)

    materials = []
    # Loop through all new objects
    for imported_object in new_objects:
        # Create a new material or use an existing one
        material_name = str(str(imported_object)+"_mat")
        mat = bpy.data.materials.get(material_name)
          
        bpy.context.view_layer.objects.active = imported_object
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='BOUNDS')
        #imported_object.location = (0,0,0)
        imported_object.parent = parent_object

        if mat is None:
            # Create a new material if it doesn't exist
            mat = bpy.data.materials.new(name=material_name)

        # Assign the material to the object
        if imported_object.data.materials:
            # If the object already has materials, replace the first one
            imported_object.data.materials[0] = mat
        else:
            # If the object has no materials, create a new slot
            imported_object.data.materials.append(mat)

        # Set the color of the material
        mat.diffuse_color = (random.uniform(0,1), random.uniform(0,1), random.uniform(0,1), 1)
        materials.append(mat)
        print(imported_object.dimensions)

    print(new_objects)
    print(findBoundingBoxLocation(parent_object), "new function")    

    print(parent_object.location, "LOCATION")    
    print(parent_object.children[0].dimensions)

    #bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='BOUNDS')
    bbd = list(findBoundingBoxDimensions(parent_object))
    # Scale objects to proportioinality
    size = 1
    print(bbd)
    #scale_factor = size / (bbd[0]+bbd[1]+bbd[2]/3)  # Adjust this value as needed
    scale_factor = size / (max(bbd))  # Adjust this value as needed
    parent_object.scale = (scale_factor, scale_factor, scale_factor)
    print(parent_object.children)
    bbd[0] *= scale_factor
    bbd[1] *= scale_factor
    bbd[2] *= scale_factor
    print(bbd)

    """
    # Set random scale (size) for the object
    scale_factor = random.uniform(0.1, 1.0)
    imported_object.scale = (scale_factor, scale_factor, scale_factor)
    """

    # Set random position for the object
    location_range = 3
    colliding = False
    searching = True
    print(findBoundingBoxDimensions(parent_object), parent_object.dimensions, "parent size")
    print("test", parent_object.location, findBoundingBoxLocation(parent_object), scale_factor, "new function")    

    while searching:
        parent_object.location = (
            random.uniform(-location_range, location_range),
            random.uniform(0, 0),
            random.uniform(-location_range/1.5, location_range/4)
        )
        colliding = False
        for i in range(len(dimensions)):
            # Check x collision
            print(parents[i].location, findBoundingBoxLocation(parents[i]), "lt", dimensions[i], "dt", parent_object.location, findBoundingBoxLocation(parent_object), "l", bbd, "d", parents[i].name, "t", parent_object.name)
            if findBoundingBoxLocation(parent_object)[0] + bbd[0]/2 >= findBoundingBoxLocation(parents[i])[0] - dimensions[i][0]/2:
                if findBoundingBoxLocation(parent_object)[0] - bbd[0] <= findBoundingBoxLocation(parents[i])[0] + dimensions[i][0]/2:
                    print("X collision")
                    # Check z collision
                    if findBoundingBoxLocation(parent_object)[2] + bbd[1]/2 >= findBoundingBoxLocation(parents[i])[2] - dimensions[i][1]/2 and findBoundingBoxLocation(parent_object)[2] - bbd[1]/2 <= findBoundingBoxLocation(parents[i])[2] + dimensions[i][1]/2 :
                        #if parent_object.location.y + bbd[2]/2 >= locations[i][1] - dimensions[i][2]/2 and parent_object.location.y - bbd[2]/2 <= locations[i][1] + dimensions[i][2]/2 :
                            colliding = True
                            print("COLLIDING")


        if not colliding:
            parents.append(parent_object)
            #locations.append(parent_object.location)
            dimensions.append(bbd)
            searching = False
            print("found")
            print(parent_object.location, bbd)

    print(findBoundingBoxLocation(parents[0]),findBoundingBoxLocation(parent_object), parents[0], parent_object, "new function")    
    #parent_object.location = (-2, 0, 0)
    print(findBoundingBoxLocation(parent_object), parent_object.location)
        
camera = bpy.data.objects["Camera"]
camera.location = (0, -10, 3)
c = (72, 0, 0)
pi = math.pi

scene = bpy.data.scenes["Scene"]
scene.camera.rotation_euler[0] = c[0] * (pi / 180.0)
scene.camera.rotation_euler[1] = c[1] * (pi / 180.0)
scene.camera.rotation_euler[2] = c[2] * (pi / 180.0)

light = bpy.data.objects["Light"]
#light.hide_set(True)
#light.hide_render = True

"""
bpy.ops.object.light_add(type='AREA')
print(bpy.context.object)
light_ob = bpy.context.object
light = light_ob.data
"""
light.location = (0, -10, 3)
c = (70, 0, 0)
"""
pi = math.pi
scene = bpy.data.scenes["Scene"]
light.rotation_euler[0] = c[0] * (pi / 180.0)
light.rotation_euler[1] = c[1] * (pi / 180.0)
light.rotation_euler[2] = c[2] * (pi / 180.0)       
"""
print(type(light))
print(findBoundingBoxDimensions(parents[0]), findBoundingBoxLocation(parents[0]), parents[0].location)
#bpy.ops.mesh.primitive_plane_add(size=0.4, enter_editmode=False, align='WORLD', location=(0, 0, 0))

# Render
bpy.ops.render.render(write_still=True)

# Complete
print("Rendering is complete.")

# Run using the following CLI line while cd'd into the abstract-art-generator file (or open a terminal there):
# blender -b art.blend -P scripts/render.py 