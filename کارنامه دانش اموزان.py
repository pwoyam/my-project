students = {}

while True:
    print("\n=== 📚 سیستم نمرات دانش‌آموزان ===")
    print("1 - اضافه کردن دانش‌آموز")
    print("2 - نمایش همه دانش‌آموزان")
    print("3 - میانگین نمرات")
    print("0 - خروج")

    choice = input("انتخاب خود را وارد کنید: ")

    if choice == "0":
        print("👋 خداحافظ!")
        break

    elif choice == "1":
        name = input("نام دانش آموز را وارد کنید:").strip()
        if name in students:
            print(f"❌ '{name}' قبلاً ثبت شده!")
        else:
            try:
                grade = float(input("نمره دانش آموز را وارد کنید: "))
                students[name] = grade
                print(f"✅ '{name}' با نمره {grade} ثبت شد.")
            except ValueError:
                print("❌ لطفاً یک نمره معتبر وارد کنید!")

    elif choice == "2":
        if len(students) == 0:
            print("❌ هیچ دانش‌آموزی ثبت نشده است.")
        else:
            print("\n📋 لیست دانش‌آموزان:")
            print(f"{'نام':^15} | {'نمره':^6} | {'وضعیت':^10}")
            for name, grade in students.items():
                status = "✅قبول" if grade >= 10 else "❌مردود"
                print(f"{name:^15} | {grade:^6} | {status:^10}")

    elif choice == "3":
        if len(students) == 0:
            print("❌ هیچ دانش‌آموزی ثبت نشده است.")
        else:
            average = sum(students.values()) / len(students)
            print(f"📊 میانگین نمرات: {average:.2f}")

    else:
        print("❌ انتخاب نامعتبر!")