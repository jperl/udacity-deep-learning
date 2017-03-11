# import numpy as np
# print(np.eye(10))

import tensorflow as tf

x = tf.Variable(tf.random_normal([10, 10], stddev=.1))

with tf.Session() as sess:
   sess.run(tf.global_variables_initializer())
   print(x.eval())
