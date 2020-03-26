class User:
    def __init__(self, name, surname, auto):
        self.name = name
        self.surname = surname
        self.auto = auto


def toJSON(obj):
    object = {
        "__class__": obj.__class__.__name__,
        "__module__": obj.__module__
    }
    object.update(obj.__dict__)
    return object


new_user = User(
    name="Valentin",
    surname="Samsonav",
    auto="Mercedes")
print(toJSON(new_user))
