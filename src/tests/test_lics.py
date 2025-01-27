import pytest
import src.compute_lics as lics

@pytest.mark.parametrize("NUMPOINTS, POINTS, E_PTS, F_PTS, AREA1, expected_result", [
    # (2, 3), (5, 3), (5, 7) gives a triangle of area 6
    # First triplet gives the answer
    (5, [[2, 3], [8, 5], [5, 3], [5, 5], [5, 7]], 1, 1, 5, True),
    # (2, 3), (5, 3), (5, 7) gives a triangle of area 6
    # E_PTS and F_PTS are different and greater than 1
    (11, [[2, 3], [8, 5], [8, 5], [8, 5], [5, 3], [5, 5], [5, 5], [5, 5], [5, 5], [5, 5], [5, 7]], 3, 5, 5, True),
    # No triplet exists
    (5, [[2, 1], [8, 5], [3, 3], [2, 5], [5, 7]], 1, 1, 5, False),
    # (2, 3), (5, 3), (5, 7) gives a triangle of area 6 
    # Check that equality does not give us true
    (5, [[2, 3], [8, 5], [5, 3], [5, 5], [5, 7]], 1, 1, 6, False),
    # (2, 3), (5, 3), (5, 7) gives a triangle of area 6 
    # Triplets exist but not at the correct spacing
    (5, [[2, 3], [8, 5], [5, 3], [5, 5], [5, 7]], 2, 1, 5, False),
    # NUMPOINTS < 5 is automatic fail
    (3, [[2, 3], [5, 3], [5, 7]], 1, 1, 5, False),
])

def test_lic_10(NUMPOINTS, POINTS, E_PTS, F_PTS, AREA1, expected_result):
    assert lics.lic_10(NUMPOINTS, POINTS, E_PTS, F_PTS, AREA1) == expected_result
    
@pytest.mark.parametrize("NUMPOINTS, POINTS, G_PTS, expected_result", [
    # (5, 3) and (1, 10) is a valid pair
    # First pair gives the right answer
    (3, [[5, 3], [99, 99], [1, 10]], 1, True),
    # (5, 3) and (1, 10) is a valid pair
    # Last pair gives the right answer
    (5, [[99, 99], [99, 99], [5, 3], [99, 99], [1, 10]], 1, True),
    # No such pair exists
    (5, [[99, 99], [99, 99], [99, 99], [99, 99], [100, 100]], 3, False),
    # (101, 100) and (100, 120) is a valid pair
    # G_PTS is greater than 1
    (6, [[101, 100], [99, 99], [99, 99], [99, 99], [99, 99], [100, 120]], 4, True),
    # NUMPOINTS < 3
    (2, [[5, 4], [3, 8]], 1, False),
])

def test_lic_11(NUMPOINTS, POINTS, G_PTS, expected_result):
    assert lics.lic_11(NUMPOINTS, POINTS, G_PTS) == expected_result

@pytest.mark.parametrize("NUMPOINTS, POINTS, K_PTS, LENGTH1, LENGTH2, expected_result", [
    # First condition satisfied with (8, 2) and (14, 2) >= 5 (LENGTH1)
    # Second condition satisfied with (6, 2) and (8, 2) <= 3 (LENGTH2)
    (5, [[6, 2], [7, 2], [8, 2], [11, 2], [14, 2]], 1, 5, 3, True),
    # Both conditions satisfied with (8, 2) and (14, 2) >= 5 (LENGTH1), <= 7 (LENGTH2)
    (5, [[8, 2], [8, 2], [8, 2], [11, 2], [14, 2]], 1, 5, 7, True),
    # First condition satisfied with (8, 2) and (14, 2) >= 5 (LENGTH1)
    # Second condition satisfied with (6, 2) and (8, 2) <= 3 (LENGTH2)
    # K_PTS > 1
    (11, [[6, 2], [7, 2], [7, 2], [7, 2], [7, 2], [8, 2], [11, 2], [11, 2], [11, 2], [11, 2], [14, 2]], 4, 5, 3, True),
    # No conditions satisfied
    (5, [[6, 2], [7, 2], [8, 2], [11, 2], [14, 2]], 1, 100, 1, False),
    # Only one condition satisfied
    (5, [[6, 2], [7, 2], [8, 2], [11, 2], [14, 2]], 1, 5, 1, False),
    # First condition satisfied with (8, 2) and (14, 2) >= 5 (LENGTH1)
    # Second condition satisfied with (6, 2) and (8, 2) <= 3 (LENGTH2)
    # However, fail due to K_PTS = 2, not allowing it
    (5, [[6, 2], [7, 2], [8, 2], [11, 2], [14, 2]], 2, 5, 3, False),
    # NUMPOINTS < 3 which automatically fails
    (2, [[6, 2], [14, 2]], 1, 1, 1, False),
])

