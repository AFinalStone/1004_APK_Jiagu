from python.MakeApkApplication import MakeApkApplication

if __name__ == '__main__':
    # code_dir = "michat-master"
    # gradle_task = "assembleRelease"
    # apk_code_dir = r"D:\PycharmProject\michat-master"
    # apk_gradle_task = "resguardMixinRelease"
    # MakeApkApplication.make_app_by_code(apk_code_dir, apk_gradle_task)

    aar_code_dir = r"HookApplication"
    apk_gradle_task = ":Proxy_Guard_Core:assembleRelease"
    MakeApkApplication.make_app_by_code(aar_code_dir, apk_gradle_task)

    aar_code_dir = r"HookApplication"
    apk_gradle_task = ":Proxy_Guard_Tools:build"
    MakeApkApplication.make_app_by_code(aar_code_dir, apk_gradle_task)
