import pytest


class Test_fix():

    def setup_class(self):
        print("开始测试了")

    def teardown_class(self):
        print("结束测试了")

    @pytest.mark.run(order=2)
    def test_001(self):
        assert False

    @pytest.mark.run(order=1)
    def test_002(self):
        assert False

