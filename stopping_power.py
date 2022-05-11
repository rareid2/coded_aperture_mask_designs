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

# select density to use
densities = [Le_rho, Be_rho, Al_rho, Si_rho, Ni_rho]

# set names
strings_files = ['Lexan','Be','Al','Si','Ni']

# create plot
fig, ax = plt.subplots()

# loop through each element
for element, rho in zip(strings_files, densities):
    # find data file
    fname = 'stopping_power_data/stoppingpower_%s.txt' %(element)
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
            line_split = line.split(' ')
            # save energy and range
            energies.append(float(line_split[0]))
            # convert range from g/cm^2 to cm by diving by rho
            ranges.append(float(line_split[1]) /rho)
    
    # convert range and energy
    ranges = np.array(ranges)*10000 # convert to um
    energies = np.array(energies)*1000 # convert to keV

    # finally, plot the result
    plt.loglog(energies, np.array(ranges),label=element)


# some plot clean up
plt.legend()
plt.xlabel('energy [keV]')
plt.ylabel('distance [um]')
plt.xlim([10,10000])
plt.ylim([0.4,100000])
ax.grid()
plt.title('electron range in various window materials')
plt.savefig('stopping_power_data/electron_range.png',dpi=300)