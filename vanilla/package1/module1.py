class Class1:
    def __init__(self, is_reversed: bool):
        self.is_reversed = is_reversed

    def say_hello(self, name: str) -> str:
        if self.is_reversed:
            return "Hello {} !".format(self.reverse_name(name))
        else:
            return "Hello {} !".format(name)

    @staticmethod  # static method when we don't need other class methods/variables
    def __valid_name(name: str) -> str:
        # __ prefix means it is a private method
        if not isinstance(name, str):
            raise TypeError('Please provide a string argument')
        else:
            return name

    def reverse_name(self, name: str) -> str:
        return self.__valid_name(name)[::-1]

    def compute_length(self, name: str) -> int:
        return len(self.__valid_name(name))

    def get_first_character(self, name: str) -> str:
        if self.is_reversed:
            return self.reverse_name(name)[0]
        else:
            return name[0]
