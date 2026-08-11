password = "12345qwe"
links = ["https://github.com", "https://facebook.com", "https://google.com"]
attempts = 3

while attempts > 0:
  user_input = input("Please enter your password: ")
  if user_input == password:
    print("Access Granted")
    for link in links:
      print(link)
      break
  else:
    attempts -= 1
    if attempts > 0:
      print(f"Incorrect password! {attempts} attempts left.")
    else:
      print("Access denied!")
