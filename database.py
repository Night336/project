import sqlite3
import yaml
from yaml.loader import SafeLoader

# получение первой записи
# one_result = cur.fetchone()

# получение нескольких записей
# three_results = cur.fetchmany(3)

# получить все записи
# all_results = cur.fetchall()

class Database:
    def __init__(self, path):
        self.conn = sqlite3.connect(path)
        self.cur = self.conn.cursor()

    def player_is_exist(self, name):
        self.cur.execute("SELECT * FROM players where name=?;", (name,))
        return bool(self.cur.fetchone())

    def get_player_id(self, name):
        self.cur.execute("SELECT * FROM players where name=?;", (name,))
        res = self.cur.fetchone()
        if res:
            return res[0]

    def delete_saves(self, player_id):
        query = """ 
                DELETE FROM saves
                WHERE saves.player_id = ?
                """
        self.cur.execute(query, (player_id,))
        self.conn.commit()

    def save_is_exist(self, name):
        query = """ 
        SELECT * FROM saves
        LEFT JOIN players
            ON players.id = saves.player_id
        WHERE players.name = ?
        ORDER BY saves.id DESC
        """
        self.cur.execute(query, (name,))
        print(self.cur.fetchall())
        return False

    def add_player(self, name):
        self.cur.execute("INSERT INTO players(name) VALUES(?);", (name,))
        self.conn.commit()

    def save_from_player(self, name):
        id = self.get_player_id(name)
        print(id)
        self.cur.execute("SELECT lvl, hp, damage FROM saves where player_id=?;", (id,))
        res = self.cur.fetchone()
        return res

    def add_saving(self, lvl, hp, player_id, damage):
        self.cur.execute("SELECT * FROM players where id=?;", (player_id,))
        one_result = self.cur.fetchone()
        if one_result:
            print('Сохранение созданно')
            self.cur.execute("INSERT INTO saves(lvl, hp, player_id, damage) VALUES(?, ?, ?, ?);",
                             (lvl, hp, player_id, damage))
            self.conn.commit()
        else:
            print('Игрок не сущетсвует')

    def update_save(self, save_id, lvl, hp, damage):
        self.cur.execute("SELECT * FROM saves where id=?;", (save_id,))
        one_result = self.cur.fetchone()
        if one_result:
            print('обновляем сохранение')
            self.cur.execute("UPDATE  saves SET lvl = ?, hp = ?, damage = ? WHERE id = ?;",
                             (lvl, hp, damage, save_id))
            self.conn.commit()
        else:
            print('Сохранения не существует')

if __name__ == "__main__":
    db = Database('data/database/db.db')
    print(db.get_player_id('sdf'))
# db.add_saving(5, 5, 2, 5)
# db.save_is_exist('Петя')

# with open('config.yaml', 'r', encoding="utf-8") as f:
#     data = list(yaml.load_all(f, Loader=SafeLoader))[0]
#     player_name = data['current_player']
#     db = Database('data/database/db.db')
#     if player_name and db.player_is_exist(player_name):
#         print("игрок найден выполняем загрузку")
#     else:
#         print("игрок не найден выполняем создание нового")
#         print('записываем в файл config')
# db.update_save(1, 10, 10, 10)