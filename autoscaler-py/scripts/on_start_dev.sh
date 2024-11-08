env | grep _ >> /etc/environment;
cd /src;
if [ ! -f /root/hasbooted ]
then
    pip install accelerate -U;
    pip install protobuf;
    pip install vllm;
    git clone https://github.com/nickgreenspan/host-server;
    touch ~/.no_auto_tmux
    /scripts/docker-entrypoint.sh python3 /app/download-model.py TheBloke/Llama-2-13B-chat-GPTQ --branch gptq-4bit-32g-actorder_True;
fi
touch /root/hasbooted
python3 /src/host-server/auth_server.py > auth.log 2>&1 &
python3 /src/host-server/model_inference_server.py > infer.log 2>&1 &