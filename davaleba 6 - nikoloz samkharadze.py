#მეგობრებო, ქვემოთ კომენტარის სახედ მოცემულია დავალების პირობები. ყოველი ამოცანის ქვეშ დაწერეთ თქვენი პასუხი. პითონ ფაილის ჩამოტვირთვისას დააწერეთ davaleba 6 - elena bliadze.py 
# ოღონდ elena bliadze -ს ნაცვლად თქვენი სახელი და გვარი. გისურვებთ წარმატებას ! ასევე გაითვალისწინეთ მოცემული დავალება ფოლდერით უნდა ატვირთოთ გითჰაბზე და ლინკი კომენტარში დაურთოთ თქვენს მიერ ატვირთულ დავალებას.
#გისურვებთ წარმატებას!

# დაწერე (ჩაფასთე მარჯვნივ(გასწვრივ)) გითჰაბის ლინკი, სადაც ატვირთე შენი ფაილი:  https://github.com/samxaradze-nikoloz/nikoloz-samkharadze


# იქამდე სანამ დავალების შესრულებას დაიწყებდე შექმენი ფოლდერი და იქ განათავსე მმოცემული პითონის ფაილი და თქსთ ფაილი, რომელთანაც იმუშავებ.

#სტრიქონები & ფაილებთან მუშაობა & try&except ბლოკი

#მოცემულია :
leqsi = """ მირბის, მიმაფრენს უგზო-უკვლოდ ჩემი მერანი,
            უკან მომჩხავის თვალბედითი შავი ყორანი!
            გასწი, მერანო, შენს ჭენებას არ აქვს სამძღვარი,
            და ნიავს მიეც ფიქრი ჩემი, შავად მღელვარი!"""


#1. დაწერეთ პროგრამა, რომელიც  დაყოფს მოცემული სტროფის 2 ტაეპს  ლისტის ობიექტებად, დაითვლის განახლებული ლისტის სიგრძეს და არსბეულ 1 და 2 ადგილზე მდგომ ობიექტებს დააკონკატენირებს.
lines = leqsi.strip().split("\n")
list_length = len(lines)
if list_length >= 2:
    concatirebulixazi = lines[0].strip() + " " + lines[1].strip()
else:
   concatirebulixazi = "araa sakmarisi tipi"
print("ganaxleebuli sigrzea", list_length)
print("1 da 2 tip :", concatirebulixazi)

#2.დაწერეთ პროგრამა, რომლის მეშვეობით გახსნით უკვე არსებულ ფაილს და ბოლოში დაამატეთ თქვენთვის სასურველი ტექსტი. 
file_name = "random.txt"
new_text = "zazazaza"
with open(file_name, "a", encoding="utf-8") as file:
    file.write("\n" + new_text)

print(f"teksti {new_text} demata {file_name}.")
#3. დაწერეთ პროგრამა რომელიც წაიკითხავს ტექსტს ფაილიდან და დაბეჭდავს ეკრანზე მაღალ რეგისტრში. (ამ შემთხვევაში შექმენი , შენი ფაილია და ჩაწერილი დახვდეს ინგლისური ასოებით ტექსტი)
with open(file_name, "r", encoding="utf-8") as file:
    content = file.read()
print("failis ragaca magal registrsi:")
print(content.upper())
#4. შექმენით ტექსტური ფაილი,რომელშიც ჩაწერთ რიცხვებს ცალ-ცალკე ხაზზე. დაწერეთ პროგრამა, რომელიც წაიკითხავს მონაცემებს ფაილიდან, აიყვანს რიცხვებს კვადრატში და ჩაწერს შედეგებს ახალ ფაილში.
numbers_file = "numbers.txt"
squared_numbers_file = "kvadrati.txt"
with open(numbers_file, "w", encoding="utf-8") as file:
    file.write("1\n2\n3\n4\n5")
with open(numbers_file, "r", encoding="utf-8") as file:
    numbers = file.readlines()
squared_numbers = [str(int(num.strip()) ** 2) for num in numbers]
with open(squared_numbers_file, "w", encoding="utf-8") as file:
    file.write("\n".join(squared_numbers))
