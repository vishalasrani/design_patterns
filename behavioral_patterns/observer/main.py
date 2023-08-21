from concrete_observable import ConcreteObservable
from concrete_observer_a import ConcreteObserverA
from concrete_observer_b import ConcreteObserverB

if __name__ == "__main__":
    # The client code.

    subject = ConcreteObservable()

    observer_a = ConcreteObserverA()
    subject.attach(observer_a)

    observer_b = ConcreteObserverB()
    subject.attach(observer_b)

    subject.some_business_logic()
    subject.some_business_logic()

    subject.detach(observer_a)

    subject.some_business_logic()