
s = "help4code is a best platformfor practicing programming"
print(s.find("help4code"))
print(s.find("python")) # python does not exist therfore -1
print(s.find("programming")) # 0 se ja tk programming ka starting character aayega that is 43


s = "nishika","bhavika","arpita"
m = '|'.join(s)
print(m)


s = "python is a High Level Programming language"
print(s.lower()) # LOWERCASE FOR ALL
print(s.upper()) # uppercase for all
print(s.swapcase()) # lower upper ho jayega and upper lower me
print(s.title()) # initial letter of each word will get capital
print(s.capitalize()) # only the 1st initial of the sentence will get capital