import numpy as np
import matplotlib.pyplot as plt
# script to plot electron energy vs mask thickness for 1/e stopping power of electrons
# data from ESTAR

# density
Le_rho = 1.2 # g/cm^3
Be_rho = 1.85 # g/cm^3
Al_rho = 2.7 # g/cm^3
Si_rho = 2.33 # g/cm^3
Ni_rho = 8.902 # g/cm^3
W_rho = 19.3 #g/cm^3

# select density to use
densities = [Si_rho, W_rho]

# set names
strings_files = ['Si','W']

# create plot
fig = plt.figure()

colors = ['#88DAE7', '#0B2D32']

# loop through each element
for element, rho, color in zip(strings_files, densities, colors):
    # find data file
    fname = 'stopping_power_data/stoppingpower_%s_photon.txt' %(element)
    file1 = open(fname, 'r')
    Lines = file1.readlines()

    count = 0
    energies = []
    ranges = []

    # extract data from file
    for line in Lines:
        count += 1
        # ignore header
        if count > 8:
            line_split = line.split('  ')
            # save energy and range
            energies.append(float(line_split[0]))
            # convert range from cm^2 / g to cm by multiplying by rho and inverting
            ranges.append( 1 / (float(line_split[1])  * rho))
    
    # convert range and energy
    ranges = np.array(ranges)*10000 # convert to um
    energies = np.array(energies)*1000 # convert to keV

    # finally, plot the result
    plt.loglog(energies,ranges,label=element,color=color)
 
plt.legend()
plt.xlim([10**0,10**4])
plt.ylim([10**0,10**5.5])
plt.xlabel('Energy [keV]')
plt.ylabel('Range [um]')
plt.title('Photon Stopping Power')

plt.text(x=278.5, y=510, s='standard medipix thickness')
plt.hlines(500,10**0,10**4, linewidth=1, linestyles='--', color='Gray',zorder=3)

plt.text(x=10, y=1270, s='thickness of tungsten mask from grant')
plt.hlines(1250,10**0,10**4, linewidth=1, linestyles='--', color='Gray',zorder=3)

plt.savefig('stopping_power_data/range_photons.png',dpi=300)
