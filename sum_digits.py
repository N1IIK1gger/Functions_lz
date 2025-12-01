def sum_digits(a):
    sum=0
    for i in range(0,len(a)):
        sum+=int(a[i])
    print('Сумма всех цифр числа',a,'=',sum)

def main():
    a=input()
    print('Введите число:')
    sum_digits(a)
if __name__ == "__main__":
    main()