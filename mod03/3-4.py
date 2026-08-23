#Lue luvut

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
if int(average)==average:
    print(f"{'Lukujen keskiarvo on '}{int(average)}{'.'}")
else:
    print(f"{'Lukujen keskiarvo on '}{average:.2f}{'.'}")