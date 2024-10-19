from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .prompts import get_prompt
import openai
import json
from django.conf import settings
from .models import ChatSession, ChatMessage
import uuid
import re

openai.api_key = settings.OPENAI_API_KEY

@csrf_exempt
def tutor_response(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_input = data.get('message', '')
            session_id = data.get('session_id', str(uuid.uuid4()))

            # Get or create the session
            session, created = ChatSession.objects.get_or_create(session_id=session_id)

            # Save user message
            ChatMessage.objects.create(session=session, role='user', content=user_input)

            # Check if the user is asking for a roadmap to become a data scientist
            roadmap_keywords = [
                "how do I become a data scientist",
                "how do I learn data science",
                "data science roadmap",
                "learn data science"
            ]
            if any(re.search(keyword, user_input, re.IGNORECASE) for keyword in roadmap_keywords):
                # Fetch the roadmap prompt
                roadmap_prompt = get_prompt("roadmap")
                full_prompt = [
                    {"role": "system", "content": get_prompt("system")},
                    {"role": "assistant", "content": roadmap_prompt},
                    {"role": "user", "content": user_input}
                ]
            else:
                # 1. Get the system prompt (fixed for every conversation)
                system_prompt = get_prompt("system")

                # 2. Dynamically choose a topic prompt based on the user's input or a predefined topic
                # For this example, assume the topic is Python basics, specifically "define a function"
                topic_key = "python_basics"
                topic_prompt = get_prompt("topic", topic_key, concept="define a function")

                # 3. Combine the system and topic prompts with the user's input to form the full conversation
                full_prompt = [
                    {"role": "system", "content": system_prompt},
                    {"role": "assistant", "content": topic_prompt},
                    {"role": "user", "content": user_input}
                ]

            # Call the OpenAI API with the constructed prompt
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",  # Ensure the correct model name is used
                messages=full_prompt
            )

            tutor_reply = response['choices'][0]['message']['content']

            # Save chatbot message
            ChatMessage.objects.create(session=session, role='assistant', content=tutor_reply)

            return JsonResponse({'response': tutor_reply, 'session_id': session.session_id})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)
