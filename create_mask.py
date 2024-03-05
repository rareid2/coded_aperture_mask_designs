from generate_coded_aperture import generate_CA, pinhole, generate_NTHT_mask
from util_fncs import make_svg

# -------------- --------------- --------------- ---------------

# to create a MURA

# mosaicked mask?
mosaic = True

# generate output files, construction file generates locations in cm
generate_files = True

# generate a construction file with location of holes (false) or location of blocks (true)
holes_inv = True

# generate plots to check accuracy
check_plots = True

# timepix design
det_size_cm = 4.941  # cm

# n elements in the original coded aperture pattern
n_elements_original = [61]

# number of pixels to be used for one element
pixels_downsample = [1]

# size of timepix pixel
pixel = 0.81  # mm

element_size_mm_list = [pixel * ps for ps in pixels_downsample]  # element size in mm

n_elements_list = [
    (ne * 2) - 1 for ne in n_elements_original
]  # total number of elements

mask_size_list = [
    round(es * ne, 2) for (es, ne) in zip(element_size_mm_list, n_elements_list)
]  # mask size in mm

for nElements, mask_size in zip(n_elements_original, mask_size_list):
    generate_CA(nElements, mask_size, mosaic, holes_inv, generate_files, check_plots)
    continue
# --------------- --------------- --------------- ---------------

"""
# to generate a pinhole, set the size of the mask and the size of the pinhole
mask_size = 21.6  # mm
# pinhole size
pinhole_size = 0.6 # mm
pinhole(mask_size, pinhole_size, plot=True)

# --------------- --------------- --------------- ---------------

# to generate a NTHT mask
# first generate MURA


# mosaicked mask? 
mosaic = True

# generate output files, construction file generates locations in cm
generate_files = True

# generate a construction file with location of holes (false) or location of blocks (true)
holes_inv = False 

# generate plots to check accuracy
check_plots = True

# timepix design
det_size_cm = 1.408

n_elements_original = [11] 

# number of pixels to be used for one element
pixels_downsample = [22]

# size of timepix pixel
pixel = 0.055 # mm

element_size_mm_list = [
    pixel * ps for ps in pixels_downsample
]  # element size in mm

n_elements_list = [
    (ne * 2) - 1 for ne in n_elements_original
]  # total number of elements

mask_size_list = [
    round(es * ne,2) for (es, ne) in zip(element_size_mm_list, n_elements_list)
]  # mask size in mm

for nElements, mask_size in zip(
            n_elements_original, mask_size_list
        ):
    generate_NTHT_mask(nElements, mask_size, mosaic, holes_inv=False, generate_files=True, check_plots=True)
"""


"""
# symmetry test
print(mask)
print("swap")
print(1 - mask)
print("rotate")
print(np.rot90(mask))
print(np.array_equal(np.rot90(mask), 1 - mask))
unequal_mask = (1 - mask) != np.rot90(mask)

# Find the indices of unequal elements
unequal_indices = np.argwhere(unequal_mask)
print(unequal_indices)
x = 1 - mask
print(x[30, 30])
print(np.rot90(mask)[30, 30])

# so 67 IS symmetric
"""
