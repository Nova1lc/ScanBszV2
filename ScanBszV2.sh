#!/bin/bash

# Mostrar el banner
banner="
+++++++++++++++++++++++++++++
+                           +
+   ScanBszV2 to BSZ!   +
+                           +
+++++++++++++++++++++++++++++
"

echo "$banner"

# Función para escanear vulnerabilidades
escanear_vulnerabilidades() {
    ip=$1
    echo "Escaneando vulnerabilidades en $ip..."

    # Ejecutar nmap con las opciones de escaneo
    nmap -sS -sCV -sU -A -O --script "vuln" -T4 $ip
}

# Pedir la IP de destino
read -p "Ingresa la direccion IP: " ip

# Validar que la IP sea válida
if [[ ! $ip =~ ^([0-9]{1,3}\.){3}[0-9]{1,3}$ ]]; then
    echo "Dirección IP inválida. Por favor, ingresa una dirección IP válida."
    exit 1
fi

# Llamar a la función de escaneo
escanear_vulnerabilidades $ip
