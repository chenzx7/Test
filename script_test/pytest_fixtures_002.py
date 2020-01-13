import pytest
@pytest.fixture()
def ini_xx():
    print("初始化数据")


class Test_fs():
    @pytest.mark.usefixtures("ini_xx")
    def test_001(self):
        print("test_001")

    @pytest.mark.usefixtures("ini_xx")
    def test_002(self):
        print("test_002")