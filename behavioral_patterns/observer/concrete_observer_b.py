from observer import Observer
from observable import Observable


class ConcreteObserverB(Observer):
    def update(self, subject: Observable) -> None:
        if subject._state == 0 or subject._state >= 3:
            print("ConcreteObserverB: Reacted to the event")
