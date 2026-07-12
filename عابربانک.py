balance = 0

history = []

while True:
    print("به عابر بانک خوش آمدید")
    print("1. واریز")
    print("2. برداشت")
    print("3. موجودی")
    print("4. تاریخچه")
    print("0. خروج")

    choice = input("لطفاً یک گزینه را انتخاب کنید: ")

    if choice == "0":
        print("خدانگهدار شما.")
        break

    if choice == "1":
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

    elif choice == "2":
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

    elif choice == "3":
        print(f"موجودی شما: {balance}")

    elif choice == "4":
        if len(history) == 0:
            print("⚠️ هیچ تراکنشی ثبت نشده!")
        
        else:
            print("تاریخچه تراکنش ها:")
            print("-" * 20)
            for action, amount in history:
                print(f"- {action}: {amount} تومان")

    else:
        print("گزینه نامعتبر است. لطفاً یک گزینه معتبر انتخاب کنید.")