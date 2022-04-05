# Locust

locust.io

Para ejecutar

```
locust -f locust_file.py --host http://URL --users 50 --spawn-rate
```
- host: para pre-rellenar la dirección URL base
- users: el número total de usuarios a alcanzar al mismo tiempo
- spwan-rate: La tasa en que deben crecer los usuarios, de dos en dos, diez en diez, etc.