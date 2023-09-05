#!/usr/bin/python3
"""Define a Module called matmul for handling matrix multiplication."""


from numpy import matmul


def lazy_matrix_mul(m_a, m_b):
    """This function multiply two matrices usign matmul.
    Args:
        m_a (list): First matrix.
        m_b (list): Second matrix.
    Returns:
        The multiplied matrix
    """
    return (matmul(m_a, m_b))
