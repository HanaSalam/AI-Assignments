"""
Day18 - TENSORFLOW
"""
#1. Create a tensor of the shape [2, 3] with all elements set to zero.
import tensorflow as tf
x1 = tf.zeros([2,3],tf.int32)

s1 = tf.Session()
output = s1.run(x1)
print('x1 = ',x1)
print('1. output1')
print(output)
print('--------------------')


#2. Let X be a tensor of [[1,2,3], [4,5,6]].Create a tensor of the same shape and dtype as X with all elements set to zero
X = tf.constant([[1,2,3],[4,5,6]])
x2 = tf.zeros_like(X,tf.int32)

s2 = tf.Session()
out2 = s2.run(x2)
print '2. Output2\n',out2
print('--------------------')

#3. Create a tensor of shape [2, 3] with all elements set to one.
x3 = tf.ones([2,3],tf.int32)
s3 = tf.Session()
out3 = s3.run(x3)
print '3. Output3\n',out3
print('--------------------')

#4. Let X be a tensor of [[1,2,3], [4,5,6]].Create a tensor of the same shape and dtype as X with all elements set to one.
x4 = tf.ones_like([[1,2,3],[4,5,6]],tf.int32)

s4 = tf.Session()
out4 = s4.run(x4)
print '4. Output4\n',out4
print('--------------------')

#5. Create a tensor of the shape [3, 2], with all elements of 5.
x5 = tf.constant([[5,5],[5,5],[5,5]])
s5 = tf.Session()
out5 = s5.run(x5)
print '5. Output5\n',out5
print('--------------------')

#6. Create a constant tensor of [[1, 3, 5], [4, 6, 8]], with dtype=float3
x6 = tf.constant([[1,3,5],[4,6,8]],tf.float32)
s6 = tf.Session()
out6 = s6.run(x6)
print '6. Output6\n',out6
print('--------------------')


#7. Create a constant tensor of the shape [2, 3], with all elements set to 4.
x7 = tf.constant([[4,4,4],[4,4,4]])
s7 = tf.Session()
out7 = s7.run(x7)
print '7.\n',out7
print('--------------------')

#8. Create a 1-D tensor of 50 evenly spaced elements between 5 and 10 inclusive.
a = tf.linspace(5.0,10.0,50,name="a")
s8 = tf.Session()
out8 = s8.run(a)
print '8.\n',out8
print('--------------------')

#9. Create a random tensor of the shape [3, 2], with elements from a normal distribution ofmean=0, standard deviation=2.
b = tf.random_normal([3,2],mean = 0,stddev = 2)
s9 = tf.Session()
print '9.\n',s9.run(b)

print('--------------------')

#10. Create a random tensor of the shape [3, 2], with all elements from a uniform distribution thatranges from 0 to 2 (exclusive).
c = tf.random_uniform([3,2],minval = 0,maxval=2,dtype=tf.float32)
s10 = tf.Session()
print '10.\n',s10.run(c)
print('--------------------')

#11. Let X be a tensor of [[1, 2], [3, 4], [5, 6]]. Shuffle X along its first dimension.
X = tf.constant([[1,2],[3,4],[5,6]])
d = tf.random_shuffle(X)
s11 = tf.Session()
print '11.\n',s11.run(d)
print('--------------------')

#12. Let X be a random tensor of the shape [10, 10, 3], with elements from a unit normaldistribution. Crop X with the shape of [5, 5, 3]. (hint:5, 3])out = tf.random_crop(X, [5,)
X = tf.random_normal([10,10,3],mean=0,stddev=1)
e = tf.random_crop(X,[5,5,3])
s = tf.Session()
print '12.\n',s.run(e)
print('----------------------------------')

#13. Let X be a tensor [[-1, -2, -3], [0, 1, 2]] and Y be a tensor of zeros with the same shape asx. Return a boolean tensor that yields True if X does not equal Y elementwise. (hint : out= tf.not_equal(X, Y))
X = tf.constant([[-1,-2,-3],[0,1,2]])
Y = tf.zeros_like(X)
Z=tf.not_equal(X,Y)
s = tf.Session()
print '13.\n',s.run(Z)
print('----------------------------------')

#14. Add x and y element-wise.(hint: out = tf.add(x, y))
x = tf.constant([[5,6,7],[8,9,10]])
y = tf.constant([[1,2,3],[4,5,6]])
z = tf.constant([[1,1,1],[1,1,1
                          ]])
s = tf.Session()
print '14.\n',s.run(tf.add(x,y))
print('----------------------------------')


#15. Subtract y from x element-wise.
print '15.\n',s.run(tf.subtract(y,x))
print('----------------------------------')

#16. Multiply x by y element-wise.
print '16.\n',s.run(tf.multiply(x,y))
print('----------------------------------')

#17. Multiply x by 5 element-wise.
print '17.\n',s.run(tf.multiply(x,5))
print('----------------------------------')

#18.Add x, y, and z element-wise.
print '18.\n',s.run(tf.add(tf.add(x,y),z))
print('----------------------------------')

#19.View the output using tensorboard for random questions
writer = tf.summary.FileWriter('.f1',s1.graph)
writer.close()
s.close()
#for i in range(5):
