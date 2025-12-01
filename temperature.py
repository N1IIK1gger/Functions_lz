def temperature(C):
    F=C*1.8+32
    print('Температуру в градусах Фаренгейта =',F)

def main():
    F=float(input())
    print('Введите температуру в градусах Цельсия:')
    temperature(F)
if __name__ == "__main__":
    main()