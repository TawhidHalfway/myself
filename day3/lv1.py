import time
print("what do you want sir?")
order = input("Your order plese:")
print(f"sir chefe is making {order}")
print("Please wait...")
for i in range(5 , -1, -1):
    print(f"\r{i}    " , end="")
    time.sleep(1)
print("\nsir it's done.")