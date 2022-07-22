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
for element, rho, color in zip(strings_files, densities, colors):
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
    plt.loglog(energies,ranges,label=element,color=color)


plt.legend()
plt.xlim([10**1,10**4])
plt.ylim([10**-0.5,10**5.5])

plt.text(x=27.3, y=7.4, s='MEPED')
plt.scatter(x=27.3, y=7.4, s=10, color='DarkSlateGray',zorder=3)

plt.text(x=23.55, y=10, s='ELFIN')
plt.scatter(x=23.55, y=10, s=10, color='DarkSlateGray',zorder=3)

plt.text(x=42.5, y=16, s='FIREBIRD')
plt.scatter(x=42.5, y=16, s=10, color='DarkSlateGray',zorder=3)

plt.text(x=278.5, y=500, s='REPTile')
plt.scatter(x=278.5, y=500, s=10, color='DarkSlateGray',zorder=3)


plt.savefig('stopping_power_data/range_poster.png',dpi=300)


# data for poster
"""
xx = [1.572713643,
2.157421289,
2.727136432,
3.289355322,
3.866566717,
4.428785607,
5.005997001,
5.575712144,
6.152923538,
6.722638681,
7.299850075,
7.862068966,
8.43928036,
9.008995502]

yy = [74.26136364,
76.47727273,
74.43181818,
65.56818182,
58.06818182,
50.22727273,
46.30681818,
42.72727273,
38.80681818,
34.88636364,
32.84090909,
30.79545455,
28.75,
26.70454545]

xx2 = [1.573566085,
2.149625935,
2.725685786,
3.294264339,
3.862842893,
4.431421446,
5,
5.57605985,
6.144638404,
6.713216958,
7.289276808,
7.865336658,
8.433915212,
8.995012469]

yy2 = [4.571428571,
3.392857143,
2.696428571,
2.214285714,
1.8125,
1.598214286,
1.383928571,
1.276785714,
1.169642857,
1.0625,
0.941964286,
0.955357143,
0.848214286,
0.848214286]

"""