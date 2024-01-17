r"""Implement some resolvers using features from standard libraries."""

from __future__ import annotations

import hashlib
import logging
import math
from pathlib import Path
from typing import Any
from urllib.parse import unquote, urlparse

from hya.registry import registry

logger = logging.getLogger(__name__)


@registry.register("hya.add")
def add_resolver(*args: Any) -> Any:
    r"""Return the addition of several objects.

    Args:
        *args: Specifies the values to add.

    Returns:
        ``arg1 + arg2 + arg3 + ... + argN``

    Example usage:

    ```pycon
    >>> from omegaconf import OmegaConf
    >>> conf = OmegaConf.create({"key": "${hya.add:1,2}"})
    >>> conf.key
    3
    >>> conf = OmegaConf.create({"key": "${hya.add:1,2,3,4}"})
    >>> conf.key
    10

    ```
    """
    output = args[0]
    for arg in args[1:]:
        output += arg
    return output


@registry.register("hya.asinh")
def asinh_resolver(number: float) -> float:
    r"""Return the inverse hyperbolic sine.

    Args:
        number: Specifies the number.

    Returns:
        The inverse hyperbolic sine of the input number.

    Example usage:

    ```pycon
    >>> from omegaconf import OmegaConf
    >>> conf = OmegaConf.create({"key": "${hya.asinh:1}"})
    >>> conf.key
    0.881373...

    ```
    """
    return math.asinh(number)


