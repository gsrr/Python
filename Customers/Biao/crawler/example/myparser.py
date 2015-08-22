





def kmdn_news(data):
    for line in data:
        if "linkTitle" in line:
            print line
        if "lblDepartment" in line:
            print line
        if "lblReleaseDate" in line:
            print line
