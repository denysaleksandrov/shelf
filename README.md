# Run in OCP 4.x

```
oc new-app --as-deployment-config -i postgresql --name=postgres \
           -e POSTGRESQL_DATABASE=shelf \
           -e POSTGRESQL_PASSWORD=shelf \
           -e POSTGRESQL_USER=shelf

oc new-app --as-deployment-config --name shelf \
           python:3.6~https://github.com/denysaleksandrov/shelf \
           -e DATABASE_NAME=shelf \
           -e DATABASE_USER=shelf \
           -e DATABASE_PASS=shelf \
           -e DATABASE_HOST=postgres \
           -e ALLOWED_DOMAIN=".apps.ocp4.lab-nec.com"
### Image stream might be different. The above command worked in OCP4.5. In OCP4.7.19 is python:3.6 doens't exists, but python:3.6-ubi does.
oc logs -f bc/shelf
...
oc logs -f $(basename $(oc get pods -l deploymentconfig=shelf -o name))
...

oc expose svc/shelf
```

# Provision data

```
git clone <repo>
cd shelf/provision
export APP_IP=$(oc get route/shelf -o jsonpath='{.spec.host}{"\n"}')
export APP_PORT=80
./create_books.py
```
