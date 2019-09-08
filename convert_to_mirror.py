import FreeCAD
import FreeCADGui
import mirror
import FreeCAD as App

class Convert_To_Mirror_Class():
    """My new command"""

    def GetResources(self):
	iconpath = FreeCAD.getUserAppDataDir().encode("utf-8")+'Mod/ehtecoptics/resources/mirror.svg.png'
	#iconpath ='/home/pi/.FreeCAD/Mod/ehtecoptics/resources/ehtec.svg'
	#print iconpath
        return {'Pixmap'  : iconpath, # the name of a svg file available in the resources
                'Accel' : "Shift+A", # a default shortcut (optional)
                'MenuText': "Convert To Absorber",
                'ToolTip' : "Converts a solid to a mirror"}

    def Activated(self):
        "Do something here"
	theobj = App.ActiveDocument.ActiveObject
	amirror = mirror.makeMirror()
	theshape = theobj.Shape
	amirror.Shape = theshape
	theobj.ViewObject.Visibility = False
	amirror.ViewObject.ShapeColor=(131.0/255,137.0/255,150.0/255)
        return

    def IsActive(self):
        """Here you can define if the command must be active or not (greyed) if certain conditions
        are met or not. This function is optional."""
        return True

FreeCADGui.addCommand('Convert_To_Mirror',Convert_To_Mirror_Class())

