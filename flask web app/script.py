import untangle
from datetime import datetime
import json


File = "Datafile.xml"

data = untangle.parse(File)

tall = input("Type a numer: ")

if tall == "1":

    """Henter ut alle caser med id, tittel og dato"""

    for case in data.cvrfdoc.Vulnerability:
                Title = case.Title.cdata
                date = case.Notes.Note[1].cdata
                id = case['Ordinal']
                print("Case with ID:", id, "and title:", Title, "was registrated", date)


    
elif tall == "2":

    """""Henter ut data for en spesifik dato"""

    brukerdato = input("Type your desired date: ")

    for case in data.cvrfdoc.Vulnerability:
        date1 = case.Notes.Note[1].cdata
        id1 = case['Ordinal']

        if id1 == brukerdato:
            print("ID", id1, "was registred", date1)

elif tall =="3":

    """""Henter ut data mellom 2 spesifike datoer"""

    #date_formate = "%Y-%m-%d"

    sDate = input("search from date (year/month/day): ")
    eDate = input("to date (year/month/day): ")

    #aStart = datetime.strptime(sDate, date_formate)
    #bEnd = datetime.strptime(eDate, date_formate)



    for case in data.cvrfdoc.Vulnerability:
        date2 = case.Notes.Note[1].cdata
        id2 = case['Ordinal']

        if sDate <= date2 <= eDate:
            print("ID", id2, "was registred", date2)

elif tall == "4":
        


        """""Henter ut all data med id, dato og tittel. skipper dersom case ikke har dato og teller totale data hentet ut."""
        liste = 0
        for case in data.cvrfdoc.Vulnerability:
                if not case.Notes.Note[1]:
                      pass
                else:
                    Title3 = case.Title
                    date3 = case.Notes.Note[1].cdata
                    id3 = case['Ordinal']
                    liste = liste+1
                    JsonListe = {
                          "id": id3,
                          "date": date3}

                    with open ("2017.json", "a") as outfile1:
                          json.dump(JsonListe,outfile1)
                          outfile1.write("\n")
        
        print(liste)


