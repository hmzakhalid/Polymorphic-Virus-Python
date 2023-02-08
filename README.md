# Polymorphic Virus in Python
#### Author: [Hamza Khalid](https://github.com/hmzakhalid) 

**Introduction:** 

This is a polymorphic virus I wrote in Python. It is polymorphic because it changes its code with each execution.

**Working:** 

I have a function that contains the Virus. When the function is called, it encrypts itself and writes the encrypted token and the encryption key to a new file with the same name. It also writes a decryption function and code to get the hash to that file. Once everything is written to the new file. The current file is deleted. 

**Code:** 

If we ignore the Hash code. We can see the actual virus code is just a few lines. 

![](/imgs/2.png)

When the Encrypted token is decrypted. This is the function that is returned (the virus function): 

![](/imgs/1.png)

**Execution:** 

As we see here, every execution has a different hash 

![](/imgs/3.png)
![](/imgs/4.png)

To see why it happens. We've to look at the files' content.  

**1.** 

![](/imgs/5.png)

**2.** 

![](/imgs/6.png)

With each execution the virus is encrypted with a new key and the file is updated. 
