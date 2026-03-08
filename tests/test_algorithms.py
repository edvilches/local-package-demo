from local_package_demo.core.algorithms import compute_mean


def test_compute_mean():

    data = [1, 2, 3, 4]

    assert compute_mean(data) == 2.5