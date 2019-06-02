import sqlite3

con = sqlite3.connect('chatbt.db')
c = con.cursor()

# c.execute("INSERT INTO userdetails VALUES('%s','%s','%s','%s');" %('test','test123','some@some.com','10-02-19'))
# c.execute("INSERT INTO users VALUES('%s','%s');" %('test','test123'))

a = c.execute('select * from users')

for j,k in a:
    # print(j, k)
    if (j == 'jack' and k == 'sadkfjkaj'):
        print('hi')
        break
    else:
        pass

con.commit()
