url = input("Enter your URL: ")

if url.startswith("https://") or url.startswith("http://"):
    if url.endswith(".com") or url.endswith(".in") or url.endswith(".org"):
        print("Valid URL")
    else:
        print("Invalid URL")
else:
    print("Invalid URL")
