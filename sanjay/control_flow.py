mark=float(input("Enter your mark: "))
if mark>=35:
    print("True")
    if mark>=95.6:
        print("Medical")
    elif mark>60:
            print("Eng")
    else:
        print("ARTS")

else:
    print("Fail")
