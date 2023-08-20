def make_repeter(n):
    def repeater(s):
        assert type(s) == str, "solo puede ingresar un numero"
        return s * n
    return repeater

def run():
    repeat_5 = make_repeter(5)
    print(repeat_5("hola"))
    repeat_10 = make_repeter(10)
    print(repeat_10("Platzi"))

if __name__ == '__main__':
    run()