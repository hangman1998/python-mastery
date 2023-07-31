class MutInt:
    __slots__ = ["value"]

    def __init__(self, value):
        self.value = value

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return f"MutInt({self.value!r})"

    def __format__(self, __format_spec: str) -> str:
        return format(self.value, __format_spec)
