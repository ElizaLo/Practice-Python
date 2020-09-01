import os
import json
import argparse
import tempfile


class Storage():

    def __init__(self):
        if not os.path.exists(storage_path):
            self.storage = dict()
        else:
            with open(storage_path, 'r') as f:
                self.storage = json.load(f)

    def write(self, key_name, value):
        if key_name not in self.storage:
            self.storage[key_name] = [value]
        else:
            self.storage[key_name].append(value)

        with open(storage_path, 'w') as f:
            json.dump(self.storage, f)

    def get(self, key_name):
        if key_name in self.storage.keys():
            return self.storage.get(key_name, [])
        return ''




if __name__ == '__main__':

    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')


    parser = argparse.ArgumentParser()
    parser.add_argument("--key", help = "Key", action="store", dest = "key_name")
    parser.add_argument("--val", help = "Value", action="store", dest = "value")
    parser.add_argument('--clear', action='store_true', help='Clear')

    args = parser.parse_args()

    storage = Storage()

    if args.clear:
        os.remove(storage_path)
    elif args.value is None:
        print(', '.join(map(str,storage.get(args.key_name))))
    elif args.key_name and args.value:
        storage.write(args.key_name, args.value)
    else:
        print('The program is called with invalid parameters.')
