import os

from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.errors import PyMongoError
from pymongo.server_api import ServerApi

load_dotenv()

MONGO_USER = os.environ["MONGO_USER"]
MONGO_PASS = os.environ["MONGO_PASS"]
APP_NAME = os.environ["APP_NAME"]


# Connecting to the database
def get_database():
    uri = f"mongodb+srv://{MONGO_USER}:{MONGO_PASS}@cluster0.wn4nl.mongodb.net/?retryWrites=true&w=majority&appName={APP_NAME}"
    client = MongoClient(uri, server_api=ServerApi("1"))
    database = client.book
    return database


# Creating a document (Create)
def create_cat(db, name, age, features):
    try:
        result = db.cats.insert_one({"name": name, "age": age, "features": features})
        print(f"Cat created with ID: {result.inserted_id}")
    except PyMongoError as e:
        print(f"Error creating document: {e}")


# Reading all documents (Read all)
def read_all_cats(db):
    try:
        cats = db.cats.find()
        for cat in cats:
            print(cat)
    except PyMongoError as e:
        print(f"Error reading documents: {e}")


# Reading a single document by name (Read by name)
def read_cat_by_name(db, name):
    try:
        cat = db.cats.find_one({"name": name})
        if cat:
            print(cat)
        else:
            print(f"Cat with name '{name}' not found.")
    except PyMongoError as e:
        print(f"Error reading document: {e}")


# Updating cat's age by name (Update age)
def update_cat_age(db, name, new_age):
    try:
        result = db.cats.update_one({"name": name}, {"$set": {"age": new_age}})
        if result.modified_count > 0:
            print(f"Cat's age '{name}' updated.")
        else:
            print(f"Cat with name '{name}' not found.")
    except PyMongoError as e:
        print(f"Error updating cat's age: {e}")


# Adding a new feature (Update feature)
def add_feature_to_cat(db, name, feature):
    try:
        result = db.cats.update_one({"name": name}, {"$push": {"features": feature}})
        if result.modified_count > 0:
            print(f"Feature added to cat '{name}'.")
        else:
            print(f"Cat with name '{name}' not found.")
    except PyMongoError as e:
        print(f"Error adding feature: {e}")


# Deleting a cat by name (Delete by name)
def delete_cat_by_name(db, name):
    try:
        result = db.cats.delete_one({"name": name})
        if result.deleted_count > 0:
            print(f"Cat with name '{name}' deleted.")
        else:
            print(f"Cat with name '{name}' not found.")
    except PyMongoError as e:
        print(f"Error deleting cat: {e}")


# Deleting all cats (Delete all)
def delete_all_cats(db):
    try:
        result = db.cats.delete_many({})
        print(f"Deleted {result.deleted_count} cats.")
    except PyMongoError as e:
        print(f"Error deleting all documents: {e}")


if __name__ == "__main__":
    db = get_database()

    # Adding cats
    create_cat(db, "barsik", 3, ["wears slippers", "allows petting", "ginger"])
    create_cat(db, "murzik", 5, ["likes to play", "gray", "loud purr"])

    # Reading all records
    print("\nAll cats:")
    read_all_cats(db)

    # Searching for a cat by name
    print("\nSearching for cat by name 'barsik':")
    read_cat_by_name(db, "barsik")

    # Updating cat's age
    print("\nUpdating cat's age 'barsik':")
    update_cat_age(db, "barsik", 4)

    # Adding a new feature
    print("\nAdding a new feature to cat 'barsik':")
    add_feature_to_cat(db, "barsik", "loves fish")

    # Deleting a cat by name
    print("\nDeleting cat 'murzik':")
    delete_cat_by_name(db, "murzik")

    # Deleting all records
    print("\nDeleting all cats:")
    delete_all_cats(db)
