import jax
from jax.experimental import jax2tf
import jax.numpy as jnp

def sum_of_squares(x):
    return jnp.sum(x ** 2)
jax2tf.convert(fun_jax=sum_of_squares, polymorphic_shapes=None, with_gradient=True, _DefaultNativeSerialization]=DEFAULT_NATIVE_SERIALIZATION, native_serialization_disabled_checks=())