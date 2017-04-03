class MyEntity(db.Model):
    dictionary_string = db.StringProperty()

payload = {{}...{}}

# Store dict
fn = MyEntity(key_name=your_key_here)
my_entity.dictionary_string = str(payload)
my_entity.put()

# Get dict
import ast
my_entity_k = db.Key.from_path('MyEntity', your_key_here)
my_entity = db.get(my_entity_k)
payload = ast.literal_eval(my_entity.dictionary_string)