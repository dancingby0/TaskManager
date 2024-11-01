import os

class System:

    # 获取启动文件的目录
    @staticmethod
    def get_current_path():
        return os.path.dirname(os.path.abspath(__file__))