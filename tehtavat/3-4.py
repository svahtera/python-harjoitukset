#Lue luvut
import math

first=int(input("Syötä ensimmäinen kokonaisluku: "))
second=int(input("Syötä toinen kokonaisluku: "))
third=int(input("Syötä kolmas kokonaisluku: "))

#Laskut
sum=sum((first,second,third))
product=first*second*third
average=sum/3

#Tulostus
print(f"{'Lukujen summa on '}{sum}{'.'}")
print(f"{'Lukujen tulo on '}{product}{'.'}")
print(f"{'Lukujen keskiarvo on '}{average:.2f}{'.'}")