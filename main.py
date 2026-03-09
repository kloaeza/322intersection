"""
Kevin Loaeza Luna
CSCI 332 Spring 2025
Programming Assignment #9
I acknowledge that I have worked on this assignment independently, except where
explicitly
noted and referenced. Any collaboration or use of external resources has been
properly cited.
I am fully aware of the consequences of academic dishonesty and agree to abide by
the
university's academic integrity policy. I understand the importance the
consequences of
plagiarism.
"""
def add_positive_integers(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Inputs must be integers")
    if a < 0 or b < 0:
        raise ValueError("Inputs must be positive")
    return a + b

# Helper function that determines the turn direction
def get_orientation(p, q, r):
    val  = (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])

    # If values are in a straight line/collinear, return 0
    if val == 0:
        return 0
    
    # If values make left turn/CCW/positive, return 2
    if val > 0:
        return 2
    # Else values make right turn/CW/negative, return 1
    else:
        return 1 

# Helper function used when point q falls between segment p*r
def on_segment(p, q, r):
    return (min(p[0], r[0]) <= q[0] <= max(p[0], r[0]) and min(p[1], r[1]) <= q[1] <= max(p[1], r[1]))

# Main logic function for if two line segments intersect
def do_intersect(seg1, seg2):
    p1, q1 = seg1
    p2, q2 = seg2

    # Calculates orientations
    orientation1 = get_orientation(p1, q1, p2)
    orientation2 = get_orientation(p1, q1, q2)
    orientation3 = get_orientation(p2, q2, p1)
    orientation4 = get_orientation(p2, q2, q1)

    # General case, if endpoints of seg.1 on opposite side of seg.2, must cross, return true
    if orientation1 != orientation2 and orientation3 != orientation4:
        return True

    # Special case
    #p1, q1, p2 collinear and p2 lies on p1*q1
    if orientation1 == 0 and on_segment(p1, p2, q1):
        return True
    
    # p1, q1, q2 collinear and q2 lies on p1*q1
    if orientation2 == 0 and on_segment(p1, q2, q1):
        return True

    # p2, q2, p1 collinear and p1 lies on p2*q2
    if orientation3 == 0 and on_segment(p2, p1, q2):
        return True
    
    # p2, q2, q1 collinear and q1 lies on p2*q2
    if orientation4 == 0 and on_segment(p2, q1, q2):
        return True
    
    # If none true then no intersection, return false
    return False
    
# Check if q lies on pr segment
def on_segment(p, q, r):

    return (min(p[0], r[0]) <= q[0] <= max(p[0], r[0]) and min(p[1], r[1]) <= q[1] <= max(p[1], r[1]))

# Intersection logic
def do_intersect(seg1, seg2):
    return
    

if __name__ == "__main__":
    # Add positive integers test
    _int_one = 5
    _int_two = 10
    math_result = add_positive_integers(_int_one, _int_two)
    print("Math Result:", math_result)

    # Line segments intersect
    segment_a = ((1, 1), (10, 1))
    segment_b = ((1, 2), (10, 0))
    print("\nLine Segment a: (1, 1), (10, 1)")
    print("Line Segment b: (1, 2), (10, 0)")
    print("Intersect:", do_intersect(segment_a, segment_b))

    # Line segments dont intersect
    segment_a = ((0, 5), (10, 5))
    segment_b = ((0, 0), (10, 0))
    print("\nLine Segment a: (0, 5), (10, 5)")
    print("Line Segment b: (0, 0), (10, 0)")
    print("Intersect:", do_intersect(segment_a, segment_b))

    # Line segments collinear and overlapping
    segment_a = ((0, 0), (5, 5))
    segment_b = ((2, 2), (6, 6))
    print("\nLine Segment a: (0, 0), (5, 5)")
    print("Line Segment b: (2, 2), (6, 6)")
    print("Intersect:   ", do_intersect(segment_a, segment_b))



