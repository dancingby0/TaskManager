import os
import modules.task_manager
import modules.pojo.task
import modules.system
import datetime

class Main:

    _running = False
    _task_manager = modules.task_manager.TaskManager()

    @staticmethod
    def run_choice(choice) -> None:
        if choice == '1':
            # 添加任务
            try:
                title = input('please input the title:')
                description = input('please input the description:')
                deadline: datetime.datetime|None = datetime.datetime.strptime(
                    input('please input the deadline(format: YYYY-mm-dd HH:MM:SS):'), 
                    '%Y-%m-%d %H:%M:%S')
                priority = int(input('please input the priority(from 1 to 10, 1 will be the most important and 10 will be the least important)'))
                if(priority < 1 or priority > 10):
                    raise Exception('Priority should be in the range of 1 to 10')
                if Main._task_manager.add_task(modules.pojo.task.Task(
                    title=title,
                    description=description,
                    deadline=deadline,
                    priority=priority
                )):
                    print('add successfully')
                else:
                    print('add failed')
            except Exception as e:
                print("Wrong input!")
                print(e)
            pass
        elif choice == '2':
            # 删除任务
            try:
                id = int(input('please input the id of the task you want to delete:'))
                if Main._task_manager.delete_task(id):
                    print('delete successfully')
                else:
                    print('delete failed')
            except Exception as e:
                print('Wrong input!')
                print(e)
        elif choice == '3':
            # 更新任务
            try:
                id = int(input('please input the id of the task you want to update:'))
                tmp = input('please input the title(input 0 to do not modify it):')
                title = tmp if tmp != '0' else None
                tmp = input('please input the description(input 0 to do not modify it):')
                description = tmp if tmp != '0' else None
                tmp: str = input('please input the deadline(format: YYYY-mm-dd HH:MM:SS)(input 0 to do not modify it):')
                deadline = datetime.datetime.strptime(tmp, '%Y-%m-%d %H:%M:%S') if tmp != '0' else None
                tmp = input('please input the priority(from 1 to 10, 1 will be the most important and 10 will be the least important)(input 0 to do not modify it):')
                priority = int(tmp) if tmp != '0' else None
                if(priority != None and(priority < 1 or priority > 10) ):
                    raise Exception('Priority should be in the range of 1 to 10')
                if Main._task_manager.update_task(id,
                                            modules.pojo.task.Task(
                                                title=title,
                                                description=description,
                                                deadline=deadline,
                                                priority=priority
                                            )):
                    print('update successfully')
                else:
                    print('update failed')
            except Exception as e:
                print('Wrong input!')
                print(e)

        elif choice == '4':
            # 显示任务
            match input('Please input the way you want to show the task(1. by id 2. by priority 3. by deadline):'):
                case '1':
                    Main._task_manager.show_task(1)
                case '2':
                    Main._task_manager.show_task(2)
                    pass
                case '3':
                    Main._task_manager.show_task(3)
                    pass
            pass
        elif choice == '5':
            # 保存任务
            if Main._task_manager.save_task():
                print('save successfully')
            else:
                print('save failed')

        elif choice == '6':
            # 退出
            Main._running = False
        else:
            print('Invalid choice')

    # 运行主程序
    @staticmethod
    def run() -> None:

        Main._running = True

        while Main._running:
            # 清除屏幕
            # os.system('cls' if os.name == 'nt' else 'clear')
            print("""
                  
            TaskManager
                  1. add a task
                  2. delete a task
                  3. update the task
                  4. show the task
                  5. save the task
                  6. quit

                  Please enter your choice(1-6):
                  """)
            choice = input()
            Main.run_choice(choice)


if __name__ == '__main__':

    Main.run()