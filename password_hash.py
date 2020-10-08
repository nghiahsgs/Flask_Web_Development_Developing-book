from werkzeug.security import generate_password_hash, check_password_hash

password='12355555'
password_hash = generate_password_hash(password, method='pbkdf2:sha1', salt_length=3)


# B1: generate_password_hash
'''
password => add salt (3 chars) to before password => md5() => pass_hash => save db
username|salt|pass_hash
'''

# B2: check password
'''
username => select => salt,pass_hash
user password =>  md5(salt + user_password) so sanh vs pass_hash
'''


456abc
md5() => result

abc




