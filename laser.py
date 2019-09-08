import FreeCAD
import FreeCAD as App
import FreeCADGui
import wavelen2rgb
import Part
from vect_ops import *
#import numpy as np
#from math import sin, cos, pi
#import Draft
#import render

class SingleRayLaser:
	def __init__(self, obj):
		'''"App two point properties" '''
		obj.addProperty("App::PropertyFloat", "Wavelength", "Lens Workbench").Wavelength = 650.0 #nanometer
		obj.addProperty("App::PropertyFloat", "Power", "Lens Workbench").Power = 1.0 #milliwatt
		obj.addProperty("App::PropertyBool", "Activated", "Lens Workbench").Activated = True
		obj.Proxy = self
		obj.Shape = Part.makeCylinder(2.0,15.0)

	def execute(self, fp):
		'''"Print a short message when doing a recomputation, this method is mandatory" '''
		wres=wavelen2rgb.wavelen2rgb(fp.Wavelength)
		lcol=tuple([x/255.0 for x in wres])
		col=[(0.8,0.8,0.8),lcol,(0.8,0.8,0.8)]
		fp.ViewObject.DiffuseColor=col

class RectangularLaser:
	def __init__(self, obj):
		'''"App two point properties" '''
		obj.addProperty("App::PropertyFloat", "Wavelength", "Lens Workbench").Wavelength = 650.0 #nanometer
		obj.addProperty("App::PropertyFloat", "Power", "Lens Workbench").Power = 1.0 #milliwatt
		obj.addProperty("App::PropertyBool", "Activated", "Lens Workbench").Activated = True
		obj.addProperty("App::PropertyFloat", "Width", "Lens Workbench").Width = 10 #mm
		obj.addProperty("App::PropertyFloat", "Height", "Lens Workbench").Height = 10 #mm
		obj.addProperty("App::PropertyFloat", "Length", "Lens Workbench").Length = 30 #mm
		obj.addProperty("App::PropertyFloat", "Density", "Lens Workbench").Density = 1 #rays/mm
		#obj.setEditorMode("Width",1)
		#obj.setEditorMode("Height",1)
		obj.Proxy = self
		obj.Shape = Part.makeBox(obj.Height, obj.Width, obj.Length)

	def execute(self, fp):
		'''"Print a short message when doing a recomputation, this method is mandatory" '''
		wres=wavelen2rgb.wavelen2rgb(fp.Wavelength)
		lcol=tuple([x/255.0 for x in wres])
		col=[(0.8,0.8,0.8),(0.8,0.8,0.8),(0.8,0.8,0.8),(0.8,0.8,0.8),(0.8,0.8,0.8),lcol]
		fp.ViewObject.DiffuseColor=col
		fp.Shape = Part.makeBox(fp.Height, fp.Width, fp.Length)

class CircularLaser:
	def __init__(self, obj):
		'''"App two point properties" '''
		obj.addProperty("App::PropertyFloat", "Wavelength", "Lens Workbench").Wavelength = 650.0 #nanometer
		obj.addProperty("App::PropertyFloat", "Power", "Lens Workbench").Power = 1.0 #milliwatt
		obj.addProperty("App::PropertyBool", "Activated", "Lens Workbench").Activated = True
		obj.addProperty("App::PropertyFloat", "Radius", "Lens Workbench").Radius = 5 #mm
#		obj.addProperty("App::PropertyFloat", "Height", "Lens Workbench").Height = 10 #mm
		obj.addProperty("App::PropertyFloat", "Length", "Lens Workbench").Length = 30 #mm
		obj.addProperty("App::PropertyFloat", "Density", "Lens Workbench").Density = 1 #rays/qmm
		#obj.setEditorMode("Width",1)
		#obj.setEditorMode("Height",1)
		obj.Proxy = self
		obj.Shape = Part.makeCylinder(obj.Radius, obj.Length)

	def execute(self, fp):
		'''"Print a short message when doing a recomputation, this method is mandatory" '''
		wres=wavelen2rgb.wavelen2rgb(fp.Wavelength)
		lcol=tuple([x/255.0 for x in wres])
		col=[(0.8,0.8,0.8),lcol,(0.8,0.8,0.8)]
		fp.ViewObject.DiffuseColor=col
		fp.Shape = Part.makeCylinder(fp.Radius, fp.Length)

def makeSingleRayLaser():
	a=FreeCAD.ActiveDocument.addObject("Part::FeaturePython","SingleRayLaser")
	SingleRayLaser(a)
	a.ViewObject.Proxy=0 # just set it to something different from None (this assignment is needed to run an internal notification)
	FreeCAD.ActiveDocument.recompute()
	return a

def makeRectangularLaser():
	a=FreeCAD.ActiveDocument.addObject("Part::FeaturePython","RectangularLaser")
	RectangularLaser(a)
	a.ViewObject.Proxy=0 # just set it to something different from None (this assignment is needed to run an internal notification)
	FreeCAD.ActiveDocument.recompute()
	return a

def makeCircularLaser():
	a=FreeCAD.ActiveDocument.addObject("Part::FeaturePython","CircularLaser")
	CircularLaser(a)
	a.ViewObject.Proxy=0 # just set it to something different from None (this assignment is needed to run an internal notification)
	FreeCAD.ActiveDocument.recompute()
	return a


