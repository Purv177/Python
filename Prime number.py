prime_count = 0
composite_count = 0

number = 0 

while number != -1:
    try:
        number = int(input("Enter a number (-1 to stop): "))
        if number == -1:
            break
        elif number < 1:
            print("Please enter a positive integer greater than 0.")
            continue

        is_prime = True
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                is_prime = False
                break

        if is_prime:
            prime_count += 1
            print(f"{number} is a prime number.")
        else:
            composite_count += 1
            print(f"{number} is a composite number.")

    except ValueError:
        print("Invalid input. Please enter a valid integer.")

print(f"\nTotal prime numbers: {prime_count}")
print(f"Total composite numbers: {composite_count}")
