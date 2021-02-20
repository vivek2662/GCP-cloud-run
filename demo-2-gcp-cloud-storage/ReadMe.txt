1) Go to Cloud Storage
    a. create bucket
    b. update code with bucket name

2) Go to IAM
    a. create role and name it role-svc-cloudstorage
    b. Add permissions
        storage.buckets.get
        storage.objects.create
        storage.objects.delete
        storage.objects.get
    c. create Service account and attach the role
        a. name: sa-svc-cloudstorage
    d. update cloudbuild.yaml file with service account name


3) Setup Cloud Build