def main():
    print("=== Депозитний калькулятор ===")

    # Введення початкових даних
    deposit = float(input("Введіть початкову суму депозиту: "))
    rate = float(input("Введіть річну відсоткову ставку (%): "))
    
    years_input = input("Введіть термін депозиту у роках (Enter = 2): ")
    years = int(years_input) if years_input.strip() else 2

    # Розрахунок
    months = years * 12
    monthly_rate = rate / 12 / 100

    print("\nПомісячна розбивка:")
    print("-" * 30)

    for month in range(1, months + 1):
        deposit += deposit * monthly_rate
        print(f"Місяць {month:2d}: {deposit:.2f} грн")

    print("-" * 30)
    print(f"Сума на рахунку після {years} років: {deposit:.2f} грн")


if __name__ == "__main__":
    main()
