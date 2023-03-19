class Singleton:
    __instance__ = None

    def __init__(self):
        if Singleton.__instance__ is None:
            Singleton.__instance__ = self
        else:
            raise Exception("This is a singleton class, so cannot create more than one instance")

    @classmethod
    def get_instance(cls):
        if cls.__instance__ is None:
            cls.__instance__ = cls()
        return cls.__instance__


if __name__ == "__main__":
    s1 = Singleton()
    print(s1)

    s2 = Singleton.get_instance()
    print(s2)

    s3 = Singleton.get_instance()
    print(s3)
    #
    s4 = Singleton.get_instance()
    print(s4)

    s5 = Singleton.get_instance()
    print(s1)
