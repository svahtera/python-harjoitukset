#Lue luvut
import math

firstStr=input("Syötä ensimmäinen kokonaisluku: ")
secondStr=input("Syötä toinen kokonaisluku: ")
thirdStr=input("Syötä kolmas kokonaisluku: ")
first=int(firstStr)
second=int(secondStr)
third=int(thirdStr)

#Laskut
sum=first+second+third
product=first*second*third
average=sum/3

#Tulostus
print(f"{'Lukujen summa on '}{sum}{'.'}")
print(f"{'Lukujen tulo on '}{product}{'.'}")
print(f"{'Lukujen keskiarvo on '}{average}{'.'}")