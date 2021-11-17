from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.id = data["id"]
        self.dojo_id = data["dojo_id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas"
        results = connectToMySQL("dojos_and_ninjas").query_db(query)


        ninjas = []
        for row in results:
            ninjas.append(Ninja(row))
        return ninjas


    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM ninjas WHERE id  = %(id)s"
        results = connectToMySQL("dojos_and_ninjas").query_db(query, data)
        if len(results) == 0:
            return False
        return Ninja(results[0])


    @classmethod
    def create(cls, data):
        query = "INSERT INTO ninjas (dojo_id, first_name, last_name, age, created_at, updated_at) VALUES(%(dojo_id)s, %(first_name)s, %(last_name)s, %(age)s, NOW(), NOW());"
        return connectToMySQL("dojos_and_ninjas").query_db(query, data)


    @classmethod
    def update(cls, data):
        query = "UPDATE ninjas SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s, updated_at = NOW() WHERE id = %(id)s"
        results = connectToMySQL("dojos_and_ninjas").query_db(query, data)
        return results


    @classmethod
    def delete(cls, data):
        query = "DELETE FROM ninjas WHERE id = %(id)s"
        connectToMySQL("dojos_and_ninjas").query_db(query, data)