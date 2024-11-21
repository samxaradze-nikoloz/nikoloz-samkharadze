#მეგობრებო, ქვემოთ კომენტარის სახედ მოცემულია დავალების პირობები. ყოველი ამოცანის ქვეშ დაწერეთ თქვენი პასუხი. პითონ ფაილის ჩამოტვირთვისას დააწერეთ davaleba 2 - elena bliadze.py 
# ოღონდ elena bliadze -ს ნაცვლად თქვენი სახელი და გვარი. გისურვებთ წარმატებას ! ასევე გაითვალისწინეთ მოცემული დავალება ფოლდერით უნდა ატვირთოთ გითჰაბზე და ლინკი კომენტარში დაურთოთ თქვენს მიერ ატვირთულ დავალებას.
#გისურვებთ წარმატებას!

# დაწერე (ჩაფასთე მარჯვნივ(გასწვრივ)) გითჰაბის ლინკი, სადაც ატვირთე შენი ფაილი: https://github.com/samxaradze-nikoloz/nikoloz-samkharadze

#1. დაბეჭდეთ 8-ის ჯერადი რიცხვები 200-დან 25-ის ჩათვლით კლებადობით.
for i in range (200, 25, -8):
    print(i)

#2. დაითვალეთ 100-დან 2500-ის ჩათვლით რიცხვების ჯამი რომლებიც არიან 7-ის და 5-ის ჯერადი
#   ერთდროულად. დაბეჭდეთ მიღებული შედეგი.
for i in range (100,2100):
    if i%7==0 and i%5==0:
        print(f" meore davaleba {i}")
# 3. დაითვალეთ 1500-დან 2100-ის ჩათვლით 5-ის ჯერადი რიცხვების რაოდენობა. დაბეჭდეთ შედეგი.
raodenoba=1
for i in range(1500,2100):
    if i %5==0:
        raodenoba+=1
        print(f"mesame davaleba : {raodenoba}")

#4. დაბეჭდეთ ეკრანზე 15-დან 150-მდე 5-ის ჯერადი რიცხვები გარდა 50-ის, 75, 80-ისა. გამოიყენეთ continue
#ოპერატორი.
for i in range(15,150):
    if i==50 or i==75 or i==80:
        continue
    if i%5==0:
      print(f"meotxe davaleba :{i}")

#5. შეიყვანეთ ნებისმიერი 2 რიცხვი. ციკლის გამოყენებით დაბეჭდეთ შეყვანილი რიცხვების საერთო გამყოფები. მაგ. 15-ის და 18-ის საერთო გამყოია 1,3
a=int(input("seiyvane pirveli rixvi : "))
b=(int(input("seiyvane meore ricxvi : ")))
for gamyopi in range(1,1000):
    if a%gamyopi==0 and b%gamyopi==0:
        print(f"{a} da {b} saerto gamyopia : {gamyopi}")
#6. შეიყვანეთ 2 დადებითი მთელი რიცხვი. იპოვეთ ამ ორი რიცხვის უმცირესი საერთო ჯერადი.



#პირობითები:
#7. დაწერეთ პროგრამა, რომლის მეშვეობითაც შეიტანთ ნებისმიერ რიცხვს. პროგრამამ შეამოწმოს, თუ შეყვანილი რიცხვი 10-ის ჯერადია, დაბეჭდოს “რიცხვი ბოლოვდება 0-ით”, 
# თუ არადა დაბეჭდოს “რიცხვი არ ბოლოვდება 0-ით”. 
# (გაითვალისწინეთ: 10-ის ჯერადი ნიშნავს რომ 10-ზე გაყოფისას ნაშთი არის 0).
z=int(input("seiyvane ricxvi (meshvide davleba) : "))
if z%10==0:
    print("ricxvi 0 it bolovdeba")
else:
    print("0 it ar bolovdeba")
#8. დაწერეთ პროგრამა, რომლის მეშვეობითაც შეიტანთ ნებისმიერ რიცხვს. პროგრამამ შეამოწმოს, თუ რიცხვი დადებითია, დაბეჭდოს ეკრანზე “Number is positive”, თუ რიცხვი უარყოფითია, 
# დაბეჭდოს “Number is negative”, თუ არადა დაბეჭდოს “Number is equal to zero”.
k=int(input("seiyvane ricxvi (8 davaleba) : "))
if k<0:
    print("nu,ber is negative")
if k==0:
    print("this number is eaqual to 0")
if k>0 :
    print("number is positive")
#9.დაწერეთ პროგრამა, რომლის მეშვეობითაც შეიტანთ ორ ნებისმიერ რიცხვს. პროგრამამ შეამოწმოს, თუ ორივე შეყვანილი რიცხვი 10-ზე მეტია, დაითვალეთ მათი საშუალო არითმეტიკული, 
# თუ არადა დაითვალეთ მათი ნამრავლი. დაბეჭდეთ მიღებული შედეგი.
j=int(input("seiyvane ricxvi (9 avaleba) : "))
m=int(input("seiyvane 2 ricxvi (9 avaleba) : "))
if j>10 and m>10:
    print(f"sashualo aritmetikulia : {(j+m)/2}")
if m<10 and j<10:
    print(f"namreavlia {j*m}")
#10. დაბეჭდე კალკულატორი ციკლის და პირობითი ოპერატოორების გამოყენებით, გამოიყენე ოპერაციებად + - მიმატება, ** - ხარისხში აყავანა, /- გაყოფა.
risigaketebaginda= str(input("cawere ras gaaketeb +, -, *, /, : "))
while risigaketebaginda== "+" :
   jamiricxvi1=int(input("seiyvane seni rixvi jamistvis : "))
   jamiricxvi2=int(input("seiyvane seni rixvi jamistvis : "))
   print(jamiricxvi1 + jamiricxvi2)
   break
while risigaketebaginda== "-" :
 minusiricxvi1=int(input("sheiyvane ricxvi minusistvis : "))
 minusiricxvi2= int(input("sheiyvane meore ricxvi minusistvis : "))
 print(minusiricxvi1 - minusiricxvi2)
 break
while risigaketebaginda== "*" :
 gamravlebaricxvi1=int(input("sheiyvane ricxvi gamravlebistvis : "))
 gamravlebaricxvi2= int(input("sheiyvane meore ricxvi gamravlebistvis : "))
 print(gamravlebaricxvi2 * gamravlebaricxvi1)
while risigaketebaginda== "/" :
 gasayopii=int(input("sheiyvane gasayopi : "))
 gamyopii= int(input("sheiyvane gamyopi : "))
 print(gasayopii / gamyopii)
 break



