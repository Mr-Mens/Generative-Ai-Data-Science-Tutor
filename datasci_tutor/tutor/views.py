from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import openai
import json

@csrf_exempt
def tutor_response(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_input = data.get('message', '')

            # Call the OpenAI API with the user input
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini", 
                messages=[
                    {"role": "system", "content": "You are a highly knowledgeable data science tutor. Your job is to teach data science concepts in a clear, detailed, and engaging manner. Provide explanations using simple language, code examples, and, where necessary, visualizations. Always check if the user understands and offer further assistance if they need clarification."},
                    {"role": "user", "content": user_input},
                ]
            )
            
            tutor_reply = response['choices'][0]['message']['content']

            return JsonResponse({'response': tutor_reply})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)
