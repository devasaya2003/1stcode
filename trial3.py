print('''
 ____  ____  _  _  __    ___    __   _  _   __   
(  _ \( ___)( \/ )/__\  / __)  /__\ ( \/ ) /__\           ^ ^
 )(_) ))__)  \  //(__)\ \__ \ /(__)\ \  / /(__)\  Hello!!  *
(____/(____)  \/(__)(__)(___/(__)(__)(__)(__)(__)         \_/

''')
print("IP\t\t Date Time\t\t  Request")

with open("website.log","r") as f:
    lines= f.readlines()
with open("output.txt",'w+') as nf:
    for line in lines:

        line = line.split(" ")
        nf.write(

            "{}\t {}\t {}\n".format(line[0], line[3].replace('[',''), line[5].replace('"',' '))

            )

