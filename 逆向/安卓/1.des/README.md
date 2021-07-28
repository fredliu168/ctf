使用jadx打开11.apk

发现如下：

MainActivity

```java

 public void onClick(View v) {
            switch (v.getId()) {
                case R.id.button1 /*{ENCODED_INT: 2131034174}*/:
                    MainActivity.this.pswd1 = MainActivity.this.Pswd.getText().toString();
                    try {
                        MainActivity.this.result1 = DES.encryptDES(MainActivity.this.pswd1, "poi7y6gt");
                    } catch (Exception e) {
                        e.printStackTrace();
                    }
                    if (MainActivity.this.check()) {
                        Toast.makeText(MainActivity.this, "恭喜过关", 1).show();
                        return;
                    } else {
                        Toast.makeText(MainActivity.this, "密码错误", 1).show();
                        return;
                    }
                default:
                    return;
            }
        }

```

发现用了两个函数一个是DES做加密，密码poi7y6gt

```java 
public class DES {
    private static byte[] iv = {1, 2, 3, 4, 5, 6, 7, 8};

    public static String encryptDES(String encryptString, String encryptKey) throws Exception {
        IvParameterSpec zeroIv = new IvParameterSpec(iv);
        SecretKeySpec key = new SecretKeySpec(encryptKey.getBytes(), "DES");
        Cipher cipher = Cipher.getInstance("DES/CBC/PKCS5Padding");
        cipher.init(1, key, zeroIv);
        return Base64.encode(cipher.doFinal(encryptString.getBytes()));
    }
}
```

还有一个校验check()函数，使用 b2 =  {102, 67, 119, 112, 103, 86, 72, 55, 124, 88, 93, 74, 85, 56, 37, 107, 95, 114, Byte.MAX_VALUE, 124, 65, 124, 102, 78, 76, 106, 106, 105, 40, 36, 93, 115};
和输入b3进行逐位异或是否等于当前的位置

异或运算
```
a^b = c

a = b^c
b = a^c

异或特点：相同为0，相异为1

0^0 = 0
1^1 = 0

0^1 = 1
1^0 = 1
```

```java
  private boolean check() {
        byte[] b2 = {102, 67, 119, 112, 103, 86, 72, 55, 124, 88, 93, 74, 85, 56, 37, 107, 95, 114, Byte.MAX_VALUE, 124, 65, 124, 102, 78, 76, 106, 106, 105, 40, 36, 93, 115};
        byte[] b3 = this.result1.getBytes();
        for (int j = 0; j < b3.length; j++) {
            Log.d("test", new StringBuilder().append((int) ((byte) (b3[j] ^ j))).toString());
        }
        if (b3.length != b2.length) {
            return false;
        }
        for (int j2 = 0; j2 < b2.length; j2++) {
            if ((b3[j2] ^ b2[j2]) != j2) {
                return false;
            }
        }
        return true;
    }
```

byte类型最大值和最小值-128~127

Byte.MAX_VALUE = 127

解题：
``` 
pip install pyDes
```

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Url__ = 'Http://www.purpleroc.com'
__author__ = 'Tracy_梓朋'
from pyDes import *
import base64
V0 = [102, 67, 119, 112, 103, 86, 72, 55, 124, 88, 93, 74, 85, 56, 37, 107, 95, 114, 127, 124, 65, 124, 102, 78, 76, 106, 106, 105, 40, 36, 93, 115]
def DeCheck(str):
    v1 = []
    for i in range(len(str)):
        v1.append(chr(str[i] ^ i))
    xx = "".join(v1)
    return xx

if __name__ == '__main__':
    key = 'poi7y6gt'
    iv = '\x01\x02\x03\x04\x05\x06\x07\x08'
    k = des(key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    flag = k.decrypt(base64.b64decode(DeCheck(V0)))
    print("Your flag is: " +  flag.decode())
```
Your flag is: wmiLcy4EG4TB0hVi
