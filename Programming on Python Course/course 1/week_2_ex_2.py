import json
from functools import wraps

def to_json(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        return json.dumps(func(*args, **kwargs))
    return wrapped


@to_json
def get_data():
  return {
    'data': 42
  }

s = get_data()  # вернёт '{"data": 42}'

print(s)
