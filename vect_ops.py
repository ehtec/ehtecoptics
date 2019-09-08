import numpy as np

def normalize(v):
	norm = np.linalg.norm(v)
	if norm == 0:
		return v
	else:
		return v / norm

def angle_between(v1,v2):
	v1_u = normalize(v1)
	v2_u = normalize(v2)
	return np.arccos(np.clip(np.dot(v1_u,v2_u),-1.0,1.0))

def rotate_vector(v,erot,angle): #vector,axis,angle in radians
	rotmeasure=np.linalg.norm(erot)
	erot=erot/rotmeasure
	norme=np.dot(v,erot)
	vplane=v-norme*erot
	plnorm=np.linalg.norm(vplane)
	ep=vplane/plnorm
	eo=np.cross(erot,ep)
	vrot=(np.cos(angle)*ep+np.sin(angle)*eo)*plnorm+norme*erot
	return vrot

def perpendicular_vector(v):
        if v[1]==0 and v[2]==0:
                if v[0]==0:
                        raise ValueError('zero vector')
                else:
                        return np.cross(v,[0,1,0])
        return np.cross(v,[1,0,0])
