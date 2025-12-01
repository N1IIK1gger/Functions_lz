def circle(R):
    S=3.14*R**2
    C=2*3.14*R
    print('Площадь круга =',S)
    print('Длина окружности =',C)

def main(): 
    R=float(input())
    print('Введите радиус круга:')
    circle(R) 
if __name__ == "__main__":
    main()