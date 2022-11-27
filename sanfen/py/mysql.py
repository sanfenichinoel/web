
import pymysql

class Mysql():
    def __init__(self) -> None:
        self.db = pymysql.connect(
                host='localhost',
                user='root',
                password='**********',
                database='sanfen_markdown'
            )
        self.cursor = self.db.cursor()

    def __del__(self) -> None:
        self.db.close()

    def select_all_data(self):
        """
        查询所有数据
        """

        sql = """
            select * from files
            order by create_time desc;
            """
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            return results
        except:
            return False

    def insert(self, name:str, time:str, url:str):
        """
        插入数据
        """

        sql = """
            insert into files
            values
            ("{}", "{}", "{}");
        """.format(name, time, url)

        try:
            self.cursor.execute(sql)
            self.db.commit()
            return True
        except:
            self.db.rollback()
            return False

    def update(self, name:str, time:str, url:str):
        """
        修改
        """
        pass

    def delete(self, url:str):
        """
        删除
        """

        sql = """
            delete from files
            where name = "{}";
        """.format(url)

        try:
            self.cursor.execute(sql)
            self.db.commit()
            return True
        except:
            self.db.rollback()
            print(sql)
            return False


# if __name__ == "__main__":
#     sql = Mysql()
    
#     ok = sql.delete("heep")
#     if not ok:
#         print("loss")

#     sql.select_all_data()

