def temperature(C):
    F=C*1.8+32
    print('Температуру в градусах Фаренгейта =',F)

def main():
    F=float(input())
    temperature(F)
    print('Введите температуру в градусах Цельсия:')
if __name__ == "__main__":
    main()