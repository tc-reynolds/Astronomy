from astropy.io import fits


def load_fits(fits_filename):
    hdulist = fits.open(fits_filename)
    data = hdulist[0].data
    return data


def mean_fits(fits_files):
    mean_stack = []
    for file in fits_files:
        dataset = load_fits(file)
        if len(mean_stack) == 0:
            mean_stack = dataset
        else:
            for i, row in enumerate(dataset):
                mean_stack[i] = mean_stack[i] + row
    for i, row in enumerate(mean_stack):
        mean_stack[i] = row / len(fits_files)
    return mean_stack

def max_value(data):
    max_value = 0
    for i, row in enumerate(data):
        row = row.tolist()
        row_max = max(row)
        if row_max > max_value:
            max_value = max(row)
            max_pos = (i, row.index(max_value))
    return max_pos


if __name__ == '__main__':
    data = mean_fits(['image0.fits', 'image1.fits', 'image2.fits'])
    data1 = mean_fits(['image0.fits', 'image1.fits', 'image3.fits'])
    data2 = mean_fits(['image0.fits', 'image1.fits', 'image2.fits', 'image3.fits', 'image4.fits'])
    print(data[100, 100])
    print(data1[100, 100])
    print(data2[100, 100])

    import matplotlib.pyplot as plt

    plt.imshow(data.T, cmap=plt.cm.viridis)
    plt.colorbar()
    plt.show()