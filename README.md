
### 1.马甲包打包脚本

>main_majiabao.py

支持对apk文件进行批量修改logo和app_name字段的需求。使用增量压缩签名的方案，极大的提高马甲包打包的效率。

### 2.自定义加固脚本 

>main_jiagu.py

加密apk文件中的*.dex类型的文件，并为app添加壳的代理application，在软件启动的时候自动解密*.dex文件