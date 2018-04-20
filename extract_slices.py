from PIL import Image
import SimpleITK as sitk
import os, fnmatch

BASE_PATH = '/Users/brandonwalker/Desktop/'
IMG_PATH = BASE_PATH + 'subset0/'

EXTRACT_PATH = BASE_PATH + '/subset0_extracted/'

# Get the list of mhd files
file_list = fnmatch.filter(os.listdir(IMG_PATH), '*.mhd')

for file in file_list:
    # Create the directory into which the slices should be extracted
    os.makedirs(EXTRACT_PATH + file[:-4])

    # Get a numpy array of the image
    mhdImage = sitk.ReadImage(IMG_PATH + file)
    numpyImage = sitk.GetArrayFromImage(mhdImage)

    # Extract/save each slice
    for i in range(numpyImage.shape[0]):
        slice_file = EXTRACT_PATH + file[:-4] + '/{}.tiff'.format(i)

        Image.fromarray(numpyImage[i]).convert('L').save(slice_file)