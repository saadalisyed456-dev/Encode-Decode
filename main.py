import base64
text="python codding"
encoded=base64.b64encode(text.encode())
print("Encoded:",encoded)
decoded=base64.b64decode(encoded).decode()
print("Decoded:",decoded)