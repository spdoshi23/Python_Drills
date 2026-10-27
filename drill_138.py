items = ["keyboard", "mouse", "monitor", "laptop"]
target = "printer"

index = 0
while index < len(items):
    if items[index] == target:
        print("Item available!")
        break
    index += 1
else:
    print("Item unavailable!")












