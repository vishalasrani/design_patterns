from observer import Observer
from observable import Observable


class ConcreteObserverA(Observer):
    def update(self, subject: Observable) -> None:
        if subject._state < 3:
            print("ConcreteObserverA: Reacted to the event")
