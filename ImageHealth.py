import os
import subprocess
import magic
from PIL import Image

def is_image(file_path):
    mime = magic.Magic(mime=True)
    try:
        file_type = mime.from_file(file_path)
        return file_type.split('/')[0] == 'image'  # Check if file is an image
    except magic.MagicException:
        return False  # Unable to determine file type

def is_image(filename):
    # Check if the file has a recognized image file extension
    image_extensions = ['png', 'jpg', 'jpeg', 'gif', 'bmp']
    if filename.split('.')[-1].lower() in image_extensions:
        return True
    else:
        return False

def is_image_corrupt(file_path):
    if not is_image(file_path):
        return False  # Not an image file
    try:
        # Attempt to open the image
        with Image.open(file_path) as img:
            # Attempt to load the image data
            img.load()
        return False  # Image is not corrupt
    except (IOError, OSError):
        return True  # Image is corrupt

def add_private_label(file_path):
    applescript = '''
    set posixPath to "%s"

    tell application "Finder"
        set theFile to POSIX file posixPath as alias
        set label index of theFile to 2
    end tell
    ''' % file_path
    subprocess.run(['osascript', '-e', applescript])

def find_and_tag_corrupt_images(directory):
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            if is_image(file_path) and is_image_corrupt(file_path):
                add_private_label(file_path)

directory = "/DIRECTORY/"
find_and_tag_corrupt_images(directory)