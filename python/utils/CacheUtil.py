from python.plugin.DictPlugin import DictPlugin
from python.plugin.FilePlugin import FilePlugin


class CacheUtil(object):

    def __init__(self, key_model):
        self.cache_file_name = "main_build_apk.ini"
        self.key_model = key_model

    # 读取缓存
    def read_value_from_cache(self, key, default=""):
        try:
            text = FilePlugin().read_str_from_file(self.cache_file_name)
            dict_cache = DictPlugin.change_str_to_dict(text)
            dict_model = dict_cache[self.key_model]
            text = dict_model[key]
        except Exception as e:
            print(e)
            text = default
        return text

    # 存储缓存
    def save_value_to_cache(self, key, value):
        text = FilePlugin().read_str_from_file(self.cache_file_name)
        dict_cache = DictPlugin.change_str_to_dict(text)
        try:
            dict_model = dict_cache[self.key_model]
        except Exception as e:
            print(e)
            dict_model = {}
        dict_model.update({key: value})
        dict_cache.update({self.key_model: dict_model})
        FilePlugin().wirte_str_to_file(str(dict_cache), self.cache_file_name)
