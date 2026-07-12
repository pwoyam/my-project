balance = 0
history = []

def show_menu():
    print("\nبه عابر بانک خوش آمدید")
    print("1. واریز")
    print("2. برداشت")
    print("3. موجودی")
    print("4. تاریخچه")
    print("0. خروج")

def deposit():
    global balance
    try:
        amount = float(input("لطفا مبلغ را وارد کنید: "))
        if amount <= 0:
            print("مبلغ باید بیشتر از صفر باشد.")
        else:
            balance += amount
            history.append(("واریز", amount))
            print(f"مبلغ {amount} به حساب شما واریز شد.")
            print(f"موجودی جدید: {balance}")
    except ValueError:
        print("لطفاً یک مبلغ معتبر وارد کنید.")


# تابع برداشت
def withdraw():
    global balance
    try:
        amount = float(input("لطفا مبلغ را وارد کنید: "))
        if amount <= 0:
            print("مبلغ باید بیشتر از صفر باشد.")
        elif amount > balance:
            print("موجودی کافی نیست.")
        else:
            balance -= amount
            history.append(("برداشت", amount))
            print(f"مبلغ {amount} از حساب شما برداشت شد.")
            print(f"موجودی جدید: {balance}")
    except ValueError:
        print("لطفاً یک مبلغ معتبر وارد کنید.")

# تابع نمایش موجودی
def show_balance():
    print(f"موجودی شما: {balance}")  

def show_history():
    if len(history) == 0:
        print("⚠️ هیچ تراکنشی ثبت نشده!")
    else:
        print("تاریخچه تراکنش‌ها:")
        print("-" * 20)
        for action, amount in history:
            print(f"- {action}: {amount} تومان")

while True:
    show_menu()
    choice = input("لطفاً یک گزینه را انتخاب کنید: ")

    if choice == "0":
        print("خدانگهدار شما.")
        break
    elif choice == "1":
        deposit()
    elif choice == "2":
        withdraw()
    elif choice == "3":
        show_balance()
    elif choice == "4":
        show_history()
    else:
        print("گزینه نامعتبر است.")