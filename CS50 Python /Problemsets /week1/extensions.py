# corresposing data type to file extensions

x = input("File Name: ").strip().lower()

if x.endswith( ".jpeg" ) or x.endswith(".jpg"):
        print("image/jpeg")
elif x.endswith(".gif"):
        print("image/gif")
elif x.endswith(".txt"):
        print("text/plain")
elif x.endswith(".png"):
        print("image/png")
elif x.endswith(".zip"):
        print("application/zip")
elif x.endswith(".pdf"):
        print("application/pdf")
else :
       print("application/octet-stream")
