def read_file(path: str) -> str:
    with open(path, 'r') as f:
        data = f.read()
        return data if isinstance(data, str) else data.decode('utf-8')


def write_file(path: str, value: str):
    with open(path, 'wb') as f:
        f.write(value.encode())
