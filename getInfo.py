import numpy as np
import h5py

def getInfo(h5File, key):
    """
    prints either items and attributes or values and attributes
    of a h5 pointer to screen.

    Input:
    h5File - hdf5 file (h5py object)
    key    - key to h5py object

    Output:
    none
    """
    space = "    "
    print("KEY: {}".format(key))
    print("ITEMS:")
    try:
        # in case it is a group with datat sets
        for i in list(h5File[key].items()):
            print(space + "{:16s}\t{}".format(i[0], i[1]))
    except AttributeError:
        # in case it is a data set
        print(space + "'Dataset' object has no attribute 'items'")
        print(space + "np.shape = {}".format(np.shape(h5File[key])))
        print(space + "Raw Data:")
        print("{}".format(h5File[key].value))

    except KeyError:
        print("The given key ({}) does not exist.".format(key))
        return
        
    print("\nATTRIBUTS:")
    for i in list(h5File[key].attrs.items()):
        print(space + "{:16s}\t{}".format(i[0], i[1]))

    return
