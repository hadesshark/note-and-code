#!/usr/local/bin/python3.5
# -*- coding: utf-8 -*-

import unittest
from novel import *

class TsetLink(unittest.TestCase):

    # 初始化工作
    def setUp(self):
        self.tclass = request_get

    # 退出清理工作
    def tearDown(self):
        pass

    # 具体的测试用例，一定要以test开头
    def test_get_sucess(self):
        self.assertEqual(self.tclass.status_code, 200)

if __name__ == '__main__':
    # unittest.main()
    suite = (unittest.TestLoader().loadTestsFromTestCase(TsetLink))
    unittest.TextTestRunner().run(suite)
