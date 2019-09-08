import numpy as np
#import matplotlib.pyplot as plt

#n = 5
def get_coordinates(n,r):
    radius = np.sqrt(np.arange(n) / float(n))

    golden_angle = np.pi * (3 - np.sqrt(5))
    theta = golden_angle * np.arange(n)

    points = np.zeros((n,2))
    points[:,0] = np.cos(theta)
    points[:,1] = np.sin(theta)
    points *= radius.reshape((n,1))

    #print points[0][0]

    l = [(x[0],x[1]) for x in points]

    #print l

    m = [np.array(x) * r for x in l]

    #print m
    return m
    #for x in zip(*points):
    #    print x

    #ziplist = [item for item in zip(*points)]

    #xylist = [(x,y) for x,y in ziplist[0],ziplist[1]]

    #plt.gca().set_aspect('equal',adjustable='box')

    #plt.scatter(*zip(*points))

#plt.show()
