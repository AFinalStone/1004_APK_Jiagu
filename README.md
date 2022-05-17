### 1.自定义加固脚本

> main_jiagu.py

[自定义加固软件](自定义加固软件)

- 加密apk文件中的*.dex类型的文件，并为app添加壳的代理application，在软件启动的时候自动解密*.dex文件；
- 代理proxy_application的代码在HookApplication,加密*.dex文件所使用的是AES算法,可以根据代码自己定制具体的key，iv，修改壳app的包名路径

```
{
  'jiagu_apk_info': {
    'apk_file_name': 'ShellApplication.apk',
    'signature_file': '签名文件.jks',
    'signature_content': '--ks-key-alias yeyan --ks-pass pass:yeyan123 --key-pass  pass:yeyan123'
  }
}
```
main_jiagu.ini配置文件的信息介绍：

- 1.apk_file_name字段为当前要加固的apk文件名称；
- 2.signature_file为签名文件名称，signature_content为签名密码信息字段
