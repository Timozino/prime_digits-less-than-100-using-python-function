def prime_digits(k):
  print("All prime digits less than k")
  for i in range(2, k):
    for j in range(2, i):
      if i%j==0:
        break
    else: 
      print(i)

prime_digits(100)