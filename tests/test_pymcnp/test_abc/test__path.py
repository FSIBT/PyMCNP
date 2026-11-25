import pytest

from pymcnp.abc._path import get_path, set_path


class Holder:
    def __init__(self) -> None:
        self.items: list = [{'a': 1}, [10, 20]]
        self.value = 3


class Test_path:
    def test_get(self) -> None:
        obj = Holder()
        assert get_path(obj, 'value') == 3
        assert get_path(obj, 'items[0]') == {'a': 1}
        assert get_path(obj, 'items.1.0') == 10
        assert get_path(obj, 'items[1][1]') == 20
        assert get_path(obj, 'items.-1.-1') == 20

    def test_get_missing(self) -> None:
        obj = Holder()
        with pytest.raises(AttributeError):
            get_path(obj, 'nope')
        with pytest.raises(IndexError):
            get_path(obj, 'items[9]')
        with pytest.raises(KeyError):
            get_path(obj, 'items[0].0')

    @pytest.mark.parametrize('path', ['', '_x', '__class__', 'a b', 'items.', '[0]x', '..', 'items[a]'])
    def test_get_invalid(self, path: str) -> None:
        with pytest.raises(AttributeError):
            get_path(Holder(), path)

    def test_set(self) -> None:
        obj = Holder()
        set_path(obj, 'value', 4)
        set_path(obj, 'items[1].0', 11)
        assert obj.value == 4
        assert obj.items[1][0] == 11

    def test_not_subscriptable(self) -> None:
        with pytest.raises(AttributeError):
            get_path(Holder(), 'value[0]')
        with pytest.raises(AttributeError):
            set_path(Holder(), 'value[0]', 1)
