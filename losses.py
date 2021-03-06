import tensorflow as tf

def mae(pred_y, true_y):
    return tf.reduce_mean(tf.squared_difference(pred_y, true_y))

def abs_criterion(pred_y, true_y):
    return tf.reduce_mean(tf.abs(pred_y - true_y))