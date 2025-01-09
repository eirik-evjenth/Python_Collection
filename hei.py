with open("hei.txt", "a") as f:
    try: 
        while True: 
            f.write("https://www.mozilla.org/nb-NO/firefox/new/\n")
    except KeyboardInterrupt:
        print("Finished writing")

quit()