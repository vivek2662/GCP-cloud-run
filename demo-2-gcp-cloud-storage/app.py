import os
from datetime import datetime
from flask import Flask, jsonify
from google.cloud import storage

app = Flask(__name__)

bucket_name = "my-awesome-bucket-102"

storage_client = storage.Client()


@app.route("/", methods=["GET"])
def create_file_and_upload_to_gcp_bucket():
    file_name = "my-file.txt"

    file_content = datetime.now().strftime('%m-%d-%y %H:%M:%S')
    with open(f"./{file_name}", "w") as file:
        file.write(file_content)

    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(f"my-folder/{file_name}")
    blob.upload_from_filename(f"./{file_name}")

    data = blob.download_as_string()

    return jsonify(success=True, data=data.decode("utf-8")), 200


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
