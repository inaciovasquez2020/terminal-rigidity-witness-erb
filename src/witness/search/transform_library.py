def identity(x):
    return x

def append_zero(x):
    return x + [0]

def rotate_left(x):
    if not x:
        return x
    return x[1:] + [x[0]]

TRANSFORMS = {
    "identity": identity,
    "append_zero": append_zero,
    "rotate_left": rotate_left,
}
