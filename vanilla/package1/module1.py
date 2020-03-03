class Class1:
    def __init__(self, is_reversed: bool):
        self.is_reversed = is_reversed

    def say_hello(self, name):
        if self.is_reversed:
            print("Hello {} !".format(self.__reverse_name(name)))
        else:
            print("Hello {} !".format(name))

    def __reverse_name(self, name):
        # __ prefix means it is a private method
        return name[::-1]
