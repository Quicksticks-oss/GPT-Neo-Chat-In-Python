from transformers import pipeline
from utils import *
import torch
import time

torch_device = torch.device("cuda:0")

start_loading = time.time()
print('Loading pipeline...')

generator = pipeline('text-generation', model='EleutherAI/gpt-neo-2.7B')
generator.model.config.pad_token_id = generator.model.config.eos_token_id

print('Pipeline loaded took', round(abs(start_loading-time.time()), 2), 'seconds.')

while True:
    prompt = input('You > ')
    if prompt.lower() in ['stop', 'quit', 'exit']:
        quit()
    start_prompt = time.time()
    res = generator(prompt, max_length=25, do_sample=True, device=torch_device, temperature=0.9)
    print('Bot >', gen_result(res), 'took', round(abs(start_prompt-time.time()), 2), 'seconds.')
