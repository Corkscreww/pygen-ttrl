_DI400Y = _days_before_year(401)
_DI100Y = _days_before_year(101)
_DI4Y   = _days_before_year(5)

assert _DI4Y == 4 * 365 + 1

assert _DI400Y == 4 * _DI100Y + 1