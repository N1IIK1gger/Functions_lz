def is_even(a):
    if a%2==0:
        print('Число',a,'четное')
    else:
        print('Число',a,'нечетное')

def main():
    a=int(input())
    is_even(a)
    print('Введите число:')
if __name__ == "__main__":
    main()