# global
from numbers import Number
from typing import Optional, Union

# local
import ivy
from ivy.backend_handler import current_backend
from ivy.func_wrapper import (
    handle_out_argument,
    to_native_arrays_and_back,
    handle_nestable,
)


# Array API Standard #
# -------------------#


@to_native_arrays_and_back
@handle_out_argument
@handle_nestable
def abs(
    x: Union[float, ivy.Array, ivy.NativeArray],
    *,
    out: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
) -> ivy.Array:
    """Calculates the absolute value for each element ``x_i`` of the input array ``x``
    (i.e., the element-wise result has the same magnitude as the respective element in
    ``x`` but has positive sign).

    .. note::
        For signed integer data types, the absolute value of the minimum representable
        integer is implementation-dependent.

    **Special Cases**

    For this particular case,

    - If ``x_i`` is ``NaN``, the result is ``NaN``.
    - If ``x_i`` is ``-0``, the result is ``+0``.
    - If ``x_i`` is ``-infinity``, the result is ``+infinity``.

    Parameters
    ----------
    x
        input array. Should have a numeric data type.
    out
        optional output array, for writing the result to. It must have a shape that the
        inputs broadcast to.

    Returns
    -------
    ret
        an array containing the absolute value of each element in ``x``. The returned
        array must have the same data type as ``x``.

    """
    return current_backend(x).abs(x, out=out)


@to_native_arrays_and_back
@handle_out_argument
@handle_nestable
def acos(
    x: Union[ivy.Array, ivy.NativeArray],
    *,
    out: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
) -> ivy.Array:
    """Calculates an implementation-dependent approximation of the principal value of
    the inverse cosine, having domain [-1, +1] and codomain [+0, +π], for each element
    x_i of the input array x. Each element-wise result is expressed in radians.

    **Special cases**

    For floating-point operands,

    - If x_i is NaN, the result is NaN.
    - If x_i is greater than 1, the result is NaN.
    - If x_i is less than -1, the result is NaN.
    - If x_i is 1, the result is +0.

    Parameters
    ----------
    x
        input array. Should have a floating-point data type.
    out
        optional output array, for writing the result to. It must have a shape that the
        inputs broadcast to.

    Returns
    -------
    ret
        an array containing the inverse cosine of each element in x. The returned array
        must have a floating-point data type determined by :ref:`type-promotion`.

    """
    return current_backend(x).acos(x, out=out)


@to_native_arrays_and_back
@handle_out_argument
@handle_nestable
def acosh(
    x: Union[ivy.Array, ivy.NativeArray],
    *,
    out: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
) -> ivy.Array:
    """Calculates an implementation-dependent approximation to the inverse hyperbolic
    cosine, having domain ``[+1, +infinity]`` and codomain ``[+0, +infinity]``, for each
    element ``x_i`` of the input array ``x``.

    **Special cases**

    For floating-point operands,

    - If ``x_i`` is ``NaN``, the result is ``NaN``.
    - If ``x_i`` is less than ``1``, the result is ``NaN``.
    - If ``x_i`` is ``1``, the result is ``+0``.
    - If ``x_i`` is ``+infinity``, the result is ``+infinity``.

    Parameters
    ----------
    x
        input array whose elements each represent the area of a hyperbolic sector.
        Should have a floating-point data type.
    out
        optional output array, for writing the result to. It must have a shape that the
        inputs broadcast to.

    Returns
    -------
    ret
        an array containing the inverse hyperbolic cosine of each element in x. The
        returned array must have a floating-point data type determined by
        :ref:`type-promotion`.

    """
    return current_backend(x).acosh(x, out=out)


