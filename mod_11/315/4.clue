def __init_subclass__(cls, /, **kwargs):

    for c in cls.__mro__:
        if '_randbelow' in c.__dict__:
            break
        if 'getrandbits' in c.__dict__:
            cls._randbelow = cls._randbelow_with_getrandbits
            break
        if 'random' in c.__dict__:
            cls._randbelow = cls._randbelow_without_getrandbits
            break