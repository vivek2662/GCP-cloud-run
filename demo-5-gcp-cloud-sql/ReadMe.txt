1) Go to Cloud SQL and create an instance
    a. name: my-awesome-db-instance
    b. create secret with name my_awesome_db_password and value of db password
    c. update code with public IP address

2) Go to IAM
    a. create role and name it role-svc-cloudsql
    b. Add permissions
        secretmanager.versions.access
        cloud sql client
    c. create Service account and attach the role
        a. name: sa-svc-cloudsql
    d. update cloudbuild.yaml file with service account name

3) Enable Cloud SQL Admin API

4) Setup Cloud Build

5) For Private IP Connectivity
    a. Enable Compute Engine API
    b.
    c. Serverless VPC Access API