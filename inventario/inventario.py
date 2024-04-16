import csv
import socket
import platform
import psutil
import winapps

# Coleta de informações do sistema com detalhes adicionais
def get_system_info():
    cpu_info = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    disk_info = psutil.disk_usage('/')
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    os_version = platform.platform()

    return {
        'IP Address': ip_address,
        'Machine Name': hostname,
        'OS Version': os_version,
        'CPU Usage (%)': cpu_info,
        'Memory Total (GB)': round(memory_info.total / (1024 ** 3), 2),
        'Memory Used (GB)': round(memory_info.used / (1024 ** 3), 2),
        'Disk Total (GB)': round(disk_info.total / (1024 ** 3), 2),
        'Disk Used (GB)': round(disk_info.used / (1024 ** 3), 2)
    }

# Lista de aplicativos instalados
def get_installed_apps():
    apps = []
    for app in winapps.list_installed():
        apps.append({
            'IP Address': socket.gethostbyname(socket.gethostname()),
            'Host Name': socket.gethostname(),
            'Name': app.name,
            'Version': app.version,
            'Install Date': app.install_date,
            'Publisher': app.publisher
        })
    return apps

# Salvar dados no arquivo CSV
def save_to_csv(apps_list):
    file_path = 'inventario.csv'
    
    with open(file_path, 'a', newline='', encoding='utf-8') as file:
        csv_writer = csv.writer(file)
        
        # Escrever cabeçalho do sistema se o arquivo estiver vazio
        if file.tell() == 0:
            csv_writer.writerow(apps_list[0].keys())  # cabeçalho dos apps
        
        # Escrever dados dos aplicativos
        for app in apps_list:
            csv_writer.writerow(app.values())

# Executando todas as funções
system_info = get_system_info()
apps_list = get_installed_apps()
save_to_csv(apps_list)

print("Inventário foi atualizado com sucesso em formato CSV!")
input("Pressione Enter para encerrar o programa...")

