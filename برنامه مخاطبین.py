contacts = {}
# دیکشنری برای ذخیره مخاطبین

while True:

    print("1 - افزودن مخاطب")
    print("2 - جستجو")
    print("3 - لیست همه")
    print("0 - خروج")
    # نمایش منو به کاربر

    choice = input("انتخاب کنید: ")
    
    if choice == "1":
        name = input("نام مخاطب: ")
        phone = input("شماره تلفن: ")
        contacts[name] = phone
        print("مخاطب اضافه شد.")

    elif choice == "2":
        name = input("نام مخاطب: ")
        if name in contacts:
            print(f"شماره تلفن {name}: {contacts[name]}")
        else:
            print("مخاطب یافت نشد.")

    elif choice == "3":
        print("لیست مخاطبین:")
        for name, phone in contacts.items():
            print(f"- {name}: {phone}")
        if len(contacts) == 0:
            print("⚠️ هیچ مخاطبی ثبت نشده!")

    elif choice == "0":
        print("👋 خداحافظ!")
        break
    else:
        print("انتخاب نامعتبر است.")