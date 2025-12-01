def sum_digits(a):
    sum=0
    for i in range(0,len(a)):
        sum+=int(a[i])
    print('Сумма всех цифр числа',a,'=',sum)

def main():
    a=input()
    sum_digits(a)
    print('Введите число:')
if __name__ == "__main__":
    main()