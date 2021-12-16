#Allows us to store information in KEY, VALUE PAIRS
#Jan -> January
monthConversions = {
    "Jan": "Janurary",
    "Feb": "February",
    "Mar": "March", #Keys should be unique
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversions)
print(monthConversions["Nov"])
print(monthConversions.get("Dec"))
print(monthConversions.get("AAA", "Not a valid key"))