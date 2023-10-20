import numpy as np

# set path for file saving
fpath = 'MURA_designs/'
def makeMURA(gridSizeX,boxSize,holes_inv,generate_files=True):

    # Creates MURA coded aperture and decoding matrices
    # centimeters

    centeringShift = 0;

    # p, must be prime and satify L = 4m + 1
    gridSizeY = gridSizeX; # (square)

    # create file w holes or with blocks
    if holes_inv == True:
        block_check = 0
    else:
        block_check = 1

    def jacobi_symbol(a, n):
        assert(n > a > 0 and n%2 == 1)
        t = 1
        while a != 0:
            while a % 2 == 0:
                a /= 2
                r = n % 8
                if r == 3 or r == 5:
                    t = -t
            a, n = n, a
            if a % 4 == n % 4 == 3:
                t = -t
            a %= n
        if n == 1:
            return t
        else:
            return 0

    def MURA_code(i, j, p):
        #
        #This function generates a Modified Uniform Redundent Aperature
        #
        if i == 0:
            return 0;
        elif j == 0 and i != 0:
            return 1;
        elif jacobi_symbol(i, p)*jacobi_symbol(j, p) == 1: 
            return 1;
        else:
            return 0;

    def MURA_decoding_matrix(i,j, block):
        if i + j == 0:
            return 1
        elif block == 1:
            return 1
        elif block == 0:
            return -1
        else:
            print("Error in decoding matrix!")
            raise

    MURAmatrix = np.zeros([gridSizeX, gridSizeY]);
    MURAdecodeMatrix = -np.ones([gridSizeX, gridSizeY]);
    
    if generate_files:
        with open(fpath+str(gridSizeX)+"MURA_matrix.txt", 'w') as f, open(fpath+str(gridSizeX)+"MURA_decode_matrix.txt", 'w') as d:
            d.write("i,j,d\n") 
            for i in range(0, gridSizeX):
                for j in range(0, gridSizeY):

                    block = MURA_code(i, j, gridSizeX);
                    decode = MURA_decoding_matrix(i,j, block);
                    MURAdecodeMatrix[i,j] = decode;

                    d.write(str(i) + "," + str(j) + "," + str(decode) + "\n")

                    boxLocArrayY = (gridSizeX*boxSize-boxSize) - (i) * boxSize + centeringShift; 
                    boxLocArrayX = (j) * boxSize + centeringShift;

                    
                    if block == block_check:
                        f.write(str(round(boxLocArrayX, 8)) + "," 
                                + str(round(boxLocArrayY, 8)) + "\n")

                        MURAmatrix[i,j] = 1;
    else:
        for i in range(0, gridSizeX):
            for j in range(0, gridSizeY):

                block = MURA_code(i, j, gridSizeX);
                decode = MURA_decoding_matrix(i,j, block);
                MURAdecodeMatrix[i,j] = decode;

                boxLocArrayY = (gridSizeX*boxSize-boxSize) - (i) * boxSize + centeringShift; 
                boxLocArrayX = (j) * boxSize + centeringShift;
                
                if block == block_check:
                    MURAmatrix[i,j] = 1;

    # flip for imshow
    MURAmatrix = np.flip(MURAmatrix,0) 
    MURAdecodeMatrix = np.flip(MURAdecodeMatrix,0) 

    return MURAmatrix, MURAdecodeMatrix

