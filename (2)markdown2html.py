
if __name__ == "__main__":
    import sys
    import os

    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html")
        exit(1)
    if os.path.exists(sys.argv[1]) == False:
        print("Missing {}".format(sys.argv[1]))
        exit(1)
  
    else:
 
        template = {"1": "<h1>", "2": "<h2>", "3": "<h3>", "4": "<h4>", "5": "<h5>", "6": "<h6>", "-": "<li>"}
        with open(sys.argv[1], 'r') as f:
            for line in f:
                with open(sys.argv[2], 'a') as html_file:
                    count = line.count("#")
                    count = str(count)
                    for k, v in template.items():
                        if count == k:                            
                            l = v + line.strip("#, \n") + "</" + v.strip("<") + "\n"
                            html_file.write(l)
                        if line[0] == k:
                            l = "<ul>\n" + v + line[1:-1] +  v.replace("<", "</") + "\n</ul>"
                            html_file.write(l)
        exit(0)
