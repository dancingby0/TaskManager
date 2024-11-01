import os
import json
import modules.system
import modules.pojo.task

class TaskManager:

    _task_file: str = os.path.join(modules.system.System.get_current_path(), 'data/task.json')
    _data_file: str = os.path.join(modules.system.System.get_current_path(), 'data/data.json')

    def __init__(self) -> None:
        # 初始化任务列表
        self.tasks = []
        self.count = 0

        # 从data文件夹中读取task.json文件
        # 读取task.json文件中的数据，将数据存储到self.tasks中

        exist_file = True

        # 如果文件夹不存在,创建
        os.makedirs(
            os.path.join(modules.system.System.get_current_path(), 'data')
            , exist_ok=True)
        # 如果文件不存在，创建
        if not os.path.exists(
            os.path.join(TaskManager._task_file)):
            with open(TaskManager._task_file, 'w') :
                exist_file = False

        if not os.path.exists(TaskManager._data_file):
            with open(TaskManager._data_file,'w'):
                exist_file = False
        if(not exist_file):
            self.save_task()

        # 读取文件
        try:
            self.load_task()
        except:
            self.save_task()
            self.load_task()

        with open(TaskManager._data_file, 'r') as f:
            data = json.load(f)
            self.count = data['count']

    # 添加任务
    def add_task(self, task) -> bool:
        self.count += 1
        self.tasks.append([self.count,task.to_dict()])
        return True

    # 删除任务
    def delete_task(self, id:int) -> bool:

        for(task_id,task) in self.tasks:
            if task_id == id:
                self.tasks.remove([task_id,task])
                return True
        return False

    # 更新任务
    def update_task(self, id, task_:modules.pojo.task.Task) -> bool:
        # 更新任务
        for(task_id,task) in self.tasks:
            if task_id == id:
                tmp = modules.pojo.task.Task.from_dict(task)
                if(task_._title != None):
                    tmp._title = task_.title
                if(task_._description != None):
                    tmp._description = task_.description
                if(task_._deadline != None):
                    tmp._deadline = task_.deadline
                if(task_._priority != None):
                    tmp._priority = task_._priority
                self.tasks.remove([task_id,task])
                self.tasks.append([task_id,tmp.to_dict()])
                return True
        return False
    
    def show_task(self, way:int) -> None:
        # 显示任务
        if way == 1:
            self.tasks.sort(key=lambda x:x[0])
        elif way == 2:
            self.tasks.sort(key=lambda x:x[1]['priority'])
        elif way == 3:
            self.tasks.sort(key=lambda x:x[1]['deadline'])
        for(task_id,task) in self.tasks:
            print(f'{task_id} - {task}')

    # 保存任务
    def save_task(self) -> bool:
        # 保存任务

        try:

            with open(TaskManager._task_file, 'w') as f:
                json.dump(self.tasks, f)
                

            with open(TaskManager._data_file, 'w') as f:
                json.dump({'count': self.count}, f)
            return True
        except:
            return False


    # 读取任务
    def load_task(self) -> None:

        with open(TaskManager._task_file, 'r') as f:
            self.tasks = json.load(f)

        with open(TaskManager._data_file, 'r') as f:
            self.count = json.load(f)['count']