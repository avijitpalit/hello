import subprocess
from PIL import Image

def set(image_path):
    # Command to change the wallpaper
    command = [
        "gsettings", "set", "org.gnome.desktop.background", "picture-uri", f"file://{image_path}"
    ]
    
    # Run the command
    subprocess.run(command, check=True)
    print(f"Wallpaper changed to {image_path}")

def convert_webp_to_png(webp_path, png_path):
  try:
    with Image.open(webp_path) as img:
      img.save(png_path, 'PNG')
  except Exception as e:
    print(f"Error converting image: {e}")
