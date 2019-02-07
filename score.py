#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
File: score.py
Author: Stephane Menard
Creation date: January 18th 2019
Description: Script that calculate the score of the tests images:
             - ./data/label_test_set.npy
             - ./images/image_gen.npy
Required package: numpy and tensorflow
'''

import os
import numpy as np

from scoreFunction import *


lowres_test= np.load('./data/input_test_set.npy')
label_test= np.load('./data/label_test_set.npy')

generated_test = np.load('./images/image_gen_test.npy')

print('lowres:', lowres_test.shape)
print('label : ', label_test.shape)
print('generated:', generated_test.shape)
print('------------------------------')

#lowres_scores = getScore(lowres_test[:,5,:,:].reshape(248,1,256,256), label_test)
#print('lowres score (mean) =', np.mean(lowres_scores))

generated_scores = getScore(generated_test, label_test)

#print('generated score =', generated_scores)

date_times = np.load('./data/date_test_set.npy')

with open('./images/image_gen_test_score.csv', 'w') as f:
    for i in range(len(date_times)):
        date_time = date_times[i].decode('UTF-8')
        score = generated_scores[i]

        print('{} --> {:10.4f}'.format(date_time, score))
        f.write('"{}","{:10.4f}"\n'.format(date_time, score))


print('generated score (mean) =', np.mean(generated_scores))

