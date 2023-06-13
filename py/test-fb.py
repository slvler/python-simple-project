import pymysql.cursors

connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password="",
                             database='test',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


cursorObj = connection.cursor()

try:
    #query = "create table Book(id INT, name VARCHAR(50))"
    #query = "insert into Book(id,name) values (1,'naber')"
    query = "select * from Book"
    cursorObj.execute(query)
    result = cursorObj.fetchone()
    print(result)
    #connection.commit()
    print('table created')
except:
    print('table not created error')