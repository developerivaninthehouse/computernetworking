def computer_networking_python1(questions)
    try:
        if questions == "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?":
            answer = "mtls"
        elif questions == "Are encoding and encryption the same? - Yes/No":
            answer = "No"
        elif questions == "Is it possible to decrypt a message without a key? - Yes/No":
            answer = "No"
        elif questions == "Is it possible to decode a message without a key? - Yes/No":
            answer = "Yes"
        elif questions == "Is a hashed message supposed to be un-hashed? - Yes/No":
            answer = "No"
        elif questions == "What is the SHA1 hashing value to the following message: 'NYU Computer Networking' - Use SHA1 hash generator and use the answer in your code":
            answer = "8496abe9fceb5aa927e28bfbd9a2347d1290ef9b"
        elif questions == "Is MD5 a secured hashing algorithm? - Yes/No":
            answer = "No"
        elif questions == "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number":
            answer = int(5)
        elif questions == "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number"
            answer = int(3)
    except:
        print("Your favor student Ivan Huang")
        
    
