# This is some testing code I wrote in order to setup minification/optimized exporting for ezcv: https://github.com/Descent098/ezcv

import os             # Used to do path manipulation
from glob import glob # Used to process multiple file paths
from PIL import Image # Used to process images
# Used to process and minify html/css/js
from css_html_js_minify import process_single_html_file, process_single_js_file, process_single_css_file

def minify_files(directory:str):
    """Goes through and minifies html, css, js and image files in directory

    Notes
    -----
    - This assumes you are following the standard template layout: https://ezcv.readthedocs.io/en/latest/theme-development/#folder-layout
    - Only image extensions supported are:

        - .jpg
        - .png
        - .jpeg

    Parameters
    ----------
    directory : str
        The directory you want to minify all files from
    """

    # Minify html/css/js
    ## Find all the files
    html = glob(f'{directory}{os.sep}*.html')
    css = glob(f'{os.path.join(os.path.join(directory, "css"))}{os.sep}*.css')
    js = glob(f'{os.path.join(os.path.join(directory, "js"))}{os.sep}*.js')

    ## Itterate through each file type and minify them
    for file in html:
        process_single_html_file(file, overwrite=True)
    for file in css:
        process_single_css_file(file, overwrite=True)
    for file in js:
        process_single_js_file(file, overwrite=True)

    # Find and process/minify images
    ## Find each file type
    png = glob(f'{os.path.join(os.path.join(directory, "images"))}{os.sep}*.png')
    jpg = glob(f'{os.path.join(os.path.join(directory, "images"))}{os.sep}*.jpg')
    jpeg = glob(f'{os.path.join(os.path.join(directory, "images"))}{os.sep}*.jpeg')

    ## Itterate through the full list of paths and minify
    for extension in [png, jpg, jpeg]:
        if extension: # if list is not empty
            for image in extension:
                pil_object = Image.open(image)
                pil_object.save(image, optimize=True, quality=85)

if __name__ == "__main__":
    directory = "site" # The directory to minify files in
    minify_files(directory)