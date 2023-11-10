

try:
    value = int(input("Enter to val: "))
    print(value)
except ZeroDivisionError:
    print("Empty")
except ValueError as e:
    print("Error : ", e)
except Exception as e:
    print("Error: ", e)
finally:
    print("tamamdır")