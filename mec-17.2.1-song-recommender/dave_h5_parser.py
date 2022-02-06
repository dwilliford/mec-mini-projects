import os
import sys
import h5py
import numpy as np

def die_with_usage():
    print('Bad usage')
    sys.exit(0)


if __name__ == '__main__':
    """ MAIN """

    # help menu
    if len(sys.argv) < 2:
        die_with_usage()

    # get params
    hdf5path = sys.argv[1]

    with h5py.File(hdf5path, 'r') as f:
        print(list(f.keys()))
        #['analysis', 'metadata', 'musicbrainz']
        dset_analysis = f['analysis']
        dset_metadata = f['metadata']
        dset_musicbrainz = f['musicbrainz']
        print('dset_analysis: type: ' + str(type(dset_analysis)))
        print('dset_metadata: type: ' + str(type(dset_metadata)))
        print('dset_musicbrainz: type: ' + str(type(dset_musicbrainz)))

        print('**** analysis ****')
        print(list(dset_analysis.keys()))
        print('**** metadata ****')
        print(list(dset_metadata.keys()))
        print('**** musicbrainz ****')
        print(list(dset_musicbrainz.keys()))

        #print('dset_analysis: shape: ' + str(dset_analysis.shape) + ' type: ' + str(dset_analysis.dtype))
        #print('dset_metadata: shape: ' + str(dset_metadata.shape) + ' type: ' + str(dset_metadata.dtype))
        #print('dset_musicbrainz: shape: ' + str(dset_musicbrainz.shape) + ' type: ' + str(dset_musicbrainz.dtype))