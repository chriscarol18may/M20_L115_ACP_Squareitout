def square_and_filter(begin, end):
    # Step 1: Calculate the square of numbers in the given range
    squares = [i ** 2 for i in range(begin, end + 1)]

    # Step 2: Filter the even and odd square values
    even_squares = [x for x in squares if x % 2 == 0]
    odd_squares = [x for x in squares if x % 2 != 0]

    # Step 3: Print the results
    print("Even square values:", even_squares)
    print("Odd square values:", odd_squares)

# Example usage:
start = int(input("Enter the beginning of the range: "))
stop = int(input("Enter the end of the range: "))

square_and_filter(start, stop)