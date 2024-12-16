#მეგობრებო, ქვემოთ კომენტარის სახედ მოცემულია დავალების პირობები. ყოველი ამოცანის ქვეშ დაწერეთ თქვენი პასუხი. პითონ ფაილის ჩამოტვირთვისას დააწერეთ davaleba 4 - elena bliadze.py 
# ოღონდ elena bliadze -ს ნაცვლად თქვენი სახელი და გვარი. გისურვებთ წარმატებას ! ასევე გაითვალისწინეთ მოცემული დავალება ფოლდერით უნდა ატვირთოთ გითჰაბზე და ლინკი კომენტარში დაურთოთ თქვენს მიერ ატვირთულ დავალებას.
#გისურვებთ წარმატებას!

# დაწერე (ჩაფასთე მარჯვნივ(გასწვრივ)) გითჰაბის ლინკი, სადაც ატვირთე შენი ფაილი:  https://github.com/samxaradze-nikoloz/nikoloz-samkharadze

#Tuples : 

#1. დაწერე პროგრამა , რომელიც დაითვლის მოცემული tupex = ((), (), ('',), 'a', 'b', ('a', 'b', 'c'), ('d'),1,2,3,4) სიგრძეს.
a=((), (), ('',), 'a', 'b', ('a', 'b', 'c'), ('d'),1,2,3,4) 
print(len(a))

#2. დაწერე პროგრამა, რომელიც დაასორტირებს ტაპლში არსებულ ელემენტებს ინტეჯერების მიხედვით data = [('item1', '12'), ('item2', '15'), ('item3', '24')]
data = [('item1', '12'), ('item2', '15'), ('item3', '24')]
sortdata=sorted(data)
print(sortdata)

#3. შექმენი სასურველი თაფლი, რომელშიც ჩაყრი სიტყვიერ მონაცემებს და შემდეგ დაალაგებ ანბანურად და ანბანურად დალაგების შემდგომმა უკუღმა.
tuple =("datvi","tagvi","avlabari", "parizi")
sortedtupli=sorted(tuple)
print(sortedtupli)
#4. გაახუთმაქ თაფლში არსებული ელემენტები, ელემენტები შენით მოიფიქრე.
a=(12,22,56,78,98, 123)
print(a*5)

#Set - ები:
#5. შექმენით სიმრავლე შემდეგი ელემენტებით : 0, 1, 2, 3, 4. დაამატეთ ნებისმიერ 3 ელემენტი სურვილისამებრ. 
# წაშალეთ ორი ელემენტი სიმრავლიდან. დაბეჭდეთ სიმრავლის ელემენტები ცალ ცალკე ხაზზე (გამოიყენეთ for ციკლი). 
# დაითვალეთ სიმრავლის ელემენტების რაოდენობა.
h={ 0, 1, 2, 3, 4}
h.discard(2)
h.add(9)
h.add(8)
h.add(6)
print(len(h))
print(h)

#6. შექმენით ორი სიმრავლე: set1 სიმრავლე ელემენტებით "green”, "blue”; set2 სიმრავლე ელემენტებით
# "blue", "yellow”. იპოვეთ ამ ორი სიმრავლის გაერთიანება, თანაკვეთა, სხვაობა და სიმეტრიული
# სხვაობა (შეასრულეთ დავალება ორი გზით: არსებული მეთოდით (ფუნქციით) და შესაბამისი
# ოპერატორით.)
setA={"green", "red", "blue"}
setB={"brown", "yellow", "blue"}
print(setA.intersection(setB))
print(setA.difference(setB))
print(setA.union(setB))
#7. დაწერეთ პროგრამა რომელიც იპოვის სიმრავლეში მაქსიმალურ და მინიმალურ მნიშვნელობას და დაბეჭდეთ შედეგი (სიმრავლე შეარჩიეთ სურვილისამებრ).
setierti={12,123,243,6,8,9,343,56}
print(min(setierti))
print(max(setierti))

#8. შექმენით 2 სეტი, დაარქვით სასურველი სახელები და შეასრულეთ ნასწავლი მასალიდან 5 მეთოდის მაგალითი.
setiarmaxsovsromeli={12,123,243,6,8,9,343,56,4364643,345345345345,345345345345345,345345345345345,34534253452457788755,23423423423423423423234234,1}
setiarmaxsovsromeli1={123,1,69,12,23,555,667,85,34,435,23234,23456546,234}
print(setiarmaxsovsromeli.intersection(setiarmaxsovsromeli1))
print(setiarmaxsovsromeli.union(setiarmaxsovsromeli1))
print(setiarmaxsovsromeli1.difference(setiarmaxsovsromeli))
print(setiarmaxsovsromeli.isdisjoint(setiarmaxsovsromeli1))
print(setiarmaxsovsromeli.issubset(setiarmaxsovsromeli1))
#9.მომხარებელს შეაყვანინეთ 2 სიტყვა. დაბეჭდეთ ამ ორი სიტყვის ყველა საერთო ასო.
sityva1=set(input("input ur word : "))
sityva2=set(input("input ur 2nd word : "))
print(sityva1.intersection(sityva2))


