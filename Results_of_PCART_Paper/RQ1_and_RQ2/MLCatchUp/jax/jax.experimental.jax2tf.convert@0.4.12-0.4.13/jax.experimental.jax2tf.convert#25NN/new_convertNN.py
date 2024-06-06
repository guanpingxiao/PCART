import jax
from jax.experimental import jax2tf
import jax.numpy as jnp

def sum_of_squares(x):
    return jnp.sum(x ** 2)
jax2tf.convert(polymorphic_shapes=None, fun_jax=sum_of_squares, experimental_native_lowering='default', enable_xla=True, with_gradient=True, _DefaultNativeSerialization]=DEFAULT_NATIVE_SERIALIZATION, native_serialization_disabled_checks=())