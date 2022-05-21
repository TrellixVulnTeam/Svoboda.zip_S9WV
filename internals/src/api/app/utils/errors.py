class DirectoryConsistencyError(Exception):
    def __init__(self, data):
        self.data = data
        self.message = "Your directory consistency were corrupted! This error occurs in: "
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}{self.data}'


class FileConsistencyError(Exception):
    def __init__(self, data):
        self.data = data
        self.message = "Your file consistency were corrupted! This error occurs in: "
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}{self.data}'


class NoSuchZippError(Exception):
    def __init__(self, data):
        self.data = data
        self.message = " zipp package is not installed! "
        super().__init__(self.message)

    def __str__(self):
        return f'<{self.data}>{self.message}'


class CorruptedZippError(Exception):
    def __init__(self, data):
        self.data = data
        self.message = "This zipp package is corrupted! This error occurs in: "
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}{self.data}'


class CorruptedFileError(Exception):
    def __init__(self, file_name, data):
        self.data = data
        self.file_name = file_name
        self.message = " is corrupted! Can't start due to: "
        super().__init__(self.message)

    def __str__(self):
        return f'"{self.file_name}"{self.message}{self.data}'


class ZippConflictError(Exception):
    def __init__(self, data):
        self.data = data
        self.message = " zipp package conflicting with another one!"
        super().__init__(self.message)

    def __str__(self):
        return f'<{self.data}>{self.message}'
