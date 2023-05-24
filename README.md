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
- All you need to do is run `python all.py` it will
  - create all the output folders and main root `before` and `after` folders
    #### - `!!! make sure you have images in the before folder`
  - take all the images from the before folder and resize them and put them in the `resize` folder
    - greyscale all the images in the resize folder and save them in the `greyscale` folder
    - blur all the images in the resize folder and save them in the `blur` folder
    - over expose all the images in the resize folder and save them in the `over_expose` folder
    - darken all the images in the resize folder and save them in the `darken` folder
    - add noise to all the images in the resize folder and save them in the `noise` folder
