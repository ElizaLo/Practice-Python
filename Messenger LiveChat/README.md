## Errors:
- **socket.error: [Errno 48] Address already in use**
    1. `sudo lsof -i:5000`
    
    This will give you a list of processes using the port if any. Once the list of processes is given, use the id on the PID column to terminate the process use
    
    2. `kill PID` use the provided PID
