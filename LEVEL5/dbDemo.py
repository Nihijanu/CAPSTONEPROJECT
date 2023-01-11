import sqlite3
connect =sqlite3.connect("c://sqllite//hcl.db")
cur=connect.cursor()
# sql="""insert into filelog values(?,?);"""
# data=(100,'c://Users//user653//demo.txt')
# cur.execute(sql,data)
# connect.commit()
cur.execute("select *from filelog where id = 100");
rows=cur.fetchall()
for r in rows:
    print(r)