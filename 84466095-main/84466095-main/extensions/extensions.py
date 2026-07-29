n=input("file name: ").lower().strip()
if n.endswith(".jpg") or n.endswith(".jpeg"):
    print("image/jpeg")
elif n.endswith(".pdf"):
    print("application/pdf")
elif n.endswith(".txt"):
    print("text/plain")
elif n.endswith(".zip"):
    print("application/zip")
elif n.endswith(".gif"):
    print("image/gif")
elif n.endswith(".png"):
    print("image/png")
else:
    print("application/octet-stream")

