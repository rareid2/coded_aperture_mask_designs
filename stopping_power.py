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
densities = [Le_rho, Be_rho, Si_rho, Al_rho, Ni_rho, W_rho]

# set names
strings_files = ['Lexan','Be','Si','Al','Ni', 'W']

# create plot
fig = plt.figure()

colors = ['#BBEAF1', '#88DAE7', '#56CADC', '#27A6B9', '#1D7887', '#0B2D32']

# loop through each element
for element, rho, color in zip(strings_files[-1:], densities[-1:], colors[2:3]):
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
    ranges = np.array(ranges)*10 # convert to mm
    energies = np.array(energies)*1000 # convert to keV

    # finally, plot the result
    plt.loglog(energies,ranges,label=element,color=color)

    # how much would 500 um get me

for i,r in enumerate(ranges):
    # 300 um
    if 0.25 < r < 0.35:
        print(r,energies[i])



#plt.ylim([10**-2,10**1])
#plt.legend()
plt.xlim([10**1,10**4])

#plt.hlines(3.3,10**1,10**4,linestyles='--',color='grey')
#plt.hlines(0.1,10**1,10**4,linestyles='--',color='grey')

#plt.ylim([10**3.477,10**3.5])

plt.ylabel('mm')
plt.xlabel('electron energy [keV]')
plt.savefig('stopping_power_data/range_prospectus.png',dpi=300)