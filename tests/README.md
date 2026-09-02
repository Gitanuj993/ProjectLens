# Tests

BASE_URL : https://projectlens-qgq3.onrender.com/

## API Health Test

```txt
curl -i https://projectlens-qgq3.onrender.com/health
```
Expected Output 
{"service":"project-evaluator","status":"ok"}


## API /analyze endpoint

```txt
!curl -X POST https://projectlens-qgq3.onrender.com/analyze \
-H "Content-Type: application/json" \
-d '{"url":"https://github.com/Gitanuj993/pylense"}'
```
Expected Output 
```txt
{"message":"URL received successfully","status":"accepted","url":"https://github.com/Gitanuj993/pylense"}
```


