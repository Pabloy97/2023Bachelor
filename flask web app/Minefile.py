import untangle
from datetime import datetime



File = "Kortfil.xml"

data = untangle.parse(File)

tall = input("Type a number: ")

# Function to get all entires of a specific year, month or date based on the user inputs
if tall == "1":
   
    DateInput = input("search from date (year/month/year) you can choose what to fill in:")
    
    
    for case in data.cvrfdoc.Vulnerability:
        Title = case.Title.cdata
        # Collect the node with the published date
        date = case.Notes.Note[1].cdata
        # Set the id
        id1 = case['Ordinal']
        # Create if loops to iterate through the publihed dates in different spliced areas to check for Year-month-day, Year-Month or Year given by the user.
        if DateInput == date[:4]:
            print("Case with ID:", id1, "and title:", Title, "was registrated", date)

        elif DateInput == date[:7]:
            print("Case with ID:", id1, "and title:", Title, "was registrated", date)
        
        elif DateInput == date:
            print("Case with ID:", id1, "and title:", Title, "was registrated", date)