
### 1、解析原始apk
- 解析APK文件，获取应用包名、版本号、application

### 2、创建壳app，加密替换原始apk的数据
- 修改Hook项目，生成Proxy_Core模块中proxyApplication的class.dex代码
- 使用Proxy_Tools模块加密原始apk文件的代码并添加新的class.dex文件

### 3、解析原始apk的androidManifest.xml文件

### 4、替换原始apk的androidManifest.xml文件

