import pytest

@pytest.fixture(params=[1,2,3,4])
def ini_xx(request):
    return request.param


class Test_fs():
    def test_001(self,ini_xx):
        assert ini_xx == 4
