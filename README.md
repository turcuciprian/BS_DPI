# Usage Instructions

- install poetry on your system
- install python if not installed

### Install packages

- in your root folder switch to poetry environment:

`poetry shell`

- Install dependencies

`poetry install`

### Code instructions

- All the scripts are in separate py files in the scripts folder
- All you need to do is run `python all.py` inside of the scripts folder
  - create all the output folders and main root `before` and `after` folders
    #### - `!!! make sure you have images in the before folder`
    The script will
      - take all the images from the before folder and resize them and put them in the `resize` folder
      - greyscale all the images in the resize folder and save them in the `greyscale` folder
      - blur all the images in the resize folder and save them in the `blur` folder
      - over expose all the images in the resize folder and save them in the `over_expose` folder
      - darken all the images in the resize folder and save them in the `darken` folder
      - add noise to all the images in the resize folder and save them in the `noise` folder
    At the end, it will:
      - take all the images from each folder and put them in `after/all/images` with the prefix of each file being the parent pfoder name (ex: parentFolder_filename.jpg)
      - take all the images in the `after/mask` folder and use the above prefix name to generate that exact (with prefix) name, like the previous point, into the `after/all/masks` folder, so that all the `after/all/images` have a coresponding mask, with the image exact name (the version with the prefix)
