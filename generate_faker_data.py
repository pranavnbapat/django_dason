from faker import Faker
import pymysql

# Database connection parameters
db_host = ""
db_user = ""
db_password = ""
db_name = ""
db_port = ""

connection = pymysql.connect(host=db_host, user=db_user, password=db_password, database=db_name, port=db_port)

fake = Faker()

# Define the number of records
record_count = 1000000


def get_long_description():
    paragraphs = []
    while len(" ".join(paragraphs)) < 5000:
        paragraphs.append(fake.paragraph())
    return " ".join(paragraphs)[:5000]


def get_keywords():
    return ",".join(fake.words(nb=10, unique=True))


with connection.cursor() as cursor:
    j = 1
    for i in range(record_count):
        row_id = j
        j += 1
        description = get_long_description()
        keywords = get_keywords()
        status = 1
        deleted = 0
        deleted_at = None
        created_at = fake.date_time_this_decade()
        updated_at = created_at

        insert_query = "INSERT INTO faker_model (id, keywords, description, status, deleted, deleted_at, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(insert_query, (row_id, keywords, description, status, deleted, deleted_at, created_at, updated_at))

    connection.commit()

print(f"Inserted {record_count} records into the faker_model table")

# Close the connection
connection.close()
