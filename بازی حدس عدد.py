import random

secret_number = random.randint(1, 101)

attempts = 0

print("به بازی حدس عدد خوش آمدید.")
print("یک عدد بین 1 تا 101 حدس بزن!")

while True:
    try:
        guess = int(input("\nعدد را حدس بزنید: "))
        attempts += 1
        
        difference = abs(guess - secret_number)
        if guess == secret_number:
            print(f"🎉 آفرین! عدد {secret_number} بود!")
            print(f"تعداد تلاش‌ها: {attempts}")
            break
        
        if guess < secret_number:
            if difference > 10:
                print("عدد حدس زده شده بسیار کمتر است.")
            else:
                print("عدد حدس زده شده کمتر است.")
        else:
            if difference > 10:
                print("عدد حدس زده شده بسیار بیشتر است.")
            else:
                print("عدد حدس زده شده بیشتر است.")
    except ValueError:
        print("لطفاً یک عدد معتبر وارد کنید.")