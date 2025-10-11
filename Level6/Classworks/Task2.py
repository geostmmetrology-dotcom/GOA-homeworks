"""2) შექმენით პროგრამა რომელშიც გექნებათ თქვენი საყვარელი ბოსტნეულის ცვლადი, შემდეგ განაახლეთ ამ ცვლადის მნიშვნლობა ჯერ უბრალო გზით შემდეგ კი მინჭბის ოპერატორით (გამოიყენეთ ორივე ოპერაცია +, *), ასევე გააკეთეთ int ტიპის ცვლადი რომლის მნიშვნელობასაც განაახლებთ უბრალო ფორმით და შემდეგ assignment ოპერატორით. ასევე კომენტარებით დაწერეთ ცვლადის სახელის წესებით, თქვენ მიერ შექმნილი ცვლადები fstring-ის მეშვეობით დაბეჭდეთ, პირველი ცვლადის fstring ჯერ ახალ message ცვლადში შეინახეთ უნდა გამოიტანოთ my favourite vegetable is <vegetable>, შემდეგ კი მეორე ცვლადისთვის პირდაპირ დაბეჭდეთ fstring-ით fstring ახსენთ კომენტარებით"""

my_favourite_vegetable = "carrot"

# ვბეჭდავთ საწყის მნიშვნელობას
print(f"{my_favourite_vegetable}")

# ცვლადის განახლება "უბრალო გზით"
my_favourite_vegetable = my_favourite_vegetable + " and cucumber"  # ვამატებთ ახალ სიტყვას "+"
print(f"{my_favourite_vegetable}")

# ცვლადის განახლება მინიჭების ოპერატორით (* ოპერაციით)
my_favourite_vegetable *= 2  # იგივეა რაც: my_favourite_vegetable = my_favourite_vegetable * 2
print(f"{my_favourite_vegetable}")


# ახლა შევქმნათ რიცხვითი (int) ტიპის ცვლადი
my_number = 5
print(f"{my_number}")

# განვაახლებთ მნიშვნელობას უბრალო გზით
my_number = my_number + 3
print(f"{my_number}")

# განვაახლებთ მნიშვნელობას მინიჭების ოპერატორით (assignment operator)
my_number += 7  # იგივეა რაც my_number = my_number + 7
print(f"{my_number}")

# f-string ახსნა და გამოყენება

# f-string არის ტექსტის ფორმატირების მეთოდი, სადაც სტრიქონში შეგვიძლია პირდაპირ ჩავწეროთ ცვლადის მნიშვნელობა {ფრჩხილებში}
# ახლა შევქმნათ ახალი ცვლადი message, სადაც შევინახავთ f-string-ს
message = f"My favourite vegetable is {my_favourite_vegetable}"

# დაბეჭდვა
print("\n" + message)

# მეორე ცვლადისთვის — პირდაპირ დაბეჭდავთ f-string-ით
print(f"My number after update is {my_number}")
