from astropy.io import fits
import time
import numpy as np
import sys


def read_fits(file_list):
    datasets = []
    for file in file_list:
        hdulist = fits.open(file)
        datasets.append(hdulist[0].data)
    return datasets


def median_fits(file_list):
    start = time.time()
    datasets = read_fits(file_list)
    # Stack arrays into a 3 dimensional array to calculate median
    FITS_stack = np.dstack(datasets)
    median = np.median(FITS_stack, axis=2)
    memory = FITS_stack.nbytes
    # convert to kB
    memory /= 1024
    stop = time.time() - start
    return median, stop, memory


if __name__ == '__main__':
    #Calculates median of fits files using np stack feature
    #Calculates time to completion and memory usage
    result = median_fits(['image0.fits', 'image1.fits'])
    print(result[0][100, 100], result[1], result[2])

