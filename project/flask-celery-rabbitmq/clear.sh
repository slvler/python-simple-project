docker stop $(docker ps -a -q) &&
docker rm $(docker ps -a -q) &&
docker rmi $(docker images -q)
docker compose up -d --build