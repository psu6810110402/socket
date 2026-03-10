import socket

PORT = 5432
HOST = input("Please input your IP address : ")

def start_server():
    # 1. สร้าง Socket แบบ TCP
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # 2. ผูก Socket เข้ากับ IP และ Port
        server_sock.bind((HOST, PORT))
        server_sock.listen(5) # เริ่มรอการเชื่อมต่อ (คิวสูงสุด 5 คิว)
        print(f"[SERVER] กำลังเปิดรอการเชื่อมต่อที่ Port {PORT}...")

        while True:
            # 3. ยอมรับการเชื่อมต่อจาก Client
            client_conn, client_addr = server_sock.accept()
            print(f"[SERVER] เชื่อมต่อสำเร็จจาก: {client_addr}")

            with client_conn:
                while True:
                    # 4. รับข้อมูลที่ส่งมาจาก Client
                    data = client_conn.recv(1024)
                    if not data:
                        break
                    
                    message = data.decode('UTF-8')
                    if message == "":
                        print(f"[SERVER] Client {client_addr} ตัดการเชื่อมต่อ")
                        break
                        
                    print(f"[SERVER] ได้รับข้อความ: '{message}'")
            
            print(f"[SERVER] ปิด Session สำหรับ {client_addr}")

    except Exception as e:
        print(f"[SERVER] เกิดข้อผิดพลาด: {e}")
    finally:
        server_sock.close()
        print("[SERVER] ปิด Server เรียบร้อย")

if __name__ == "__main__":
    start_server()