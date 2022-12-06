#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
	if sys.argv[1] ==  "-h":
		print("> Use with URLs in stdin")
		print("> URLs should end with the last directory")
		print("> examples:")
		print("    echo \"http://asdf.qwer.dd/qqq/aaa/zzz/\" | urlDirStep.py")
		print("    echo \"http://asdf.qwer.dd/dir1/dir2/dir3\" | urlDirStep.py")
		print("    cat urls.txt | urlDirStep.py")
		exit(0)

for line in sys.stdin:
	inputLine = line.strip("\n")

	if inputLine.endswith("/"):
		inputLine = inputLine[:-1]

	try:
		parts = inputLine.split("/")
		base = f"{parts[0]}//{parts[2]}/"

		urls = [base]

		for i in range(3, len(parts)):
			base = f"{base}{parts[i]}/"
			urls.append(base)

		for url in urls:
			sys.stdout.write(f"{url}\n")

	except Exception:
		pass
		#sys.stdout.write(f"Something went wrong... Input: {line}\n")
