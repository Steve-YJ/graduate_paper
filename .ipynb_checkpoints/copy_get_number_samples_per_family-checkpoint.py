# Get number of samples per family

import os,glob,numpy
os.chdir('K:/malimg') # the parent folder with sub-folders

list_fams = os.listdir(os.getcwd()) # vector of strings with family names

no_imgs = [] # No. of samples per family

for i in range(len(list_fams)):
 os.chdir(list_fams[i])
 len1 = len(glob.glob('*.png')) # assuming the images are stored as 'png'
 no_imgs.append(len1)
 os.chdir('..')

total = sum(no_imgs) # total number of all samples
y = numpy.zeros(total) # label vector

temp1 = numpy.zeros(len(no_imgs)+1)
temp1[1:len(temp1)]=no_imgs
temp2 = int(temp1[0]); # now temp2 is [0 no_imgs]

for jj in range(len(no_imgs)): 
    temp3 = temp2 +int(temp1[jj+1])
    for ii in range(temp2,temp3): 
       y[ii] = jj
    temp2 = temp2+ int(temp1[jj+1])




print(y)