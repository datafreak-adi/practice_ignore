print("--------Beginner-------")
first, *remainder= "qwerty"
print(f"first : {first}, *remainder :{remainder} ")

alpha, *remainder= "qwerty"
print(f"first : {alpha}, *remainder :{remainder} ")


first, *middle, last= {"a":11 , "b":22 , "c":33}
print(f"first:{first},middle:{middle} , last:{last}")


print("--------Intermediate-------")

first,*remainder, last=[1,2,[3,4,5,6,7],3,4,5,6]
print(f"first:{first}, remainder: {remainder},last:{last}")