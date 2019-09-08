ehtecoptics is a FreeCAD extension for modelling 3D lenses, snell's law, and so on.

1) installation

Install FreeCAD from the website or from the repositories if you use Debian or Ubuntu.

sudo apt-get install freecad

Install Python Numpy.

sudo apt-get install python-numpy

OR

pip install numpy

OR

from the website. You need to have Python 2.7 installed.

Copy the ehtecoptics directory to your .FreeCAD/Mod directory.

When you start FreeCAD, you will find a Workbench named ehtec Optics in the workbench menu.

2) Usage

Create a part object of your choice using the part Workbench.

Change to the ehtecoptics workbench. Select the solid you created and click on the first icon in the menu ( when you hover over it you will see: "convert a solid to a lens") #todo: change icon

Click on the second icon in the menu to create a laser. Move the Lens in front of the Laser via Edit -> Placement.

Open the Python Console (View menu.) Type "import render" (without the quotes) and press Return. Then type "render.render()" again without quotes and press return. You may need to wait a few seconds, depending on your cpu. The program will render a beam through the lens.

You can change the color of the beam by changing the Wavelength property of the laser. You can make a multi-ray-laser by typing "import laser" and then "laser.makeRectangularLaser". #todo: make accessible by button
