import pymongo
import certifi 


con_str="mongodb+srv://kyleparker:123456714@cluster0.6tfmrdz.mongodb.net/?retryWrites=true&w=majority"


client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())


db=client.get_database("OrganikaStore")