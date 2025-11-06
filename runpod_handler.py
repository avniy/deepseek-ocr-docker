"""
RunPod Serverless Handler for vLLM DeepSeek-OCR
This wraps vLLM's OpenAI-compatible API in RunPod's serverless format
"""
import runpod
import requests
import base64
import os

# vLLM server runs on localhost:8000
VLLM_URL = "http://localhost:8000/v1/completions"

def handler(job):
    """
    RunPod serverless handler
    Expects input: { "prompt": "text", "image_base64": "optional", "max_tokens": 512 }
    """
    try:
        job_input = job['input']

        # Extract parameters
        prompt = job_input.get('prompt', '<image>\nExtract text from this image.')
        image_base64 = job_input.get('image_base64')
        max_tokens = job_input.get('max_tokens', 512)

        # Build the request to vLLM
        vllm_request = {
            "model": "deepseek-ai/DeepSeek-OCR",
            "prompt": prompt,
            "max_tokens": max_tokens,
            "temperature": 0.0
        }

        # If image provided, add it
        if image_base64:
            vllm_request["prompt"] = f"<image>{prompt}"

        # Call vLLM API
        response = requests.post(
            VLLM_URL,
            json=vllm_request,
            timeout=300
        )

        if response.status_code == 200:
            result = response.json()
            return {
                "success": True,
                "text": result['choices'][0]['text'],
                "model": result['model'],
                "usage": result.get('usage', {})
            }
        else:
            return {
                "success": False,
                "error": f"vLLM returned status {response.status_code}",
                "details": response.text
            }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

# Start the handler
runpod.serverless.start({"handler": handler})
