import json
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse, Http404

def interactive_video_view(request):
    """Widok serwujący główny interfejs aplikacji."""
    return render(request, 'interactive_video/index.html')

def api_get_story(request):
    """API zwracające pełną strukturę narracyjną z pliku JSON."""
    
    # Zaktualizowana ścieżka docelowa wskazująca na folder 'data'
    file_path = settings.BASE_DIR / 'data' / 'story.json'

    print("hello world")

    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            story_data = json.load(f)
        return JsonResponse(story_data)
    except FileNotFoundError:
        raise Http404(f"Plik konfiguracyjny nie został znaleziony. Szukano w: {file_path}")
    except json.JSONDecodeError:
        return JsonResponse({"error": "Błąd parsowania pliku JSON. Sprawdź składnię."}, status=500)