def add_positive_integers(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Inputs must be integers")
    if a < 0 or b < 0:
        raise ValueError("Inputs must be positive")
    return a + b

def get_orientation(p, q, r):
    val  = (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])

    if val == 0:
        return 0
    
    if val > 0:
        return 2
    else:
        return 1 

def on_segment(p, q, r):
    return (min(p[0], r[0]) <= q[0] <= max(p[0], r[0]) and min(p[1], r[1]) <= q[1] <= max(p[1], r[1]))
    

if __name__ == "__main__":

    _int_one = 5
    _int_two = 10

    math_result = add_positive_integers(_int_one, _int_two)
    print("Math Result:", math_result)


