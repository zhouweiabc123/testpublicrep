import base64
#编码
s = "hello world!"
encode_str = base64.encodebytes(s.encode("utf-8"))
print("编码：",encode_str.decode())
# 解码
decode_str = base64.decodebytes(encode_str)
print("解码：",decode_str.decode())