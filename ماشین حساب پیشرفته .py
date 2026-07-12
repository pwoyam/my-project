while True:
    print("\n=== ماشین‌حساب پیشرفته ===")
    print("1 - جمع")
    print("2 - تفریق")
    print("3 - ضرب")
    print("4 - تقسیم")
    print("5 - توان")
    print("6 - باقیمانده")
    print("7 - تاریخچه محاسبات")
    print("0 - خروج")

    choice = input("\nلطفاً یک گزینه را انتخاب کنید: ")
    if choice == "0":
        print("خداحافظ")
        break
    
    elif choice in ["1", "2", "3", "4", "5", "6"]:
        try:
            num1 = float(input("عدد اول را وارد کنید: "))
            num2 = float(input("عدد دوم را وارد کنید: "))
        except ValueError:
            print("خطا: لطفاً اعداد معتبر وارد کنید.")
            continue

        if choice == "1":
            result = num1 + num2
            
        elif choice == "2":
            result = num1 - num2
        elif choice == "3":
            result = num1 * num2
        elif choice == "4":
            if num2 == 0:
                print("خطا: تقسیم بر صفر ممکن نیست.")
                continue
            result = num1 / num2
        elif choice == "5":
            result = num1 ** num2
        elif choice == "6":
            result = num1 % num2
            
        print(f"نتیجه: {result}")

    else:
        print("انتخاب نامعتبر")    