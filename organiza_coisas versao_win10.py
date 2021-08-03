# program for organize files
import os
from colorama import Fore
import getpass
import time
import shutil
from colorama import init


init()


def greet_user():
    """greeting the user"""
    time.sleep(1)
    user = getpass.getuser()
    print(Fore.LIGHTGREEN_EX + f'Bem vindo(a), {user.title()}!')
    time.sleep(1)


def search_path():
    """Find the path"""
    user = getpass.getuser()
    os.chdir(f'C:\\Users\\{user}\\')
    caminho: str = f'C:\\Users\\{user}\\'
    contador_pdf: int = 0
    contador_doc: int = 0
    contador_xml: int = 0
    contador_mp3: int = 0
    contador_mp4: int = 0
    contador_pes: int = 0
    contador_jpeg: int = 0
    contador_jpg: int = 0
    contador_img: int = 0
    contador_txt: int = 0
    contador_ppt: int = 0
    try:
        print(Fore.CYAN + 'Digite o nome, corretamente, da pasta que deseja organizar: ')
        time.sleep(1)
        print(Fore.RED + 'OBS: se for pasta dentro de pasta, é necessário especificar o caminho todo')
        print("Por exemplo: \\Documents\\Jogos\\")
        time.sleep(1)
        caminho_escolhido: str = str(input(Fore.BLUE + '>>> '))
        caminho_escolhido = caminho + caminho_escolhido + '\\'
        for arquivos in os.listdir(caminho_escolhido):
            if arquivos.endswith('.pdf'):
                contador_pdf += 1
            elif arquivos.endswith('.doc') or arquivos.endswith('.docx'):
                contador_doc += 1
            elif arquivos.endswith('.xml') or arquivos.endswith('xmlm'):
                contador_xml += 1
            elif arquivos.endswith('.mp3'):
                contador_mp3 += 1
            elif arquivos.endswith('.mp4'):
                contador_mp4 += 1
            elif arquivos.endswith('.pes'):
                contador_pes += 1
            elif arquivos.endswith('.jpg'):
                contador_jpg += 1
            elif arquivos.endswith('.img'):
                contador_img += 1
            elif arquivos.endswith('.txt'):
                contador_txt += 1
            elif arquivos.endswith('.ppt'):
                contador_ppt += 1
            elif arquivos.endswith('.png'):
                contador_jpeg += 1
        print(Fore.CYAN + f"""
        -------------------------------
        Relação de itens encontrados:
        -------------------------------       
        PDF: {contador_pdf}
        TXT: {contador_txt}
        PES: {contador_pes}
        WORD: {contador_doc}
        EXCEL: {contador_xml}
        IMAGENS: {contador_jpeg + contador_jpg + contador_img}
        AUDIOS: {contador_mp3}
        VIDEOS: {contador_mp4}
        POWER_POINT: {contador_ppt} 
        -------------------------------      
        """)
        time.sleep(1)
        print(Fore.YELLOW + 'ORGANIZANDO...')
        for files in os.listdir(caminho_escolhido):
            if contador_pdf >= 1:
                if 'PDFs' in os.listdir(caminho_escolhido):
                    if files.endswith('.pdf'):
                        shutil.move(f'{caminho_escolhido}{files}', f'{caminho_escolhido}PDFs\\')
                else:
                    os.mkdir(f'{caminho_escolhido}PDFs')
                    time.sleep(1)
                    if files.endswith('.pdf'):
                        shutil.move(f'{caminho_escolhido}{files}', f'{caminho_escolhido}PDFs\\')
        for files in os.listdir(caminho_escolhido):
            if contador_txt >= 1:
                if 'TXTs' in os.listdir(caminho_escolhido):
                    if files.endswith('.txt'):
                        shutil.move(f'{caminho_escolhido}{files}', f'{caminho_escolhido}TXTs\\')
                else:
                    os.mkdir(f'{caminho_escolhido}TXTs')
                    time.sleep(1)
                    if files.endswith('.txt'):
                        shutil.move(f'{caminho_escolhido}{files}', f'{caminho_escolhido}TXTs\\')
        for files in os.listdir(caminho_escolhido):
            if contador_pes >= 1:
                if 'PES' in os.listdir(caminho_escolhido):
                    if files.endswith('.pes'):
                        shutil.move(f'{caminho_escolhido}{files}', f'{caminho_escolhido}PES\\')
                else:
                    os.mkdir(f'{caminho_escolhido}PES')
                    time.sleep(1)
                    if files.endswith('.pes'):
                        shutil.move(f'{caminho_escolhido}{files}', f'{caminho_escolhido}PES\\')
        for files in os.listdir(caminho_escolhido):
            if contador_doc >= 1:
                if 'WORDS' in os.listdir(caminho_escolhido):
                    if files.endswith('.doc') or files.endswith('.docx'):
                        shutil.move(f'{caminho_escolhido}{files}', f'{caminho_escolhido}WORDS\\')
                else:
                    os.mkdir(f'{caminho_escolhido}WORDS')
                    time.sleep(1)
                    if files.endswith('.doc') or files.endswith('.docx'):
                        shutil.move(f'{caminho_escolhido}{files}', f'{caminho_escolhido}WORDS\\')
        for files in os.listdir(caminho_escolhido):
            if contador_xml >= 1:
                if 'EXCELS' in os.listdir(caminho_escolhido):
                    if files.endswith('.xml') or files.endswith('.xmlm'):
                        shutil.move(f'{caminho_escolhido}{files}', f'{caminho_escolhido}EXCELS\\')
                else:
                    os.mkdir(f'{caminho_escolhido}EXCELS')
                    time.sleep(1)
                    if files.endswith('.xml') or files.endswith('.xmlm'):
                        shutil.move(f'{caminho_escolhido}{files}', f'{caminho_escolhido}EXCELS\\')
        for files in os.listdir(caminho_escolhido):
            if contador_xml >= 1:
                if 'EXCELS' in os.listdir(caminho_escolhido):
                    if files.endswith('.xml') or files.endswith('.xmlm'):
                        shutil.move(f'{caminho_escolhido}{files}', f'{caminho_escolhido}EXCELS\\')
                else:
                    os.mkdir(f'{caminho_escolhido}EXCELS')
                    time.sleep(1)
                    if files.endswith('.xml') or files.endswith('.xmlm'):
                        shutil.move(f'{caminho_escolhido}{files}', f'{caminho_escolhido}EXCELS\\')
        for files in os.listdir(caminho_escolhido):
            if contador_jpg >= 1 or contador_img >= 1 or contador_jpeg >= 1 or contador_jpeg >= 1:
                if 'IMAGENS' in os.listdir(caminho_escolhido):
                    if files.endswith('.jpeg') or files.endswith('.jpg') or files.endswith('.img') or files.endswith('.png') or files.endswith('.img'):
                        shutil.move(f'{caminho_escolhido}{files}', f'{caminho_escolhido}IMAGENS\\')
                else:
                    os.mkdir(f'{caminho_escolhido}IMAGENS')
                    time.sleep(1)
                    if files.endswith('.jpeg') or files.endswith('.png') or files.endswith('.jpg') or files.endswith('.png') or files.endswith('.img'):
                        shutil.move(f'{caminho_escolhido}{files}', f'{caminho_escolhido}IMAGENS\\')
        for files in os.listdir(caminho_escolhido):
            if contador_ppt >= 1:
                if 'POWERPOINT' in os.listdir(caminho_escolhido):
                    if files.endswith('.ppt') or files.endswith('.ppd'):
                        shutil.move(f'{caminho_escolhido}{files}', f'{caminho_escolhido}POWERPOINT\\')
                else:
                    os.mkdir(f'{caminho_escolhido}POWERPOINT')
                    time.sleep(1)
                    if files.endswith('.ppt') or files.endswith('.ppd'):
                        shutil.move(f'{caminho_escolhido}{files}', f'{caminho_escolhido}POWERPOINT\\')
        for files in os.listdir(caminho_escolhido):
            if contador_mp4 >= 1:
                if 'VIDEOS' in os.listdir(caminho_escolhido):
                    if files.endswith('.mp4'):
                        shutil.move(f'{caminho_escolhido}{files}', f'{caminho_escolhido}VIDEOS\\')
                else:
                    os.mkdir(f'{caminho_escolhido}VIDEOS')
                    time.sleep(1)
                    if files.endswith('.mp4'):
                        shutil.move(f'{caminho_escolhido}{files}', f'{caminho_escolhido}VIDEOS\\')
        for files in os.listdir(caminho_escolhido):
            if contador_mp3 >= 1:
                if 'AUDIOS' in os.listdir(caminho_escolhido):
                    if files.endswith('.mp3'):
                        shutil.move(f'{caminho_escolhido}{files}', f'{caminho_escolhido}AUDIOS\\')
                else:
                    os.mkdir(f'{caminho_escolhido}AUDIOS')
                    time.sleep(1)
                    if files.endswith('.mp3'):
                        shutil.move(f'{caminho_escolhido}{files}', f'{caminho_escolhido}AUDIOS\\')
        time.sleep(3)
        print(Fore.LIGHTGREEN_EX + 'CONCLUÍDO')
    except FileNotFoundError:
        time.sleep(3)
        print(Fore.RED + 'Error! Verifique o caminho escolhido.')


if __name__ == '__main__':
    greet_user()
    search_path()
