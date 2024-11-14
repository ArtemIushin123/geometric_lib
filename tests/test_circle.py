import pytest
from contextlib import nullcontext as does_not_raise
from Programs.circle import area, perimeter


class TestCircle:
    @pytest.mark.parametrize(
        "r, result, expectation",
        [
            (4, 50.26548245743669, does_not_raise()),
            (2.5, 19.634954084936208, does_not_raise()),
            ("0.4", None, pytest.raises(TypeError)),
            (-2, None, pytest.raises(TypeError)),
        ]
    )
    def test_area(self, r, result, expectation):
        with expectation:
            assert area(r) == pytest.approx(result, rel=1e-9)

    @pytest.mark.parametrize(
        "r, result, expectation",
        [
            (3, 18.84955592153876, does_not_raise()),
            (4.4, 27.646015351590183, does_not_raise()),
            ("0.4", None, pytest.raises(TypeError)),
            (0, None, pytest.raises(TypeError)),
        ]
    )
    def test_perimeter(self, r, result, expectation):
        with expectation:
            assert perimeter(r) == pytest.approx(result, rel=1e-9)
