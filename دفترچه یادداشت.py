notes = []

while True:
    print("\n=== دفترچه یادداشت ===")
    print("1 - افزودن یادداشت")
    print("2 - نمایش یادداشت ")
    print("3 - حذف یادداشت")
    print("0 - خروج")

    choice = input("\ یک گزینه را انتخاب کنید: ")
    if choice == "0":
        print("خداحافظ")
        break

    elif choice == "1":
        note = input("یادداشت را وارد کنید:")
        notes.append(note)
        print("یادداشت اضافه شد.")

    elif choice == "2":
        if len(notes) == 0:
            print("هیج یادداشتی ثبت نشده.!")
        else:
            print("یادداشت ها:")
            for i, note in enumerate(notes):
                print(f"{i + 1} - {note}")

    elif choice == "3":
        if len(notes) == 0:
            print("⚠️ هیچ یادداشتی برای حذف وجود ندارد!")
        else:
            print("یادداشت ها:")
            for i, note in enumerate(notes):
                print(f"{i + 1} - {note}")
            try:
                index = int(input("یادداشت مورد نظر را برای حذف انتخاب کنید: ")) - 1
                if 0 <= index < len(notes):
                    del notes[index]
                    print("یادداشت حذف شد.")
                else:
                    print("یادداشت مورد نظر یافت نشد.")
            except ValueError:
                print("لطفاً یک عدد معتبر وارد کنید.")

    else:
        print("انتخاب نامعتبر!")