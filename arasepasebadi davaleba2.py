#5- is jeradebi 20 idan 125 amde
a=1
b=a+1

# for a in range(125):
#     if a%5==0 and a<125 and a>20:
#      print(a)


#  #ricxvebi 1500 dan 2100 amde 5 is da 7 is jeradebi
# for a in range(2101):
#    if a>1500 and a<2100 and a%7==0 and a%5==0:
#       print(f"meore davaleba : {a}")

# #1500 dan 2100 amde ricxvebis jame 20000 meti ar unda ikos
# for ricxvi in range(1500,2101):
#    if ricxvi%5==0 and ricxvi%7==0:
#       a+=ricxvi
#       if a>20000:
#          break
#       print(f"mesame davaleba : {a}")

#1-100 luwi ricxvebis jami
# for g in range(1,100):
#    if g%2==0:
#       a+=g
#       print(f"meotxe davaleba : {a}")
   
#• შეიყვანეთ რიცხვი. დაითვალეთ ამ რიცხვის ფაქტორიალი და
#დაბეჭდეთ. მაგ. 5-ის ფაქტორიალი იგივია რაც 1 ∗ 2 ∗ 3 ∗ 4 ∗ 5
# paktoriali=1
# c=int(input("input number"))
# for g in range(1,c+1):
#    paktoriali *=g
#    print(f"ricxvi :{c} faktorialia : {paktoriali}")


#• შეიყვანეთ 2 დადებითი მთელი რიცხვი. იპოვეთ ამ ორი რიცხვის
#უმცირესი საერთო ჯერადი.
# num1=int(input("input number : "))
# num2=int(input("input second number : "))
# if num1 > num2:
#     ricxvi = num2
# else:
#     ricxvi = num1

# for g in range(ricxvi, num1 * num2 + 1, ricxvi):
#     if g % num1 == 0 and g % num2 == 0:
#         print(f"{num1} da {num2}-umciresi jeradia {g}")
#         break
 



 #დაბეჭდეთ 2-დან 1000-მდე ყველა მარტივი რიცხვი. 
# for ricxvi in range(1,1000):
#  for o in range(2, int(ricxvi** 0.5) + 1):
#         if ricxvi % o == 0:
#             break
#  else:
#      print(ricxvi)

#შეიყვანეთ ნებისმიერი რიცხვი. იპოვეთ ამ რიცხვის ციფრთა ჯამი და
#დაბეჭდეთ.
# ricxvi= input("seiyvanet ricxvi: ")
# ricxta_jami= sum(int(digit) for digit in ricxvi)
# print(f"ricxvis{ricxvi} ciprta jamia: {ricxta_jami}")

#naxati
print("*")
print("**")
print("***")
print("****")
print("*****")
print("****")
print("***")
print("**")
print("*")