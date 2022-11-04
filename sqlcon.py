import mysql.connector as c
con=c.connect(host="localhost",
              user="root",
              passwd="",
              database="event")
cursor=con.cursor()
while True:
    id=int(input("enter participants id:"))
    name=input("enter participants name:")
    addr=input("enter participant address:")
    query="Insert into participants values({},'{}','{}')".format(id,name,addr)
    cursor.execute(query)
    con.commit()
    print("Data inserted successfully...")
    x=int(input("1->Enter More\n2->Exit\nEnter choice:"))
    if x==2:
        break
query="update participants set name='jay' where id=2"
cursor.execute(query)   
con.commit()
print("Data updated successfully...")
print()
query="delete from participants where name='Sham'"
cursor.execute(query)   
con.commit()
print("Data deleted successfully...")
print()
