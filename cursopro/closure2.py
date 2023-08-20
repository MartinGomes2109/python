def make_division(x):
    def division(y):
        return y / x
    return division

def run():
    div_3 = make_division(3)
    print(div_3(18))
    div_5 = make_division(5)
    print(div_5(100))
    div_18 = make_division(18)
    print(div_18(54))
    
if __name__ == '__main__':
    run()