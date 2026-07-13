# Replace the image below with your project's approved SHA256-pinned base image.
FROM <approved-base-image>@sha256:<digest>

WORKDIR /app

# Install pinned verifier dependencies during image build.
RUN pip install pytest pytest-json-report

# Do NOT copy any solution or solution_hint files into this image.
