import FreeCAD as App
import FreeCADGui
import FreeCAD
import Part

class Mirror:
    def __init__(self, obj):
        '''"App two point properties" '''
        obj.addProperty("App::PropertyBool", "Activated", "Lens Workbench").Activated = True
        obj.Proxy = self

    def execute(self, fp):
        '''"Print a short message when doing a recomputation, this method is mandatory" '''
	pass

def makeMirror():
	a=FreeCAD.ActiveDocument.addObject("Part::FeaturePython","Mirror")
	Mirror(a)
	a.ViewObject.Proxy=0 # just set it to something different from None (this assignment is needed to run an internal notification)
	FreeCAD.ActiveDocument.recompute()
	return a
