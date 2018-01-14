![https://travis-ci.org/segator/electricity_companies_prometheus_exporter](https://travis-ci.org/segator/electricity_companies_prometheus_exporter.svg?branch=master)

# Electricity company price prometheus exporter

The script will get kwh price from differents electricity companies and export on port default 8111 for prometheus metrics.

# Usage

```
 electricity_exporter.py [-h] [-p <port>]
```

- `-h` Help
- `-p` port to listen (where prometheus will connect). Default port 8111
