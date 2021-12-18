#Giraffe Language
#Vovels -> g
#------------------
#dog -> dgg
#cat -> cgt

#make function
def translate(phrase):
    translation = ""
    for i in phrase:
        if i in "AEIOUaeiou": #newwwww
        #if i.lower in "aeiou": #newwwww    
            translation = translation + "g"
        else:
            translation = translation + i
    return translation

print(translate(input("Enter a phrase: ")))


'''
yeye
yeee
yee
'''