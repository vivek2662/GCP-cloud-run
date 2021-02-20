
2) Go to IAM
    a. create role and name it role-svc-pubsub
    b. Add permissions
        pubsub.subscriptions.consume
    c. create Service account and attach the role
        a. name: sa-svc-pubsub
    d. update cloudbuild.yaml file with service account name


3) Setup Cloud Build