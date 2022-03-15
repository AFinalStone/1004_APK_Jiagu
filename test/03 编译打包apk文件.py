import os

code_dir = "apk_code_dir"
Root_SDK_Dir = "D\:\\Android_SDK"

print('\n')
print('=============================================')
print('gradle clean')
print('=============================================')
os.system('gradle clean')

print('\n')
print('=============================================')
print('gradle assembleDebug, generate apk')
print('=============================================')
os.system('gradle resguardMixinRelease')
