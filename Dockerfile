# Minimal RunPod Serverless wrapper for vLLM DeepSeek-OCR
FROM vllm/vllm-openai:v0.8.5

# Install RunPod SDK and supervisor
RUN pip install --no-cache-dir runpod requests supervisor

# Copy handler
COPY runpod_handler.py /app/handler.py

# Copy supervisor config to manage both vLLM and handler
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

WORKDIR /app

# Expose port
EXPOSE 8000

# Start supervisor (manages vLLM server + RunPod handler)
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]