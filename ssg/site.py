from pathlib import Path


class Site:
    def __init__(self, source, dest):
        self.source = Path(source)
        self.dest = Path(dest)

    def create_dir(self, path):
        directory = Path(self.dest + '/' + path.relative_to(self.source))
        directory.mkdir(exist_ok=True, parents=True)

    def build(self):
        self.dest.mkdir(exist_ok=True, parents=True)
        for path in self.source.rglob('*'):
            if path.is_dir():
                self.create_dir(path)
