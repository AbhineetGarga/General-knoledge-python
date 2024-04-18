s= "Abhineet is a good boy"

with open("hendling.txt","w") as f:
    f.write(s)
    # f.read(s)


#same thing as
# fp= open("hendling.txt","w")
# fp.write(s)
# fp.close()


#Reading file

with open("abhineet.txt","r") as f:
    s=f.read()
    print(s)


#same thing as
# fp= open("hendling.txt","r")
# fp.read(s)
# fp.close()



# 3rd way ia append  write as a "a"

with open("hendling.txt","a") as f:
    f.write("asmsdhjgghvehfhbhfgyewfteyhjehja")
    # f.read(s)


#same thing as
# f= open("hendling.txt","a")
# f.write(s)
# f.close()