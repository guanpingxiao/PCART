import tensorflow as tf
scce = tf.keras.losses.SparseCategoricalCrossentropy(False, tf.keras.losses.Reduction.NONE, 'sparse_categorical_crossentropy', ignore_class=None)