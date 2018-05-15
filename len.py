import rsa
import base64
import hashlib
(pubkey, privkey) = rsa.newkeys(1024)

with open('public.pem', 'w+') as f:
    f.write(pubkey.save_pkcs1().decode())
with open('private.pem', 'w+') as f:
    f.write(privkey.save_pkcs1().decode())


try:
    with open('public_key.pem', 'r') as f:
        pubkey = rsa.PublicKey.load_pkcs1_openssl_pem(f.read().encode())
except Exception as e:
    print(e)
with open('private.pem', 'r') as f:
    privkey = rsa.PrivateKey.load_pkcs1(f.read().encode())

signstr = "hello"



sha256 = hashlib.sha256()
sha256.update(signstr.encode('utf-8'))
res = sha256.hexdigest()
print("256hash", res)
signature = rsa.sign(signstr.encode('utf-8'), privkey, 'SHA-256')

print("第一次签名", base64.b64encode(signature))



def sign(data):
    signature = rsa.sign(data.encode('utf-8'), privkey, 'SHA-256')
    return base64.b64encode(signature)

#key = base64.b64decode("MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC0bSURh/UGzUnr16umNhhITIg9/A/l3SSBHyKsDeBw9XGJbokA6JN8B7kZJfOWvrm/DMzsQuC/8Fxd4UBnwZ0U3lxnifcCcQrIEpUHQwJqt+F0nGJpskfk520mf/DVqdHytKWuBmN/NHt15NiL3h4v+BxKR/2rkd8rdEYNmjkqVQIDAQAB")

#signature = rsa.sign(signstr2.encode(), privkey, 'SHA-256')

print("最后一次签名：", sign(signstr))
a = sign(signstr)
def verify(data, sign):
    try:
        if rsa.verify(data.encode('utf-8'), base64.b64decode(sign), pubkey) == True:
            return "签名验证成功:" + data
    except Exception as e:
        return "签名验证失败", e, sign, data.encode(),


print("验证签名：", verify(signstr, a))

