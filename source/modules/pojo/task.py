import datetime

class Task:

    def __init__(self,title:str|None, description:str|None,deadline:datetime.datetime|None, priority:int|None) -> None:
        self._title = title
        self._description = description
        self._deadline = deadline
        self._priority = priority

    def __str__(self) -> str:
        return f'{self._title} - {self._description} - {self._deadline} - {self._priority}'
    
    @property
    def title(self) -> str|None:
        return self._title
    
    @title.setter
    def title(self, title:str) -> None:
        self._title = title

    @property
    def description(self) -> str|None:
        return self._description
    
    @description.setter
    def description(self, description:str) -> None:
        self._description = description

    @property
    def deadline(self) -> datetime.datetime|None:
        return self._deadline
    
    @deadline.setter
    def deadline(self, deadline:datetime.datetime) -> None:
        self._deadline = deadline

    @property
    def priority(self) -> int|None:
        return self._priority
    
    @priority.setter
    def priority(self, priority:int) -> None:
        self._priority = priority

    def to_dict(self) -> dict:
        return {
            'title': self._title,
            'description': self._description,
            'deadline': self._deadline.strftime('%Y-%m-%d %H:%M:%S') if self._deadline != None else None,
            'priority': self._priority
        }
    
    @staticmethod
    def from_dict(data:dict):
        return Task(
            title=data['title'],
            description=data['description'],
            deadline=datetime.datetime.strptime(data['deadline'], '%Y-%m-%d %H:%M:%S') if data['deadline'] != None else None,
            priority=data['priority']
        )