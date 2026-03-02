def add_positive_integers(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Inputs must be integers")
    if a < 0 or b < 0:
        raise ValueError("Inputs must be positive")
    return a + b

def orientation(p, q, r):
    val  = (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])

    if val == 0:
        return 0
    
    if val > 0:
        return 2
    else:
        return 1
