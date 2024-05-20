#!/bin/bash

echo "╔══╣ Install: Ollama Python (STARTING) ╠══╗"

sudo apt-get update

curl -fsSL https://ollama.com/install.sh | sh

pip install ollama

sudo apt install xterm

echo "╚══╣ Install: Ollama Python (FINISHED) ╠══╝"