from generate_coded_aperture import generate_CA, pinhole

# --------------- --------------- --------------- ---------------
# create MURA - first set rank
nElements = 67

# set desired mask size in mm
mask_size = 87 # mm

# mosaicked mask? 
mosaic = True

# generate output files, construction file generates locations in cm
generate_files = True

# generate a construction file with location of holes (false) or location of blocks (true)
holes_inv = True 

# generate plots to check accuracy
check_plots = True

#generate_CA(nElements, mask_size, mosaic, holes_inv, generate_files, check_plots)
pinhole(mask_size, 1)