import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Programs')))
from contextlib import nullcontext as does_not_raise
from Programs.calculate import calc




class TestCalc:
    @pytest.mark.parametrize(
        "fig, funcs, size, result, expectation",
        [
            ('circle', 'area', [2], 12.566370614359172, does_not_raise()),
            ('circle', 'perimeter', [2], 12.566370614359172, does_not_raise()),
            ('square', 'area', [3], 9, does_not_raise()),
            ('square', 'perimeter', [3], 12,does_not_raise()),
            ('circle', 'area', [-2], None, pytest.raises(ValueError)),
            ('circle', 'perimeter', ["two"], None, pytest.raises(ValueError)),
            ('circle', 'perimeter', [0], None, pytest.raises(ValueError)),
            ('square', 'area', [-1], None, pytest.raises(ValueError)),
            ('square', 'perimeter', ["a"], None, pytest.raises(ValueError)),
            ('triangle', 'area', [2], None, pytest.raises(ValueError)),
            ('circle', 'volume', [2], None, pytest.raises(ValueError)),
            ('circle', 'area', [], None, pytest.raises(ValueError)),
        ]
    )
    def test_calc(self, fig, funcs, size, result, expectation):
        with expectation:
            assert calc(fig, funcs, size) == result
