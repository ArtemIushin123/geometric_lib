import pytest
from contextlib import nullcontext as does_not_raise
from Programs.square import area, perimeter


class TestSquare:
    @pytest.mark.parametrize(
        "a, result, expectation",
        [
            (2, 4, does_not_raise()),
            (2.5, 6.25, does_not_raise()),
            ("0.4", None, pytest.raises(TypeError)),
            (-2, None, pytest.raises(TypeError)),
        ]
    )
    def test_area(self, a, result, expectation):
        with expectation:
            assert area(a) == pytest.approx(result, rel=1e-9)

    @pytest.mark.parametrize(
        "a, result, expectation",
        [
            (2, 8, does_not_raise()),
            (2.5, 10, does_not_raise()),
            ("0.4", None, pytest.raises(TypeError)),
            (0, None, pytest.raises(TypeError)),
        ]
    )
    def test_perimeter(self, a, result, expectation):
        with expectation:
            assert perimeter(a) == pytest.approx(result, rel=1e-9)
