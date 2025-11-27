def is_even(a):
    if a%2==0:
        print('Число',a,'четное')
    else:
        print('Число',a,'нечетное')
print('Введите введите число:')

def main():
    a=int(input())
    is_even(a)
if __name__ == "__main__":
    main()