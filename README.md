## FreeCAD ehtecoptics workbench

ehtecoptics is a FreeCAD extension for modeling 3D lenses, snell's law, and so on.

## Screenshots


## Prerequisites

* [FreeCAD](https://freecad.org) v0.19 or higher
* Python3
* NumPY

## Installation

* Install FreeCAD 

  ```bash
  sudo apt-get install freecad
  ```

* Install Python Numpy

  Debian/Ubuntu
    ```bash
    sudo apt-get install python-numpy
    ```
  pip
    ```bash
    pip3 install numpy
    ```

* Copy the ehtecoptics directory to your `.FreeCAD/Mod` directory.
* Start FreeCAD. A new workbench named `ehtec Optics` will be available in the workbench dropdown menu.

## Usage

1. Start FreeCAD
2. Open the Part workbench from the workbench dropdown menu.
3. Create a part object of your choice.
4. Change to the ehtecoptics workbench (in the workbench dropdown menu)
5. Select the solid you created and click on the first icon in the menu (hovering over it you will see: "convert a solid to a lens")
6. Click on the second icon in the menu to create a laser.
7. Move the Lens in front of the Laser via `Edit -> Placement`
8. Open the Python Console (View menu).
9. Type `import render` and press `Enter`.
10. Then type `render.render()` and press `Enter`.  

**Result:** You may need to wait a few seconds, depending on your cpu. The program will render a beam through the lens.

**Notes:** 
* You can change the color of the beam by changing the Wavelength property of the laser.
* You can make a multi-ray-laser by clicking the relevant button.
