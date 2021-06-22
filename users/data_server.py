import base64
import paramiko

from polar_auth.settings import data_server, data_folder, data_server_key
from polar_auth.settings import rsa_key_file, ssh_username

# Set up an SSH client and add the data server key
try:
    server_key = paramiko.RSAKey(data=base64.decodebytes(data_server_key))
    ssh_client = paramiko.SSHClient()
    ssh_client.get_host_keys().add(data_server, 'ssh-rsa', server_key)
    rsa_key = paramiko.RSAKey.from_private_key_file(rsa_key_file)
except:
    from django.conf import settings
    if not settings.DEBUG:
        raise
    print("Can not load SSH keys.  Ignoring because this is debug mode.")


# Communicate the access token to the data server
def communicate_token(polar_id, access_token, subject_id):
    ''' Communicate a token to the data server over ssh. '''

    ssh_client.connect(hostname=data_server, username=ssh_username, pkey=rsa_key)
    sftp_client = ssh_client.open_sftp()
    remote_file = data_folder + '/new_tokens'
    token_file = sftp_client.file(remote_file, mode='a', bufsize=1)
    token_file.write(f'{access_token} {polar_id} {subject_id}\n')
    token_file.flush()
    token_file.close()


# Communicate the access token to the data server
def delete_token(subject_id):
    ''' Communicate a token to the data server over ssh. '''

    ssh_client.connect(hostname=data_server, username=ssh_username, pkey=rsa_key)
    sftp_client = ssh_client.open_sftp()
    remote_file = data_folder + '/delete_tokens'
    token_file = sftp_client.file(remote_file, mode='a', bufsize=1)
    token_file.write(f'{subject_id}\n')
    token_file.flush()
    token_file.close()


# Read the list of IDs with gathered date
def get_ids_with_data():
    ''' Fetch the list of tokens with data over ssh. '''

    ssh_client.connect(hostname=data_server, username=ssh_username, pkey=rsa_key)
    sftp_client = ssh_client.open_sftp()
    remote_file = data_folder + '/ids_with_data'
    print(remote_file)
    id_file = sftp_client.file(remote_file, mode='r', bufsize=1)
    ids = [int(id) for id in id_file]
    id_file.close()
    return ids