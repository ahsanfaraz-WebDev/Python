letter = '''  
Dear <|Name|>, 
You are selected! 
<|Date|> 
''' 
print(
letter.replace("<|Name|>","Ahsan").replace("<|Date|>", "01 March 2025"))