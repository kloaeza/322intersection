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

def do_intersect(seg1, seg2):
    p1, q1 = seg1
    p2, q2 = seg2

    orientation1 = get_orientation(p1, q1, p2)
    orientation2 = get_orientation(p1, q1, q2)
    orientation3 = get_orientation(p2, q2, p1)
    orientation4 = get_orientation(p2, q2, q1)

    # General case
    if orientation1 != orientation2 and orientation3 != orientation4:
        return True

    # Special case
    
    

if __name__ == "__main__":

    _int_one = 5
    _int_two = 10

    math_result = add_positive_integers(_int_one, _int_two)
    print("Math Result:", math_result)


