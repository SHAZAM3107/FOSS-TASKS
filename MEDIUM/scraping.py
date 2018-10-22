from googlesearch import search
query=input("what do you want to search\n")
query=query.split()
for i in range(0,len(query)):
        
        for j in search((query[i]), tld='com', num=20, stop=1, pause= 10):
                print(j)
