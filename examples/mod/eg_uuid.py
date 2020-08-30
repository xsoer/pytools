import uuid

print(uuid.uuid1())

# print(uuid.uuid3('namespace', 'name'))

print(uuid.uuid4())
print(uuid.uuid4().hex)

print(uuid.uuid5('filename', 'name'))