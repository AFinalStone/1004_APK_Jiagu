### 1.马甲包打包脚本

> main_majiabao.py

[马甲包打包脚本软件](马甲包打包软件)

该exe程序支持修改apk文件的logo和app_name。使用增量压缩V2签名的方案，提高马甲包打包的效率和安全性。

```
{
  'majiabao_apk_info': {
    'apk_file_name': 'ShellApplication.apk',
    'app_logo': 'logo.png',
    'change_axml': True,
    'signature_file': '签名文件.jks',
    'signature_content': '--ks-key-alias yeyan --ks-pass pass:yeyan123 --key-pass  pass:yeyan123',
    'config_file_name': '马甲包.txt'
  }
}
```

main_majiabao.ini配置文件的信息介绍：

- 1.apk_file_name字段为当前要打马甲包的apk文件
- 2.app_logo字段为该apk文件本身的logo图片名称，脚本会遍历res目录，找到对应名称的第一个资源文件，使用新的logo替换
- 3.change_axml字段影响修改app_name字段的方式
- 3.1为False，脚本直接修改AndroidManifest文件，然后打包，此方式app_name长度可变；
- 3.2为True的时候，脚本直接修改resource.arsc文件，然后打包，此方式app_name长度不可变；
- 4.signature_file为签名文件名称，signature_content为签名密码信息字段
- 5.config_file_name为马甲包配置信息文件名称，读取一行信息为【新的马甲包名称，新的马甲包logo】

### 2.自定义加固脚本

> main_jiagu.py

[自定义加固软件](自定义加固软件)

加密apk文件中的*.dex类型的文件，并为app添加壳的代理application，在软件启动的时候自动解密*.dex文件

```
{
  'jiagu_apk_info': {
    'apk_file_name': 'ShellApplication.apk',
    'signature_file': '签名文件.jks',
    'signature_content': '--ks-key-alias yeyan --ks-pass pass:yeyan123 --key-pass  pass:yeyan123'
  }
}
```

- 1.apk_file_name字段为当前要加固的apk文件名称；
- 2.signature_file为签名文件名称，signature_content为签名密码信息字段