def test_lic_12(NUMPOINTS, POINTS, K_PTS, LENGTH1, LENGTH2, expected_result):
    assert lics.lic_12(NUMPOINTS, POINTS, K_PTS, LENGTH1, LENGTH2) == expected_result
    

@pytest.mark.parametrize("NUMPOINTS, POINTS, A_PTS, B_PTS, RADIUS1, RADIUS2, expected_result", [
    # First condition satisfied with (-3, 3), (5, 5), (5, 7) since r = sqrt(21.25) > 4 (RADIUS1)
    # Second condition satisfied with (5, 5), (5, 7), (3, 5)  since r = sqrt(1.56) <= 2 (RADIUS2)
    (7, [[-3, 3], [0, 0], [5, 5], [0, 0], [5, 7],
         [0, 0], [3, 6]], 1, 1, 1, 3, True),
    # Both conditions satisfied with (3, 6), (5, 5), (5, 7) since r = sqrt(1.56) > 1 (RADIUS1) 
    # and sqrt(1.56) <= 3 (RADIUS2)
    (5, [[3, 6], [0, 0], [5, 5], [0, 0], [5, 7]], 1, 1, 1, 3, True),
    # Both conditions satisfied with a line (4, 8), (8, 8), (12, 8)
    # since r = 4 > 2 (RADIUS1) and <= 5 (RADIUS2)
    (5, [[4, 8], [0, 0], [8, 8], [0, 0], [12, 8]], 1, 1, 2, 5, True),
    # None of the conditions are satisfied
    (5, [[3, 6], [0, 0], [5, 5], [0, 0], [5, 7]], 1, 1, 100, 1, False),
    # Only one condition is satisfied with (3, 6), (5, 5), (5, 7) 
    # since r = sqrt(1.56) <= 3 (RADIUS2), but RADIUS1 = 3 > sqrt(1.56) 
    (5, [[3, 6], [0, 0], [5, 5], [0, 0], [5, 7]], 1, 1, 3, 3, False),
])

def test_lic_13(NUMPOINTS, POINTS, A_PTS, B_PTS, RADIUS1, RADIUS2, expected_result):
    assert lics.lic_13(NUMPOINTS, POINTS, A_PTS, B_PTS, RADIUS1, RADIUS2) == expected_result
    

@pytest.mark.parametrize("NUMPOINTS, POINTS, E_PTS, F_PTS, AREA1, AREA2, expected_result", [
    # First condition satisfied with (4, 9), (8, 14), (8, 9) since area = 10 > 9 (AREA1) 
    # Second condition satisfied with (11, 12), (10, 11), (11, 11) since area = sqrt(2) < 2 (AREA2)
    (10, [[4, 9], [0, 0], [8, 14], [0, 0], [8, 9],
         [11, 12], [0, 0], [10, 11], [0, 0], [11, 11]], 1, 1, 9, 2, True),
    # Both conditions satisfied with (4, 9), (8, 14), (8, 9) since area = 10 > 9 (AREA1) and < 11 (AREA2)
    (5, [[4, 9], [0, 0], [8, 14], [0, 0], [8, 9]], 1, 1, 9, 11, True),
    # Both conditions satisfied with an area of 0 from (4, 8), (8, 8), (12, 8)
    # since 0 > -1 (AREA1) and 0 < 1 (AREA2)
    (5, [[4, 8], [0, 0], [8, 8], [0, 0], [12, 8]], 1, 1, -1, 1, True),
    # Only one condition satisfied with (4, 9), (8, 14), (8, 9) since area = 10 > 9 (AREA1) but > 8 (AREA2)
    (5, [[4, 9], [0, 0], [8, 14], [0, 0], [8, 9]], 1, 1, 9, 8, False),
    # No condition satisfied
    (5, [[4, 9], [0, 0], [8, 14], [0, 0], [8, 9]], 1, 1, 100, 0, False),
])

def test_lic_14(NUMPOINTS, POINTS, E_PTS, F_PTS, AREA1, AREA2, expected_result):
    assert lics.lic_14(NUMPOINTS, POINTS, E_PTS, F_PTS, AREA1, AREA2) == expected_result
