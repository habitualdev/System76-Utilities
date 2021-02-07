def read_file(path):
    with open(path, 'r') as f:
        return f.read().decode('utf-8')
