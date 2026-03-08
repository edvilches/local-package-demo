from local_package_demo.utils.math_utils import normalize


def test_normalize():

    result = normalize(5, 10)

    assert result == 0.5
