#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    import calculator_1 as c
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        if argv[2] == "+":
            math = c.add(a, b)
            print("{:d} + {:d} = {:d}".format(a, b, math))
        elif argv[2] == "*":
                math = c.mul(a, b)
                print("{:d} * {:d} = {:d}".format(a, b, math))
        elif argv[2] == "-":
                math = c.sub(a, b)
                print("{:d} - {:d} = {:d}".format(a, b, math))
        elif argv[2] == "/":
                math = c.div(a, b)
                print("{:d} / {:d} = {:d}".format(a, b, math))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
