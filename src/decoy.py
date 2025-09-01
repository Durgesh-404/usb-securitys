import os

def create_decoy_files():
    decoy_dir = os.path.join(os.getcwd(), 'decoy_files')
    os.makedirs(decoy_dir, exist_ok=True)
    for i in range(5):
        with open(os.path.join(decoy_dir, f'decoy_file_{i}.txt'), 'w') as f:
            f.write('This is a fake decoy file.')
