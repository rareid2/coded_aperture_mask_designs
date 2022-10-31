from generate_coded_aperture import generate_CA, pinhole

# --------------- --------------- --------------- ---------------
# create MURA - first set rank
nElements = 67

# set desired mask size in mm
mask_size = 14.08  # mm

# mosaicked mask? 
mosaic = True

# generate output files, construction file generates locations in cm
generate_files = True

# generate a construction file with location of holes (false) or location of blocks (true)
holes_inv = True 

# generate plots to check accuracy
check_plots = False

# timepix design
det_size_cm = 1.408

# loop through rank options (primes)
n_elements_original = [7, 11, 17, 31]  # n elements no mosaic
multiplier = [36, 22,14,8]
pixel = 0.055 # mm

element_size_mm_list = [
    pixel * mult for mult in multiplier
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
pinhole(14.08, 1.76/2)