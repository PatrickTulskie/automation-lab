# Use Jupyter base image with Python
FROM jupyter/datascience-notebook:latest

# Install required Python packages
RUN pip install --no-cache-dir \
    langchain \
    langchain-ollama \
    langchain-openai \
    openai \
    pydantic \
    requests

# Expose Jupyter's default port
EXPOSE 8888

# Start Jupyter automatically when the container is run
CMD ["start-notebook.sh", "--NotebookApp.token=''"]
