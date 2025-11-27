def sum_digits(a):
    sum=0
    for i in range(0,len(a)):
        sum+=int(a[i])
    print('Сумма всех цифр числа',a,'=',sum)
print('Введите число:')

def main():
    a=input()
    sum_digits(a)
if __name__ == "__main__":
    main()