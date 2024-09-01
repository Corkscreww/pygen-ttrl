try:
    from _sha512 import sha512 as _sha512
except ImportError:
    from hashlib import sha512 as _sha512