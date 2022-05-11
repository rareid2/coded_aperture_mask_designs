This repo contains code to generate coded aperture mask designs and evaluate mask thickness

full credit to [Grant Berland](https://github.com/GrantBerland) for the code to generate MURA designs, it is just reproduced here 

stopping_power.py will generate a plot of energy vs thickness of mask needed for 1/e stopping poewr of electrons
takes in data from ESTAR, some data is already included in stopping_power/

create_mask.py will create a coded aperture design that will be output as a matrix and with a construction file
thats gives the location of either the holes or the blocks used in geant
the decoding array will also be output as a matrix and saved as a file 

here's a neat example of a coded aperture design

![67MURA](/MURA_designs/67mosaicMURA_fromfile.png)