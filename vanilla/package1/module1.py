class Class1:
    def __init__(self, is_reversed: bool):
        self.is_reversed = is_reversed

    def say_hello(self, name: str) -> None:
        if self.is_reversed:
            print("Hello {} !".format(self.__reverse_name(name)))
        else:
            print("Hello {} !".format(name))

    def __reverse_name(self, name: str) -> str:
        # __ prefix means it is a private method
        return name[::-1]
