# "\n" is new line
print("Kamala Niketan\nMontessori School")

# "\"" is used for '"', \ is the escape character
print("Kamala Niketan\"Montessori School")

# \ is put in directly
print("Kamala Niketan\Montessori School")

phrase = "Kamala Niketan Montessori School"
print(phrase + " is cool") #Kamala Niketan Montessori School is cool
print(phrase.lower()) #kamala niketan montessori school
print(phrase.isupper()) #False 
print(phrase.upper().isupper()) #True
print(len(phrase)) #32
print(phrase[0]) #K
print(phrase[3]) #a
print(phrase.index("M")) #15
print(phrase.replace("School", "College")) #Kamala Niketan Montessori College