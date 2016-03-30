import numpy as np
import h5py

def getInfo(h5Pointer):
    """
    prints either items and attributes or values and attributes
    of a h5 pointer to screen.

    Input:
    h5Pointer - h5py object

    Output:
    none
    """
    print("ITEMS:")
    try:
        # in case it is a group with datat sets
        for i in list(h5Pointer.items()):
            print(i)
    except AttributeError:
        # in case it is a data set
        print("'Dataset' object has no attribute 'items'")
        print("np.shape = {}".format(np.shape(h5Pointer)))
        print(h5Pointer.value)
        
    print("\nATTRIBUTS:")
    for i in list(h5Pointer.attrs.items()):
        print(i)
