dictRooms=[
    {
        "Name":"Tori",
        "Desc":"Tori jossa voit ostaa esineitä",
        "Items":["Miekka", "Lyhty"],
        "Dest":["Alkemisti", "Suo", "Mäki", "Kartano"]
    },
    {
        "Name":"Alkemisti",
        "Desc":"Laboratorio, josta myydään tulipommeja.",
        "Items":["Tulipommi"],
        "Dest":["Tori", "Suo"]
    },
    {
        "Name":"Suo",
        "Desc":"Saastainen suo, joka kuhisee hirviömäisiä hyönteisiä. Käytä tulipommia täällä.",
        "Items":["McGuffin 1"],
        "Dest":["Tori", "Alkemisti"]
    },
    {
        "Name":"Mäki",
        "Desc":"Kuiva mäki, josta tarinat kertovat asuvan epätavallisen kokoisia rottia. Maassa lojuu kiviä.",
        "Items":["Kivi"],
        "Dest":["Tori", "Luola"]
    },
    {
        "Name":"Luola",
        "Desc":"Pimeä onkalo. Pimeydestä kuuluu olentöjen vikinää.",
        "Items":["Kivi"],
        "Dest":["Mäki", "Syvemmälle"]
    },
    {
        "Name":"Syvä Luola",
        "Desc":"Pimeä onkalo. Pimeydestä kuuluu olentöjen vikinää.",
        "Items":["Kivi"],
        "ReqItem":"Lyhty",
        "FailDesc":"Kompuroit kimeässä. Terävä veitsi päättää seikkailusi ennen kun pääset takaisin jaloillesi.",
        "Dest":["Mäki", "Syvemmälle"]
    },
    {
        "Name":"Testitila",
        "Desc":"Muodoton testitila",
        "Items":["Tt-33"],
        "Dest":["Tori"]
    }
]