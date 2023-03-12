# coding: utf-8

"""
    playground

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import playground_client
from playground_client.models.run_process_response import RunProcessResponse  # noqa: E501
from playground_client.rest import ApiException

class TestRunProcessResponse(unittest.TestCase):
    """RunProcessResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RunProcessResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RunProcessResponse`
        """
        model = playground_client.models.run_process_response.RunProcessResponse()  # noqa: E501
        if include_optional :
            return RunProcessResponse(
                stderr = [
                    playground_client.models.out_stderr_response.OutStderrResponse(
                        type = 'Stderr', 
                        timestamp = 1.337, 
                        line = '', )
                    ], 
                stdout = [
                    playground_client.models.out_stdout_response.OutStdoutResponse(
                        type = 'Stdout', 
                        timestamp = 1.337, 
                        line = '', )
                    ], 
                process_id = ''
            )
        else :
            return RunProcessResponse(
                stderr = [
                    playground_client.models.out_stderr_response.OutStderrResponse(
                        type = 'Stderr', 
                        timestamp = 1.337, 
                        line = '', )
                    ],
                stdout = [
                    playground_client.models.out_stdout_response.OutStdoutResponse(
                        type = 'Stdout', 
                        timestamp = 1.337, 
                        line = '', )
                    ],
                process_id = '',
        )
        """

    def testRunProcessResponse(self):
        """Test RunProcessResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
