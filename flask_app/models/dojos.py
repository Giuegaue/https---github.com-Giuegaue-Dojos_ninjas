from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models.ninjas import Ninja


class Dojo:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.ninjas = []


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos"
        results = connectToMySQL("dojos_and_ninjas").query_db(query)


        dojos = []
        for row in results:
            dojos.append(Dojo(row))
        return dojos


    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s"
        results = connectToMySQL("dojos_and_ninjas").query_db(query, data)
        if len(results) == 0:
            return False
        dojo = Dojo(results[0])

        if results[0]["ninjas.id"] != None:
            for row in results:
                ninjaData = {
                    **row,
                    "id": row['ninjas.id'],
                    "dojo_id": row['dojo_id'],
                    "created_at": row['created_at'],
                    "updated_at": row['updated_at']
                }
                print(ninjaData)
                dojo.ninjas.append(Ninja(ninjaData))

        return dojo


    @classmethod
    def create(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES(%(name)s, NOW(), NOW());"
        results = connectToMySQL("dojos_and_ninjas").query_db(query, data)
        return results


    @classmethod
    def update(cls, data):
        query = "UPDATE dojos SET name = %(name)s = )s, updated_at = NOW() WHERE id = %(id)s"
        results = connectToMySQL("dojos_and_ninjas").query_db(query, data)
        return results


    @classmethod
    def delete(cls, data):
        query = "DELETE FROM dojos WHERE id = %(id)s"
        connectToMySQL("dojos_and_ninjas").query_db(query, data)