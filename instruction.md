Analyze the Apache-style access log located at /app/access.log.

Write a JSON report to /app/report.json.

Success criteria:
1. Read every log entry.
2. Count the total number of requests.
3. Count the number of unique client IP addresses.
4. Determine the most frequently requested path.
5. Write a valid JSON object with the keys total_requests, unique_ips, and top_path.