# ----------------------------------------------------------------
def make_mosaic_MURA(gridSizeX,boxSize,holes=True,generate_files=False):
    # gonna do this the stupid way (not using a cyclic permutation)
    # but also confirming w Gottesman & Fennimore 1989 Fig 5
    detSize = 4. # unused

    # p, must be prime and satify L = 4m + 1
    gridSizeY = gridSizeX; # (square)

    def jacobi_symbol(a, n):
        assert(n > a > 0 and n%2 == 1)
        t = 1
        while a != 0:
            while a % 2 == 0:
                a /= 2
                r = n % 8
                if r == 3 or r == 5:
                    t = -t
            a, n = n, a
            if a % 4 == n % 4 == 3:
                t = -t
            a %= n
        if n == 1:
            return t
        else:
            return 0

    def MURA_code(i, j, p):
        #
        #This function generates a Modified Uniform Redundent Aperature
        #
        if i == 0:
            return 0;
        elif j == 0 and i != 0:
            return 1;
        elif jacobi_symbol(i, p)*jacobi_symbol(j, p) == 1: 
            return 1;
        else:
            return 0;

    def MURA_decoding_matrix(i,j, block):
        if i + j == 0:
            return 1
        elif block == 1:
            return 1
        elif block == 0:
            return -1
        else:
            print("Error in decoding matrix!")
            raise

    MURAmatrix = np.zeros([gridSizeX*2, gridSizeY*2]);
    MURAdecodeMatrix = -np.ones([gridSizeX*2, gridSizeY*2]); # remove first column and row after the fact
    if generate_files:
        with open(fpath+str(gridSizeX)+"mosaicMURA_matrix.txt", 'w') as f, open(fpath+str(gridSizeX)+"mosaicMURA_decode_matrix.txt", 'w') as d:
            d.write("i,j,d\n")
            # repeat this four times -- this will become lower right pattern 
            for m in range(4):

                if m == 0:
                    # first one, no shift - lower right
                    shiftx = boxSize*gridSizeX
                    shifty = 0
                    shifti = gridSizeX
                    shiftj = 0
                elif m == 1: # upper right
                    shiftx = boxSize*gridSizeX
                    shifty = boxSize*gridSizeX
                    shifti = gridSizeX
                    shiftj = gridSizeX
                elif m == 2: # lower left
                    shiftx = 0
                    shifty = 0
                    shifti = 0
                    shiftj = 0
                else:  # upper left
                    shiftx = 0
                    shifty = boxSize*gridSizeX
                    shifti = 0
                    shiftj = gridSizeX

                for i in range(0, gridSizeX):
                    for j in range(0, gridSizeY):

                        block = MURA_code(i, j, gridSizeX);
                        decode = MURA_decoding_matrix(i,j, block);
                        MURAdecodeMatrix[shifti+i,shiftj+j] = decode;
                        MURAmatrix[shifti+i,shiftj+j] = block;

                        d.write(str(i) + "," + str(j) + "," + str(decode) + "\n")

                        # shift up by grid size - 1 so that the matrix builds top down 
                        # maps row 0 to the TOP of the mask rather than bottom row
                        boxLocArrayY = (gridSizeX*boxSize-boxSize) - (i) * boxSize + shifty; 
                        
                        boxLocArrayX = (j) * boxSize + shiftx;

                        if holes==False:
                            blockcheck = 1
                        else:
                            blockcheck = 0
                        if block == blockcheck:
                            # remove first row and column
                            if boxLocArrayY > gridSizeX*boxSize*2 - boxSize:
                                pass
                            elif boxLocArrayX == 0:
                                pass
                            else:
                                #print(boxLocArrayX,boxLocArrayY,gridSizeX*boxSize*2)

                                # shift the boxSize left by one so that everything lines up w origin
                                f.write(str(round(boxLocArrayX-boxSize, 8)) + "," 
                                        + str(round(boxLocArrayY, 8)) + "\n")
            f.close()
            d.close()
        
    # same thing but dont write to a file
    else:
        # repeat this four times -- this will become lower right pattern 
        for m in range(4):

            if m == 0:
                # first one, no shift - lower right
                shiftx = boxSize*gridSizeX
                shifty = 0
                shifti = gridSizeX
                shiftj = 0
            elif m == 1: # upper right
                shiftx = boxSize*gridSizeX
                shifty = boxSize*gridSizeX
                shifti = gridSizeX
                shiftj = gridSizeX
            elif m == 2: # lower left
                shiftx = 0
                shifty = 0
                shifti = 0
                shiftj = 0
            else:  # upper left
                shiftx = 0
                shifty = boxSize*gridSizeX
                shifti = 0
                shiftj = gridSizeX

            for i in range(0, gridSizeX):
                for j in range(0, gridSizeY):

                    block = MURA_code(i, j, gridSizeX);
                    decode = MURA_decoding_matrix(i,j, block);
                    MURAdecodeMatrix[shifti+i,shiftj+j] = decode;
                    MURAmatrix[shifti+i,shiftj+j] = block;

                    # shift up by grid size - 1 so that the matrix builds top down 
                    # maps row 0 to the TOP of the mask rather than bottom row
                    boxLocArrayY = (gridSizeX*boxSize-boxSize) - (i) * boxSize + shifty; 
                    
                    boxLocArrayX = (j) * boxSize + shiftx;

                    if holes==True:
                        blockcheck = 1
                    else:
                        blockcheck = 0
                    if block == blockcheck:
                        # remove first row and column
                        if boxLocArrayY > gridSizeX*boxSize*2 - boxSize:
                            pass
                        elif boxLocArrayX == 0:
                            pass
                        else:
                            pass
        

    # remove first row and column from decode
    MURAdecodeMatrix = np.delete(MURAdecodeMatrix, (0), axis=0)
    MURAdecodeMatrix = np.delete(MURAdecodeMatrix, (0), axis=1)
    MURAmatrix = np.delete(MURAmatrix, (0), axis=0)
    MURAmatrix = np.delete(MURAmatrix, (0), axis=1)
                    
                    
    return MURAmatrix, MURAdecodeMatrix    


