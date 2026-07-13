# Replaced with the Harbor-approved base image and its SHA256 digest.
FROM <approved-base-image>@sha256:<approved-digest>

WORKDIR /app

RUN pip install --no-cache-dir \
    pytest==8.4.1 \
    pytest-json-ctrf==0.3.5

COPY access.log /app/access.log

# Do NOT copy solution_hint.py or any other reference solution.

CMD ["/bin/bash"]
