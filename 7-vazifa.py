keys = ["name", "description", "title", "keywords", "content", "charset"]
values = ["document", "The best document", "My document", "doc, word, excel", "None"]

result = {k: v for k, v in zip(keys, values)}

print(result)