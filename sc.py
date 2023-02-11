import os
import cv2


  ####     ####    ##  ##   ##  ##     ##     ##  ##
 ##  ##   ##  ##   ##  ##   ### ##    ####    ##  ##
 ##       ##  ##   ##  ##   ######   ##  ##   ##  ##
 ## ###   ##  ##   ##  ##   ######   ######   ##  ##
 ##  ##   ##  ##   ##  ##   ## ###   ##  ##   ##  ##
 ##  ##   ##  ##   ##  ##   ##  ##   ##  ##   ##  ##
  ####     ####     ####    ##  ##   ##  ##    ####

# link: https://github.com/gounau/sc-py

# Localização da pasta com arquivos de vídeo
video_folder = "sua pasta videos"

# Localização da pasta para salvar as capturas de tela
screenshot_folder = "sua pasta sc"

# Verifica se a pasta de capturas de tela existe, caso contrário, cria uma nova
if not os.path.exists(screenshot_folder):
    os.makedirs(screenshot_folder)

# Obter a lista de arquivos de vídeo na pasta
video_files = [f for f in os.listdir(video_folder) if f.endswith((".mp4", ".mkv", ".avi", ".wmv"))]

# Número de screenshots a serem capturados
num_screenshots = 4

# Para cada arquivo de vídeo
for video_file in video_files:
    # Montar o caminho completo para o arquivo de vídeo
    video_path = os.path.join(video_folder, video_file)
    
    # Abrir o arquivo de vídeo usando o FFmpeg
    video = cv2.VideoCapture(video_path, cv2.CAP_FFMPEG)
    
    # Obter o número total de quadros no vídeo
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    
    # Intervalo entre as capturas de tela
    frame_interval = total_frames // num_screenshots
    
    # Para cada screenshot
    for i in range(0, total_frames, frame_interval):
        # Ir para o quadro especificado
        video.set(cv2.CAP_PROP_POS_FRAMES, i)
        ret, frame = video.read()
        
        # Verificar se o quadro foi lido com sucesso
        if ret:
            # Montar o nome da imagem de screenshot
            screenshot_name = "{}_{}_{}.jpg".format(video_file, i, "screenshot")
            screenshot_path = os.path.join(screenshot_folder, screenshot_name)
            
            # Salvar a screenshot
            cv2.imwrite(screenshot_path, frame)
    
    # Liberar o recurso de vídeo
    video.release()
