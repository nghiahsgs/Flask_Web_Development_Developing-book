import random
import string
import hashlib

# B1: generate_password_hash
'''
salt la random
password => add salt (3 chars) to before password => md5() => pass_hash => save db
username|salt|pass_hash
'''

# B2: check password
'''
username => select => salt,pass_hash
user password =>  md5(salt + user_password) so sanh vs pass_hash
'''

def get_salt(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str
    
def generate_password_hash(password):
    salt = get_salt(3)
    password = '%s%s'%(password,salt)
    password_hash = hashlib.md5(password.encode('utf-8')).hexdigest()
    return password_hash,salt

def check_password(user_password, password_hash,salt):
    user_password = '%s%s'%(user_password,salt)
    user_password_hash = hashlib.md5(user_password.encode('utf-8')).hexdigest()
    return user_password_hash ==password_hash
    

if __name__ =="__main__":
    #khi nguoi dung dang ky, luu password_hash,salt vao db thay vi luu password
    password = '261997'
    password_hash,salt = generate_password_hash(password)

    #khi nguoi dung dang nhap, nguoi dung dien user_password => check password co dung ko de authenticate
    user_password = '261998'
    # user_password = '261997'
    kq = check_password(user_password, password_hash,salt)