1) Go to Secret Manager and create a secret
    a. name: my_awesome_secret_from_secret_manager

2) Go to IAM
    a. create role and name it role-svc-secretmanager
    b. Add permissions
        secretmanager.versions.access
    c. create Service account and attach the role
        a. name: sa-svc-secretmanager
    d. update cloudbuild.yaml file with service account name


3) Setup Cloud Build