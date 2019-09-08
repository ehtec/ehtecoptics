import FreeCAD
import FreeCADGui
import absorber
import FreeCAD as App

class Convert_To_Absorber_Class():
    """My new command"""

    def GetResources(self):
	iconpath = FreeCAD.getUserAppDataDir().encode("utf-8")+'Mod/ehtecoptics/resources/absorber.svg.png'
	#iconpath ='/home/pi/.FreeCAD/Mod/ehtecoptics/resources/ehtec.svg'
	#print iconpath
        return {'Pixmap'  : iconpath, # the name of a svg file available in the resources
                'Accel' : "Shift+A", # a default shortcut (optional)
                'MenuText': "Convert To Absorber",
                'ToolTip' : "Converts a solid to an absorber"}

    def Activated(self):
        "Do something here"
	theobj = App.ActiveDocument.ActiveObject
	aabsorber = absorber.makeAbsorber()
	theshape = theobj.Shape
	aabsorber.Shape = theshape
	theobj.ViewObject.Visibility = False
	aabsorber.ViewObject.ShapeColor=(0.0/255,0.0/255,0.0/255)
        return

    def IsActive(self):
        """Here you can define if the command must be active or not (greyed) if certain conditions
        are met or not. This function is optional."""
        return True

FreeCADGui.addCommand('Convert_To_Absorber',Convert_To_Absorber_Class())

