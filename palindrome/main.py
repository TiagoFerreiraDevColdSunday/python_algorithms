import math

def main(x : int) -> bool:

    if (x < 0):
        return False

    y = 0
    loop_condition = float(x)

    while( loop_condition >= 1 ):
        loop_condition = loop_condition / 10
        
        frac, loop_condition = math.modf(loop_condition)

        y = round((y * 10) + (frac * 10))

    print(f"SAIU! Valor do y: {y} e do x: {x}")
    if (x == (y)):
        return True
    else:
        return False


if __name__ == "__main__":
    print(f"\nResult is {main(1000000001)}")