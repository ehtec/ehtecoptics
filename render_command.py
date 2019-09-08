import FreeCAD
import FreeCADGui
import render
import FreeCAD as App

class Render_Class():
    """My new command"""

    def GetResources(self):
	iconpath = FreeCAD.getUserAppDataDir().encode("utf-8")+'Mod/ehtecoptics/resources/render.svg.png'
	#iconpath ='/home/pi/.FreeCAD/Mod/ehtecoptics/resources/ehtec.svg'
	#print iconpath
        return {'Pixmap'  : iconpath, # the name of a svg file available in the resources
                'Accel' : "Shift+X", # a default shortcut (optional)
                'MenuText': "Render",
                'ToolTip' : "Performs the rendering"}

    def Activated(self):
        "Do something here"
	render.render()
	return

    def IsActive(self):
        """Here you can define if the command must be active or not (greyed) if certain conditions
        are met or not. This function is optional."""
        return True

FreeCADGui.addCommand('Render',Render_Class())
