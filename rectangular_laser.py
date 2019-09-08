import FreeCAD
import FreeCADGui
import laser
import FreeCAD as App

class Rectangular_Laser_Class():
    """My new command"""

    def GetResources(self):
	iconpath = FreeCAD.getUserAppDataDir().encode("utf-8")+'Mod/ehtecoptics/resources/rectangularlaser.svg.png'
	#iconpath ='/home/pi/.FreeCAD/Mod/ehtecoptics/resources/ehtec.svg'
	#print iconpath
        return {'Pixmap'  : iconpath, # the name of a svg file available in the resources
                'Accel' : "Shift+R", # a default shortcut (optional)
                'MenuText': "Rectangular Laser",
                'ToolTip' : "Creates a rectangular laser"}

    def Activated(self):
        "Do something here"
	laser.makeRectangularLaser()
	return

    def IsActive(self):
        """Here you can define if the command must be active or not (greyed) if certain conditions
        are met or not. This function is optional."""
        return True

FreeCADGui.addCommand('Rectangular_Laser',Rectangular_Laser_Class())
