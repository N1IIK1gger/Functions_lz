def temperature(C):
    F=C*1.8+32
    print('Температуру в градусах Фаренгейта =',F)
print('Введите температуру в градусах Цельсия:')

def main():
    F=float(input())
    temperature(F)
if __name__ == "__main__":
    main()