@to_native_arrays_and_back
@handle_out_argument
@handle_nestable
def add(
    x1: Union[float, ivy.Array, ivy.NativeArray],
    x2: Union[float, ivy.Array, ivy.NativeArray],
    *,
    out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """Calculates the sum for each element ``x1_i`` of the input array ``x1`` with the
    respective element ``x2_i`` of the input array ``x2``.

    **Special cases**

    For floating-point operands,

    - If either ``x1_i`` or ``x2_i`` is ``NaN``, the result is ``NaN``.
    - If ``x1_i`` is ``+infinity`` and ``x2_i`` is ``-infinity``, the result is ``NaN``.
    - If ``x1_i`` is ``-infinity`` and ``x2_i`` is ``+infinity``, the result is ``NaN``.
    - If ``x1_i`` is ``+infinity`` and ``x2_i`` is ``+infinity``, the result is
      ``+infinity``.
    - If ``x1_i`` is ``-infinity`` and ``x2_i`` is ``-infinity``, the result is
      ``-infinity``.
    - If ``x1_i`` is ``+infinity`` and ``x2_i`` is a finite number, the result is
      ``+infinity``.
    - If ``x1_i`` is ``-infinity`` and ``x2_i`` is a finite number, the result is
      ``-infinity``.
    - If ``x1_i`` is a finite number and ``x2_i`` is ``+infinity``, the result is
      ``+infinity``.
    - If ``x1_i`` is a finite number and ``x2_i`` is ``-infinity``, the result is
      ``-infinity``.
    - If ``x1_i`` is ``-0`` and ``x2_i`` is ``-0``, the result is ``-0``.
    - If ``x1_i`` is ``-0`` and ``x2_i`` is ``+0``, the result is ``+0``.
    - If ``x1_i`` is ``+0`` and ``x2_i`` is ``-0``, the result is ``+0``.
    - If ``x1_i`` is ``+0`` and ``x2_i`` is ``+0``, the result is ``+0``.
    - If ``x1_i`` is either ``+0`` or ``-0`` and ``x2_i`` is a nonzero finite number,
      the result is ``x2_i``.
    - If ``x1_i`` is a nonzero finite number and ``x2_i`` is either ``+0`` or ``-0``,
      the result is ``x1_i``.
    - If ``x1_i`` is a nonzero finite number and ``x2_i`` is ``-x1_i``, the result is
      ``+0``.
    - In the remaining cases, when neither ``infinity``, ``+0``, ``-0``, nor a ``NaN``
      is involved, and the operands have the same mathematical sign or have different
      magnitudes, the sum must be computed and rounded to the nearest representable
      value according to IEEE 754-2019 and a supported round mode. If the magnitude is
      too large to represent, the operation overflows and the result is an `infinity`
      of appropriate mathematical sign.

    .. note::
       Floating-point addition is a commutative operation, but not always associative.

    Parameters
    ----------
    x1
        first input array. Should have a numeric data type.
    x2
        second input array. Must be compatible with ``x1`` (see :ref:`broadcasting`).
        Should have a numeric data type.
    out
        optional output array, for writing the result to. It must have a shape that the
        inputs broadcast to.

    Returns
    -------
     ret
        an array containing the element-wise sums. The returned array must have a data
        type determined by :ref:`type-promotion`.

    This function conforms to the `Array API Standard
    <https://data-apis.org/array-api/latest/>`_. This docstring is an extension of the
    `docstring <https://data-apis.org/array-api/latest/API_specification/generated/signatures.elementwise_functions.add.html>`_ # noqa
    in the standard.

    Both the description and the type hints above assumes an array input for simplicity,
    but this function is *nestable*, and therefore also accepts :code:`ivy.Container`
    instances in place of any of the arguments.

    Examples
    --------
    With :code:`ivy.Array` inputs:

    >>> x = ivy.array([1, 2, 3])
    >>> y = ivy.array([4, 5, 6])
    >>> z = ivy.add(x, y)
    >>> print(z)
    ivy.array([5, 7, 9])

    >>> x = ivy.array([[1.1, 2.3, -3.6]])
    >>> y = ivy.array([[4.8], [5.2], [6.1]])
    >>> z = ivy.zeros((3, 3))
    >>> ivy.add(x, y, out=z)
    >>> print(z)
    ivy.array([[5.9, 7.1, 1.2],
               [6.3, 7.5, 1.6],
               [7.2, 8.4, 2.5]])

    >>> x = ivy.array([[[1.1], [3.2], [-6.3]]])
    >>> y = ivy.array([[8.4], [2.5], [1.6]])
    >>> ivy.add(x, y, out=x)
    >>> print(x)
    ivy.array([[[9.5],
                [5.7],
                [-4.7]]])

    With one :code:`ivy.Container` input:

    >>> x = ivy.array([[1.1, 2.3, -3.6]])
    >>> y = ivy.Container(a=ivy.array([[4.], [5.], [6.]]),\
                          b=ivy.array([[5.], [6.], [7.]]))
    >>> z = ivy.add(x, y)
    >>> print(z)
    {
        a: ivy.array([[5.1, 6.3, 0.4],
                      [6.1, 7.3, 1.4],
                      [7.1, 8.3, 2.4]]),
        b: ivy.array([[6.1, 7.3, 1.4],
                      [7.1, 8.3, 2.4],
                      [8.1, 9.3, 3.4]])
    }

    With multiple :code:`ivy.Container` inputs:

    >>> x = ivy.Container(a=ivy.array([1, 2, 3]), \
                          b=ivy.array([2, 3, 4]))
    >>> y = ivy.Container(a=ivy.array([4, 5, 6]),\
                          b=ivy.array([5, 6, 7]))
    >>> z = ivy.add(x, y)
    >>> print(z)
    {
        a: ivy.array([5, 7, 9]),
        b: ivy.array([7, 9, 11])
    }
    """
    return current_backend(x1, x2).add(x1, x2, out=out)


@to_native_arrays_and_back
@handle_out_argument
@handle_nestable
def asin(
    x: Union[ivy.Array, ivy.NativeArray],
    *,
    out: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
) -> ivy.Array:
    """Calculates an implementation-dependent approximation of the principal value of
    the inverse sine, having domain ``[-1, +1]`` and codomain ``[-π/2, +π/2]`` for each
    element ``x_i`` of the input array ``x``. Each element-wise result is expressed in
    radians.

    **Special cases**

    For floating-point operands,

    - If ``x_i`` is ``NaN``, the result is ``NaN``.
    - If ``x_i`` is greater than ``1``, the result is ``NaN``.
    - If ``x_i`` is less than ``-1``, the result is ``NaN``.
    - If ``x_i`` is ``+0``, the result is ``+0``.
    - If ``x_i`` is ``-0``, the result is ``-0``.

    Parameters
    ----------
    x
        input array. Should have a floating-point data type.
    out
        optional output array, for writing the result to. It must have a shape that the
        inputs broadcast to.

    Returns
    -------
    ret
        an array containing the inverse sine of each element in ``x``. The returned
        array must have a floating-point data type determined by :ref:`type-promotion`.

    This function conforms to the `Array API Standard
    <https://data-apis.org/array-api/latest/>`_. This docstring is an extension of the
    `docstring <https://data-apis.org/array-api/latest/API_specification/generated/
        signatures.elementwise_functions.tan.html>`_
    in the standard.

    Both the description and the type hints above assumes an array input for simplicity,
    but this function is *nestable*, and therefore also accepts :code:`ivy.Container`
    instances in place of any of the arguments.

    Functional Examples
    -------------------

    With :code:`ivy.Array` input:

    >>> x = ivy.array([-2.4, -0, +0, 3.2, float('nan')])
    >>> y = ivy.asin(x)
    >>> print(y)
    ivy.array([nan,  0.,  0., nan, nan], dtype=float32)

    >>> x = ivy.array([-1, -0.5, 0.6, 1])
    >>> y = ivy.zeros(4)
    >>> ivy.asin(x, out=y)
    >>> print(y)
    ivy.array([-1.5707964 , -0.5235988 ,
               0.64350116,  1.5707964 ], dtype=float32)

    >>> x = ivy.array([[0.1, 0.2, 0.3], \
                       [-0.4, -0.5, -0.6]])
    >>> ivy.asin(x, out=x)
    >>> print(x)
    ivy.array([[ 0.10016742,  0.20135793,  0.30469266], \
               [-0.41151685, -0.5235988 , -0.64350116]], dtype=float32)

    With :code:`ivy.NativeArray` input:

    >>> x = ivy.native_array([-1, -0.5, 0.6, 1])
    >>> y = ivy.asin(x)
    >>> print(y)
    ivy.array([-1.5707964 , -0.5235988 ,
               0.64350116,  1.5707964 ], dtype=float32)

    With :code:`ivy.Container` input:

    >>> x = ivy.Container(a=ivy.array([0., 0.1, 0.2]), \
                          b=ivy.array([0.3, 0.4, 0.5]))
    >>> y = ivy.asin(x)
    >>> print(y)
    {
        a: ivy.array([0., 0.10016742, 0.20135793], dtype=float32),
        b: ivy.array([0.30469266, 0.41151685, 0.5235988], dtype=float32)
    }

    Instance Method Examples
    ------------------------

    Using :code:`ivy.Array` instance method:

    >>> x = ivy.array([-1, -0.5, 0.6, 1])
    >>> y = x.asin()
    >>> print(y)
    ivy.array([-1.5707964 , -0.5235988 ,
               0.64350116,  1.5707964 ], dtype=float32)

    Using :code:`ivy.Container` instance method:

    >>> x = ivy.Container(a=ivy.array([0., 0.1, 0.2]), \
                          b=ivy.array([0.3, 0.4, 0.5]))
    >>> y = x.asin()
    >>> print(y)
    {
        a: ivy.array([0., 0.10016742, 0.20135793], dtype=float32),
        b: ivy.array([0.30469266, 0.41151685, 0.5235988], dtype=float32)
    }

    """
    return current_backend(x).asin(x, out=out)


@to_native_arrays_and_back
@handle_out_argument
@handle_nestable
def asinh(
    x: Union[ivy.Array, ivy.NativeArray],
    *,
    out: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
) -> ivy.Array:
    """Calculates an implementation-dependent approximation to the inverse hyperbolic
    sine, having domain ``[-infinity, +infinity]`` and codomain
    ``[-infinity, +infinity]``, for each element ``x_i`` in the input array ``x``.

    **Special cases**

    For floating-point operands,

    - If ``x_i`` is ``NaN``, the result is ``NaN``.
    - If ``x_i`` is ``+0``, the result is ``+0``.
    - If ``x_i`` is ``-0``, the result is ``-0``.
    - If ``x_i`` is ``+infinity``, the result is ``+infinity``.
    - If ``x_i`` is ``-infinity``, the result is ``-infinity``.

    Parameters
    ----------
    x
        input array whose elements each represent the area of a hyperbolic sector.
        Should have a floating-point data type.
    out
        optional output array, for writing the result to. It must have a shape that the
        inputs broadcast to.

    Returns
    -------
    ret
        an array containing the inverse hyperbolic sine of each element in ``x``. The
        returned array must have a floating-point data type determined by
        :ref:`type-promotion`.

    """
    return current_backend(x).asinh(x, out=out)


@to_native_arrays_and_back
@handle_out_argument
@handle_nestable
def atan(
    x: Union[ivy.Array, ivy.NativeArray],
    *,
    out: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
) -> ivy.Array:
    """Calculates an implementation-dependent approximation of the principal value of
    the inverse tangent, having domain ``[-infinity, +infinity]`` and codomain
    ``[-π/2, +π/2]``, for each element ``x_i`` of the input array ``x``. Each
    element-wise result is expressed in radians.

    **Special cases**

    For floating-point operands,

    - If ``x_i`` is ``NaN``, the result is ``NaN``.
    - If ``x_i`` is ``+0``, the result is ``+0``.
    - If ``x_i`` is ``-0``, the result is ``-0``.
    - If ``x_i`` is ``+infinity``, the result is an implementation-dependent
      approximation to ``+π/2``.
    - If ``x_i`` is ``-infinity``, the result is an implementation-dependent
      approximation to ``-π/2``.

    Parameters
    ----------
    x
        input array. Should have a floating-point data type.
    out
        optional output array, for writing the result to. It must have a shape that the
        inputs broadcast to.

    Returns
    -------
    ret
        an array containing the inverse tangent of each element in ``x``. The returned
        array must have a floating-point data type determined by :ref:`type-promotion`.

    """
    return current_backend(x).atan(x, out=out)


@to_native_arrays_and_back
@handle_out_argument
@handle_nestable
def atan2(
    x1: Union[ivy.Array, ivy.NativeArray],
    x2: Union[ivy.Array, ivy.NativeArray],
    *,
    out: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
) -> ivy.Array:
    """Calculates an implementation-dependent approximation of the inverse tangent of
    the quotient ``x1/x2``, having domain ``[-infinity, +infinity] x.
    [-infinity, +infinity]`` (where the ``x`` notation denotes the set of ordered pairs
    of elements ``(x1_i, x2_i)``) and codomain ``[-π, +π]``, for each pair of elements
    ``(x1_i, x2_i)`` of the input arrays ``x1`` and ``x2``, respectively. Each
    element-wise result is expressed in radians. The mathematical signs of
    ``x1_i and x2_i`` determine the quadrant of each element-wise result. The quadrant
    (i.e., branch) is chosen such that each element-wise result is the signed angle in
    radians between the ray ending at the origin and passing through the point ``(1,0)``
    and the ray ending at the origin and passing through the point ``(x2_i, x1_i)``.

    **Special cases**

    For floating-point operands,

    - If either ``x1_i`` or ``x2_i`` is ``NaN``, the result is ``NaN``.
    - If ``x1_i`` is greater than ``0`` and ``x2_i`` is ``+0``, the result is an
      approximation to ``+π/2``.
    - If ``x1_i`` is greater than ``0`` and ``x2_i`` is ``-0``, the result is an
      approximation to ``+π/2``.
    - If ``x1_i`` is ``+0`` and ``x2_i`` is greater than ``0``, the result is ``+0``.
    - If ``x1_i`` is ``+0`` and ``x2_i`` is ``+0``, the result is ``+0``.
    - If ``x1_i`` is ``+0`` and ``x2_i`` is ``-0``, the result is an approximation to
      ``+π``.
    - If ``x1_i`` is ``+0`` and ``x2_i`` is less than 0, the result is an approximation
      to ``+π``.
    - If ``x1_i`` is ``-0`` and ``x2_i`` is greater than ``0``, the result is ``-0``.
    - If ``x1_i`` is ``-0`` and ``x2_i`` is ``+0``, the result is ``-0``.
    - If ``x1_i`` is ``-0`` and ``x2_i`` is ``-0``, the result is an approximation to
      ``-π``.
    - If ``x1_i`` is ``-0`` and ``x2_i`` is less than ``0``, the result is an
      approximation to ``-π``.
    - If ``x1_i`` is less than ``0`` and ``x2_i`` is ``+0``, the result is an
      approximation to ``-π/2``.
    - If ``x1_i`` is less than ``0`` and ``x2_i`` is ``-0``, the result is an
      approximation to ``-π/2``.
    - If ``x1_i`` is greater than ``0``, ``x1_i`` is a finite number, and ``x2_i`` is
      ``+infinity``, the result is ``+0``.
    - If ``x1_i`` is greater than ``0``, ``x1_i`` is a finite number, and ``x2_i`` is
      ``-infinity``, the result is an approximation to ``+π``.
    - If ``x1_i`` is less than ``0``, ``x1_i`` is a finite number, and ``x2_i`` is
      ``+infinity``, the result is ``-0``.
    - If ``x1_i`` is less than ``0``, ``x1_i`` is a finite number, and ``x2_i`` is
      ``-infinity``, the result is an approximation to ``-π``.
    - If ``x1_i`` is ``+infinity`` and ``x2_i`` is finite, the result is an
      approximation to ``+π/2``.
    - If ``x1_i`` is ``-infinity`` and ``x2_i`` is finite, the result is an
      approximation to ``-π/2``.
    - If ``x1_i`` is ``+infinity`` and ``x2_i`` is ``+infinity``, the result is an
      approximation to ``+π/4``.
    - If ``x1_i`` is ``+infinity`` and ``x2_i`` is ``-infinity``, the result is an
      approximation to ``+3π/4``.
    - If ``x1_i`` is ``-infinity`` and ``x2_i`` is ``+infinity``, the result is an
      approximation to ``-π/4``.
    - If ``x1_i`` is ``-infinity`` and ``x2_i`` is ``-infinity``, the result is an
      approximation to ``-3π/4``.

    Parameters
    ----------
    x1
        input array corresponding to the y-coordinates. Should have a floating-point
        data type.
    x2
        input array corresponding to the x-coordinates. Must be compatible with ``x1``.
        Should have a floating-point data type.
    out
        optional output array, for writing the result to. It must have a shape that the
        inputs broadcast to.

    Returns
    -------
    ret
        an array containing the inverse tangent of the quotient ``x1/x2``. The returned
        array must have a floating-point data type.

    """
    return current_backend(x1).atan2(x1, x2, out=out)


@to_native_arrays_and_back
@handle_out_argument
@handle_nestable
def atanh(
    x: Union[ivy.Array, ivy.NativeArray],
    *,
    out: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
) -> ivy.Array:
    """Returns a new array with the inverse hyperbolic tangent of the elements of ``x``.

    Parameters
    ----------
    x
        input array whose elements each represent the area of a hyperbolic sector.
        Should have a floating-point data type.

    Returns
    -------
    ret
        an array containing the inverse hyperbolic tangent of each element in ``x``. The
        returned array must have a floating-point data type determined by Type Promotion
        Rules.

    Examples
    --------
    >>> x = ivy.atanh(ivy.array([0, -0.5]))
    >>> print(x)
    ivy.array([0., -0.549])

    """
    return current_backend(x).atanh(x, out=out)


@to_native_arrays_and_back
@handle_out_argument
@handle_nestable
def bitwise_and(
    x1: Union[int, bool, ivy.Array, ivy.NativeArray],
    x2: Union[int, bool, ivy.Array, ivy.NativeArray],
    *,
    out: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
) -> ivy.Array:
    """Computes the bitwise AND of the underlying binary representation of each element
    ``x1_i`` of the input array ``x1`` with the respective element ``x2_i`` of the input
    array ``x2``.

    Parameters
    ----------
    x1
        first input array. Should have an integer or boolean data type.
    x2
        second input array. Must be compatible with ``x1`` (see :ref:`broadcasting`).
        Should have an integer or boolean data type.
    out
        optional output array, for writing the result to. It must have a shape that the
        inputs broadcast to.

    Returns
    -------
    ret
        an array containing the element-wise results. The returned array must have a
        data type determined by :ref:`type-promotion`.


    This function conforms to the `Array API Standard
    <https://data-apis.org/array-api/latest/>`_. This docstring is an extension of the
    `docstring <https://data-apis.org/array-api/latest/API_specification/generated/signatures.elementwise_functions.bitwise_and.html>`_ # noqa
    in the standard. The descriptions above assume an array input for simplicity, but
    the method also accepts :code:`ivy.Container` instances in place of
    :code:`ivy.Array` or :code:`ivy.NativeArray` instances, as shown in the type hints
    and also the examples below.

    Functional Examples
    -------------------

    With :code:`ivy.Array` inputs:

    >>> x = ivy.array([2, 3, 7])
    >>> y = ivy.array([7, 1, 15])
    >>> z = ivy.bitwise_and(x, y)
    >>> print(z)
    ivy.array([2, 1, 7])

    >>> x = ivy.array([[True], \
                       [False]])
    >>> y = ivy.array([[True], \
                       [True]])
    >>> ivy.bitwise_and(x, y, out=x)
    >>> print(x)
    ivy.array([[ True],
               [False]])

    >>> x = ivy.array([1])
    >>> y = ivy.array([3])
    >>> ivy.bitwise_and(x, y, out=y)
    >>> print(y)
    ivy.array([1])

    With :code:`ivy.NativeArray` inputs:

    >>> x = ivy.native_array([True, True, False, False])
    >>> y = ivy.native_array([True, False, True, False])
    >>> ivy.bitwise_and(x, y, out=y)
    >>> print(y)
    ivy.native_array([ True, False, False, False])

    >>> x = ivy.native_array([[True, False]])
    >>> y = ivy.native_array([[True], \
                              [False]])
    >>> z = ivy.bitwise_and(x, y)
    >>> print(z)
    ivy.array([[ True, False],
               [False, False]])

    With a mix of :code:`ivy.Array` and :code:`ivy.NativeArray` inputs:

    >>> x = ivy.array([[6, 5], \
                       [3, 7]])
    >>> y = ivy.native_array([[2, 11], \
                              [9, 13]])
    >>> z = ivy.bitwise_and(x, y)
    >>> print(z)
    ivy.array([[2, 1],
               [1, 5]])

    With :code:`ivy.Container` input:

    >>> x = ivy.Container(a=ivy.array([1, 2, 3]), b=ivy.array([4, 5, 6]))
    >>> y = ivy.Container(a=ivy.array([7, 8, 9]), b=ivy.array([10, 11, 11]))
    >>> z = ivy.bitwise_and(x, y)
    >>> print(z)
    {
        a: ivy.array([1, 0, 1]),
        b: ivy.array([0, 1, 2])
    }

    With a mix of :code:`ivy.Array` and :code:`ivy.Container` inputs: 

    >>> x = ivy.array([True, True])
    >>> y = ivy.Container(a=ivy.array([True, False]), b=ivy.array([False, True]))
    >>> z = ivy.bitwise_and(x, y)
    >>> print(z)
    {
        a: ivy.array([True, False]),
        b: ivy.array([False, True])
    }

    Instance Method Examples
    ------------------------

    Using :code:`ivy.Array` instance method:

    >>> x = ivy.array([True, False])
    >>> y = ivy.array([True, True])
    >>> x.bitwise_and(y, out=y)
    >>> print(y)
    ivy.array([ True, False])

    >>> x = ivy.array([[7], \
                       [8], \
                       [9]])
    >>> y = ivy.native_array([[10], \
                              [11], \
                              [12]])
    >>> z = x.bitwise_and(y)
    >>> print(z)
    ivy.array([[2],
               [8],
               [8]])

    Using :code:`ivy.Container` instance method:
    
    >>> x = ivy.Container(a=ivy.array([True, True]), b=ivy.array([False, True]))
    >>> y = ivy.Container(a=ivy.array([False, True]), b=ivy.array([False, True]))
    >>> x.bitwise_and(y, out=y)
    >>> print(y)
    {
        a: ivy.array([False, True]),
        b: ivy.array([False, True])
    }

    """
    return current_backend(x1, x2).bitwise_and(x1, x2, out=out)


@to_native_arrays_and_back
@handle_out_argument
@handle_nestable
def bitwise_invert(
    x: Union[int, bool, ivy.Array, ivy.NativeArray],
    *,
    out: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
) -> ivy.Array:
    """Inverts (flips) each bit for each element ``x_i`` of the input array ``x``.

    Parameters
    ----------
    x
        input array. Should have an integer or boolean data type.
    out
        optional output array, for writing the result to. It must have a shape that the
        inputs broadcast to.

    Returns
    -------
    ret
        an array containing the element-wise results. The returned array must have the
        same data type as x.

    Examples
    --------
    >>> x = ivy.array([1, 6, 9])
    >>> y = ivy.bitwise_invert(x)
    >>> print(y)
    ivy.array([-2, -7, -10])

    """
    return current_backend(x).bitwise_invert(x, out=out)


@to_native_arrays_and_back
@handle_out_argument
@handle_nestable
def bitwise_left_shift(
    x1: Union[int, ivy.Array, ivy.NativeArray],
    x2: Union[int, ivy.Array, ivy.NativeArray],
    *,
    out: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
) -> ivy.Array:
    """Shifts the bits of each element ``x1_i`` of the input array ``x1`` to the left by
    appending ``x2_i`` (i.e., the respective element in the input array ``x2``) zeros to
    the right of ``x1_i``.

    Parameters
    ----------
    x1
        first input array. Should have an integer data type.
    x2
        second input array. Must be compatible with ``x1`` (see :ref:`broadcasting`).
        Should have an integer data type. Each element must be greater than or equal to
        ``0``.
    out
        optional output array, for writing the result to. It must have a shape that the
        inputs broadcast to.

    Returns
    -------
    ret
        an array containing the element-wise results. The returned array must have a
        data type determined by :ref:`type-promotion`.

    """
    return current_backend(x1, x2).bitwise_left_shift(x1, x2, out=out)


@to_native_arrays_and_back
@handle_out_argument
@handle_nestable
def bitwise_or(
    x1: Union[int, bool, ivy.Array, ivy.NativeArray],
    x2: Union[int, bool, ivy.Array, ivy.NativeArray],
    *,
    out: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
) -> ivy.Array:
    """Computes the bitwise OR of the underlying binary representation of each element
    ``x1_i`` of the input array ``x1`` with the respective element ``x2_i`` of the input
    array ``x2``.

    Parameters
    ----------
    x1
        first input array. Should have an integer or boolean data type.
    x2
        second input array. Must be compatible with ``x1`` (see :ref:`broadcasting`).
        Should have an integer or boolean data type.
    out
        optional output array, for writing the result to. It must have a shape that the
        inputs broadcast to.

    Returns
    -------
    ret
        an array containing the element-wise results. The returned array must have a
        data type determined by :ref:`type-promotion`.

    """
    return current_backend(x1, x2).bitwise_or(x1, x2, out=out)


@to_native_arrays_and_back
@handle_out_argument
@handle_nestable
def bitwise_right_shift(
    x1: Union[int, ivy.Array, ivy.NativeArray],
    x2: Union[int, ivy.Array, ivy.NativeArray],
    *,
    out: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
) -> ivy.Array:
    """Shifts the bits of each element ``x1_i`` of the input array ``x1`` to the right
    according to the respective element ``x2_i`` of the input array ``x2``.

    .. note::
       This operation must be an arithmetic shift (i.e., sign-propagating) and thus
       equivalent to floor division by a power of two.

    Parameters
    ----------
    x1
        first input array. Should have an integer data type.
    x2
        second input array. Must be compatible with ``x1`` (see  ref:`broadcasting`).
        Should have an integer data type. Each element must be greater than or equal to
        0.
    out
        optional output array, for writing the result to. It must have a shape that the
        inputs broadcast to.

    Returns
    -------
    ret
        out (array), an array containing the element-wise results.
        The returned array must have a data type determined by Type Promotion Rules.

    Examples
    --------
    >>> lhs = ivy.array([5, 2, 3, 1], dtype=ivy.int64)
    >>> rhs = ivy.array([1, 3, 2, 1], dtype=ivy.int64)
    >>> y = ivy.bitwise_right_shift(lhs, rhs)
    >>> print(y)
    ivy.array([2, 0, 0, 0])
    """
    return current_backend(x1, x2).bitwise_right_shift(x1, x2, out=out)


@to_native_arrays_and_back
@handle_out_argument
@handle_nestable
def bitwise_xor(
    x1: Union[int, bool, ivy.Array, ivy.NativeArray],
    x2: Union[int, bool, ivy.Array, ivy.NativeArray],
    *,
    out: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
) -> ivy.Array:
    """Computes the bitwise XOR of the underlying binary representation of each element
    ``x1_i`` of the input array ``x1`` with the respective element ``x2_i`` of the
    input
    array ``x2``.

    **Special cases**

    This function does not take floating point operands

    Parameters
    ----------
    x1
        first input array. Should have an integer or boolean data type.
    x2
        second input array. Must be compatible with ``x1`` (see :ref:`broadcasting`).
        Should have an integer or boolean data type.
    out
        optional output array, for writing the result to. It must have a shape that the
        inputs broadcast to.

    Returns
    -------
    ret
        an array containing the element-wise results. The returned array must have a
        data type determined by :ref:`type-promotion`.

    This function conforms to the `Array API Standard
    <https://data-apis.org/array-api/latest/>`_. This docstring is an extension of the
    `docstring <https://data-apis.org/array-api/latest/API_specification/generated/signatures.elementwise_functions.bitwise_xor.html>`_ # noqa
    in the standard. The descriptions above assume an array input for simplicity, but
    the method also accepts :code:`ivy.Container` instances in place of
    :code:`ivy.Array` or :code:`ivy.NativeArray` instances, as shown in the type hints
    and also the examples below.

    Functional Examples
    -------------------

    With :code:`ivy.Array` input:

    >>> a = ivy.array([1, 2, 3])
    >>> b = ivy.array([3, 2, 1])
    >>> y = ivy.bitwise_xor(a, b)
    >>> print(y)
    ivy.array([2, 0, 2])

    >>> a = ivy.array([78, 91, 23])
    >>> b = ivy.array([66, 77, 88])
    >>> ivy.bitwise_xor(a, b, out=y)
    >>> print(y)
    ivy.array([12, 22, 79])

    >>> a = ivy.array([1, 2, 3])
    >>> b = ivy.array([3, 2, 1])
    >>> ivy.bitwise_xor(a, b, out = a)
    >>> print(a)
    ivy.array([2, 0, 2])

    With :code: `ivy.NativeArray` input:

    >>> a = ivy.native_array([0, 1, 3, 67, 91])
    >>> b = ivy.native_array([4, 7, 90, 89, 98])
    >>> y = ivy.bitwise_xor(a, b)
    >>> print(y)
    ivy.array([[ 4, 6, 89, 26, 57]])

    With a mix of :code: `ivy.Array` and :code:`ivy.NativeArray` inputs:

    >>> a = ivy.array([0, 1, 3, 67, 91])
    >>> a = ivy.native_array([4, 7, 90, 89, 98])
    >>> y = ivy.bitwise_xor(a, b)
    >>> print(y)
    ivy.array([[4, 6, 89, 26, 57]])

    With :code: `ivy.Container` input:

    >>> x = ivy.Container(a = ivy.array([89]), \
    b = ivy.array([90]))
    >>> y = ivy.container(a = ivy.array([12])), \
    b = ivy.array([78]))
    >>> z = ivy.bitwise_xor(x, y)
    >>> print(z)
    {
    a:ivy.array([20])
    b:ivy.array([85])
    }

    With a mix of :code:`ivy.Array` and :code:`ivy.Container` inputs:

    >>> x = ivy.Container(a = ivy.array([-67, 21]), \
    b = ivy.array([78, 34]))
    >>> y = ivy.array([12, 13]])
    >>> z = ivy.bitwise_xor(x, y)
    >>> print(z)
    {
    a: ivy.array([-79, 24])
    b: ivy.array([6, 74])
    }

    Instance Method Examples
    ------------------------

    Using :code: `ivy.Array` instance method:

    >>> a = ivy.array([[89, 51, 32], [14, 18, 19]])
    >>> b = ivy.array([[[19, 26, 27], [22, 23, 20]]])
    >>> y = a.bitwise_xor(b)
    >>> print(y)
    ivy.array([[74, 41, 59],
    [24, 5, 7]])

    Using :code:`ivy.Container` instance method:

    >>>x = ivy.Container(a = ivy.array([89]), \
    b = ivy.array([90]))
    >>> y = ivy.container(a = ivy.array([12])), \
    b = ivy.array([78]))
    >>>z = x.bitwise_xor(y)
    >>>print(z)
    {
    a:ivy.array([20])
    b:ivy.array([85])
    }

    Operator Examples
    -----------------

    With :code:`ivy.Array` instances:

    >>> a = ivy.array([1, 2, 3])
    >>> b = ivy.array([3, 2, 1])
    >>> y = a ^ b
    >>> print(y)
    ivy.array([2, 0, 2])

    With :code:`ivy.Container` instances:

    >>> x = ivy.Container(a = ivy.array([89]), \
    b = ivy.array([90]))
    >>> y = ivy.container(a = ivy.array([12])), \
    b = ivy.array([78]))
    >>> z = x ^ y
    >>> print(z)
    {
    a:ivy.array([20])
    b:ivy.array([85])
    }

    With mix of :code:`ivy.Array` and :code:`ivy.Container` instances:

    >>> x = ivy.Container(a = ivy.array([-67, 21]), \
    b = ivy.array([78, 34]))
    >>> y = ivy.array([12, 13]])
    >>> z = x ^ y
    >>> print(z)
    {
    a: ivy.array([-79, 24])
    b: ivy.array([6, 74])
    }
    """
    return current_backend(x1, x2).bitwise_xor(x1, x2, out=out)


@to_native_arrays_and_back
@handle_out_argument
@handle_nestable
def ceil(
    x: Union[ivy.Array, ivy.NativeArray],
    *,
    out: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
) -> ivy.Array:
    """Rounds each element ``x_i`` of the input array ``x`` to the smallest (i.e.,
    closest to ``-infinity``) integer-valued number that is not less than ``x_i``.

    **Special cases**

    - If ``x_i`` is already integer-valued, the result is ``x_i``.

    For floating-point operands,

    - If ``x_i`` is ``+infinity``, the result is ``+infinity``.
    - If ``x_i`` is ``-infinity``, the result is ``-infinity``.
    - If ``x_i`` is ``+0``, the result is ``+0``.
    - If ``x_i`` is ``-0``, the result is ``-0``.
    - If ``x_i`` is ``NaN``, the result is ``NaN``.

    Parameters
    ----------
    x
        input array. Should have a numeric data type.
    out
        optional output array, for writing the result to. It must have a shape that the
        inputs broadcast to.

    Returns
    -------
    ret
        an array containing the rounded result for each element in ``x``. The returned
        array must have the same data type as ``x``.

    This method conforms to the
    `Array API Standard <https://data-apis.org/array-api/latest/>`_.
    This docstring is an extension of the
    `docstring <https://data-apis.org/array-api/latest/API_specification/generated/signatures.elementwise_functions.ceil.html>`_  # noqa
    in the standard.
    
    Both the description and the type hints above assumes an array input for simplicity,
    but this function is *nestable*, and therefore also accepts :code:`ivy.Container`
    instances in place of any of the arguments.
    
    Examples
    --------
    With :code:`ivy.Array` input:
    
    >>> x = ivy.array([0.1, 0, -0.1])
    >>> y = ivy.ceil(x)
    >>> print(y)
    ivy.array([1., 0., -0.])
    
    >>> x = ivy.array([2.5, -3.5, 0, -3, -0])
    >>> y = ivy.ones(5)
    >>> ivy.ceil(x, out=y)
    >>> print(y)
    ivy.array([ 3., -3.,  0., -3.,  0.])
    
    >>> x = ivy.array([[3.3, 4.4, 5.5], [-6.6, -7.7, -8.8]])
    >>> ivy.ceil(x, out=x)
    >>> print(x)
    ivy.array([[ 4.,  5.,  6.],
               [-6., -7., -8.]])
    
    With :code:`ivy.NativeArray` input:
    
    >>> x = ivy.native_array([0, -0, -2.5, -1, 2, 3.5])
    >>> y = ivy.ceil(x)
    >>> print(y)
    ivy.array([ 0.,  0., -2., -1.,  2.,  4.])
    
    With :code:`ivy.Container` input:
    
    >>> x = ivy.Container(a=ivy.array([2.5, 0.5, -1.4]),\
                          b=ivy.array([5.4, -3.2, -0, 5.2]))
    >>> y = ivy.ceil(x)
    >>> print(y)
    {
        a: ivy.array([3., 1., -1.]),
        b: ivy.array([6., -3., 0., 6.])
    }
    """
    return current_backend(x).ceil(x, out=out)


@to_native_arrays_and_back
@handle_out_argument
@handle_nestable
def cos(
    x: Union[ivy.Array, ivy.NativeArray],
    *,
    out: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
) -> ivy.Array:
    """Calculates an implementation-dependent approximation to the cosine, having domain
    ``(-infinity, +infinity)`` and codomain ``[-1, +1]``, for each element ``x_i`` of
    the input array ``x``. Each element ``x_i`` is assumed to be expressed in radians.

    **Special cases**

    For floating-point operands,

    - If ``x_i`` is ``NaN``, the result is ``NaN``.
    - If ``x_i`` is ``+0``, the result is ``1``.
    - If ``x_i`` is ``-0``, the result is ``1``.
    - If ``x_i`` is ``+infinity``, the result is ``NaN``.
    - If ``x_i`` is ``-infinity``, the result is ``NaN``.

    Parameters
    ----------
    x
        input array whose elements are each expressed in radians. Should have a
        floating-point data type.
    out
        optional output array, for writing the result to. It must have a shape that the
        inputs broadcast to.

    Returns
    -------
    ret
        an array containing the cosine of each element in ``x``. The returned array must
        have a floating-point data type determined by :ref:`type-promotion`.

    Examples
    --------
    >>> x = ivy.array([0., 1., 2.])
    >>> y = ivy.cos(x)
    >>> print(y)
    ivy.array([1., 0.54, -0.416])

    """
    return current_backend(x).cos(x, out=out)


@to_native_arrays_and_back
@handle_out_argument
@handle_nestable
def cosh(
    x: Union[ivy.Array, ivy.NativeArray],
    *,
    out: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
) -> ivy.Array:
    """Calculates an implementation-dependent approximation to the hyperbolic cosine,
    having domain ``[-infinity, +infinity]`` and codomain ``[-infinity, +infinity]``,
    for each element ``x_i`` in the input array ``x``.

    **Special cases**

    For floating-point operands,

    - If ``x_i`` is ``NaN``, the result is ``NaN``.
    - If ``x_i`` is ``+0``, the result is ``1``.
    - If ``x_i`` is ``-0``, the result is ``1``.
    - If ``x_i`` is ``+infinity``, the result is ``+infinity``.
    - If ``x_i`` is ``-infinity``, the result is ``+infinity``.

    Parameters
    ----------
    x
        input array whose elements each represent a hyperbolic angle. Should have a
        floating-point data type.
    out
        optional output array, for writing the result to. It must have a shape that the
        inputs broadcast to.

    Returns
    -------
    ret
        an array containing the hyperbolic cosine of each element in ``x``. The returned
        array must have a floating-point data type determined by :ref:`type-promotion`.

    This function conforms to the `Array API Standard
    <https://data-apis.org/array-api/latest/>`_. This docstring is an extension of the
    `docstring <https://data-apis.org/array-api/latest/API_specification/generated/signatures.elementwise_functions.cosh.html>`_ # noqa
    in the standard. The descriptions above assume an array input for simplicity, but
    the method also accepts :code:`ivy.Container` instances in place of
    :code:`ivy.Array` or :code:`ivy.NativeArray` instances, as shown in the type hints
    and also the examples below.

    Functional Examples
    -------------------

    With :code:`ivy.Array` input:

    >>> x = ivy.array([1, 2, 3, 4])
    >>> y = ivy.cosh(x)
    >>> print(y)
    ivy.array([ 1.5430806,  3.7621958, 10.067662 , 27.308231 ], dtype=float32)

    >>> x = ivy.array([0.2, -1.7, -5.4, 1.1])
    >>> y = ivy.zeros(4)
    >>> ivy.cosh(x, out=y)
    ivy.array([  1.0200667,   2.8283155, 110.705475 ,   1.6685185], dtype=float32)

    >>> x = ivy.array([[1.1, 2.2, 3.3, 3.2], \
                       [-4.4, -5.5, -6.6, -7.2]])
    >>> y = ivy.cosh(x)
    >>> print(y)
    ivy.array([[  1.6685185,   4.567909 ,  13.57476  ,  12.286647 ],
               [ 40.731575 , 122.34801  , 367.54822  , 669.71564  ]],
              dtype=float32)

    With :code:`ivy.Container` input:

    >>> x = ivy.Container(a=ivy.array([1., 2., 3.]), b=ivy.array([6., 7., 8.]))
    >>> y = ivy.cosh(x)
    >>> print(y)
    {
        a: ivy.array([1.5430806, 3.7621958, 10.067662], dtype=float32),
        b: ivy.array([201.71564, 548.317, 1490.4791], dtype=float32)
    }

    Instance Method Examples
    ------------------------

    Using :code:`ivy.Array` instance method:

    >>> x = ivy.array([1., 2., 3.])
    >>> y = x.cosh()
    >>> print(y)
    ivy.array([ 1.5430806,  3.7621958, 10.067662 ], dtype=float32)

    >>> x = ivy.Container(a=ivy.array([1., 2., 3.]), b=ivy.array([6., 7., 8.]))
    >>> y = x.cosh()
    >>> print(y)
    {
        a: ivy.array([1.5430806, 3.7621958, 10.067662], dtype=float32),
        b: ivy.array([201.71564, 548.317, 1490.4791], dtype=float32)
    }
    """
    return current_backend(x).cosh(x, out=out)


@to_native_arrays_and_back
@handle_out_argument
@handle_nestable
def divide(
    x1: Union[float, ivy.Array, ivy.NativeArray],
    x2: Union[float, ivy.Array, ivy.NativeArray],
    *,
    out: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
) -> ivy.Array:
    """Calculates the division for each element x1_i of the input array x1 with the
    respective element x2_i of the input array x2.

    Parameters
    ----------
    x1
        dividend input array. Should have a numeric data type.
    x2
        divisor input array. Must be compatible with x1 (see Broadcasting). Should have
        a numeric data type.

    Returns
    -------
    ret
        an array containing the element-wise results. The returned array must have a
        floating-point data type determined by Type Promotion Rules.

    """
    return current_backend(x1, x2).divide(x1, x2, out=out)


@to_native_arrays_and_back
@handle_out_argument
@handle_nestable
def equal(
    x1: Union[float, ivy.Array, ivy.NativeArray],
    x2: Union[float, ivy.Array, ivy.NativeArray],
    *,
    out: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
) -> ivy.Array:
    """Computes the truth value of x1_i == x2_i for each element x1_i of the input array
    x1 with the respective element x2_i of the input array x2.

    Parameters
    ----------
    x1
        first input array. May have any data type.
    x2
        second input array. Must be compatible with x1 (with Broadcasting). May have any
        data type.

    Returns
    -------
    ret
        an array containing the element-wise results. The returned array must have a
        data type of bool.

    """
    return current_backend(x1, x2).equal(x1, x2, out=out)


@to_native_arrays_and_back
@handle_out_argument
@handle_nestable
def exp(
    x: Union[ivy.Array, ivy.NativeArray],
    *,
    out: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
) -> ivy.Array:
    """Calculates an implementation-dependent approximation to the exponential function,
    having domain ``[-infinity, +infinity]`` and codomain ``[+0, +infinity]``, for each
    element ``x_i`` of the input array ``x`` (``e`` raised to the power of ``x_i``,
    where ``e`` is the base of the natural logarithm).

    **Special cases**

    For floating-point operands,

    - If ``x_i`` is ``NaN``, the result is ``NaN``.
    - If ``x_i`` is ``+0``, the result is ``1``.
    - If ``x_i`` is ``-0``, the result is ``1``.
    - If ``x_i`` is ``+infinity``, the result is ``+infinity``.
    - If ``x_i`` is ``-infinity``, the result is ``+0``.

    Parameters
    ----------
    x
        input array. Should have a floating-point data type.
    out
        optional output array, for writing the result to. It must have a shape that the
        inputs broadcast to.

    Returns
    -------
    ret
        an array containing the evaluated exponential function result for each element
        in ``x``. The returned array must have a floating-point data type determined by
        :ref:`type-promotion`.

    Examples
    --------
    >>> x = ivy.array([1., 2., 3.])
    >>> y = ivy.exp(x)
    >>> print(y)
    ivy.array([2.7182817, 7.389056, 20.085537])

    """
    return current_backend(x).exp(x, out=out)


@to_native_arrays_and_back
@handle_out_argument
@handle_nestable
def expm1(
    x: Union[ivy.Array, ivy.NativeArray],
    *,
    out: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
) -> ivy.Array:
    """Calculates an implementation-dependent approximation to ``exp(x)-1``, having
    domain ``[-infinity, +infinity]`` and codomain ``[-1, +infinity]``, for each element
    ``x_i`` of the input array ``x``.

    .. note::
       The purpose of this function is to calculate ``exp(x)-1.0`` more accurately when
       ``x`` is close to zero. Accordingly, conforming implementations should avoid
       implementing this function as simply ``exp(x)-1.0``. See FDLIBM, or some other
       IEEE 754-2019 compliant mathematical library, for a potential reference
       implementation.

    **Special cases**

    For floating-point operands,

    - If ``x_i`` is ``NaN``, the result is ``NaN``.
    - If ``x_i`` is ``+0``, the result is ``+0``.
    - If ``x_i`` is ``-0``, the result is ``-0``.
    - If ``x_i`` is ``+infinity``, the result is ``+infinity``.
    - If ``x_i`` is ``-infinity``, the result is ``-1``.

    Parameters
    ----------
    x
        input array. Should have a numeric data type.
    out
        optional output array, for writing the result to. It must have a shape that the
        inputs broadcast to.

    Returns
    -------
    ret
        an array containing the evaluated result for each element in ``x``. The returned
        array must have a floating-point data type determined by :ref:`type-promotion`.

    """
    return current_backend(x).expm1(x, out=out)


@to_native_arrays_and_back
@handle_out_argument
@handle_nestable
def floor(
    x: Union[ivy.Array, ivy.NativeArray],
    *,
    out: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
) -> ivy.Array:
    """Rounds each element ``x_i`` of the input array ``x`` to the greatest (i.e.,
    closest to ``+infinity``) integer-valued number that is not greater than ``x_i``.

    **Special cases**

    - If ``x_i`` is already integer-valued, the result is ``x_i``.

    For floating-point operands,

    - If ``x_i`` is ``+infinity``, the result is ``+infinity``.
    - If ``x_i`` is ``-infinity``, the result is ``-infinity``.
    - If ``x_i`` is ``0``, the result is ``0``.
    - If ``x_i`` is ``NaN``, the result is ``NaN``.

    Parameters
    ----------
    x
        input array. Should have a numeric data type.
    out
        optional output array, for writing the result to. It must have a shape that the
        inputs broadcast to.

    Returns
    -------
    ret
        an array containing the rounded result for each element in ``x``. The returned
        array must have the same data type as ``x``.

    This method conforms to the
    `Array API Standard<https://data-apis.org/array-api/latest/>`_.
    This docstring is an extension of the
    `docstring <https://data-apis.org/array-api/latest/API_specification/
    generated/signatures.elementwise_functions.floor.html>`_ in the standard.

    Both the description and the type hints above assumes an array input for simplicity,
    but this function is *nestable*, and therefore also accepts :code:`ivy.Container`
    instances in place of any of the arguments.

    Functional Examples
    -------------------

    With :code:`ivy.Array` input:

    >>> x = ivy.array([2,3,4])
    >>> y = ivy.floor(x)
    >>> print(y)
    ivy.array([2, 3, 4])

    >>> x = ivy.array([1.5, -5.5, 0, -1, -0])
    >>> y = ivy.zeros(5)
    >>> ivy.floor(x, out=y)
    >>> print(y)
    ivy.array([ 1., -6.,  0., -1.,  0.])

    >>> x = ivy.array([[1.1, 2.2, 3.3], [-4.4, -5.5, -6.6]])
    >>> ivy.floor(x, out=x)
    >>> print(x)
    ivy.array([[ 1.,  2.,  3.],
               [-5., -6., -7.]])


    With :code:`ivy.NativeArray` input:

    >>> x = ivy.native_array([0, -0, -1.5, -1, 1, 2.5])
    >>> y = ivy.floor(x)
    >>> print(y)
    ivy.array([ 0.,  0., -2., -1.,  1.,  2.])

    With :code:`ivy.Container` input:

    >>> x = ivy.Container(a=ivy.array([0., 1.5, -2.4]),\
                          b=ivy.array([3.4, -4.2, -0, -1.2]))
    >>> y = ivy.floor(x)
    >>> print(y)
    {
        a: ivy.array([0., 1., -3.]),
        b: ivy.array([3., -5., 0., -2.])
    }

    Instance Method Examples
    ------------------------

    Using :code:`ivy.Array` instance method:

    >>> x = ivy.array([1.5, -5.5, 0.5, -0])
    >>> y = x.floor()
    >>> print(y)
    ivy.array([ 1., -6.,  0.,  0.])

    Using :code:`ivy.Container` instance method:

    >>> x = ivy.Container(a=ivy.array([0.5, 1.5, -2.4]), b=ivy.array([3.4, -4.2, 1.2]))
    >>> y = x.floor()
    >>> print(y)
    {
        a: ivy.array([0., 1., -3.]),
        b: ivy.array([3., -5., 1.])
    }
    """
    return current_backend(x).floor(x, out=out)


@to_native_arrays_and_back
@handle_out_argument
@handle_nestable
def floor_divide(
    x1: Union[float, ivy.Array, ivy.NativeArray],
    x2: Union[float, ivy.Array, ivy.NativeArray],
    *,
    out: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
) -> ivy.Array:
    """Rounds the result of dividing each element x1_i of the input array x1 by the
    respective element x2_i of the input array x2 to the greatest (i.e., closest to
    +infinity) integer-value number that is not greater than the division result.

    Parameters
    ----------
    x1
        first input array. Must have a numeric data type.
    x2
        second input array. Must be compatible with x1 (with Broadcasting). Must have a
        numeric data type.

    Returns
    -------
    ret
        an array containing the element-wise results. The returned array must have a
        numeric data type.

    """
    if isinstance(x1, float) or isinstance(x1, int):
        x1 = ivy.array(x1, dtype=x1.dtype)
    if isinstance(x2, float) or isinstance(x2, int):
        x2 = ivy.array(x2, dtype=x2.dtype)
    return current_backend(x1, x2).floor_divide(x1, x2)


@to_native_arrays_and_back
@handle_out_argument
@handle_nestable
def greater(
    x1: Union[float, ivy.Array, ivy.NativeArray],
    x2: Union[float, ivy.Array, ivy.NativeArray],
    *,
    out: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
) -> ivy.Array:
    """Computes the truth value of x1_i < x2_i for each element x1_i of the input array
    x1 with the respective element x2_i of the input array x2.

    Parameters
    ----------
    x1
        Input array.
    x2
        Input array.
    f
        Machine learning framework. Inferred from inputs if None.

    Returns
    -------
    ret
        an array containing the element-wise results. The returned array must have a
        data type of bool.

    Examples
    --------
    >>> x = ivy.greater(ivy.array([1,2,3]),ivy.array([2,2,2]))
    >>> print(x)
    ivy.array([False, False,  True])

    """
    return current_backend(x1, x2).greater(x1, x2, out=out)


@to_native_arrays_and_back
@handle_out_argument
@handle_nestable
def greater_equal(
    x1: Union[float, ivy.Array, ivy.NativeArray],
    x2: Union[float, ivy.Array, ivy.NativeArray],
    *,
    out: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
) -> ivy.Array:
    """Computes the truth value of x1_i >= x2_i for each element x1_i of the input array
    x1 with the respective element x2_i of the input array x2.

    Parameters
    ----------
    x1
        first input array. May have any data type.
    x2
        second input array. Must be compatible with x1 (with Broadcasting). May have any
        data type.

    Returns
    -------
    ret
        an array containing the element-wise results. The returned array must have a
        data type of bool.

    Functional Examples
    -------------------

    With :code:`ivy.Array` input:

    >>> x = ivy.greater_equal(ivy.array([1,2,3]),ivy.array([2,2,2]))
    >>> print(x)
    ivy.array([False, True,  True])

    >>> x = ivy.array([[10.1, 2.3, -3.6]])
    >>> y = ivy.array([[4.8], [5.2], [6.1]])
    >>> shape = (3,3)
    >>> fill_value = False
    >>> z = ivy.full(shape, fill_value)
    >>> ivy.greater_equal(x, y, out=z)
    >>> print(z)
    ivy.array([[ True, False, False],
       [ True, False, False],
       [ True, False, False]])

    >>> x = ivy.array([[[1.1], [3.2], [-6.3]]])
    >>> y = ivy.array([[8.4], [2.5], [1.6]])
    >>> ivy.greater_equal(x, y, out=x)
    >>> print(x)
    ivy.array([[[0.],[1.],[0.]]])

    With :code:`ivy.NativeArray` input:

    >>> x = ivy.native_array([1, 2])
    >>> y = ivy.native_array([4, 5])
    >>> z = ivy.greater_equal(x, y)
    >>> print(z)
    ivy.array([False, False])

    With a mix of :code:`ivy.Array` and :code:`ivy.NativeArray` inputs:

    >>> x = ivy.array([1, 2, 3])
    >>> y = ivy.native_array([4, 5, 0])
    >>> z = ivy.greater_equal(x, y)
    >>> print(z)
    ivy.array([False, False,  True])

    With a mix of :code:`ivy.Array` and :code:`ivy.Container` inputs:

    >>> x = ivy.array([[5.1, 2.3, -3.6]])
    >>> y = ivy.Container(a=ivy.array([[4.], [5.], [6.]]),\
                           b=ivy.array([[5.], [6.], [7.]]))
    >>> z = ivy.greater_equal(x, y)
    >>> print(z)
    {
        a: ivy.array([[True, False, False],
                      [True, False, False],
                      [False, False, False]]),
        b: ivy.array([[True, False, False],
                      [False, False, False],
                      [False, False, False]])
    }

    With :code:`ivy.Container` input:

    >>> x = ivy.Container(a=ivy.array([4, 5, 6]),\
                  b=ivy.array([2, 3, 4]))
    >>> y = ivy.Container(a=ivy.array([1, 2, 3]),\
                      b=ivy.array([5, 6, 7]))
    >>> z = ivy.greater_equal(x, y)
    >>> print(z)
    {
        a: ivy.array([True, True, True]),
        b: ivy.array([False, False, False])
    }

    Instance Method Examples
    ------------------------

    Using :code:`ivy.Array` instance method:

    >>> x = ivy.array([1, 2, 3])
    >>> y = ivy.array([4, 5, 6])
    >>> z = z = x.greater_equal(y)
    >>> print(z)
    ivy.array([ True, False, False])

    Using :code:`ivy.Container` instance method:

    >>> x = ivy.Container(a=ivy.array([4, 5, 6]),\
                  b=ivy.array([2, 3, 4]))
    >>> y = ivy.Container(a=ivy.array([1, 2, 3]),\
                      b=ivy.array([5, 6, 7]))
    >>> z = x.greater_equal(y)
    >>> print(z)
    {
        a: ivy.array([True, True, True]),
        b: ivy.array([False, False, False])
    }

    Operator Examples
    -----------------

    With :code:`ivy.Array` instances:

    >>> x = ivy.array([6, 2, 3])
    >>> y = ivy.array([4, 5, 6])
    >>> z = x >= y
    >>> print(z)
    ivy.array([ True, False, False])

    With :code:`ivy.Container` instances:

    >>> x = ivy.Container(a=ivy.array([4, 5, 6]),\
                  b=ivy.array([2, 3, 4]))
    >>> y = ivy.Container(a=ivy.array([1, 2, 3]),\
                      b=ivy.array([5, 6, 7]))
    >>> z = x >= y
    >>> print(z)
    {
        a: ivy.array([True, True, True]),
        b: ivy.array([False, False, False])
    }

    With mix of :code:`ivy.Array` and :code:`ivy.Container` instances:

    >>> x = ivy.array([[5.1, 2.3, -3.6]])
    >>> y = ivy.Container(a=ivy.array([[4.], [5.], [6.]]),\
                          b=ivy.array([[5.], [6.], [7.]]))
    >>> z = x >= y
    >>> print(z)
    {
        a: ivy.array([[True, False, False],
                      [True, False, False],
                      [False, False, False]]),
        b: ivy.array([[True, False, False],
                      [False, False, False],
                      [False, False, False]])
    }

    """
    return current_backend(x1, x2).greater_equal(x1, x2, out=out)


@to_native_arrays_and_back
@handle_out_argument
@handle_nestable
def isfinite(
    x: Union[ivy.Array, ivy.NativeArray],
    *,
    out: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
) -> ivy.Array:
    """Tests each element ``x_i`` of the input array ``x`` to determine if finite (i.e.,
    not ``NaN`` and not equal to positive or negative infinity).

    Parameters
    ----------
    x
        input array. Should have a numeric data type.
    out
        optional output array, for writing the result to. It must have a shape that the
        inputs broadcast to.

    Returns
    -------
    ret
        an array containing test results. An element ``out_i`` is ``True`` if ``x_i`` is
        finite and ``False`` otherwise. The returned array must have a data type of
        ``bool``.

    """
    return current_backend(x).isfinite(x, out=out)


@to_native_arrays_and_back
@handle_out_argument
@handle_nestable
def isinf(
    x: Union[ivy.Array, ivy.NativeArray],
    *,
    out: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
) -> ivy.Array:
    """Tests each element x_i of the input array x to determine if equal to positive or
    negative infinity.

    Parameters
    ----------
    x
        input array. Should have a numeric data type.
    out
        optional output array, for writing the result to. It must have a shape that the
        inputs broadcast to.

    Returns
    -------
    ret
        an array containing test results. An element out_i is True if x_i is either
        positive or negative infinity and False otherwise. The returned array must have
        a data type of bool.

    """
    return current_backend(x).isinf(x, out=out)


@to_native_arrays_and_back
@handle_out_argument
@handle_nestable
def isnan(
    x: Union[ivy.Array, ivy.NativeArray],
    *,
    out: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
) -> ivy.Array:
    """Tests each element ``x_i`` of the input array ``x`` to determine whether the
    element is ``NaN``.

    Parameters
    ----------
    x
        input array. Should have a numeric data type.
    out
        optional output array, for writing the result to. It must have a shape that the
        inputs broadcast to.

    Returns
    -------
    ret
        an array containing test results. An element ``out_i`` is ``True`` if ``x_i`` is
        ``NaN`` and ``False`` otherwise. The returned array should have a data type of
        ``bool``.

    """
    return current_backend(x).isnan(x, out=out)


@to_native_arrays_and_back
@handle_out_argument
@handle_nestable
def less(
    x1: Union[float, ivy.Array, ivy.NativeArray],
    x2: Union[float, ivy.Array, ivy.NativeArray],
    *,
    out: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
) -> ivy.Array:
    """Computes the truth value of ``x1_i < x2_i`` for each element ``x1_i`` of the
    input array ``x1`` with the respective element ``x2_i`` of the input array ``x2``.

    Parameters
    ----------
    x1
        first input array. Should have a numeric data type.
    x2
        second input array. Must be compatible with ``x1`` (see  ref:`broadcasting`).
        Should have a numeric data type.
    out
        optional output array, for writing the result to. It must have a shape that the
        inputs broadcast to.

    Returns
    -------
    ret
        an array containing the element-wise results. The returned array must have a
        data type of ``bool``.

    Examples
    --------
    >>> x = ivy.less(ivy.array([1,2,3]),ivy.array([2,2,2]))
    >>> print(x)
    ivy.array([True, False, False])

    """
    return current_backend(x1).less(x1, x2, out=out)


@to_native_arrays_and_back
@handle_out_argument
@handle_nestable
def less_equal(
    x1: Union[float, ivy.Array, ivy.NativeArray],
    x2: Union[float, ivy.Array, ivy.NativeArray],
    *,
    out: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
) -> ivy.Array:
    """Computes the truth value of x1_i <= x2_i for each element x1_i of the input array
    x1 with the respective element x2_i of the input array x2.

    Parameters
    ----------
    x1
        first input array. May have any data type.
    x2
        second input array. Must be compatible with x1 (with Broadcasting). May have any
        data type.

    Returns
    -------
     ret
        an array containing the element-wise results. The returned array must have a
        data type of bool.

    """
    return current_backend(x1, x2).less_equal(x1, x2, out=out)


@to_native_arrays_and_back
@handle_out_argument
@handle_nestable
def log(
    x: Union[ivy.Array, ivy.NativeArray],
    *,
    out: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
) -> ivy.Array:
    """Calculates an implementation-dependent approximation to the natural (base ``e``)
    logarithm, having domain ``[0, +infinity]`` and codomain ``[-infinity, +infinity]``,
    for each element ``x_i`` of the input array ``x``.

    **Special cases**

    For floating-point operands,

    - If ``x_i`` is ``NaN``, the result is ``NaN``.
    - If ``x_i`` is less than ``0``, the result is ``NaN``.
    - If ``x_i`` is either ``+0`` or ``-0``, the result is ``-infinity``.
    - If ``x_i`` is ``1``, the result is ``+0``.
    - If ``x_i`` is ``+infinity``, the result is ``+infinity``.

    Parameters
    ----------
    x
        input array. Should have a floating-point data type.
    out
        optional output array, for writing the result to. It must have a shape that the
        inputs broadcast to.

    Returns
    -------
    ret
        an array containing the evaluated natural logarithm for each element in ``x``.
        The returned array must have a floating-point data type determined by
        :ref:`type-promotion`.

    """
    return current_backend(x).log(x, out=out)


@to_native_arrays_and_back
@handle_out_argument
@handle_nestable
def log10(
    x: Union[ivy.Array, ivy.NativeArray],
    *,
    out: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
) -> ivy.Array:
    """Calculates an implementation-dependent approximation to the base ``10``
    logarithm, having domain ``[0, +infinity]`` and codomain ``[-infinity, +infinity]``,
    for each element ``x_i`` of the input array ``x``.

    **Special cases**

    For floating-point operands,

    - If ``x_i`` is ``NaN``, the result is ``NaN``.
    - If ``x_i`` is less than ``0``, the result is ``NaN``.
    - If ``x_i`` is either ``+0`` or ``-0``, the result is ``-infinity``.
    - If ``x_i`` is ``1``, the result is ``+0``.
    - If ``x_i`` is ``+infinity``, the result is ``+infinity``.

    Parameters
    ----------
    x
        input array. Should have a floating-point data type.
    out
        optional output array, for writing the result to. It must have a shape that the
        inputs broadcast to.

    Returns
    -------
    ret
        an array containing the evaluated base ``10`` logarithm for each element in
        ``x``. The returned array must have a floating-point data type determined by
        :ref:`type-promotion`.

    """
    return current_backend(x).log10(x, out=out)


@to_native_arrays_and_back
@handle_out_argument
@handle_nestable
def log1p(
    x: Union[ivy.Array, ivy.NativeArray],
    *,
    out: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
) -> ivy.Array:
    """Calculates an implementation-dependent approximation to log(1+x), where log
    refers to the natural (base e) logarithm.

    Parameters
    ----------
    x
        input array.
    out
        optional output array, for writing the result to. It must have a shape that the
        inputs broadcast to.

    Returns
    -------
    ret
        a new array containing the evaluated result for each element in x.

    """
    return current_backend(x).log1p(x, out=out)


@to_native_arrays_and_back
@handle_out_argument
@handle_nestable
def log2(
    x: Union[ivy.Array, ivy.NativeArray],
    *,
    out: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
) -> ivy.Array:
    """Calculates an implementation-dependent approximation to the base ``2`` logarithm,
    having domain ``[0, +infinity]`` and codomain ``[-infinity, +infinity]``, for each
    element ``x_i`` of the input array ``x``.

    **Special cases**

    For floating-point operands,

    - If ``x_i`` is ``NaN``, the result is ``NaN``.
    - If ``x_i`` is less than ``0``, the result is ``NaN``.
    - If ``x_i`` is either ``+0`` or ``-0``, the result is ``-infinity``.
    - If ``x_i`` is ``1``, the result is ``+0``.
    - If ``x_i`` is ``+infinity``, the result is ``+infinity``.

    Parameters
    ----------
    x
        input array. Should have a floating-point data type.
    out
        optional output array, for writing the result to. It must have a shape that the
        inputs broadcast to.

    Returns
    -------
    ret
        an array containing the evaluated base ``2`` logarithm for each element in
        ``x``. The returned array must have a floating-point data type determined by
        :ref:`type-promotion`.

    """
    return current_backend(x).log2(x, out=out)


@to_native_arrays_and_back
@handle_out_argument
@handle_nestable
def logaddexp(
    x1: Union[ivy.Array, ivy.NativeArray],
    x2: Union[ivy.Array, ivy.NativeArray],
    *,
    out: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
) -> ivy.Array:
    """Calculates the logarithm of the sum of exponentiations ``log(exp(x1) + exp(x2))``
    for each element ``x1_i`` of the input array ``x1`` with the respective element
    ``x2_i`` of the input array ``x2``.

    **Special cases**

    For floating-point operands,

    - If either ``x1_i`` or ``x2_i`` is ``NaN``, the result is ``NaN``.
    - If ``x1_i`` is ``+infinity`` and ``x2_i`` is not ``NaN``, the result is
      ``+infinity``.
    - If ``x1_i`` is not ``NaN`` and ``x2_i`` is ``+infinity``, the result is
      ``+infinity``.

    Parameters
    ----------
    x1
        first input array. Should have a floating-point data type.
    x2
        second input array. Must be compatible with ``x1`` (see :ref:`broadcasting`).
        Should have a floating-point data type.
    out
        optional output array, for writing the result to. It must have a shape that the
        inputs broadcast to.

    Returns
    -------
    ret
        an array containing the element-wise results. The returned array must have a
        floating-point data type determined by :ref:`type-promotion`.

    """
    return current_backend(x1, x2).logaddexp(x1, x2, out=out)


# ToDo: compare the examples against special case for zeros.


@to_native_arrays_and_back
@handle_out_argument
@handle_nestable
def logical_and(
    x1: ivy.Array,
    x2: ivy.Array,
    *,
    out: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
) -> ivy.Array:
    """Computes the logical AND for each element x1_i of the input array x1 with the
    respective element x2_i of the input array x2.

    Parameters
    ----------
    x1
        first input array. Should have a boolean data type.
    x2
        second input array. Must be compatible with x1.
        Should have a boolean data type.
    out
        optional output array, for writing the result to. It must have a shape that the
        inputs broadcast to.

    Returns
    -------
    ret
        an array containing the element-wise results. The returned array must have a
        data type of bool.

    """
    return current_backend(x1, x2).logical_and(x1, x2, out=out)


@to_native_arrays_and_back
@handle_out_argument
@handle_nestable
def logical_not(
    x: Union[ivy.Array, ivy.NativeArray],
    *,
    out: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
) -> ivy.Array:
    """Computes the logical NOT for each element ``x_i`` of the input array ``x``.

    .. note::
       While this specification recommends that this function only accept input arrays
       having a boolean data type, specification-compliant array libraries may choose to
       accept input arrays having numeric data types. If non-boolean data types are
       supported, zeros must be considered the equivalent of ``False``, while non-zeros
       must be considered the equivalent of ``True``.

    Parameters
    ----------
    x
        input array. Should have a boolean data type.
    out
        optional output array, for writing the result to. It must have a shape that the
        inputs broadcast to.

    Returns
    -------
    ret
        an array containing the element-wise results. The returned array must have a
        data type of ``bool``.

    """
    return current_backend(x).logical_not(x, out=out)


@to_native_arrays_and_back
@handle_out_argument
@handle_nestable
def logical_or(
    x1: Union[ivy.Array, ivy.NativeArray],
    x2: Union[ivy.Array, ivy.NativeArray],
    *,
    out: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
) -> ivy.Array:
    """Computes the logical OR for each element ``x1_i`` of the input array ``x1`` with
    the respective element ``x2_i`` of the input array ``x2``.

    .. note::
       While this specification recommends that this function only accept input arrays
       having a boolean data type, specification-compliant array libraries may choose to
       accept input arrays having numeric data types. If non-boolean data types are
       supported, zeros must be considered the equivalent of ``False``, while non-zeros
       must be considered the equivalent of ``True``.

    Parameters
    ----------
    x1
        first input array. Should have a boolean data type.
    x2
        second input array. Must be compatible with ``x1`` (see :ref:`broadcasting`).
        Should have a boolean data type.
    out
        optional output array, for writing the result to. It must have a shape that the
        inputs broadcast to.

    Returns
    -------
    ret
        an array containing the element-wise results. The returned array must have a
        data type of ``bool``.

    """
    return current_backend(x1, x2).logical_or(x1, x2, out=out)


@to_native_arrays_and_back
@handle_out_argument
@handle_nestable
def logical_xor(
    x1: Union[ivy.Array, ivy.NativeArray],
    x2: Union[ivy.Array, ivy.NativeArray],
    *,
    out: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
) -> ivy.Array:
    """Computes the bitwise XOR of the underlying binary representation of each element
    ``x1_i`` of the input array ``x1`` with the respective element ``x2_i`` of the input
    array ``x2``.

    Parameters
    ----------
    x1
        first input array. Should have an integer or boolean data type.
    x2
        second input array. Must be compatible with ``x1`` (see :ref:`broadcasting`).
        Should have an integer or boolean data type.
    out
        optional output array, for writing the result to. It must have a shape that the
        inputs broadcast to.

    Returns
    -------
    ret
        an array containing the element-wise results. The returned array must have a
        data type determined by :ref:`type-promotion`.

    """
    return current_backend(x1, x2).logical_xor(x1, x2, out=out)


@to_native_arrays_and_back
@handle_out_argument
@handle_nestable
def multiply(
    x1: Union[float, ivy.Array, ivy.NativeArray],
    x2: Union[float, ivy.Array, ivy.NativeArray],
    *,
    out: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
) -> ivy.Array:
    """Calculates the product for each element ``x1_i`` of the input array ``x1`` with
    the respective element ``x2_i`` of the input array ``x2``.

    **Special cases**

    For floating-point operands,

    - If either ``x1_i`` or ``x2_i`` is ``NaN``, the result is ``NaN``.
    - If ``x1_i`` is either ``+infinity`` or ``-infinity`` and ``x2_i`` is either ``+0``
      or ``-0``, the result is ``NaN``.
    - If ``x1_i`` is either ``+0`` or ``-0`` and ``x2_i`` is either ``+infinity`` or
      ``-infinity``, the result is ``NaN``.
    - If ``x1_i`` and ``x2_i`` have the same mathematical sign, the result has a
      positive mathematical sign, unless the result is ``NaN``. If the result is
      ``NaN``, the “sign” of ``NaN`` is implementation-defined.
    - If ``x1_i`` and ``x2_i`` have different mathematical signs, the result has a
      negative mathematical sign, unless the result is ``NaN``. If the result is
      ``NaN``, the “sign” of ``NaN`` is implementation-defined.
    - If ``x1_i`` is either ``+infinity`` or ``-infinity`` and ``x2_i`` is either
      ``+infinity`` or ``-infinity``, the result is a signed infinity with the
      mathematical sign determined by the rule already stated above.
    - If ``x1_i`` is either ``+infinity`` or ``-infinity`` and ``x2_i`` is a nonzero
      finite number, the result is a signed infinity with the mathematical sign
      determined by the rule already stated above.
    - If ``x1_i`` is a nonzero finite number and ``x2_i`` is either ``+infinity`` or
      ``-infinity``, the result is a signed infinity with the mathematical sign
      determined by the rule already stated above.

    In the remaining cases, where neither ``infinity`` nor ``NaN`` is involved, the
    product must be computed and rounded to the nearest representable value according to
    IEEE 754-2019 and a supported rounding mode. If the magnitude is too large to
    represent, the result is an ``infinity`` of appropriate mathematical sign. If the
    magnitude is too small to represent, the result is a zero of appropriate
    mathematical sign.

    .. note::
        Floating-point multiplication is not always associative due to finite precision.

    Parameters
    ----------
    x1
        first input array. Should have a numeric data type.
    x2
        second input array. Must be compatible with ``x1`` (see  ref:`Broadcasting`).
        Should have a numeric data type.
    out
        optional output array, for writing the result to. It must have a shape that the
        inputs broadcast to.

    Returns
    -------
    ret
        an array containing the element-wise products. The returned array must have a
        data type determined by :ref:`Type Promotion Rules`.

    """
    return current_backend(x1, x2).multiply(x1, x2, out=out)


@to_native_arrays_and_back
@handle_out_argument
@handle_nestable
def negative(
    x: Union[float, ivy.Array, ivy.NativeArray],
    *,
    out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """Computes the numerical negative of each element x_i (i.e., y_i = -x_i) of the
    input array x.

    Parameters
    ----------
    x
        Input array
    out
        optional output array, for writing the result to. It must have a shape that the
        inputs broadcast to.

    Returns
    -------
    ret
        an array containing the evaluated result for each element in x

    Functional Examples
    -------------------

    With :code:`ivy.Array` input:

    >>> x = ivy.array([0,1,1,2])
    >>> y = ivy.negative(x)
    >>> print(y)
    ivy.array([ 0, -1, -1, -2])

    >>> x = ivy.array([0,-1,-0.5,2,3])
    >>> y = ivy.zeros(5)
    >>> ivy.negative(x,out=y)
    >>> print(y)
    ivy.array([-0. ,  1. ,  0.5, -2. , -3. ], dtype=float32)

    >>> x = ivy.array([[1.1,2.2,3.3], \
                       [-4.4,-5.5,-6.6]])
    >>> ivy.negative(x,out=x)
    >>> print(x)
    ivy.array([[-1.1, -2.2, -3.3],
               [ 4.4,  5.5,  6.6]], dtype=float32)

    With :code:`ivy.NativeArray` input:

    >>> x = ivy.native_array([-1.1,-1,0,1,1.1])
    >>> y = ivy.negative(x)
    >>> print(y)
    ivy.array([ 1.1,  1. , -0. , -1. , -1.1], dtype=float32)

    With :code:`ivy.Container` input:

    >>> x = ivy.Container(a=ivy.array([0.,1.,2.]),\
                         b=ivy.array([3.,4.,-5.]))
    >>> y = ivy.negative(x)
    >>> print(y)
    {
        a: ivy.array([-0., -1., -2.], dtype=float32),
        b: ivy.array([-3., -4., 5.], dtype=float32)
    }

    Instance Method Examples
    -------------------

    Using :code:`ivy.Array` instance method:

    >>> x = ivy.array([-1.1,-1,0,-0,1,1.1])
    >>> y = x.negative()
    >>> print(y)
    ivy.array([ 1.1,  1. , -0. , -0. , -1. , -1.1], dtype=float32)

    Using :code:`ivy.Container` instance method:

    >>> x = ivy.Container(a=ivy.array([1,2,3]),\
                         b=ivy.array([-4.4,5,-6.6]))
    >>> y = x.negative()
    >>> print(y)
    {
        a: ivy.array([-1, -2, -3]),
        b: ivy.array([4.4, -5., 6.6], dtype=float32)
    }

    Operator Examples
    -----------------

    Using :code:`ivy.Array` instance method:

    >>> x = ivy.array([1,2,3])
    >>> y = -x
    >>> print(y)
    ivy.array([-1, -2, -3])

    Using :code:`ivy.Container` instance method:

    >>> x = ivy.Container(a=ivy.array([1,2,3]),\
                         b=ivy.array([-4.4,5,-6.6]))
    >>> y = -x
    >>> print(y)
    {
        a: ivy.array([-1, -2, -3]),
        b: ivy.array([4.4, -5., 6.6], dtype=float32)
    }

    """
    return current_backend(x).negative(x, out=out)


@to_native_arrays_and_back
@handle_out_argument
@handle_nestable
def not_equal(
    x1: Union[float, ivy.Array, ivy.NativeArray],
    x2: Union[float, ivy.Array, ivy.NativeArray],
    *,
    out: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
) -> ivy.Array:
    """Computes the truth value of ``x1_i != x2_i`` for each element ``x1_i`` of the
    input array ``x1`` with the respective element ``x2_i`` of the input array ``x2``.

    Parameters
    ----------
    x1
        first input array. Should have a numeric data type.
    x2
        second input array. Must be compatible with ``x1`` (see  ref:`broadcasting`).
        Should have a numeric data type.
    out
        optional output array, for writing the result to. It must have a shape that the
        inputs broadcast to.

    Returns
    -------
    ret
        an array containing the element-wise results. The returned array must have a
        data type of ``bool``.

    """
    return current_backend(x1, x2).not_equal(x1, x2, out=out)


@to_native_arrays_and_back
@handle_out_argument
@handle_nestable
def positive(
    x: Union[float, ivy.Array, ivy.NativeArray],
    *,
    out: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
) -> ivy.Array:
    """Returns a new array with the positive value of each element in ``x``.

    Parameters
    ----------
    x
        Input array.

    Returns
    -------
    ret
        A new array with the positive value of each element in ``x``.

    """
    return current_backend(x).positive(x, out=out)


@to_native_arrays_and_back
@handle_out_argument
@handle_nestable
def pow(
    x1: Union[float, ivy.Array, ivy.NativeArray],
    x2: Union[float, ivy.Array, ivy.NativeArray],
    *,
    out: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
) -> ivy.Array:
    """Calculates an implementation-dependent approximation of exponentiation by raising
    each element ``x1_i`` (the base) of the input array ``x1`` to the power of ``x2_i``
    (the exponent), where ``x2_i`` is the corresponding element of the input array
    ``x2``.

    .. note::
       If both ``x1`` and ``x2`` have integer data types, the result of ``pow`` when
       ``x2_i`` is negative (i.e., less than zero) is unspecified and thus
       implementation-dependent. If ``x1`` has an integer data type and ``x2`` has a
       floating-point data type, behavior is implementation-dependent (type promotion
       between data type "kinds" (integer versus floating-point) is unspecified).

    **Special cases**

    For floating-point operands,

    - If ``x1_i`` is not equal to ``1`` and ``x2_i`` is ``NaN``, the result is ``NaN``.
    - If ``x2_i`` is ``+0``, the result is ``1``, even if ``x1_i`` is ``NaN``.
    - If ``x2_i`` is ``-0``, the result is ``1``, even if ``x1_i`` is ``NaN``.
    - If ``x1_i`` is ``NaN`` and ``x2_i`` is not equal to ``0``, the result is ``NaN``.
    - If ``abs(x1_i)`` is greater than ``1`` and ``x2_i`` is ``+infinity``, the result
      is ``+infinity``.
    - If ``abs(x1_i)`` is greater than ``1`` and ``x2_i`` is ``-infinity``, the result
      is ``+0``.
    - If ``abs(x1_i)`` is ``1`` and ``x2_i`` is ``+infinity``, the result is ``1``.
    - If ``abs(x1_i)`` is ``1`` and ``x2_i`` is ``-infinity``, the result is ``1``.
    - If ``x1_i`` is ``1`` and ``x2_i`` is not ``NaN``, the result is ``1``.
    - If ``abs(x1_i)`` is less than ``1`` and ``x2_i`` is ``+infinity``, the result is
      ``+0``.
    - If ``abs(x1_i)`` is less than ``1`` and ``x2_i`` is ``-infinity``, the result is
      ``+infinity``.
    - If ``x1_i`` is ``+infinity`` and ``x2_i`` is greater than ``0``, the result is
      ``+infinity``.
    - If ``x1_i`` is ``+infinity`` and ``x2_i`` is less than ``0``, the result is
      ``+0``.
    - If ``x1_i`` is ``-infinity``, ``x2_i`` is greater than ``0``, and ``x2_i`` is an
      odd integer value, the result is ``-infinity``.
    - If ``x1_i`` is ``-infinity``, ``x2_i`` is greater than ``0``, and ``x2_i`` is not
      an odd integer value, the result is ``+infinity``.
    - If ``x1_i`` is ``-infinity``, ``x2_i`` is less than ``0``, and ``x2_i`` is an odd
      integer value, the result is ``-0``.
    - If ``x1_i`` is ``-infinity``, ``x2_i`` is less than ``0``, and ``x2_i`` is not an
      odd integer value, the result is ``+0``.
    - If ``x1_i`` is ``+0`` and ``x2_i`` is greater than ``0``, the result is ``+0``.
    - If ``x1_i`` is ``+0`` and ``x2_i`` is less than ``0``, the result is
      ``+infinity``.
    - If ``x1_i`` is ``-0``, ``x2_i`` is greater than ``0``, and ``x2_i`` is an odd
      integer value, the result is ``-0``.
    - If ``x1_i`` is ``-0``, ``x2_i`` is greater than ``0``, and ``x2_i`` is not an odd
      integer value, the result is ``+0``.
    - If ``x1_i`` is ``-0``, ``x2_i`` is less than ``0``, and ``x2_i`` is an odd integer
      value, the result is ``-infinity``.
    - If ``x1_i`` is ``-0``, ``x2_i`` is less than ``0``, and ``x2_i`` is not an odd
      integer value, the result is ``+infinity``.
    - If ``x1_i`` is less than ``0``, ``x1_i`` is a finite number, ``x2_i`` is a finite
      number, and ``x2_i`` is not an integer value, the result is ``NaN``.

    Parameters
    ----------
    x1
        first input array whose elements correspond to the exponentiation base. Should
        have a numeric data type.
    x2
        second input array whose elements correspond to the exponentiation exponent.
        Must be compatible with ``x1`` (see :ref:`broadcasting`). Should have a numeric
        data type.
    out
        optional output array, for writing the result to. It must have a shape that the
        inputs broadcast to.

    Returns
    -------
    ret
        an array containing the element-wise results. The returned array must have a
        data type determined by :ref:`type-promotion`.

    """
    return current_backend(x1, x2).pow(x1, x2, out=out)


@to_native_arrays_and_back
@handle_out_argument
@handle_nestable
def remainder(
    x1: Union[float, ivy.Array, ivy.NativeArray],
    x2: Union[float, ivy.Array, ivy.NativeArray],
    *,
    out: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
) -> ivy.Array:
    """Returns the remainder of division for each element ``x1_i`` of the input array
    ``x1`` and the respective element ``x2_i`` of the input array ``x2``.

    .. note::
        This function is equivalent to the Python modulus operator ``x1_i % x2_i``. For
        input arrays which promote to an integer data type, the result of division by
        zero is unspecified and thus implementation-defined. In general, similar to
        Python’s ``%`` operator, this function is not recommended for floating-point
        operands as semantics do not follow IEEE 754. That this function is specified
        to accept floating-point operands is primarily for reasons of backward
        compatibility.

    **Special Cases**

    For floating-point operands,

    - If either ``x1_i`` or ``x2_i`` is ``NaN``, the result is ``NaN``.
    - If ``x1_i`` is either ``+infinity`` or ``-infinity`` and ``x2_i`` is either
      ``+infinity`` or ``-infinity``, the result is ``NaN``.
    - If ``x1_i`` is either ``+0`` or ``-0`` and ``x2_i`` is either ``+0`` or ``-0``,
      the result is ``NaN``.
    - If ``x1_i`` is ``+0`` and ``x2_i`` is greater than ``0``, the result is ``+0``.
    - If ``x1_i`` is ``-0`` and ``x2_i`` is greater than ``0``, the result is ``+0``.
    - If ``x1_i`` is ``+0`` and ``x2_i`` is less than ``0``, the result is ``-0``.
    - If ``x1_i`` is ``-0`` and ``x2_i`` is less than ``0``, the result is ``-0``.
    - If ``x1_i`` is greater than ``0`` and ``x2_i`` is ``+0``, the result is ``NaN``.
    - If ``x1_i`` is greater than ``0`` and ``x2_i`` is ``-0``, the result is ``NaN``.
    - If ``x1_i`` is less than ``0`` and ``x2_i`` is ``+0``, the result is ``NaN``.
    - If ``x1_i`` is less than ``0`` and ``x2_i`` is ``-0``, the result is ``NaN``.
    - If ``x1_i`` is ``+infinity`` and ``x2_i`` is a positive (i.e., greater than ``0``)
      finite number, the result is ``NaN``.
    - If ``x1_i`` is ``+infinity`` and ``x2_i`` is a negative (i.e., less than ``0``)
      finite number, the result is ``NaN``.
    - If ``x1_i`` is ``-infinity`` and ``x2_i`` is a positive (i.e., greater than ``0``)
      finite number, the result is ``NaN``.
    - If ``x1_i`` is ``-infinity`` and ``x2_i`` is a negative (i.e., less than ``0``)
      finite number, the result is ``NaN``.
    - If ``x1_i`` is a positive (i.e., greater than ``0``) finite number and ``x2_i`` is
      ``+infinity``, the result is ``x1_i``. (note: this result matches Python
      behavior.)
    - If ``x1_i`` is a positive (i.e., greater than ``0``) finite number and ``x2_i`` is
      ``-infinity``, the result is ``x2_i``. (note: this result matches Python
      behavior.)
    - If ``x1_i`` is a negative (i.e., less than ``0``) finite number and ``x2_i`` is
      ``+infinity``, the result is ``x2_i``. (note: this results matches Python
      behavior.)
    - If ``x1_i`` is a negative (i.e., less than ``0``) finite number and ``x2_i`` is
      ``-infinity``, the result is ``x1_i``. (note: this result matches Python
      behavior.)
    - In the remaining cases, the result must match that of the Python ``%`` operator.

    Parameters
    ----------
    x1
        dividend input array. Should have a numeric data type.
    x2
        divisor input array. Must be compatible with ``x1`` (see  ref:`Broadcasting`).
        Should have a numeric data type.
    out
        optional output array, for writing the result to. It must have a shape that the
        inputs broadcast to.

    Returns
    -------
    ret
        an array containing the element-wise results. Each element-wise result must have
        the same sign as the respective element ``x2_i``. The returned array must have a
        data type determined by :ref:`Type Promotion Rules`.

    """
    return current_backend(x1, x2).remainder(x1, x2, out=out)


@to_native_arrays_and_back
@handle_out_argument
@handle_nestable
def round(
    x: Union[ivy.Array, ivy.NativeArray],
    *,
    out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """Rounds each element ``x_i`` of the input array ``x`` to the nearest
    integer-valued number.

    **Special cases**

    - If ``x_i`` is already an integer-valued, the result is ``x_i``.

    For floating-point operands,

    - If ``x_i`` is ``+infinity``, the result is ``+infinity``.
    - If ``x_i`` is ``-infinity``, the result is ``-infinity``.
    - If ``x_i`` is ``+0``, the result is ``+0``.
    - If ``x_i`` is ``-0``, the result is ``-0``.
    - If ``x_i`` is ``NaN``, the result is ``NaN``.
    - If two integers are equally close to ``x_i``, the result is
      the even integer closest to ``x_i``.

    Parameters
    ----------
    x
        input array containing elements to round.
    out
        optional output array, for writing the result to. It must have a shape that the
        inputs broadcast to.

    Returns
    -------
    ret
        An array of the same shape and type as x, with the elements rounded to integers.


    This function conforms to the `Array API Standard
    <https://data-apis.org/array-api/latest/>`_. This docstring is an extension of the
    `docstring <https://data-apis.org/array-api/latest/API_specification/generated/signatures.elementwise_functions.round.html>`_ # noqa
    in the standard. The descriptions above assume an array input for simplicity, but
    the method also accepts :code:`ivy.Container` instances in place of
    :code:`ivy.Array` or :code:`ivy.NativeArray` instances, as shown in the type hints
    and also the examples below.

    Functional Examples
    -------------------

    With :code:`ivy.Array` input:
    >>> x = ivy.array([1.2, 2.4, 3.6])
    >>> y = ivy.round(x)
    >>> print(y)
    ivy.array([1., 2., 4.], dtype=float32)

    >>> x = ivy.array([-0, 5, 4.5])
    >>> y = ivy.round(x)
    >>> print(y)
    ivy.array([0., 5., 4.], dtype=float32)

    >>> x = ivy.array([1.5654, 2.034, 15.1, -5.0])
    >>> y = ivy.zeros(4)
    >>> ivy.round(x, out=y)
    >>> print(y)
    ivy.array([ 2.,  2., 15., -5.], dtype=float32)

    >>> x = ivy.array([[0, 5.433, -343.3, 1.5], \
                      [-5.5, 44.2, 11.5, 12.01]])
    >>> ivy.round(x, out=x)
    >>> print(x)
    ivy.array([[   0.,    5., -343.,    2.],
               [  -6.,   44.,   12.,   12.]], dtype=float32)

    With :code:`ivy.NativeArray` input:
    >>> x = ivy.NativeArray([20.2, 30.5, -5.81])
    >>> y = ivy.round(x)
    >>> print(y)
    ivy.array([20., 30., -6.], dtype=float32)

    With :code:`ivy.Container` input:
    >>> x = ivy.Container(a=ivy.array([4.20, 8.6, 6.90, 0.0]),\
                  b=ivy.array([-300.9, -527.3, 4.5]))
    >>> y = ivy.round(x)
    >>> print(y)
    {
        a: ivy.array([4., 9., 7., 0.], dtype=float32),
        b: ivy.array([-301., -527., 4.], dtype=float32)
    }

    Instance Method Examples
    ------------------------

    Using :code:`ivy.Array` instance method:

    >>> x = ivy.array([5.4, 1.2, 2.3])
    >>> y = x.round()
    >>> print(y)
    ivy.array([5., 1., 2.])

    Using :code:`ivy.Container` instance method:

    >>> x = ivy.Container(a=ivy.array([0.3, 1.5, 201.5]), b=ivy.array([3.6, 4.4, -5.2]))
    >>> y = x.round()
    >>> print(y)
    {
        a: ivy.array([0., 2., 202.]),
        b: ivy.array([4., 4., -5.])
    }

    """
    return current_backend(x).round(x, out=out)


@to_native_arrays_and_back
@handle_out_argument
@handle_nestable
def sign(
    x: Union[ivy.Array, ivy.NativeArray],
    *,
    out: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
) -> ivy.Array:
    """Returns an indication of the sign of a number for each element ``x_i`` of the
    input array ``x``.

    **Special cases**

    - If ``x_i`` is less than ``0``, the result is ``-1``.
    - If ``x_i`` is either ``-0`` or ``+0``, the result is ``0``.
    - If ``x_i`` is greater than ``0``, the result is ``+1``.

    Parameters
    ----------
    x
        input array. Should have a numeric data type.
    out
        optional output array, for writing the result to. It must have a shape that the
        inputs broadcast to.

    Returns
    -------
    ret
        an array containing the evaluated result for each element in ``x``. The returned
        array must have the same data type as ``x``.

    """
    return current_backend(x).sign(x, out=out)


@to_native_arrays_and_back
@handle_out_argument
@handle_nestable
def sin(
    x: Union[ivy.Array, ivy.NativeArray],
    *,
    out: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
) -> ivy.Array:
    """Calculates an implementation-dependent approximation to the sine, having domain
    ``(-infinity, +infinity)`` and codomain ``[-1, +1]``, for each element ``x_i`` of
    the input array ``x``. Each element ``x_i`` is assumed to be expressed in radians.

    **Special cases**

    For floating-point operands,

    - If ``x_i`` is ``NaN``, the result is ``NaN``.
    - If ``x_i`` is ``+0``, the result is ``+0``.
    - If ``x_i`` is ``-0``, the result is ``-0``.
    - If ``x_i`` is either ``+infinity`` or ``-infinity``, the result is ``NaN``.

    Parameters
    ----------
    x
        input array whose elements are each expressed in radians. Should have a
        floating-point data type.
    out
        optional output array, for writing the result to. It must have a shape that the
        inputs broadcast to.

    Returns
    -------
    ret
        an array containing the sine of each element in ``x``. The returned array must
        have a floating-point data type determined by :ref:`type-promotion`.

    """
    return current_backend(x).sin(x, out=out)


@to_native_arrays_and_back
@handle_out_argument
@handle_nestable
def sinh(
    x: Union[ivy.Array, ivy.NativeArray],
    *,
    out: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
) -> ivy.Array:
    """Calculates an implementation-dependent approximation to the hyperbolic sine,
    having domain ``[-infinity, +infinity]`` and codomain ``[-infinity, +infinity]``,
    for each element ``x_i`` of the input array ``x``.

    **Special cases**

    For floating-point operands,

    - If ``x_i`` is ``NaN``, the result is ``NaN``.
    - If ``x_i`` is ``+0``, the result is ``+0``.
    - If ``x_i`` is ``-0``, the result is ``-0``.
    - If ``x_i`` is ``+infinity``, the result is ``+infinity``.
    - If ``x_i`` is ``-infinity``, the result is ``-infinity``.

    Parameters
    ----------
    x
        input array whose elements each represent a hyperbolic angle. Should have a
        floating-point data type.
    out
        optional output array, for writing the result to. It must have a shape that the
        inputs broadcast to.

    Returns
    -------
    ret
        an array containing the hyperbolic sine of each element in ``x``. The returned
        array must have a floating-point data type determined by :ref:`type-promotion`.

    """
    return current_backend(x).sinh(x, out=out)


@to_native_arrays_and_back
@handle_out_argument
@handle_nestable
def sqrt(
    x: Union[ivy.Array, ivy.NativeArray],
    *,
    out: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
) -> ivy.Array:
    """Calculates the square root, having domain ``[0, +infinity]`` and codomain
    ``[0, +infinity]``, for each element ``x_i`` of the input array ``x``. After
    rounding, each result must be indistinguishable from the infinitely precise result
    (as required by IEEE 754).

    **Special cases**

    For floating-point operands,

    - If ``x_i`` is ``NaN``, the result is ``NaN``.
    - If ``x_i`` is less than ``0``, the result is ``NaN``.
    - If ``x_i`` is ``+0``, the result is ``+0``.
    - If ``x_i`` is ``-0``, the result is ``-0``.
    - If ``x_i`` is ``+infinity``, the result is ``+infinity``.

    Parameters
    ----------
    x
        input array. Should have a floating-point data type.
    out
        optional output array, for writing the result to. It must have a shape that the
        inputs broadcast to.

    Returns
    -------
    ret
        an array containing the square root of each element in ``x``. The returned array
        must have a floating-point data type determined by :ref:`type-promotion`.

    """
    return current_backend(x).sqrt(x, out=out)


@to_native_arrays_and_back
@handle_out_argument
@handle_nestable
def square(
    x: Union[ivy.Array, ivy.NativeArray],
    *,
    out: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
) -> ivy.Array:
    """Each element ``x_i`` of the input array ``x``.

    Parameters
    ----------
    x
        Input array.

    Returns
    -------
    ret
        an array containing the evaluated result for each element in ``x``.

    """
    return current_backend(x).square(x, out=out)


@to_native_arrays_and_back
@handle_out_argument
@handle_nestable
def subtract(
    x1: Union[float, ivy.Array, ivy.NativeArray],
    x2: Union[float, ivy.Array, ivy.NativeArray],
    *,
    out: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
) -> ivy.Array:
    """Calculates the difference for each element ``x1_i`` of the input array ``x1``
    with the respective element ``x2_i`` of the input array ``x2``.

    Parameters
    ----------
    x1
        first input array. Should have a numeric data type.
    x2
        second input array. Must be compatible with ``x1`` (see  ref:`broadcasting`).
        Should have a numeric data type.
    out
        optional output array, for writing the result to. It must have a shape that the
        inputs broadcast to.

    Returns
    -------
    ret
        an array containing the element-wise differences.

    """
    return current_backend(x1).subtract(x1, x2, out=out)


@to_native_arrays_and_back
@handle_out_argument
@handle_nestable
def tan(
    x: Union[ivy.Array, ivy.NativeArray],
    *,
    out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """Calculates an implementation-dependent approximation to the tangent, having
    domain ``(-infinity, +infinity)`` and codomain ``(-infinity, +infinity)``, for each
    element ``x_i`` of the input array ``x``. Each element ``x_i`` is assumed to be
    expressed in radians.

    **Special cases**

    For floating-point operands,

    - If ``x_i`` is ``NaN``, the result is ``NaN``.
    - If ``x_i`` is ``+0``, the result is ``+0``.
    - If ``x_i`` is ``-0``, the result is ``-0``.
    - If ``x_i`` is either ``+infinity`` or ``-infinity``, the result is ``NaN``.

    Parameters
    ----------
    x
        input array whose elements are expressed in radians. Should have a
        floating-point data type.
    out
        optional output, for writing the result to. It must have a shape that the inputs
        broadcast to.

    Returns
    -------
    ret
        an array containing the tangent of each element in ``x``. The return must have a
        floating-point data type determined by :ref:`type-promotion`.


    This function conforms to the `Array API Standard
    <https://data-apis.org/array-api/latest/>`_. This docstring is an extension of the
    `docstring <https://data-apis.org/array-api/latest/API_specification/generated/signatures.elementwise_functions.tan.html>`_ # noqa
    in the standard.

    Both the description and the type hints above assumes an array input for simplicity,
    but this function is *nestable*, and therefore also accepts :code:`ivy.Container`
    instances in place of any of the arguments.

    Examples
    --------
    With :code:`ivy.Array` input:

    >>> x = ivy.array([0., 1., 2.])
    >>> y = ivy.tan(x)
    >>> print(y)
    ivy.array([0., 1.56, -2.19])

    >>> x = ivy.array([0.5, -0.7, 2.4])
    >>> y = ivy.zeros(3)
    >>> ivy.tan(x, out=y)
    >>> print(y)
    ivy.array([0.546, -0.842, -0.916])

    >>> x = ivy.array([[1.1, 2.2, 3.3],\
                        [-4.4, -5.5, -6.6]])
    >>> ivy.tan(x, out=x)
    >>> print(x)
    ivy.array([[1.96, -1.37, 0.16],
        [-3.1, 0.996, -0.328]])

    With :code:`ivy.Container` input:

    >>> x = ivy.Container(a=ivy.array([0., 1., 2.]), b=ivy.array([3., 4., 5.]))
    >>> y = ivy.tan(x)
    >>> print(y)
    {
        a: ivy.array([0., 1.56, -2.19]),
        b: ivy.array([-0.143, 1.16, -3.38])
    }
    """
    return ivy.current_backend(x).tan(x, out=out)


@to_native_arrays_and_back
@handle_out_argument
@handle_nestable
def tanh(
    x: Union[ivy.Array, ivy.NativeArray],
    *,
    out: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
) -> ivy.Array:
    """Returns a new array with the hyperbolic tangent of the elements of x.

    Parameters
    ----------
    x
        Input array.

    Returns
    -------
    ret
        A new array with the hyperbolic tangent of the elements of x.

    """
    return current_backend(x).tanh(x, out=out)


@to_native_arrays_and_back
@handle_out_argument
@handle_nestable
def trunc(
    x: Union[ivy.Array, ivy.NativeArray],
    *,
    out: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
) -> ivy.Array:
    """Rounds each element x_i of the input array x to the integer-valued number that is
    closest to but no greater than x_i.

    **Special cases**

    - If ``x_i`` is already an integer-valued, the result is ``x_i``.

    For floating-point operands,

    - If ``x_i`` is ``+infinity``, the result is ``+infinity``.
    - If ``x_i`` is ``-infinity``, the result is ``-infinity``.
    - If ``x_i`` is ``+0``, the result is ``+0``.
    - If ``x_i`` is ``-0``, the result is ``-0``.
    - If ``x_i`` is ``NaN``, the result is ``NaN``.

    Parameters
    ----------
    x
        input array. Should have a numeric data type.

    Returns
    -------
    ret
        an array containing the values before the decimal point for each element ``x``.
        The returned array must have the same data type as ``x``.

    """
    return current_backend(x).trunc(x, out=out)


# Extra #
# ------#


@to_native_arrays_and_back
@handle_out_argument
@handle_nestable
def erf(
    x: Union[ivy.Array, ivy.NativeArray],
    *,
    out: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
) -> Union[ivy.Array, ivy.NativeArray]:
    """Computes the Gauss error function of ``x`` element-wise.

    Parameters
    ----------
    x
        Value to compute exponential for.

    Returns
    -------
    ret
        The Gauss error function of x.

    """
    return current_backend(x).erf(x, out=out)


@to_native_arrays_and_back
@handle_out_argument
@handle_nestable
def maximum(
    x1: Union[ivy.Array, ivy.NativeArray, Number],
    x2: Union[ivy.Array, ivy.NativeArray, Number],
    *,
    out: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
) -> Union[ivy.Array, ivy.NativeArray]:
    """Returns the max of x1 and x2 (i.e. x1 > x2 ? x1 : x2) element-wise.

    Parameters
    ----------
    x1
        Input array containing elements to maximum threshold.
    x2
        Tensor containing maximum values, must be broadcastable to x1.

    Returns
    -------
    ret
        An array with the elements of x1, but clipped to not be lower than the x2
        values.


    Functional Examples
    -------------------

    With :code:`ivy.Array` inputs:

    >>> x = ivy.array([7, 9, 5])
    >>> y = ivy.array([9, 3, 2])
    >>> z = ivy.maximum(x, y)
    >>> print(z)
    ivy.array([9, 9, 5])

    With :code:`ivy.NativeArray` inputs:

    >>> x = ivy.native_array([1, 5, 9, 8, 3])
    >>> y = ivy.native_array([9, 3, 2, 0, 7])
    >>> ivy.maximum(x, y)
    >>> print(y)
    ivy.native_array([9, 5, 9, 8, 7])

    With :code:`Number` inputs:

    >>> z = ivy.zeros(1)
    >>> ivy.maximum(1, 5, out=z)
    >>> print(z)
    ivy.array([5])

    With a mix of :code:`ivy.Array` and :code:`ivy.NativeArray` inputs:

    >>> x = ivy.array([7, 3])
    >>> y = ivy.native_array([0, 7])
    >>> z = ivy.maximum(x, y)
    >>> print(z)
    ivy.array([7, 3])

    With a mix of :code:`ivy.Array` and :code:`Number` inputs:

    >>> x = ivy.array([1, 7, 3])
    >>> z = ivy.maximum(x, 5)
    >>> print(z)
    ivy.array([5, 7, 5])

    With a mix of :code:`ivy.NativeArray` and :code:`Number` inputs:

    >>> x = ivy.native_array([1, 3])
    >>> z = ivy.maximum(x, 5)
    >>> print(z)
    ivy.native_array([5, 5])

    Instance Method Examples
    ------------------------

    With :code:`ivy.Array` instance method using :code:`ivy.Array` input:

    >>> x = ivy.array([4, 8, 3])
    >>> y = ivy.array([9, 3, 2])
    >>> x.maximum(y, out=y)
    >>> print(y)
    ivy.array([9, 8, 3])

    With :code:`ivy.Array` instance method using :code:`ivy.NativeArray` input:

    >>> x = ivy.array([4, 1, 8, 3])
    >>> y = ivy.native_array([9, 3, 2, 6])
    >>> z = x.maximum(y)
    >>> print(z)
    ivy.array([9, 3, 8, 6])

    With :code:`ivy.Array` instance method using :code:`Number` input:

    >>> x = ivy.array([1, 7, 8])
    >>> z = ivy.zeros(3)
    >>> x.maximum(3, out=z)
    >>> print(z)
    ivy.array([3, 7, 8])

    """
    return current_backend(x1).maximum(x1, x2, out=out)


@to_native_arrays_and_back
@handle_out_argument
@handle_nestable
def minimum(
    x1: Union[ivy.Array, ivy.NativeArray],
    x2: Union[ivy.Array, ivy.NativeArray],
    *,
    out: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
) -> Union[ivy.Array, ivy.NativeArray]:
    """Returns the min of x1 and x2 (i.e. x1 < x2 ? x1 : x2) element-wise.

    Parameters
    ----------
    x1
        Input array containing elements to minimum threshold.
    x2
        Tensor containing minimum values, must be broadcastable to x1.

    Returns
    -------
    ret
        An array with the elements of x1, but clipped to not exceed the x2 values.


    Functional Examples
    -------------------

    With :code:`ivy.Array` inputs:
    >>> x = ivy.array([1, 5, 9])
    >>> y = ivy.array([2, 6, 8])
    >>> z = ivy.minimum(x, y)
    >>> print(z)
    ivy.array([1, 5, 8])

    With :code:`ivy.NativeArray` inputs:

    >>> x = ivy.native_array([2, 6, 8, 5])
    >>> y = ivy.native_array([1, 5, 9, 6])
    >>> ivy.minimum(x, y)
    >>> print(y)
    ivy.native_array([1, 5, 8, 5])

    With :code:`Number` inputs:

    >>> z = ivy.zeros(1)
    >>> ivy.minimum(1, 5, out=z)
    >>> print(z)
    ivy.array([1])

    With a mix of :code:`ivy.Array` and :code:`ivy.NativeArray` inputs:

    >>> x = ivy.array([2, 3])
    >>> y = ivy.native_array([0, 4])
    >>> z = ivy.minimum(x, y)
    >>> print(z)
    ivy.array([0, 3])

    With a mix of :code:`ivy.Array` and :code:`Number` inputs:

    >>> x = ivy.array([2, 3, 9])
    >>> z = ivy.minimum(x, 5)
    >>> print(z)
    ivy.array([2, 3, 5])

    With a mix of :code:`ivy.NativeArray` and :code:`Number` inputs:

    >>> x = ivy.native_array([2, 3, 9, 7, 3])
    >>> z = ivy.minimum(x, 5)
    >>> print(z)
    ivy.native_array([2, 3, 5, 5, 3])

    Instance Method Examples
    ------------------------

    With :code:`ivy.Array` instance method using :code:`ivy.Array` input:

    >>> x = ivy.array([4, 7, 3])
    >>> y = ivy.array([3, 3, 2])
    >>> z = x.minimum(y)
    >>> print(z)
    ivy.array([3, 3, 2])

    With :code:`ivy.Array` instance method using :code:`ivy.NativeArray` input:

    >>> x = ivy.array([4, 7])
    >>> y = ivy.native_array([6, 0])
    >>> x.minimum(y)
    >>> print(y)
    ivy.native_array([4, 0])

    With :code:`ivy.Array` instance method using :code:`Number` input:

    >>> x = ivy.array([1, 4, 8])
    >>> z = ivy.zeros(3)
    >>> x.minimum(3)
    >>> print(z)
    ivy.array([1, 4, 5])

    """
    return current_backend(x1).minimum(x1, x2, out=out)
