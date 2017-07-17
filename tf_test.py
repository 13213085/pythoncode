# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 00:17:56 2017

@author: 29907
"""

import tensorflow as tf
sess = tf.Session()
a = tf.constant(10)
b = tf.constant(22)
print(sess.run(a + b))