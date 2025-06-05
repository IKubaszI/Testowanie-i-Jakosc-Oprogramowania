from abc import ABC, abstractmethod

class IWorker(ABC):
    @abstractmethod
    def work(self):
        pass

class IEatable(ABC):
    @abstractmethod
    def eat(self):
        pass

class HumanWorker(IWorker, IEatable):
    def work(self):
        print("Human worker working")

    def eat(self):
        print("Human worker eating")

class RobotWorker(IWorker):
    def work(self):
        print("Robot worker working")

human = HumanWorker()
robot = RobotWorker()
human.eat()
robot.work()
