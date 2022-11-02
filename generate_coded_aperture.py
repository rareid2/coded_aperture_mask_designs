import matplotlib.pyplot as plt
import matplotlib.cm
import numpy as np
import os

# import functions to create matrices
from util_fncs import *

# --------------- --------------- --------------- ---------------
def generate_CA(nElements, mask_size, mosaic, holes_inv, generate_files, check_plots):
    # calculate element size for mask in mm
    if mosaic: 
        element_size = round(mask_size / (nElements*2-1),4) # mm
        mask, decode = make_mosaic_MURA(nElements, element_size, holes_inv, generate_files)
        os.rename(fpath + str(nElements) + 'mosaicMURA_matrix.txt', 'MURA_designs/'+str(nElements) + 'mosaicMURA_matrix_'+str(mask_size)+'.txt')

    # if not mosaicked, do not double  nelements
    else:
        element_size = round(mask_size / (nElements),4) # mm
        # generate the mask pattern and the decoding array
        mask, decode = makeMURA(nElements,element_size,holes_inv, generate_files)
        os.rename(fpath+str(nElements) + 'MURA_matrix.txt', 'MURA_designs/'+str(nElements) + 'MURA_matrix_'+str(mask_size)+'.txt')

    if check_plots:
        plot_output(mask, decode, element_size, nElements, mask_size, mosaic, holes_inv, generate_files)

 
def plot_output(mask, decode, boxdim, nElements, mask_size, mosaic, holes_inv, generate_files):
    #  --------------- --------------- --------------- ---------------
    # for plotting
    if holes_inv:
        cmap = 'binary'
        fc = 'white'
        fc_block = 'black'
    else:
        cmap = 'binary_r'
        fc = 'black'
        fc_block = 'white'
    
    if mosaic:
        fm = 'mosaic'
    else:
        fm = ''

    # ------------- plot the matrix to confirm correct ---------------
    # plot MURA from matrix
    fig = plt.figure(figsize=(8,6))
    ax = fig.add_subplot(111)


    cmap = matplotlib.colors.ListedColormap(['white', '#2D1E2F'])
    plt.imshow(mask, cmap=cmap, origin='lower')
    if mosaic:
        plt.xlim([0,nElements*2-1])
        plt.ylim([0,nElements*2-1])
    else:
        plt.xlim([0,nElements])
        plt.ylim([0,nElements])
    plt.colorbar(); plt.title("%i Element MURA" % nElements)

    # save it
    cwd = os.getcwd()

    ax.set_aspect('equal')
    plt.savefig(os.path.join(cwd,fpath+str(nElements)+fm+'MURA_frommatrix.png'),dpi=300)
    plt.clf()
    # ------------- plot the decoder to confirm correct ---------------
    # plot decoder from matrix
    plt.figure(figsize=(8,6))
    plt.imshow(decode, cmap=cmap, origin='lower');
    plt.colorbar(); plt.title("%i Element MURA" % nElements);

    # save it
    cwd = os.getcwd()
    plt.savefig(os.path.join(cwd,fpath+str(nElements)+fm+'MURA_decode_frommatrix.png'))
    plt.clf()

    # --------------------- if files are generated ---------------
    if generate_files:
        print('generating plots')
        # ------------- plot the matrix from the file generated ---------------
        # now plot in physical dimensions - cm
        fig = plt.figure()
        ax=fig.add_subplot(111)
        ax.set_facecolor(fc)

        # open file
        f = open(fpath+str(nElements)+fm+'MURA_matrix_'+str(mask_size)+".txt", "r")
        lines = f.readlines()
        hole_loc = []

        # read in lines to add holes
        for line in lines:
            holes = line.split(',')
            holes_int = [float(ho) for ho in holes]
            hole_loc.append(holes_int)
        for hl in hole_loc:
            # add hole at specified locations
            rectangle = plt.Rectangle((hl[0],hl[1]), boxdim, boxdim, fc=fc_block)
            plt.gca().add_patch(rectangle)
        plt.axis('scaled')
        f.close()

        if mosaic:
            plt.xlim([0,boxdim*(nElements*2-1)])
            plt.ylim([0,boxdim*(nElements*2-1)])
        else:
            plt.xlim([0,boxdim*nElements])
            plt.ylim([0,boxdim*nElements])

        plt.savefig(os.path.join(cwd,fpath+str(nElements)+fm+'MURA_fromfile.png'))
        plt.clf()
        # ------------- plot the decoder from the file generated ---------------
        # now plot in physical dimensions - cm
        fig = plt.figure()
        ax=fig.add_subplot(111)
        ax.set_facecolor('white')

        # open file
        f = open(fpath+str(nElements)+fm+"MURA_decode_matrix.txt", "r")
        lines = f.readlines()
        hole_loc = []
        dval = []

        # read lines
        line_count = 1
        for line in lines:
            if line_count == 1: # skip the header
                pass
            else:
                holes = line.split(',')
                holes_int = [float(ho) for ho in holes]
                hole_loc.append(holes_int[0:2])
                dval.append(holes_int[2])
            line_count +=1

        for hl,v in zip(hole_loc,dval):
            # add decode value (1 or -1) -- this will be upside down .... 
            if int(v) == 1:
                rectangle = plt.Rectangle((hl[0],hl[1]), 1, 1, fc='black')
            else:
                rectangle = plt.Rectangle((hl[0],hl[1]), 1, 1, fc='white')
            plt.gca().add_patch(rectangle)
        plt.axis('scaled')
        f.close()
        plt.savefig(os.path.join(cwd,fpath+str(nElements)+fm+'MURA_deocde_fromfile.png'))
        plt.clf()

def pinhole(size,boxsize, plot=False):

    boxsize = boxsize / 2
    # generate file that has a box everywhere
    with open('MURA_designs/1MURA_matrix_%0.2f.txt' %(size), 'w') as fp:

        for nx in np.arange(0,size,boxsize):
            for ny in np.arange(0,size,boxsize):
                if (size) / nx == 2.0 and (size) / ny == 2.0:
                    print(nx,ny)
                elif size / (nx+boxsize) == 2.0 and (size) / (ny+boxsize) == 2.0:
                    print(nx,ny)
                elif size / (nx+boxsize) == 2.0 and (size) / ny == 2.0:
                    print(nx,ny)
                elif size / (nx) == 2.0 and (size) / (ny+boxsize) == 2.0:
                    print(nx,ny)
                else:
                    fp.write(str(round(nx, 4)) + "," + str(round(ny, 4)) + "\n")
        print('file created')

    fp.close()


    # open file
    f = open('MURA_designs/1MURA_matrix_%0.2f.txt' %(size), 'r')
    lines = f.readlines()
    hole_loc = []

    # read in lines to add holes
    for line in lines:
        holes = line.split(',')
        holes_int = [float(ho) for ho in holes]
        hole_loc.append(holes_int)
    for hl in hole_loc:
        # add hole at specified locations
        rectangle = plt.Rectangle((hl[0],hl[1]), boxsize, boxsize, fc='black')
        plt.gca().add_patch(rectangle)
    plt.axis('scaled')
    f.close()

    plt.savefig('MURA_designs/1MURA_matrix_%0.2f.png' %(size))

    #  --------------- --------------- --------------- ---------------