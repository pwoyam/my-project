import random

player_score = 0
computer_score = 0

# لیست انتخاب‌های ممکن
choice = ["سنگ", "کاغذ", "قیچی"]

# تابع انتخاب تصادفی کامپیوتر
def computer_choice():
    return random.choice(choice)

# تابع محاسبه نتیجه هر مرحله
def calculate_result(player, computer):
    if player == computer:
        return "مساوی"
    elif (player == "سنگ" and computer == "قیچی") or (player == "کاغذ" and computer == "سنگ") or (player == "قیچی" and computer == "کاغذ"):
        return "برد"
    else:
        return "باخت"

# تابع نمایش امتیازها
def show_score():
    print(f"\n📊 امتیاز شما: {player_score} | امتیاز کامپیوتر: {computer_score}")

# تابع اصلی بازی
def play():
    global player_score, computer_score

    print("- بازی سنگ و کاغذ و قیچی -")
    print("1 - سنگ")
    print("2 - کاغذ")
    print("3 - قیچی")

    choice = input("انتخاب کنید: ")

    if choice == "1":
        player = "سنگ"
    elif choice == "2":
        player = "کاغذ"
    elif choice == "3":
        player = "قیچی"
    else:
        print("❌ انتخاب نامعتبر!")
        return
    
    computer = computer_choice()
    print(f"\n🧑 شما: {player}")
    print(f"🤖 کامپیوتر: {computer}")
    
    result = calculate_result(player, computer)

    if result == "برد":
        player_score += 1
        print("🎉 شما بردید!")
    elif result == "باخت":
        computer_score += 1
        print("😞 کامپیوتر برد!")
    else:
        print("🤝 مساوی!")

    show_score()

# حلقه اصلی
while True:
    play()
    again = input("\nدوباره؟ (y/n): ")
    if again == "n":
        print("\n--- نتیجه نهایی ---")
        show_score()
        if player_score > computer_score:
            print("🏆 شما برنده کل بازی شدید!")
        elif computer_score > player_score:
            print("🤖 کامپیوتر برنده کل بازی شد!")
        else:
            print("🤝 کل بازی مساوی شد!")
        print("👋 خداحافظ!")
        break