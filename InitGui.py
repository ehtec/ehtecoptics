import FreeCAD

# Import all command modules to register them with FreeCAD
import convert_to_lens
import convert_to_absorber
import convert_to_mirror
import single_ray_laser
import rectangular_laser
import circular_laser
import render_command


class ehtecOptics(Workbench):
    MenuText = "ehtec Optics"
    ToolTip = "A description of my workbench"
    # Icon = """/home/pi/.FreeCAD/Mod/ehtecoptics/resources/ehtec.svg"""
    Icon = FreeCAD.getUserAppDataDir() + "Mod/ehtecoptics/resources/lens.svg"

    def Initialize(self):
        "This function is executed when FreeCAD starts"
        self.list = ["Convert_To_Lens", "Convert_To_Absorber", "Convert_To_Mirror", "Single_Ray_Laser",
                     "Rectangular_Laser", "Circular_Laser",
                     "Render"]  # A list of command names created in the line above
        self.appendToolbar("My Commands", self.list)  # creates a new toolbar with your commands
        self.appendMenu("My New Menu", self.list)  # creates a new menu
        self.appendMenu(["An existing Menu", "My submenu"], self.list)  # appends a submenu to an existing menu

    def Activated(self):
        "This function is executed when the workbench is activated"
        return

    def Deactivated(self):
        "This function is executed when the workbench is deactivated"
        return

    def ContextMenu(self, recipient):
        "This is executed whenever the user right-clicks on screen"
        # "recipient" will be either "view" or "tree"
        self.appendContextMenu("My commands", self.list)  # add commands to the context menu

    def GetClassName(self):
        # this function is mandatory if this is a full python workbench
        return "Gui::PythonWorkbench"


Gui.addWorkbench(ehtecOptics())
