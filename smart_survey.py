ratings = []
count = 0
total = 0

print("Hello user, complete the survey.")
print("1 = Terrible \n2 = Poor \n3 = Average \n4 = Good \n5 = Excellent")
print('\nEnter a rating from 1 to 5 (or enter "e" to exit).')

while True:
    user_input = input("Enter your rating: ")

    if user_input == "e":
        break

    try:
        rating = int(user_input)
        if 1 <= rating <= 5:
            ratings.append(rating)
            count += 1
            total += rating
            print(f"You rated: {rating}")
        else:
            print("Please enter a number between 1 and 5.")
    except ValueError:
        print('Invalid input. Please enter a number from 1–5 or "e" to exit.')

if count > 0:
    average = total / count
    print("\nRating Summary:")
    print(f"Total Ratings: {count}")
    print(f"Average Rating: {average:.2f}")
    print(f"All Ratings: {ratings}")
else:
    print("\nNo ratings were entered.")
