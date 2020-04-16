# Get number of samples per family

import os
import glob
import numpy as np
os.chdir('K:\malimg')

list_fams = os.listdir(os.getcwd()) # vector of strings with family names

no_imgs = [] # No. of samples per family
# print(list_fams)
# print(len(list_fams))
# print(os.getcwd())

for i in range(len(list_fams)):
    # list_1 = os.path.join(os.getcwd(), list_fams[i])
    # print(list_1)
    # os.chdir(list_1)
    os.chdir(list_fams[i])
    len1= len(glob.glob('*png'))
    no_imgs.append(len1)
    os.chdir('..')

# print('num_img: ', no_imgs)

total = sum(no_imgs) # total number of all samples
# print('total: ', total)
y = np.zeros(total)  # label vector
                     # initialization
# print('y: ', y)
# print('len(y): ', len(y))

temp1 = np.zeros(len(no_imgs)+1)  # 26개의 영행렬을 만들어준다.
                                  # 만들어주는 이유는 뒤에서 나오겠지!
# print('temp1: ',temp1)
# print('len(temp1): ', len(temp1))
temp1[1:len(temp1)]=no_imgs  # temp1은 0번째 인덱스를 제외하면
                             # 2부터 26인덱스까지는 no_imgs의 값을
                             # 순차대로 저장하고 있다.
temp2 = int(temp1[0])  # now temp2 is [0 no_imgs]
                       # temp2는 그냥 0이야
# print('temp2: ', temp2)


for jj in range(len(no_imgs)):
    temp3 = temp2 + int(temp1[jj+1])
    for ii in range(temp2, temp3):  # 0부터 no_img[0]까지 루프
        y[ii] = jj  # y의 0, 1, 2, ...len(no_img[0])까지 레이블은 0이다.
    
    temp2 = temp2 + int(temp1[jj+1]) # 첫 레이블링이 다되면 temp2를 1올려준다.
      
print('y는 레이블값을 나타낸다.')
print("y: ", y)
print("y[0:121]", y[0:121])

print("y[122]: ", y[122])
## 디렉터리 내에 파일 읽는 방법 찾기
## 찾고 직접 구현해보기
## Done

# Note: temp2는 뭐고, temp3은 뭐냐!
# 20.04.03.Fri