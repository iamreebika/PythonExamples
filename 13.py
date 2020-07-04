from builtins import list, open, csv

persons=[{'name':'Lata', 'age':22, 'marks':45}, {'name':'Anil', 'age':21, 'marks':56}, {'name':'John', 'age':20, 'marks':60}]
csvfile=open('persons.csv','w', newline='')
fields=list(persons[0].keys())
obj=csv.DictWriter(csvfile, fieldnames=fields)
obj.writeheader()
obj.writerows(persons)
csvfile.close()
