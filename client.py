import socket
import sys

PORT = 5432

def connect_server(server_ip):
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print(f"[CLIENT] กำลังเชื่อมต่อ {server_ip}:{PORT} ...")

    try:
        client_sock.connect((server_ip, PORT))
        print(f"[CLIENT] พิมพ์ข้อความแล้วกด Enter เพื่อส่ง (กด Enter โดยไม่ต้องพิมพ์อะไร เพื่อออก)\n")

        while True:
            try:
                user_input = input("คุณ >> ")
            except EOFError:
                user_input = ""

            # ย้ายส่วนนี้เข้ามาใน Loop
            client_sock.sendall(user_input.encode('UTF-8'))
            
            if user_input == "":
                print("[CLIENT] กำลัง Disconnect จาก Server ....")
                break

            print(f"[CLIENT] ส่งข้อความสำเร็จ : '{user_input}'")

    except ConnectionRefusedError:
        print(f"[CLIENT] ไม่สามารถเชื่อมต่อได้: Server อาจจะยังไม่เปิดที่ {server_ip}:{PORT}")
    except Exception as err:
        print(f"[CLIENT] เกิดข้อผิดพลาด: {err}")
    finally:
        client_sock.close()
        print(f"[CLIENT] ปิด Socket เรียบร้อย End.....")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        server_ip = input("กรุณาใส่ IP address ของ Server: ").strip()
    else:
        server_ip = sys.argv[1]
    
    # แก้ชื่อฟังก์ชันให้ตรงกัน
    connect_server(server_ip)