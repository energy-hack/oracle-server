# quasar-research
You can't fight what you can't see

Build & run in docker:

```
docker build -t quasar_flask_api:latest .
docker run -d -p 5000:5000 quasar_flask_api
docker ps
docker logs -ft <id>
```