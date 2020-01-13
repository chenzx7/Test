import pytest

@pytest.fixture(scope="class",autouse=True)
def ini_xx():
    print("初始化数据")


class Test_fs():
    def test_001(self):
        print("test_001")

    def test_002(self):
        print("test_002")