def get_decoder_MURA(mask,rank,holes_inv,check):
    #check = 1
    decode = np.zeros((rank,rank))
    # looking for central pattern of mask
    shift = rank//2
    for j in range(rank//2,rank+rank//2):
        for i in range(rank//2,rank+rank//2):
            #print(i,j)
            element = mask[i,j]
            if i-shift ==0 and j-shift==0:
                dd = 1
            else:
                if element == check:
                    dd = 1
                else:
                    dd = -1
            decode[i-shift,j-shift] = dd
    #decode[18,18] = -1

    return decode


# ------------------------------------------------------------------------------

# code to generate a no two holes touching mask from original mask pattern

def make_NTHT(mask, mosiac):
    
    newMask = np.array([]);
    zArray_column = np.zeros([np.size(mask, 0),1]);

    newMask = mask[:,0];
    newMask = np.column_stack( (newMask, np.zeros([len(newMask),1])) );
    for i in range( 1, len(mask) ):
        newMask = np.column_stack( (newMask, mask[:,i]) );
        if i % 1 == 0:
            newMask = np.column_stack( (newMask, zArray_column) );

    zArray_row = np.zeros([np.size(newMask, 1), 1]);
    newMask = np.insert(newMask, [i for i in range(0, len(mask)) if i % 1 == 0], zArray_row.T, axis=0);

    return newMask

# -------------------------------------------------------------------------------------------------------

def make_svg(build_file,fname,boxdim,mask_size):
    import svgwrite

    # scale everything
    # 1 pixel = 1 block
    sizex = mask_size
    sizey = mask_size

    svg_document = svgwrite.Drawing(filename = fname,
                                    size = ("%.2fpx" % sizex, "%.2fpx" % sizey))

    svg_document.add(svg_document.rect(insert=(0, 0), size=('100%', '100%'), rx=None, ry=None, fill='black'))


    # open file
    f = open(build_file, "r")
    lines = f.readlines()
    hole_loc = []

    # read in lines to add holes
    for line in lines:
        holes = line.split(',')
        holes_int = [float(ho) for ho in holes]
        hole_loc.append(holes_int)
    for hl in hole_loc:
        svg_document.add(svg_document.rect(insert=(hl[0], (sizey - boxdim) - hl[1]), size=('4.7619047619%', '4.7619047619%'), rx=None, ry=None, fill='white'))

    svg_document.save()