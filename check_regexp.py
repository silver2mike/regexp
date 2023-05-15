import os
import re

pattern_pub = r'^(ssh-rsa|ssh-dss|ecdsa-sha2-nistp256|ssh-ed25519) AAAA[A-E][0-9A-Za-z+/]+[=]{0,2}( [^\s@]+@[^@\s]+)?$'

pattern_sec = r'^-----BEGIN [A-Z]+ PRIVATE KEY-----(\r?\n)([A-Za-z0-9+/=\r\n]+)(\r?\n)-----END [A-Z]+ PRIVATE KEY-----$'

directory_path = r'test_files'

for filename in os.listdir(directory_path):
    file_path = os.path.join(directory_path, filename)
    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            content = file.read()
            if re.match(pattern_pub, content):
                print(f'File "{filename}" is an public SSH key.')
            elif re.match(pattern_sec, content):
                print(f'File "{filename}" is an private SSH key.')            
