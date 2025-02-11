import nmap

banner = """
+++++++++++++++++++++++++++++
+                           +
+   ScanBszV2 to BSZ!   +
+                           +
+++++++++++++++++++++++++++++
"""

print(banner)

def escanear_vulnerabilidades(ip):
    scanner = nmap.PortScanner()
    try:
        print(f"Escaneando vulnerabilidades en {ip}. . .")
        resultado = scanner.scan(hosts=ip, arguments='-sS -sCV -sU -A -O --script vuln -T4')
        
        for host in resultado['scan']:
            print(f"\nHost: {host} ({resultado['scan'][host].get('hostaname')})")
            print(f"Estado: {resultado['scan'][host]['status']['state']}")

            if 'tcp' in resultado['scan'][host]:
                for puerto, detalles in resultado['scan'][host]['tcp'].items():
                    print(f"\nPuerto: {puerto}")
                    print(f"Estado: {detalles['state']}")
                    if 'script' in detalles:
                        for script, output in detalles['script'].items():
                            print(f"- {script}: {output}")
            else:
                print("No se encontraron puertos abiertos")
    except Exception as e:
        print(f"Error durante el escaneo: {e}")
ip = input("Ingresa la direccion IP: ")
escanear_vulnerabilidades(ip)


