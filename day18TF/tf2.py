"""
Variables & Placeholders
20. Create a variable w with an initial value of 1.0 and name weight. Then, print out the value
of w.
21. Write a program with three variables and get the sum of these three variables
22. Create a Placeholder. Assign a value to it and print the same.
23. Write a program with three Placeholders and get the sum of the three values given to these
variables.
"""
import tensorflow as tf
import numpy as np
w = tf.Variable(1.0,name="weight")




x=tf.Variable(3,name="x")
y=tf.Variable(4,name="x")
z=tf.Variable(5,name="x")

z1 = tf.add_n([x,y,z])
init = tf.global_variables_initializer()
with tf.Session() as s:
    s.run(init)
    print(s.run(x.assign_add(y)))
    print(s.run(x.assign_add(z)))
    
"""
p1 = tf.placeholder(tf.int32,(2,2))
p2 = np.random.rand(2,2)

x1 = tf.placeholder(tf.int32)
x2 = tf.placeholder(tf.int32)
x3 = tf.placeholder(tf.int32)
sum1 = tf.add_n([x1,x2,x3])
init = tf.global_variables_initializer()
s = tf.Session()
s.run(init)
print(s.run(sum1,feed_dict={x1:25,x2:35,x3:45}))
s.close()

"""
