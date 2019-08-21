#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: 罗兴红
@contact: EX-LUOXINGHONG001@pingan.com.cn
@file: get_res.py
@time: 2019/7/2 13:46
@desc:
'''
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.nlp.v20190408 import nlp_client, models
try:
    cred = credential.Credential("AKIDSnFTYV7yUsLl18apTwF3kGdptpeMeVN7", "lLjwulRwKXggYv8GCzb4SiQxJWaTEqJN")
    httpProfile = HttpProfile()
    httpProfile.endpoint = "nlp.tencentcloudapi.com"

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = nlp_client.NlpClient(cred, "ap-guangzhou", clientProfile)

    req = models.LexicalAnalysisRequest()
    params = '{"Flag":1,"Text":"平安保险真好"}'
    req.from_json_string(params)

    resp = client.LexicalAnalysis(req)
    print(resp.to_json_string())

except TencentCloudSDKException as err:
    print(err)