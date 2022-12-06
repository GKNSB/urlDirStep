## urlDirStep

Receives URLs as stdin that have some directory strucutre. For instance http://example.com/dir1/dir2 and breaks this down to seperate urls for each directory step returned as stdout.

Examples:
```
$ echo "http://asdf.qwer.dd/qqq/aaa/zzz/" | urlDirStep.py
http://asdf.qwer.dd/
http://asdf.qwer.dd/qqq/
http://asdf.qwer.dd/qqq/aaa/
http://asdf.qwer.dd/qqq/aaa/zzz/

$ echo "http://asdf.qwer.dd/dir1/dir2/dir3/dir4" | urlDirStep.py
http://asdf.qwer.dd/
http://asdf.qwer.dd/dir1/
http://asdf.qwer.dd/dir1/dir2/
http://asdf.qwer.dd/dir1/dir2/dir3/
http://asdf.qwer.dd/dir1/dir2/dir3/dir4/
```

Help:
```
$ urlDirStep.py -h
> Use with URLs in stdin
> URLs should end with the last directory
> examples:
    echo "http://asdf.qwer.dd/qqq/aaa/zzz/" | urlDirStep.py
    echo "http://asdf.qwer.dd/dir1/dir2/dir3" | urlDirStep.py
    cat urls.txt | urlDirStep.py
```
