# Image Corruption Checker

This Python script checks for corrupt images in a specified directory and tags them as private using macOS Finder labels.

## Installation

### Prerequisites
- Python 3.x
- `magic` library (Install using `pip install python-magic-bin`)
- `Pillow` library (Install using `pip install Pillow`)

## Usage

1. Clone this repository or download the script `corrupt_image_checker.py`.
2. Install the required libraries as mentioned in the prerequisites.
3. Replace `"/DIRECTORY/"` in the script with the path to the directory you want to scan for corrupt images.
4. Run the script using the command `python corrupt_image_checker.py`.
5. The script will search for corrupt images in the specified directory and tag them as private in macOS Finder.

## Functionality

- The script first checks if a file is an image based on its MIME type.
- It then verifies if the image file is corrupt by attempting to open and load the image using the `Pillow` library.
- If the image is found to be corrupt, it tags it as private using macOS Finder labels.

## Notes

- This script is specifically designed for macOS systems due to its reliance on Finder labels.
- Ensure that the directory path provided is accessible and contains the images you want to check for corruption.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

