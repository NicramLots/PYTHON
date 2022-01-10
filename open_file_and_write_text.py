with open ("C:\OTHER\DEV\PYTHON\misc.txt","a") as o:
    o.write("Hello")
    o.write("\nJust adding some stuff into the file")

with open("C:\OTHER\DEV\PYTHON\misc.txt", "w") as external_file:
    add_text = "This text will be added to the file"
    print(add_text, file=external_file)
    external_file.close()
