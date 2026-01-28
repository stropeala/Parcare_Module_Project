from clients import clients

"""
Pentru a fi mai usor de aplicat si de inteles singurele modificari pe care le am facut de cerinta sunt:
    in loc de 72 de ore am limitat timpul la 10 secunde

    in json uri la timp, 1 sec este echivalenta cu o ora

    clientii care stau mai putin sau egal cu 3 secunde sunt cei care stau "sub 2 ore" in parcare:
        timp <=3 sec => 2 hr

    clientii care stau intre 3 si 7 secunde sunt cei care "depasesc 2 ore":
        3 sec < timp < 7 sec => 2+ ore

    clientii care stau peste 7 secunde sunt cei care stau "3 zile":
        7 sec <= timp => 3 zile

    clientii care au depasit 7 secunde a.k.a. "3 zile" li se va schimba pariah din False in True

In rest totul este exact ca si in cerinta de la proiect (sper)
Avem deja 10 clienti gata sortati, daca dam run la main, acest va mai adauga 10 si ii va sorta
La final vom avea 20 de clienti toti dortati frumos la locul lor

Am incercat sa explic cat mai bine tot ce am facut
Sper ca o sa intelegeti, nu sunt cel mai bun la limba romana :)

In drafts sunt toate ciornele mele, nothing important
"""

if __name__ == "__main__":
    clients(
        "JSON/data/clients.json",
        "Lynn",
        "Newton",
        "(206) 342-8631",
        "Seattle, WA",
    )
    clients(
        "JSON/data/clients.json",
        "Genaro",
        "Willis",
        "(717) 550-1675",
        "Harrisburg, PA",
    )
    clients(
        "JSON/data/clients.json",
        "Rosanne",
        "Maldonado",
        "(248) 762-0356",
        "Farmington Hills, MIV",
    )
    clients(
        "JSON/data/clients.json",
        "Pauline",
        "Figueroa",
        "(253) 644-2182",
        "Auburn, WA",
    )
    clients(
        "JSON/data/clients.json",
        "Rickey",
        "Clements",
        "(212) 658-3916",
        "New York City, NY",
    )
    clients(
        "JSON/data/clients.json",
        "Jeanne",
        "Wolf",
        "(209) 300-2557",
        "Ceres, CA",
    )
    clients(
        "JSON/data/clients.json",
        "Dustin",
        "Carrillo",
        "(262) 162-1585",
        "Menomonee Falls, WI",
    )
    clients(
        "JSON/data/clients.json",
        "Sally",
        "Reeves",
        "(252) 258-3799",
        "Greenville, NC",
    )
    clients(
        "JSON/data/clients.json",
        "Jaclyn",
        "Andersen",
        "(234) 109-6666",
        "Akron, OH",
    )
    clients(
        "JSON/data/clients.json",
        "Esteban",
        "Shelton",
        "(201) 874-8593",
        "Bayonne, NJ",
    )
