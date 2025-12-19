from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
import openai 
from django.conf import settings
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch


# openai.api_key = ""
def chat_with_openai(request):
    user_message = request.GET.get('message', 'Hello!')

#     response = openai.chat.completions.create(
#         model="gpt-4",
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant."},
#             {"role": "user", "content": user_message}
#         ]
#     )

#     answer = response.choices[0].message.content
#     return JsonResponse({"reply": answer})

# Model name
    model_name = "gpt2"

# Load tokenizer & model
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

# Force CPU
    device = torch.device("cpu")
    model.to(device)

# Input text
    text = user_message
    inputs = tokenizer(text, return_tensors="pt")
    inputs = {k: v.to(device) for k, v in inputs.items()}

# Generate text
    with torch.no_grad():  # saves memory
     outputs = model.generate(
        **inputs,
        max_length=50,
        do_sample=True,
        temperature=0.7
    )

    return JsonResponse({"reply": tokenizer.decode(outputs[0], skip_special_tokens=True)})
# print(tokenizer.decode(outputs[0], skip_special_tokens=True))


def home(request):
    return render(request, 'index.html')
def about(request):
    return HttpResponse("tell me about")
def services(request):
    return HttpResponse("services")
def askagain(request):
    return render(request, 'index.html')
