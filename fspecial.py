import numpy as np

def fspecial(*kargs):
    '''
    H = FSPECIAL('gaussian',HSIZE,SIGMA) returns a rotationally
    symmetric Gaussian lowpass filter  of size HSIZE with standard
    deviation SIGMA (positive). HSIZE can be a vector specifying the
    number of rows and columns in H or a scalar, in which case H is a
    square matrix.
    The default HSIZE is [3 3], the default SIGMA is 0.5.
    '''
    if(kargs[0] == 'gaussian'):
        if len(kargs) == 1:
            sig  = 0.5
            siz = (3-1)/2
        elif len(kargs) == 2:
            sig = 0.5
            siz = (kargs[1]-1)/2
        else:
            sig = kargs[2]
            siz = (kargs[1]-1)/2
        xx = np.arange(-siz,siz+1)
        x, y = np.meshgrid(xx,xx,indexing="xy")
        a = np.exp(-(x**2+y**2)/(2*sig**2))
        eps = np.spacing(1)
        a[a<(eps*a.max())] = 0
        suma = a.sum()

        if suma != 0:
            a = a/suma
            return a
        return None

