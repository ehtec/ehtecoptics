import FreeCAD


class Lens:
    def __init__(self, obj):
        '''"App two point properties" '''
        obj.addProperty("App::PropertyFloat", "Refractive index", "Lens Workbench").Refractive_index = 1.5
        obj.addProperty("App::PropertyBool", "Activated", "Lens Workbench").Activated = True
        obj.Proxy = self

    def execute(self, fp):
        '''"Print a short message when doing a recomputation, this method is mandatory" '''
        pass


def makeLens():
    a = FreeCAD.ActiveDocument.addObject("Part::FeaturePython", "Lens")
    Lens(a)
    a.ViewObject.Proxy = 0  # just set it to something different from None (this assignment is needed to run an internal notification)
    FreeCAD.ActiveDocument.recompute()
    return a
