"""
collatz = int(input("Please enter firstnumbers of collatz sequence"))
list_collatz = []
list_collatz.append(collatz)
while collatz > 1:
    if collatz % 2 == 0:
        collatz = collatz // 2
        list_collatz.append(collatz)
    else:
        collatz = 3 * collatz + 1
        list_collatz.append(collatz)
print(list_collatz)
"""
"""
from timeit import timeit
def for_loop() :
    result = []
    for i in range(1000000) :
        result.append(i)
    return result
def list_comp():
    return [i for i in range(1000000)]

time1 = timeit(for_loop, number= 1000)
time2 = timeit(list_comp, number= 1000)
print(f"list compreshion is {round(time1/time2 , 2)} times fater than for_loop")
"""
"""
import smtplib
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls
server.login("bmdundar1989", "Erzincan24" )
message = "\n This is my test mail to distunguihed trainee. "
server.sendmail("bmdundar1989@gmail.com", "bmdundar1989@gmail.com", message )
"""
"""
pip install textblob
from textblob import TextBlob
yazi = "data science is one of the best paid professions "
blob = TextBlob(yazi)
blob_eng = blob.translate(to='tr')
blob_Hirvat = blob.translate(to='hr')
blob_Hind = blob.translate(to='hi')
blob_Ru = blob.translate(to='ru')
blob_Tr = blob.translate(to='tr')
"""