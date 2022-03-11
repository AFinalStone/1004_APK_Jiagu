import threading

from python.JZBApplication import JZBApplication

current_index = 0


class JZBTaskThread(threading.Thread):

    def __init__(self, threadId, apk_name, signer_file, new_apk_name_list):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.apk_name = apk_name
        self.signer_file = signer_file
        self.new_apk_name_list = new_apk_name_list
        self.apk_dir = apk_name.replace(".apk", "_" + threadId)

    def run(self):
        # threading.threadLock.
        apk_name = self.new_apk_name_list[current_index]
        JZBApplication(self.apk_name, self.signer_file, self.apk_dir).create_jizhunbao_apk(apk_name)
