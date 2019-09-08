import FreeCAD
import FreeCAD as App
import FreeCADGui
import wavelen2rgb
import Part
from vect_ops import *
import numpy as np
#from math import sin, cos, pi
import Draft
import spreadpoints

MAXRAYLENGTH = 1000 #mm

SURROUNDING_N = 1.0 #refractive index of air

#lenses = ["Lens"]

#global A
#global B
#global A_v
#global B_v
#global remaining_distance
#global n
#global next_ray


#A_v = FreeCAD.Vector(0,0,0)
#B_v = FreeCAD.Vector(0,0,0)
#A = np.array([0,0,0])
#B = np.array([0,0,0])
#remaining_distance = MAXRAYLENGTH
#n= SURROUNDING_N
#next_ray = np.array([0,0,0])


def render():
	A_v = FreeCAD.Vector(0,0,0)
	B_v = FreeCAD.Vector(0,0,0)
	A = np.array([0,0,0])
	B = np.array([0,0,0])
	remaining_distance = MAXRAYLENGTH
	n= SURROUNDING_N
	next_ray = np.array([0,0,0])
	#global A
	#global B
	#global A_v
	#global B_v
	#global remaining_distance
	#global n
	#global next_ray
	#remaining_distance = MAXRAYLENGTH
	#obj = App.ActiveDocument.Laser
	#get all lenses and rays in the document
	objs = App.ActiveDocument.Objects
	objnames = [aobj.Name for aobj in objs]
	lenses = [alensname for alensname in objnames if "Lens" in alensname]
	#remove all lenses which are not Activated
	lenses = [alensname for alensname in lenses if App.ActiveDocument.getObject(alensname).Activated ]
	#get all absorbers
	absorbers = [aabsorbername for aabsorbername in objnames if "Absorber" in aabsorbername]
	#remove all absorbers which are not activated
	absorbers = [aabsorbername for aabsorbername in absorbers if App.ActiveDocument.getObject(aabsorbername).Activated]
	#get all mirrors
	mirrors = [amirrorname for amirrorname in objnames if "Mirror" in amirrorname]
	#remove all mirrors which are nkt Activated
	mirrors = [amirrorname for amirrorname in mirrors if App.ActiveDocument.getObject(amirrorname).Activated]
	#remove the ray folder if existent
	grp = None
	if App.ActiveDocument.getObject("Rays") is not None:
                App.ActiveDocument.removeObject("Rays")
        #create new Ray folder
        grp = App.ActiveDocument.addObject("App::DocumentObjectGroup","Rays")
	#get the rays
	lines = [alinename for alinename in objnames if "Line" in alinename]
	#remove all lines
	for alinename in lines:
		App.ActiveDocument.removeObject(alinename)
	lines = [] 
	#get all lasers
	lasers = [alasername for alasername in objnames if "Laser" in alasername]
	beams = []
	for laser in lasers:
                #beams = []
		obj = App.ActiveDocument.getObject(laser)
		if obj.Activated == False:
			continue
                #set up the laser ray by laser type
		if "SingleRayLaser" in obj.Name:
                        #type is SingleRayLaser
                        A = np.array([obj.Placement.Base.x,obj.Placement.Base.y,obj.Placement.Base.z])
                        #rot = obj.Placement.Rotation.toEuler()
                        #crx = rot[2] #roll
                        #cry = rot[1] #pitch
                        #crz = rot[0] #yaw
                        #crx = crx * np.pi / 180.0
                        #cry = cry * np.pi / 180.0
                        #crz = crz * np.pi / 180.0
                        #x = np.sin(cry)
                        #y = -(np.sin(crx) * np.cos(crz))
                        #z = np.cos(crx) * np.cos(cry)
                        #view = FreeCAD.Vector(x,y,z)
                        #print x
                        #print y
                        #print z
                        #AB = np.array([x,y,z])
                        #changed euler angles to use of normalAt
                        AB = np.array([obj.Shape.Faces[1].normalAt(0,0).x,obj.Shape.Faces[1].normalAt(0,0).y,obj.Shape.Faces[1].normalAt(0,0).z])
                        B = A + MAXRAYLENGTH*AB
                        next_ray = AB
                        #draw the first ray and start loop
                        A_v = FreeCAD.Vector(A[0],A[1],A[2])
                        B_v = FreeCAD.Vector(B[0],B[1],B[2])
                        beams.append((A,B,A_v,B_v,next_ray,obj))
                elif "RectangularLaser" in obj.Name:
                        #print 'yes'
                        ver2 = obj.Shape.Vertexes[0]
                        ver4 = obj.Shape.Vertexes[2]
                        ver6 = obj.Shape.Vertexes[4]
                        ver2_np = np.array([ver2.X,ver2.Y,ver2.Z])
                        ver4_np = np.array([ver4.X,ver4.Y,ver4.Z])
                        ver6_np = np.array([ver6.X,ver6.Y,ver6.Z])
                        v24 = ver4_np - ver2_np
                        #print v24
                        v26 = ver6_np - ver2_np
                        #get the rotation of the object
                        A = np.array([obj.Placement.Base.x,obj.Placement.Base.y,obj.Placement.Base.z])
                        #rot = obj.Placement.Rotation.toEuler()
                        #crx = rot[2] #roll
                        #cry = rot[1] #pitch
                        #crz = rot[0] #yaw
                        #crx = crx * np.pi / 180.0
                        #cry = cry * np.pi / 180.0
                        #crz = crz * np.pi / 180.0
                        #x = np.sin(crz)
                        #y = -(np.sin(crx) * np.cos(crz))
                        #z = np.cos(crx) * np.cos(cry)
                        #view = FreeCAD.Vector(x,y,z)
                        #print x
                        #print y
                        #print z
                        #AB = np.array([x,y,z])
                        #changed to normalAt instead of euler angles
                        AB = np.array([obj.Shape.Faces[5].normalAt(0,0).x,obj.Shape.Faces[5].normalAt(0,0).y,obj.Shape.Faces[5].normalAt(0,0).z])
                        next_ray = AB
                        #get coordinates of A points
                        A_list = []
                        v24_step = normalize(v24)/obj.Density
                        v26_step = normalize(v26)/obj.Density
                        v24_number = np.linalg.norm(v24)*obj.Density
                        v26_number = np.linalg.norm(v26)*obj.Density
                        #print v24_number
                        for  i in range(int(v24_number)):
                                for j in range(int(v26_number)):
                                        A_list.append((ver2_np + i * v24_step + j * v26_step))
                        for elem in A_list:
                                A = elem
                                B = elem + AB * MAXRAYLENGTH
                                A_v = FreeCAD.Vector(A[0],A[1],A[2])
                                B_v = FreeCAD.Vector(B[0],B[1],B[2])
                                beams.append((A,B,A_v,B_v,next_ray,obj))
                                #print 'yesyes'
                elif "CircularLaser" in obj.Name:
                        A = np.array([obj.Placement.Base.x, obj.Placement.Base.y, obj.Placement.Base.z])
                        AB = np.array([obj.Shape.Faces[1].normalAt(0,0).x, obj.Shape.Faces[1].normalAt(0,0).y, obj.Shape.Faces[1].normalAt(0,0).z])
                        next_ray = AB
                        A_list = []
                        N = int(round(obj.Density * ((obj.Radius)**2) * np.pi))
                        thecoordinates = spreadpoints.get_coordinates(N,obj.Radius)
                        v1 = normalize(perpendicular_vector(AB))
                        v2 = normalize(np.cross(AB,v1))
                        for elem in thecoordinates:
                                A_list.append(v1 * elem[0] + v2 * elem[1] + A)
                        for elem in A_list:
                                A = elem
                                B = elem + AB*MAXRAYLENGTH
                                A_v = FreeCAD.Vector(A[0],A[1],A[2])
                                B_v = FreeCAD.Vector(B[0],B[1],B[2])
                                beams.append((A,B,A_v,B_v,next_ray,obj))
        #print beams
        for beam in beams:
                A = beam[0]
                B = beam[1]
                A_v = beam[2]
                B_v = beam[3]
                next_ray = beam[4]
                obj = beam[5]
                remaining_distance = MAXRAYLENGTH
                #j = 0
                totref = False
                while True:
                        outside = False
                        #j = j+1
                        #if j>3:
                                #break
                        #global A_v
                        #global B_v
                        #global remaining_distance
                        #A_v = FreeCAD.Vector(A[0],A[1],A[2])
                        #B_v = FreeCAD.Vector(B[0],B[1],B[2])
                        line = Draft.makeLine(A_v,B_v)
                        #add the line to the Rays folder
                        grp.addObject(line)
                        #input('press enter')
                        #set the color
                        wres=wavelen2rgb.wavelen2rgb(obj.Wavelength)
                        lcol=tuple([x/255.0 for x in wres])
                        line.ViewObject.LineColor = lcol
                        #search for intersection points with all lenses
                        intersection_points = []
                        for alens in lenses:
                                lobj = App.ActiveDocument.getObject(alens)
                                s1 = lobj.Shape
                                s2 = line.Shape
                                cs = s1.common(s2)
                                #intersection_points = []
                                if cs.Vertexes:
                                        for v in cs.Vertexes:
                                                print "intersection point : ", v.Point
                                                nv = np.array([v.Point.x,v.Point.y,v.Point.z])
                                                intersection_points.append((nv,alens))
                        for aabsorber in absorbers:
                                lobj = App.ActiveDocument.getObject(aabsorber)
                                s1 = lobj.Shape
                                s2 = line.Shape
                                cs = s1.common(s2)
                                #intersection_points = []
                                if cs.Vertexes:
                                        for v in cs.Vertexes:
                                                print "intersection point : ", v.Point
                                                nv = np.array([v.Point.x,v.Point.y,v.Point.z])
                                                intersection_points.append((nv,aabsorber))
                        for amirror in mirrors:
                                lobj = App.ActiveDocument.getObject(amirror)
                                s1 = lobj.Shape
                                s2 = line.Shape
                                cs = s1.common(s2)
                                #intersection_points = []
                                if cs.Vertexes:
                                        for v in cs.Vertexes:
                                                print "intersection point : ", v.Point
                                                nv = np.array([v.Point.x,v.Point.y,v.Point.z])
                                                intersection_points.append((nv,amirror))
                        if intersection_points:
                                mindist = -1.0
                                minpoint = None
                                minlens = None
                                for ip in intersection_points:
                                        dist = np.linalg.norm(ip[0]-A)
                                        if dist == 0:
                                                continue
                                        if any([mindist < 0, dist < mindist]):
                                                mindist = dist
                                                minpoint = ip[0]
                                                minlens = ip[1]
                                if minpoint is None:
                                        break
                                App.ActiveDocument.removeObject(line.Name)
                                line = Draft.makeLine(A_v,FreeCAD.Vector(minpoint[0],minpoint[1],minpoint[2]))
                                grp.addObject(line)
                                line.ViewObject.LineColor = lcol
                                #end beam calculation if object is absorber type
                                if minlens in absorbers:
                                        break
                                remaining_distance = remaining_distance - mindist
                                #normal vector
                                o = App.ActiveDocument.getObject(minlens)
                                os = o.Shape
                                thefaces = os.Faces
                                pt = FreeCAD.Vector(minpoint[0],minpoint[1],minpoint[2])
                                for aface in thefaces:
                                        if aface.isInside(pt,0.0000000001,True):
                                                f = aface
                                                break
                                fs = f.Surface
                                uv = fs.parameter(pt)
                                nv = f.normalAt(uv[0],uv[1])
                                #nv.normalize()
                                print nv
                                np_v = np.array([nv.x,nv.y,nv.z])
                                np_vn = normalize(np_v)
                                print np_vn
                                #compute lot
                                v1 = minpoint+15*np_vn
                                v2 = minpoint -15*np_vn
                                v1_v = FreeCAD.Vector(v1[0],v1[1],v1[2])
                                v2_v = FreeCAD.Vector(v2[0],v2[1],v2[2])
                                lot = Draft.makeLine(v1_v,v2_v)
                                grp.addObject(lot)
                                #print angle
                                alpha = angle_between(np_vn,next_ray)
                                #make alpha opposite in case it is greater than 90 degrees
                                if alpha > np.pi/2:
                                        alpha = np.pi - alpha
                                        outside = False
                                else:
                                        outside = True
                                print alpha
                                #leave all the n stuff untouched if it is not a lens
                                if minlens in lenses:
                                        if totref == False:
                                                lastn = n
                                        #n = o.Refractive_index not always working
                                        #compute refractive index of next body
                                        #in case there is only one intersection lens for this point and the ray is going outside set it to SURROUNDING_N
                                        j = 0
                                        for elem in intersection_points:
                                                if not (elem[0] - minpoint).any():
                                                        j = j +1 
                                        if j == 1:
                                                if outside:
                                                        n = SURROUNDING_N
                                                else:
                                                        n = o.Refractive_index
                                        #now check for other lenses#
                                        else:
                                                if outside:
                                                        for elem in intersection_points:
                                                                if elem[1]==o.Name:
                                                                        continue
                                                                if not (elem[0] - minpoint).any():
                                                                        n = App.ActiveDocument.getObject(elem[1]).Refractive_index
                                                                        break
                                                else:
                                                        n = o.Refractive_index
                                        #for refraction / total reflection
                                        print "n=:"
                                        print n
                                        print "lastn=:"
                                        print lastn
                                        chi = lastn * np.sin(alpha) / n
                                        if chi >= 1: #total reflection
                                                print "totalreflection"
                                                totref = True
                                                beta = np.pi - alpha
                                        else: #refraction
                                                print "refraction"
                                                totref = False
                                                beta = np.arcsin(chi)
                                if minlens in mirrors:
                                        beta = np.pi - alpha
                                print beta
                                if outside:
                                        normal_rot = normalize(np.cross(next_ray,np_vn))
                                else:
                                        normal_rot = normalize(np.cross(next_ray,-np_vn))
                                if outside:
                                        next_ray1 = normalize(rotate_vector(np_vn,normal_rot,beta))
                                        next_ray2 = normalize(rotate_vector(np_vn,normal_rot,-beta))
                                else:
                                        next_ray1 = normalize(rotate_vector(-np_vn,normal_rot,beta))
                                        next_ray2 = normalize(rotate_vector(-np_vn,normal_rot,-beta))
                                #print angle_between(-np_vn,next_ray)
                                #if outside:
                                        #if np.dot(next_ray1,np_vn) > np.dot(next_ray2,np_vn):
                                                #next_ray = next_ray1
                                        #else:
                                                #next_ray = next_ray2
                                #else:
                                        #if np.dot(next_ray1,-np_vn) > np.dot(next_ray2,-np_vn):
                                                #next_ray = next_ray1
                                        #else:
                                                #next_ray = next_ray2
                                if np.dot(next_ray1,next_ray) > np.dot(next_ray2,next_ray):
                                        next_ray = next_ray1
                                else:
                                        next_ray = next_ray2
                                A = minpoint
                                B = next_ray*remaining_distance + A
                                A_v = FreeCAD.Vector(A[0],A[1],A[2])
                                B_v = FreeCAD.Vector(B[0],B[1],B[2])
                                #line2 = Draft.makeLine(A_v,B_v)
                                #line2.ViewObject.LineColor=lcol
                        else:
                                break
