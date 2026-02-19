#!/usr/bin/env python3
# Shadowsocks Base64 Decoder for E2B Sandbox
# Usage: python decode_shadowsocks.py <base64_file>

import base64
import subprocess
import sys

def decode_and_extract(b64_path, output_name):
    """Decode base64 file and extract."""
    print(f"📥 Decoding {b64_path}...")
    
    # Read base64
    with open(b64_path, 'r') as f:
        b64_data = f.read().strip()
    
    # Decode
    binary_data = base64.b64decode(b64_data)
    print(f"   Decoded: {len(binary_data):,} bytes")
    
    # Write
    with open(output_name, 'wb') as f:
        f.write(binary_data)
    print(f"   Written: {output_name}")
    
    # Extract if tar
    if output_name.endswith(('.tar.xz', '.tar.gz')):
        print(f"📂 Extracting {output_name}...")
        if output_name.endswith('.tar.xz'):
            subprocess.run(['tar', '-xJf', output_name], check=True)
        else:
            subprocess.run(['tar', '-xzf', output_name], check=True)
        print("✅ Extraction complete!")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python decode_shadowsocks.py <base64_file>")
        sys.exit(1)
    
    b64_file = sys.argv[1]
    
    # Determine output name
    if b64_file.endswith('.b64'):
        output = b64_file[:-4]
    else:
        output = b64_file + '.decoded'
    
    decode_and_extract(b64_file, output)
