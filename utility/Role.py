class Role:
    @staticmethod
    def convert(aggregateRootObj, roleClassName):
        for objName in dir(aggregateRootObj):
            obj = getattr(aggregateRootObj, objName)
            if obj.__class__.__name__ == roleClassName:
                return obj

    @staticmethod
    def add_role(root, role):
        for attr in dir(role):
            if hasattr(root, attr):
                continue
            setattr(root, attr, getattr(role, attr))
