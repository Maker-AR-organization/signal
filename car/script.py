# coding: utf-8
import json
from huaweicloudsdkcore.auth.credentials import GlobalCredentials
from huaweicloudsdkiam.v3.region.iam_region import IamRegion
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkiam.v3 import *
import requests


# 自定义编码器将response对象转换为JSON字符串
class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, KeystoneCreateUserTokenByPasswordResponse):
            return obj.to_dict()
        return super().default(obj)


def getToken():
    # The AK and SK used for authentication are hard-coded or stored in plaintext, which has great security risks. It is recommended that the AK and SK be stored in ciphertext in configuration files or environment variables and decrypted during use to ensure security.
    # In this example, AK and SK are stored in environment variables for authentication. Before running this example, set environment variables CLOUD_SDK_AK and CLOUD_SDK_SK in the local environment
    ak = "MJI56TRASQOYAPJEFIDE"
    sk = "U0Fm1sBqFD7fSbaUjpCD19j9sXk1aOs1YD6Vig3O"

    credentials = GlobalCredentials(ak, sk) \

    client = IamClient.new_builder() \
        .with_credentials(credentials) \
        .with_region(IamRegion.value_of("cn-north-4")) \
        .build()

    try:
        request = KeystoneCreateUserTokenByPasswordRequest()
        projectScope = AuthScopeProject(
            id="22f29e6c93b4485ab7540fe2c8f8e353",
            name="cn-north-4"
        )
        scopeAuth = AuthScope(
            project=projectScope
        )
        domainUser = PwdPasswordUserDomain(
            name="darren_jiang"
        )
        userPassword = PwdPasswordUser(
            domain=domainUser,
            name="jiang",
            password="jly040624...."
        )
        passwordIdentity = PwdPassword(
            user=userPassword
        )
        listMethodsIdentity = [
            "password"
        ]
        identityAuth = PwdIdentity(
            methods=listMethodsIdentity,
            password=passwordIdentity
        )
        authbody = PwdAuth(
            identity=identityAuth,
            scope=scopeAuth
        )
        request.body = KeystoneCreateUserTokenByPasswordRequestBody(
            auth=authbody
        )
        response = client.keystone_create_user_token_by_password(request)
        # print(response)
        # 使用自定义编码器将response对象转换为JSON字符串
        response_str = json.dumps(response, cls=CustomEncoder)

        # 解析JSON数据
        json_data = json.loads(response_str)

        # # 获取"X-Subject-Token"字段的值
        x_subject_token = json_data["x_subject_token"]
        print(x_subject_token)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)

    return x_subject_token

# coding=utf-8



    # # Config url, token and file path.
    url = "https://c634a986f3644512a8d495a5bb082c07.apig.cn-north-4.huaweicloudapis.com/v1/infers/44c521be-946d-4f20-a21a-9ce99c72195b"
    token = getToken()
    file_path = "预测文件的本地路径"

    # Send request.
    headers = {
        'X-Auth-Token': token
    }
    files = {
        'images': open(file_path, 'rb')
    }
    resp = requests.post(url, headers=headers, files=files)

    # Print result.
    print(resp.status_code)
    print(resp.text)
