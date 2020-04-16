# unpickling

import pickle
import LeNet 

with open('malimg_data.pkl', 'rb') as f:
    data = pickle.load(f)

# pickle 데이터 확인

print('data[0]: array, vector per each samples: ')
print(data[0].shape)
print(data[0])
print('data[0]: <Example> one sample')
print(data[0][0])
print(data[0][0].shape)  # expect (channel, width, height)

print('-'*40)
print('data[1]: array, y label per each samples: ')
print(data[1])
print(data[1].shape)
print('-'*40)
print('data[2]: list, of class names')
print(data[2])
print('-'*40)
print('data[3]: list, num of samples per class')
print(data[3])
print('-'*40)
print('')

