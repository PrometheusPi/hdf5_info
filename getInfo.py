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
    space = "    "
    print("ITEMS:")
    try:
        # in case it is a group with datat sets
        for i in list(h5Pointer.items()):
            print(space + "{:16s}\t{}".format(i[0], i[1]))
    except AttributeError:
        # in case it is a data set
        print(space + "'Dataset' object has no attribute 'items'")
        print(space + "np.shape = {}".format(np.shape(h5Pointer)))
        print(space + "Raw Data:")
        print("{}".format(h5Pointer.value))
        
    print("\nATTRIBUTS:")
    for i in list(h5Pointer.attrs.items()):
        print(space + "{:16s}\t{}".format(i[0], i[1]))
