# ReadMe

Clone this repository then install the following software.

```sh
git clone https://github.com/1homas/AI.git
cd AI
```

## Installation

### [podman](https://podman.io)

Use `podman` (free, rootless Docker) to run containers:

```sh
brew install podman
brew install podman-compose       # optional for dockerfiles and Kubernetes
brew install podman-desktop       # manage containers via UI

podman machine init
podman machine start
```

### [OpenWebUI](https://github.com/open-webui/open-webui)

Open WebUI is an extensible, feature-rich, and user-friendly self-hosted AI platform designed to operate entirely offline. It supports various LLM runners like Ollama and OpenAI-compatible APIs, with built-in inference engine for RAG, making it a powerful AI deployment solution.
https://GitHub.com/open-webui/open-webui

```sh
podman run -d -p 3000:8080 \
--add-host=localhost:127.0.0.1 \
-v open-webui:/app/backend/data \
--name open-webui \
--restart always \
ghcr.io/open-webui/open-webui:main

open http://localhost:3000
```

> ⚠ It may take a minue for OpenWebUI to initialize

### Ollama

There are many large language models (LLMs) to choose from with more being made everyday. Pick one or five and play. Many people talk about which models are better for certain tasks so your mileage may vary. These models are usually freely distributed from the site [HuggingFace](huggingface.co).

Advantages of running ollama LLMs locally over an AI service:

- Privacy concerns - running LLMs locally provides a lot of security.
- Ease of use - setting up LLMs can be challenging. With Ollama, it's an easy process
- Cost efficiency - no more cloud-based services (which can be costly)
- Latency reduction - local execution reduces the latency issues Customization - greater flexibility in customizing our models

On macOS:

```sh
brew install ollama           # macOS: install Ollama LLM
brew services start ollama    # macOS: start ollama as a service
ollama serve                  # Alternatively, run in a terminal

curl http://127.0.0.1:11434   # Test ollama API; output: `Ollama is running`

brew services stop ollama     # macOS: stop ollama as a service

ollama help                   # help about any command
ollama list                   # list models
ollama run MODEL
ollama run llama3.1:8b        # exit using `CTRL+D`
ollama pull MODEL             # pull the model from a registry
ollama run llama3.1:latest    # pull and run the model
ollama run llama3.1:latest --prompt "Why is the sky blue?" --temperature 0.7 --max-tokens 200 --verbose
ollama rm MODEL               # delete the model
```

Most people won’t need environment variables but if you want to use them:

```sh
export OLLAMA_HOST=127.0.0.1
export OLLAMA_PORT=11434
```

#### Modelfiles

Use [Ollama modelfiles](https://github.com/ollama/ollama/blob/main/docs/modelfile.md) from the `modelfiles` directory to create an Ollama model with a custom System Prompt.

```sh
ollama create {name} -f {modelfile}
ollama create llama-claude -f ollama_claude.modelfile
ollama list                # show your added model
ollama rm llama-claude     # delete model
```

### n8n

Start n8n [as a detached container](https://docs.n8n.io/hosting/installation/docker/) with a separate data volume (`n8n_data`) to locally store persistent data:

```sh
podman volume create n8n_data
podman run -d --name n8n -p 5678:5678  -v n8n_data:/home/node/.n8n  docker.io/n8nio/n8n
open http://localhost:5678
```

Once running, you can access n8n by opening: [http://localhost:5678](http://localhost:5678)

## Upgrading

```sh
podman pull docker.n8n.io/n8nio/n8n    # pull the latest image
podman stop n8n                        # stop existing container
podman rm n8n                          # delete existing container
podman run -d --name n8n -p 5678:5678  -v n8n_data:/home/node/.n8n  docker.io/n8nio/n8n
open http://localhost:5678
```

### Python

```sh
git clone {url}
cd {directory}

uv venv                     # create a virtual environment (venv) without pre-installing any packages
uv venv --seed              # pre-install a set of default packages or dependencies into the venv
uv add --dev ipykernel      # Jupyter require ipykernel
uv add -r requirements.txt

source .venv/bin/activate   # activate virtual environment
```
