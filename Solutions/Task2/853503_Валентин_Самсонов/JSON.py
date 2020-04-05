class Car:
    def __init__(self, mark,number):
        self.mark = mark
        self.number = number

my_car = Car(mark = "Mercedes", number = 4356)


class JsonFormat:
    def JsonConvert(self, obj):
        if isinstance(obj, (list, tuple)):
            return self.ListConvert(obj)
        elif isinstance(obj, dict):
            return self.DictConvert(obj)
        else:
            return self.DictConvert(self.ClassConvert(obj))

    def NormalTypeConvert(self, obj):
        if isinstance(obj, (int, float)):
            return '{}'.format(obj)
        elif type(obj) == str:
            return "'{}'".format(obj)
        elif isinstance(type(obj), bool):
            if obj:
                return 'True'
            return 'False'
        elif type(obj) == type(None):
            return 'None'

    def ListConvert(self, obj):
        temp = []
        for i in obj:
            if isinstance(i, (int, float, str, bool, type(None))):
                temp.append(self.NormalTypeConvert(i))
            elif isinstance(i, dict):
                temp.append(self.DictConvert(i))
            elif isinstance(i, (list, tuple)):
                temp.append(self.ListConvert(i))
            else:
                temp.append(self.DictConvert(self.ClassConvert(i)))
        end_str = ', '.join(temp)
        return '[ ' + end_str + ' ]'

    def DictConvert(self, obj):
        temp = []
        for key, value in obj.items():
            if isinstance(value, (int, float, str, bool, type(None))):
                temp.append(self.DictFormat(key, self.NormalTypeConvert(value)))
            elif isinstance(value, dict):
                temp.append(self.DictFormat(key, self.DictConvert(value)))
            elif isinstance(value, (list, tuple)):
                temp.append(self.DictFormat(key, self.ListConvert(value)))
            else:
                temp.append(self.DictFormat(key, self.DictConvert(self.ClassConvert(value))))
        end_str = ', '.join(temp)
        return '{ ' + end_str + ' }'

    def ClassConvert(self, obj):
        obj_dict = {obj.__class__.__name__: obj.__dict__}
        return obj_dict

    def DictFormat(self, key, value):
        return "'{key}':{value}".format(key=key, value=value)

data = JsonFormat()
print(data.JsonConvert({'1': 2, '3': True, '5': my_car}))