print(f"kvadratuli rixcxvebi daemata failshi '{squared_numbers_file}'.")

#5. მოიფიქრე და დაწერე ,მხოლოდ try-except ით ბლოკი, ფაილებთან სამუშაოდ. გაითვალისწინე გამონაკლისად, მინიმუმ 2 შეცდომა მაინც უნდა გქონდეს , შესაბამის მესიჯთან ერთად.
try:
    with open(numbers_file, "r", encoding="utf-8") as file:
        numbers = file.readlines()
    squared_numbers = [str(int(num.strip()) ** 2) for num in numbers]
    with open(squared_numbers_file, "w", encoding="utf-8") as file:
        file.write("\n".join(squared_numbers))
    print(f"warmatebit daemata failsi'{squared_numbers_file}'.")
except FileNotFoundError:
    print("faili ar moidzebna")
except ValueError:
    print("faili ar moidzebna")

#6. დაწერე კალკულატორი, ციკლის, try-except ბლოკის გამოყენებით და შენმა კალკულატორმა დაითვალოს +, - ან / .
while True:
    try:
        print("\n mogesalmebit kalkurataorsi(rom gamoxvide daweere'exit')")
        num1 = input("siyvane ricxvi ;  ")
        if num1.lower() == "exit":
            break
        num1 = float(num1)
        operation = input("ras gaaketebt ser/mis(+, -, /): ")
        if operation not in ["+", "-", "/"]:
            raise ValueError("jer araa updati")
        num2 = input("seiyvaen 2 ricxvi:  ")
        if num2.lower() == "exit":
            break
        num2 = float(num2)
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "/":
            if num2 == 0:
                raise ZeroDivisionError("nulze ver gakop")
            result = num1 / num2
        print(f"result: {result}")
    except ValueError as ve:
        print(f"eror {ve}")
    except ZeroDivisionError as zde:
        print(f"error :  {zde}")

#7.  დაუმატე შენს მიერ დაწერილ კალკულატორს raise (ანუ მოიფიქრე შენი ერორი)
        if abs(result) > 1e6:
            raise OverflowError("pasuxi didia gamosatvlelad")
        print(f"pasuxi: {result}")
    except ValueError as ve:
        print(f"secdoma: {ve}")
    except ZeroDivisionError as zde:
        print(f"secdoma: {zde}")
    except OverflowError as oe:
        print(f"secdoma: {oe}")
#8. გამოიყენე f-format მეთოდი, და დაწერე შენთვის სასურველი პროგრამის მგალაითი ნასწავლი მასალიდან.
name = input("saxeli: ")
age = int(input("asaki "))
year_of_birth = 2025 - age
print(f"helou {name}! sen daibade {year_of_birth} (tu dagaviwkda).")

#9.გამოიტენე %s, %d, %f პროგრამის მესიჯის დასაბეჭდათ, და დაწერე შენთვის სასურველი მაგალითი ნასწავლი მასალიდან.
item = "romis imperia"
quantity = 5
price = 1.20
message = "sen ikide %s raodenobit %d ertis pasia %.2f lari." % (item, quantity, price)
print(message)

#10. დაწერეთ კოდი, რომელიც გამოითვლის და დაბეჭდავს [100, 450] შუალედიდან აღებული ყველა 3-ის ჯერადი მთელი რიცხვის კუბების ჯამს გამოკლებული 
# იმავე შუალედიდან აღებული 7-ის ჯერადი რიცხვების კვადრატების ჯამი. გამოიტანე შენთვის სასურველი მესიჯი, ნაცნობი ფორმატირების ხერხებით.
samisjeradisjami= sum(x**3 for x in range(100, 451) if x % 3 == 0)
svidisjeradisjami= sum(x**2 for x in range(100, 451) if x % 7 == 0)
result =samisjeradisjami-svidisjeradisjami
print(f"3 is jeradi kvadfratis jamio: {samisjeradisjami}")
print(f"7is jeradi kvaratis jami: {svidisjeradisjami}")
print(f"saboloo jamia : {result}")
