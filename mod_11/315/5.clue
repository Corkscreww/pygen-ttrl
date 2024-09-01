def randbytes(self, n):
    return self.getrandbits(n * 8).to_bytes(n, 'little')


def randrange(self, start, stop=None, step=_ONE):
    
    istart = _index(start)
    if stop is None:
        if step is not _ONE:
            raise TypeError("Missing a non-None stop argument")
        if istart > 0:
            return self._randbelow(istart)
        raise ValueError("empty range for randrange()")