def main():
    nums = []

    while True:
        num = input("\nEnter a number or type 'done' to finish: ")

        if num == 'done':
            break

        try:
            num = int(num)
        except ValueError:
            print("That's not a valid number!")
            continue

        nums.append(num)

        average = sum(nums) / len(nums)
        print(f"\nThe current average value of the list is: {average}")

main()