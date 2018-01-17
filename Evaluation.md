
1. Did it work?

    So the basic functionality for the program definitely works. However, there are a few snags. Firstly, it's pretty dependant 
    on the actual encoding of the text file. In the Java version, I used ASCII codes, and so obviously the program would only work
    with ANSI-encoded text. When I switched over to Python, I changed to using a string of printable characters. The thing is, the Python
    version STILL only works with ANSI because of the way it streams files-- it'll read files in as ANSI unless otherwise specified, and
    since there's no good way to guess what the encoding of a text file is just based on its contents, I just decided to let the user know
    to encode their text files with ANSI. Apparently, UTF-8 is superior but since ANSI is the Windows default, I just coded for that. It'd
    probably be best to add functionality to create a backup of the user's data, since their data is lost if they try any other file encoding,
    but that would kinda undermine the whole point of the program. So the code is ready somewhere on my computer, but I didn't release it.
    
    Secondly, I had originally intended this to be a program running off of a Raspberry Pi, but I guess I didn't understand the capabilities
    of the system very well. My original vision for this project was a discrete little box you could plug a USB into, and all your .txt files
    would come out as gibberish. The thing is, Raspberry Pis are kind of expensive and don't include batteries, and even then the battery wouldn't
    last very long. Long story short, I decided to adapt the program to any computer. As it is, it searches the directory it was run from and encrypts
    (or tries to) encrypt all the .txt files. I think if I ever got my hands on a Raspberry Pi, I could still program it to work. I'd just need
    the script running constantly, and I'd just detect and search new directories constantly. That would take a lot of power, though, and I don't
    think anybody would keep an Encrypter box plugged in all the time, just sucking power.
    
2. Does it address the criteria for success?

    Okay, so all the Java (and Python) mastery elements from CS20 are here, just in a different form from what I first expected. The essential
    features all work, so that's a success. Given an actually Raspberry Pi device, I'm sure I could've finished all the nice-to-haves as well.
    Overall, the program works as intended, even though there are some unforseen limitations.
    
3. Did it work for some data sets, but not others?
    
    Yeah so as mentioned above, it only works when reading ANSI files. In the Python version, it's actually not a flaw of coding, like
    it is in my Java version. It's because to support different encodings, I'd have to detect those encodings. Since there's actually
    no good way of doing this for any given text file, it's better just to tell people to encode in ANSI. It's not hard, after all.
    One thing that the program doesn't support is HTML characters, actually. So, things like the right side apostrophe, or the left side
    apostrophe, or other weird internet-formatting characters like that. It's because HTML characters aren't in the regular printable
    charset, so my program doesn't cover them. I can think of at least two ways to fix that, though.
    
4. Does the program have any limitations in its current form?

    Well, I don't want to sound like a broken record with the encoding thing, but that's about it. Oh, and the data loss when someone
    doesn't follow the instructions and tries to encrypt a file with some other encoding. I could always make backups, but again, that would
    compromise security. 

5. What additional features could the program have?
    
    So there's one way I'd recode my program to make it better, and that would be to go through every text file and create a seed
    containing only the necessary characters. This way, the program would support those pesky HTML characters as well. The second
    feature I think it should have is a log? Like if anything goes wrong, the program would record it and let you know. I don't really
    know how to log properly though, so I've stayed away from it so far. The last thing I'd want to do is to obfuscate the code. Like,
    that's pretty important for a cryptography program. In Python 3, obfuscation is actually pretty easy. You can use whitespace characters
    and non-unicode characters to obfuscate, which really makes your code look like a huge mess. Obviously, I've left it unobfuscated
    here because it probably would be good for my grade if you could actually read the stuff.
    
6. Was the initial design appropriate?

    Well, after actually coding it, the program isn't as large or complicated as I had originally thought. I think a large part
    of the appeal was making it work with a Raspberry Pi. I was never actually able to acquire one so that kinda sucked. I'm
    pretty happy with how the program turned out, however, because it's actually useful to some degree. Originally, I didn't
    think I'd have to learn a whole new coding language for it, but I'm glad I did because I'm liking Python a lot more than
    I liked Java when I first started.
