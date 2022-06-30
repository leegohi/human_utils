log=lambda _:_
log.info=print


def rsa_encrypt(text:str,rsa_pub_key:str)->bytes:
    #rsa_pub_key = "-----BEGIN PUBLIC KEY-----\n"+"xxx"+"\n"+"-----END PUBLIC KEY-----"
    from Crypto.Cipher import PKCS1_v1_5

    from Crypto.PublicKey import RSA

    from base64 import b64encode

    rsa_key = RSA.importKey(rsa_pub_key)
    cipher = PKCS1_v1_5.new(rsa_key)
    enc_text = cipher.encrypt(text.encode("utf-8"))
    return b64encode(enc_text)

def sign_sha1_with_rsa(text:str,rsa_private_key:str)->bytes:
    #rsa_private_key= "-----BEGIN PRIVATE KEY-----\n"+"xxx"+"\n"+"-----END PRIVATE KEY-----"
    from Crypto.Signature import pkcs1_15
    from Crypto.PublicKey import RSA
    from Crypto.Hash import SHA1
    rsa_key = RSA.importKey(rsa_private_key)
    signer=pkcs1_15.new(rsa_key)
    sha1=SHA1.new()
    sha1.update(text.encode())
    sign=signer.sign(sha1)
    return base64.b64encode(sign)

def aes_encrypt(text:str,aes_key:str,mode:int,pad_block=16,iv:str=None)->str:
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import pad,unpad
    if mode in[AES.MODE_CBC, AES.MODE_CFB, AES.MODE_OFB,AES.MODE_OPENPGP]:
        log.info("use iv:%s",iv)
        if not iv:
            raise Exception("need iv in this mode")
        aes=AES.new(aes_key.encode("utf-8"),mode,iv.encode("utf-8"))
    else:
        aes=AES.new(aes_key.encode("utf-8"),mode)
    encode_text=text.encode("utf-8")
    content=aes.encrypt(pad(encode_text,pad_block)).hex()
    return content

def aes_decrypt(text:bytes,aes_key:str,mode:int,pad_block=16,iv:str=None)->bytes:
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import pad,unpad
    if mode in[AES.MODE_CBC, AES.MODE_CFB, AES.MODE_OFB,AES.MODE_OPENPGP]:
        if not iv:
            raise Exception("need iv in this mode")
        aes=AES.new(aes_key.encode("utf-8"),mode,iv.encode("utf-8"))
    else:
        aes=AES.new(aes_key.encode("utf-8"),mode)
    raw_content=unpad(aes.decrypt(text),pad_block)
    log.info(raw_content)
    content=raw_content
    return content
