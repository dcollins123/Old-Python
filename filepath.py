import pathlib

# path of the given file
print(pathlib.Path("hello.py").parent.absolute())

# current working directory
print(pathlib.Path().absolute())