@registry.register("hya.ceildiv")
def ceildiv_resolver(dividend: float, divisor: float) -> int:
    r"""Return the ceiling division of two numbers.

    Args:
        dividend: The dividend.
        divisor: The divisor.

    Returns:
        int: The output of the ceiling division.

    Example usage:

    ```pycon
    >>> from omegaconf import OmegaConf
    >>> conf = OmegaConf.create({"key": "${hya.ceildiv:11,4}"})
    >>> conf.key
    3

    ```
    """
    return -(dividend // -divisor)


@registry.register("hya.exp")
def exp_resolver(number: float) -> float:
    r"""Return the exponential value of the input.

    Args:
        number: Specifies the number.

    Returns:
        The exponential value of the input.

    Example usage:

    ```pycon
    >>> from omegaconf import OmegaConf
    >>> conf = OmegaConf.create({"key": "${hya.exp:0}"})
    >>> conf.key
    1.0

    ```
    """
    return math.exp(number)


@registry.register("hya.floordiv")
def floordiv_resolver(dividend: float, divisor: float) -> int:
    r"""Return the floor division of two numbers.

    Args:
        dividend: The dividend.
        divisor: The divisor.

    Returns:
        ``dividend // divisor``

    Example usage:

    ```pycon
    >>> from omegaconf import OmegaConf
    >>> conf = OmegaConf.create({"key": "${hya.floordiv:11,4}"})
    >>> conf.key
    2

    ```
    """
    return dividend // divisor


@registry.register("hya.len")
def len_resolver(obj: Any) -> int:
    r"""Return the length of an object.

    Args:
        obj: Specifies the object.

    Returns:
        The length of the object.

    Example usage:

    ```pycon
    >>> from omegaconf import OmegaConf
    >>> conf = OmegaConf.create({"key": "${hya.len:[1,2,3]}"})
    >>> conf.key
    3

    ```
    """
    return len(obj)


@registry.register("hya.log")
def log_resolver(number: float, base: float = math.e) -> float:
    r"""Compute logarithm of the input value to the given base.

    Args:
        number: Specifies the number.
        base: Specifies the base.

    Returns:
        The logarithm of the input value to the given base.

    Example usage:

    ```pycon
    >>> from omegaconf import OmegaConf
    >>> conf = OmegaConf.create({"key": "${hya.log:1}"})
    >>> conf.key
    0.0

    ```
    """
    return math.log(number, base)


@registry.register("hya.log10")
def log10_resolver(number: float) -> float:
    r"""Compute base 10 logarithm of the input value.

    Args:
        number: Specifies the number.

    Returns:
        The base 10 logarithm of the input value.

    Example usage:

    ```pycon
    >>> from omegaconf import OmegaConf
    >>> conf = OmegaConf.create({"key": "${hya.log10:1}"})
    >>> conf.key
    0.0

    ```
    """
    return math.log10(number)


@registry.register("hya.max")
def max_resolver(*args: Any) -> Any:
    r"""Return the maximum between multiple values.

    Args:
        *args: Specifies the values.

    Returns:
        ``max(arg1, arg2, arg3, ..., argN)``

    Example usage:

    ```pycon
    >>> from omegaconf import OmegaConf
    >>> conf = OmegaConf.create({"key": "${hya.max:1,2,3}"})
    >>> conf.key
    3

    ```
    """
    return max(*args)


@registry.register("hya.min")
def min_resolver(*args: Any) -> Any:
    r"""Return the minimum between multiple values.

    Args:
        *args: Specifies the values.

    Returns:
        ``min(arg1, arg2, arg3, ..., argN)``

    Example usage:

    ```pycon
    >>> from omegaconf import OmegaConf
    >>> conf = OmegaConf.create({"key": "${hya.min:1,2,3}"})
    >>> conf.key
    1

    ```
    """
    return min(*args)


@registry.register("hya.mul")
def mul_resolver(*args: Any) -> Any:
    r"""Return the multiplication of several objects.

    Args:
        *args: Specifies the values to multiply.

    Returns:
        ``arg1 * arg2 * arg3 * ... * argN``

    Example usage:

    ```pycon
    >>> from omegaconf import OmegaConf
    >>> conf = OmegaConf.create({"key": "${hya.mul:1,2}"})
    >>> conf.key
    2
    >>> conf = OmegaConf.create({"key": "${hya.mul:1,2,3}"})
    >>> conf.key
    6

    ```
    """
    output = args[0]
    for arg in args[1:]:
        output *= arg
    return output


@registry.register("hya.neg")
def neg_resolver(number: float) -> float:
    r"""Return the negation (``-number``).

    Args:
        number: Specifies the number.

    Returns:
        The negated input number.

    Example usage:

    ```pycon
    >>> from omegaconf import OmegaConf
    >>> conf = OmegaConf.create({"key": "${hya.neg:1}"})
    >>> conf.key
    -1

    ```
    """
    return -number


@registry.register("hya.path")
def path_resolver(path: str) -> Path:
    r"""Return a path object.

    Args:
        path: Specifies the target path.

    Returns:
        The path object.

    Example usage:

    ```pycon
    >>> from omegaconf import OmegaConf
    >>> conf = OmegaConf.create({"key": "${hya.path:/my/path}"})
    >>> conf.key
    PosixPath('/my/path')

    ```
    """
    return Path(path).expanduser().resolve()


@registry.register("hya.pi")
def pi_resolver() -> float:
    r"""Return the value PI.

    Returns:
        The value of PI.

    Example usage:

    ```pycon
    >>> from omegaconf import OmegaConf
    >>> conf = OmegaConf.create({"key": "${hya.pi:}"})
    >>> conf.key
    3.14159...

    ```
    """
    return math.pi


@registry.register("hya.pow")
def pow_resolver(value: float, exponent: float) -> float:
    r"""Return a value to a given power.

    Args:
        value: The value or base.
        exponent: The exponent.

    Returns:
        ``x ** y``

    Example usage:

    ```pycon
    >>> from omegaconf import OmegaConf
    >>> conf = OmegaConf.create({"key": "${hya.pow:2,3}"})
    >>> conf.key
    8

    ```
    """
    return value**exponent


@registry.register("hya.sqrt")
def sqrt_resolver(number: float) -> float:
    r"""Return the square root of a number.

    Args:
        number: Specifies the number to compute the
            square root.

    Returns:
        The square root of the input number.

    Example usage:

    ```pycon
    >>> from omegaconf import OmegaConf
    >>> conf = OmegaConf.create({"key": "${hya.sqrt:4}"})
    >>> conf.key
    2.0

    ```
    """
    return math.sqrt(number)


@registry.register("hya.sha256")
def sha256_resolver(obj: Any) -> str:
    r"""Return the SHA-256 hash of the input object.

    Args:
        obj: Specifies the object to compute the SHA-256 hash.

    Returns:
        The SHA-256 hash of the object.

    Example usage:

    ```pycon
    >>> from omegaconf import OmegaConf
    >>> conf = OmegaConf.create({"key": "${hya.sha1:mystring}"})
    >>> conf.key
    9ce3ea4d6fac2165933b3971e6d5a13753c7d878

    ```
    """
    return hashlib.sha256(bytes(str(obj), "utf-8")).hexdigest()


@registry.register("hya.sinh")
def sinh_resolver(number: float) -> float:
    r"""Return the hyperbolic sine.

    Args:
        number: Specifies the number.

    Returns:
        The hyperbolic sine of the input number.

    Example usage:

    ```pycon
    >>> from omegaconf import OmegaConf
    >>> conf = OmegaConf.create({"key": "${hya.sinh:1}"})
    >>> conf.key
    1.175201...

    ```
    """
    return math.sinh(number)


@registry.register("hya.sub")
def sub_resolver(object1: Any, object2: Any) -> Any:
    r"""Return the subtraction of two objects.

    Args:
        object1: The first object.
        object2: The second object.

    Returns:
        ``object1 - object2``

    Example usage:

    ```pycon
    >>> from omegaconf import OmegaConf
    >>> conf = OmegaConf.create({"key": "${hya.sub:3,1}"})
    >>> conf.key
    2

    ```
    """
    return object1 - object2


@registry.register("hya.to_path")
def to_path_resolver(path: str) -> Path:
    r"""Return the input path into a ``pathlib.Path``.

    Args:
        path: Specifies the path to convert. This value should be
            compatible with ``pathlib.Path``.

    Returns:
        The converted path.

    Example usage:

    ```pycon
    >>> from omegaconf import OmegaConf
    >>> conf = OmegaConf.create({"key": "${hya.to_path:/my/path}"})
    >>> conf.key
    PosixPath('/my/path')

    ```
    """
    return Path(unquote(urlparse(path).path)).expanduser().resolve()


@registry.register("hya.truediv")
def truediv_resolver(dividend: float, divisor: float) -> float:
    r"""Return the true division of two numbers.

    Args:
        dividend: The dividend.
        divisor: The divisor.

    Returns:
        ``dividend / divisor``

    Example usage:

    ```pycon
    >>> from omegaconf import OmegaConf
    >>> conf = OmegaConf.create({"key": "${hya.truediv:1,2}"})
    >>> conf.key
    0.5

    ```
    """
    return dividend / divisor
