left_m = 3
left_c = 3
right_m = 0
right_c = 0
boat = "left"

print("Game Start\n")
print("Now the task is to move all of them to right side of the river")
print("Rules:")
print("1. The boat can carry at most two people")
print("2. If cannibals are greater than missionaries, the missionaries will be eaten")
print("3. The boat cannot cross the river by itself with no people on board\n")

while True:

    print("\nLeft Bank : ", "M " * left_m + "C " * left_c)
    print("Right Bank:", "M " * right_m + "C " * right_c)

    if left_m == 0 and left_c == 0:
        print("\nCongratulations! You solved the problem.")
        break

    print("\n", boat.capitalize(), "side ->", "Right" if boat == "left" else "Left", "side river travel")

    m = int(input("Enter number of Missionaries travel => "))
    c = int(input("Enter number of Cannibals travel => "))

    if m + c == 0 or m + c > 2:
        print("Invalid input please retry !!")
        continue

    if boat == "left":
        if m > left_m or c > left_c:
            print("Invalid input please retry !!")
            continue

        left_m -= m
        left_c -= c
        right_m += m
        right_c += c
        boat = "right"

    else:
        if m > right_m or c > right_c:
            print("Invalid input please retry !!")
            continue

        right_m -= m
        right_c -= c
        left_m += m
        left_c += c
        boat = "left"

    if (left_m > 0 and left_c > left_m) or (right_m > 0 and right_c > right_m):
        print("\nCannibals ate the Missionaries!")
        print("Game Over.")
        break
