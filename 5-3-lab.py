word = "Found name ="
ids = {"name": "Alice", "age": 27}
def fun(word, name, *args, age=None):
    print(word, name)
    print("Age", age)
    print(args)
fun(word, **ids)
fun(word, ids["name"], *list(range(1, 10)))