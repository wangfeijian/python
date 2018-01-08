text = "Bananas, give me bananas!!!"
words = {"banana", "bananas"}
test_text = text.lower()
num = 0
for i in words:
    if i in test_text:
        num += 1
            
print(num)
