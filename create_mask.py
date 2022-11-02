from generate_coded_aperture import generate_CA, pinhole

# --------------- --------------- --------------- ---------------
# create MURA - first set rank
nElements = 67

# mosaicked mask? 
mosaic = True

# generate output files, construction file generates locations in cm
generate_files = True

# generate a construction file with location of holes (false) or location of blocks (true)
holes_inv = True 

# generate plots to check accuracy
check_plots = True

# timepix design
det_size_cm = 1.408

# n elements in the original coded aperture pattern
n_elements_original = [7, 11, 17, 31] 

# number of pixels to be used for one element
pixels_downsample = [36, 22, 14, 8]

# size of timepix pixel
pixel = 0.055 # mm

# size of 
element_size_mm_list = [
    pixel * ps for ps in pixels_downsample
]  # element size in mm

n_elements_list = [
    (ne * 2) - 1 for ne in n_elements_original
]  # total number of elements
mask_size_list = [
    round(es * ne,2) for (es, ne) in zip(element_size_mm_list, n_elements_list)
]  # mask size in mm
for nElements, element_size_mm, mask_size in zip(
            n_elements_original, element_size_mm_list, mask_size_list
        ):
    generate_CA(nElements, mask_size, mosaic, holes_inv, generate_files, check_plots)
    continue

# to generate a pinhole, set the size of the mask and the size of the pinhole
mask_size = 14.08 # mm
# pinhole size
pinhole_size = 1.76 # mm
pinhole(mask_size, pinhole_size, plot=True)