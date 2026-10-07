dictRooms=[
    {
        "Name":"Tori",
        "Desc":"Näet kauppiaan myymässä miekkaa, toisen myymässä lyhtyä. Tie johtaa kartanolle, jossa kreivi Hammark asuu. Torin rajalla sijaitsee alkemistin talo. Polut vievät suolle ja mäelle.",
        "Items":["Miekka", "Lyhty"],
        "Dest":["Alkemisti", "Suo", "Mäki", "Kartano"],
        "ReqItem":""
    },
    {
        "Name":"Alkemisti",
        "Desc":"Laboratorio, josta myydään tulipommeja. Sijainti on kivenheiton päässä torista. Polku johtaa suolle.",
        "Items":["Tulipommi"],
        "Dest":["Tori", "Suo"],
        "ReqItem":""
    },
    {
        "Name":"Suo",
        "Desc":"Saastainen suo mäen juurella, joka kuhisee parveittain hirviömäisiä ötököitä. Luita pilkottaa märästä maasta. Suon toisella puolella sijaitsee suohon vajonnut maja.Polut johtavat torille ja alkemistin laboratoriolle.",
        "Items":["Keppi"],
        "Dest":["Tori", "Alkemisti", "Maja", "Mäki"],
        "ReqItem":"Tulipommi",
        "FailDesc":"Korvia vihlova surina ympäröi sinut kun kuljet pidemmälle suota. Parvi koiran kokoisia hyttysiä saartaa sinut ja imevät sinut kuivaksi. Olet nyt uusin suolle jääneistä.",
        "SuccDesc":"Suon haju ei ole tulipommisi jäljiltä mielyttävämpi, mutta ötökät vaikenevat. Luita pilkottaa märästä maasta. Suon toisella puolella sijaitsee suohon vajonnut maja."
    },
    {
        "Name":"Maja",
        "Desc":"Ränsistynyt mökki on lähes kokonaan kadonnut suohon.",
        "Items":["Kruunu"],
        "Dest":["Suo"],
        "ReqItem":"Tulipommi"
    },
    {
        "Name":"Mäki",
        "Desc":"Kuiva kivinen mäki torin tuntumassa. Kallionseinämässä on luola, johon paikalliset kertovat katoavan karjaa. Suo on lähellä.",
        "Items":["Kivi"],
        "Dest":["Tori", "Suo", "Luola"],
        "ReqItem":""
    },
    {
        "Name":"Luola",
        "Desc":"Pimeän onkalon syvennyksestä kantautuu mädäntyvän lihan haju. Epälet kuulevasi hirviön raskasta hengitystä. Tunneli johtaa syvään luolaan",
        "Items":["Kivi"],
        "ReqItem":"Lyhty",
        "Dest":["Mäki", "Syvä luola"],
        "FailDesc":"Kompuroit kimeässä. Terävät päättävät seikkailusi ennen kun pääset takaisin jaloillesi.",
        "SuccDesc":"Lyhty valaisee limaisen tunnelin hirviön pesään. Epäilet kuulevasi hirviön raskasta hengitystä syvästä luolasta."
    },
    {
        "Name":"Syvä luola",
        "Desc":"Löydät itsesi kasvokkain suuren, limaisen peikon kanssa. Hän pudottaa edellisen ateriansa sivuun ja keskittää huomionsa sinuun.",
        "Items":["Kivi", "Valtikka"],
        "ReqItem":"Lyhty",
        "Dest":["Luola"],
        "FailDesc":"Käännät katseesi pois peikosta vain hetkeksi, ja päädyt hänen kitaan.",
        "SuccDesc":"Peikko on päihitetty."
    },
    {
        "Name":"Kartano",
        "Desc":"Kreivi Hamamrk ottaa sinut vastaan. Hän on utelias näkemään mitä olet löytänyt.",
        "Items":[],
        "Dest":["Tori"],
        "ReqItem":""
    },]