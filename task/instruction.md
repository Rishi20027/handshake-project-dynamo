An access log is present in the container working directory. Analyze the traffic lines and summarize what you find by counting the metrics completely.

Your application must generate a JSON file saved precisely at `/app/report.json` with the following structural calculations:
1. `total_requests`: The absolute number of request lines found inside the log file.
2. `unique_ips`: The total count of unique client IP addresses present across all log lines.
3. `top_path`: The specific string path matching the most frequently requested web resource.
