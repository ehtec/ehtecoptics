import FreeCAD
import FreeCADGui
import lens
import FreeCAD as App

class Convert_To_Lens_Class():
    """My new command"""

    def GetResources(self):
	iconpath = FreeCAD.getUserAppDataDir().encode("utf-8")+'Mod/ehtecoptics/resources/lens.svg.png'
	#iconpath ='/home/pi/.FreeCAD/Mod/ehtecoptics/resources/lens.svg'
	#print iconpath
        return {'Pixmap'  : iconpath, # the name of a svg file available in the resources
                'Accel' : "Shift+L", # a default shortcut (optional)
                'MenuText': "Convert To Lens",
                'ToolTip' : "Converts a solid to a lens"}

    def Activated(self):
        "Do something here"
	theobj = App.ActiveDocument.ActiveObject
	alens = lens.makeLens()
	theshape = theobj.Shape
	alens.Shape = theshape
	theobj.ViewObject.Visibility = False
	alens.ViewObject.Transparency = 50
	alens.ViewObject.ShapeColor=(176.0/255,224.0/255,230.0/255)
        return

    def IsActive(self):
        """Here you can define if the command must be active or not (greyed) if certain conditions
        are met or not. This function is optional."""
        return True

FreeCADGui.addCommand('Convert_To_Lens',Convert_To_Lens_Class())
