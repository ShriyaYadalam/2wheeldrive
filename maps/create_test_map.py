#!/usr/bin/env python3
"""
Simple script to create a test map for RViz debugging
"""
import numpy as np
from PIL import Image
import os

def create_test_map():
    # Create a 80x80 pixel map (4m x 4m at 0.05m resolution)
    size = 80
    
    # Create map data (0 = free, 128 = unknown, 255 = occupied)
    map_data = np.full((size, size), 128, dtype=np.uint8)  # Start with unknown
    
    # Add free space in the center
    map_data[20:60, 20:60] = 254  # Free space (white)
    
    # Add some walls/obstacles
    map_data[10:15, :] = 0      # Top wall (black)
    map_data[65:70, :] = 0      # Bottom wall
    map_data[:, 10:15] = 0      # Left wall
    map_data[:, 65:70] = 0      # Right wall
    
    # Add some interior obstacles
    map_data[30:35, 30:35] = 0  # Small obstacle
    map_data[45:50, 45:50] = 0  # Another obstacle
    
    # Create PIL Image and save as PGM
    img = Image.fromarray(map_data, mode='L')
    
    # Save the map
    img.save('test_map.pgm')
    print("Created test_map.pgm")
    
    # Also create the YAML content
    yaml_content = """image: test_map.pgm
resolution: 0.05 
origin: [-2.0, -2.0, 0.0]
negate: 0
occupied_thresh: 0.65
free_thresh: 0.196"""
    
    with open('test_map.yaml', 'w') as f:
        f.write(yaml_content)
    print("Created test_map.yaml")
    
    print("\nMap details:")
    print(f"Size: {size}x{size} pixels")
    print(f"Real size: {size*0.05}m x {size*0.05}m")
    print(f"Origin: (-2.0, -2.0)")
    print(f"Resolution: 0.05 m/pixel")

if __name__ == "__main__":
    create_test_map()
