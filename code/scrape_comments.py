import os
import csv
import re
from googleapiclient.discovery import build
from dotenv import load_dotenv

# 1. Cargar la API key desde el archivo .env
load_dotenv()
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("⚠️ No se encontró 'API_KEY' en el archivo .env")

# 2. Inicializar cliente de YouTube API
youtube = build("youtube", "v3", developerKey=API_KEY)

# 3. Extraer video ID desde la URL
def extract_video_id(url):
    match = re.search(r"(?:v=|youtu\.be/)([\w-]{11})", url)
    if match:
        return match.group(1)
    else:
        raise ValueError(f"No se pudo extraer un video ID válido de: {url}")

# 4. Obtener comentarios de un video (máximo 500)
def get_comments(video_id, max_results=500):
    comments = []
    next_page_token = None

    while len(comments) < max_results:
        response = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            pageToken=next_page_token,
            maxResults=min(100, max_results - len(comments)),
            textFormat="plainText"
        ).execute()

        for item in response["items"]:
            comment = item["snippet"]["topLevelComment"]["snippet"]
            comments.append({
                "comment_id": item["id"],
                "text": comment["textDisplay"],
                "video_id": video_id
            })

        next_page_token = response.get("nextPageToken")
        if not next_page_token:
            break

    return comments

# 5. Guardar comentarios en CSV
def save_to_csv(comments, filename="data/dataset.csv"):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["comment_id", "text", "video_id"])
        writer.writeheader()
        writer.writerows(comments)

# 6. Ejecutar como script
if __name__ == "__main__":
    video_urls = [
        "https://www.youtube.com/watch?v=B43YEW2FvDs",
        # Agrega más URLs aquí si quieres
    ]

    all_comments = []

    for url in video_urls:
        try:
            video_id = extract_video_id(url)
            print(f"📥 Descargando hasta 500 comentarios de {video_id}...")
            comments = get_comments(video_id, max_results=500)
            all_comments.extend(comments)
        except Exception as e:
            print(f"❌ Error con el video {url}: {e}")

    save_to_csv(all_comments)
    print(f"✅ Se guardaron {len(all_comments)} comentarios en data/dataset.csv")
