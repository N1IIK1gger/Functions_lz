def circle(R):
    S=3.14*R**2
    C=2*3.14*R
    print('Площадь круга =',S)
    print('Длина окружности =',C)
print('Введите радиус круга:')

def main(): 
    R=float(input())
    circle(R)
if __name__ == "__main__":
    main()