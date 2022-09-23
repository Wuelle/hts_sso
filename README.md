## Login
3 Frame Authentication process
* Username
* Password
* MFA (if enabled)

## TODO
* consider hosting static assets (bootstrap) instead of using a CDN
* Seperate response codes for username not found vs invalid credentials?


## Useful stuff
At least during debugging, api code can be generated using a hosted swagger instance like this:
```
curl
    https://generator3.swagger.io/api/generate \
    -H 'content-type: application/json' \
    -d '{
        "specURL" : "https://raw.githubusercontent.com/OAI/OpenAPI-Specification/master/examples/v3.0/petstore.yaml",
        "lang" : "java",
        "type" : "CLIENT",
        "codegenVersion" : "V3"
    }'
    --output "docs.zip"
```

