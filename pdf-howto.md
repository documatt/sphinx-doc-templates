
docker compose build
docker compose run docs make html
docker compose run docs make latexpdf
docker compose run docs make latexpdf LATEXMKOPTS="-silent -f -interaction=nonstopmode"