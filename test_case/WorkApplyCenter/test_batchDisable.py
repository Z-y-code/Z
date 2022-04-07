#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2022-04-07 21:03:43
# @Author : 余少琪


import allure
import pytest
from config.setting import ConfigHandler
from utils.readFilesUtils.get_yaml_data_analysis import CaseData
from utils.assertUtils.assertControl import Assert
from utils.requestsUtils.requestControl import RequestControl


TestData = CaseData(ConfigHandler.data_path + r'uplpad_file_test/batchDisable.yaml').case_process()


@allure.epic("换社会")
@allure.feature("登录模块")
class TestBatchdisable:

    @allure.story("测试patch请求方式")
    @pytest.mark.parametrize('in_data', TestData, ids=[i['detail'] for i in TestData])
    def test_batchDisable(self, in_data, case_skip):
        """
        :param :
        :return:
        """

        res = RequestControl().http_request(in_data)
        Assert(in_data['assert']).assert_equality(response_data=res[0], sql_data=res[1])


if __name__ == '__main__':
    pytest.main(['test_batchDisable.py', '-s', '-W', 'ignore:Module already imported:pytest.PytestWarning'])