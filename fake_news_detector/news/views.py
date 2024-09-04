import joblib
import os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Establecer la ruta del archivo .pkl
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, 'fake_news_model.pkl')

# Cargar el modelo desde el archivo .pkl
model = joblib.load(model_path)

@csrf_exempt
def predict_news(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            text = data['text']
            prediction = model.predict([text])
            result = 'Fake' if prediction[0] == 0 else 'Real'
            return JsonResponse({'result': result})
        except KeyError:
            return JsonResponse({'error': 'Invalid input'}, status=400)
    return JsonResponse({'error': 'Only POST method is allowed'}, status=405)
