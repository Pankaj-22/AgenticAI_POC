import tensorflow as tf

x = tf.constant([[1, 1, 1],
                 [1, 1, 1],
                 [1, 1, 1]])

a = tf.constant([[2],
                 [5],
                 [5]])

y = tf.tensordot(x,a,1)
print(y)

z= x * a
print(z)

test = tf.constant([2,8])

print(test.shape , " and *************************" )

# if tf.config.list_physical_devices('GPU'):
#   print("TensorFlow **IS** using the GPU")
# else:
#   print("TensorFlow **IS NOT** using the GPU")

 