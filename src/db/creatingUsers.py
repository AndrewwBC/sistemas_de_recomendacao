from faker import Faker
import query
fake = Faker()

print(fake.name())

# username email password age

for x in range(1001):
    values = [fake.uuid4(),fake.user_name(), fake.email(), fake.password(), fake.random_number()]
    query.createQuery(f"""
                      INSERT INTO users(user_id, username, email, password, age)
                      VALUES(%s, %s, %s, %s, %s) RETURNING *
                      """, values)
    x = x + 1
