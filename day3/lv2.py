import time
print("sir it's a progress bar")
load_unit = "#"
loading_bar = ""
for i in range(10):
    loading_bar += load_unit
    print(loading_bar, end="\r")
    time.sleep(1)
print("it's done!")