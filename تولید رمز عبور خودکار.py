import random

uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
special = "@#!"

def generate_password(length):
    if length < 8:
        print("⚠️ طول رمز باید حداقل ۸ باشه — به ۸ تغییر دادم!")
        length = 8
    
    password = []
    password.append(random.choice(uppercase))
    password.append(random.choice(numbers))
    password.append(random.choice(special))

    all_chars = uppercase + lowercase + numbers + special
    for i in range(length-3):
        password.append(random.choice(all_chars))

    random.shuffle(password)

    return "".join(password)

def check_password(password):
    has_upper = any(c in uppercase for c in password)
    has_number = any(c in numbers for c in password)
    has_special = any(c in special for c in password)
    has_length = len(password) >= 8

    print("\n--- بررسی رمز عبور ---")
    print(f"حرف بزرگ: {'✅' if has_upper else '❌'}")
    print(f"عدد: {'✅' if has_number else '❌'}")
    print(f"کاراکتر خاص: {'✅' if has_special else '❌'}")
    print(f"حداقل ۸ کاراکتر: {'✅' if has_length else '❌'}")

while True:
    print("\n=== 🔐 تولید رمز عبور ===")
    print("1 - تولید رمز عبور")
    print("0 - خروج")

    choice = input("\nانتخاب کنید: ")

    if choice == "0":
        print("👋 خداحافظ!")
        break

    elif choice == "1":
        try:
            length = int(input("طول رمز عبور: "))
            password = generate_password(length)
            print(f"\n🔑 رمز عبور شما: {password}")
            

            again = input("\nرمز دیگه‌ای میخوای؟ (y/n): ")
            if again == "n":
                print("👋 خداحافظ!")
                break

        except ValueError:
            print("❌ فقط عدد وارد کن!")

    else:
        print("❌ انتخاب نامعتبر!")