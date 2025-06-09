import socket
import ssl
from datetime import datetime
import json
import os
import dns.resolver


DOMAINS = [
    "google.com",
    "ngc.gov.in",
    "results.nic.in",
    "mahafood.gov.in",
    "expired.badssl.com"
]

def get_certificate_info(domain):
    try:
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()

        issuer = dict(x[0] for x in cert['issuer'])['organizationName']
        valid_from = datetime.strptime(cert['notBefore'], "%b %d %H:%M:%S %Y %Z")
        valid_to = datetime.strptime(cert['notAfter'], "%b %d %H:%M:%S %Y %Z")
        days_left = (valid_to - datetime.now()).days

        status = "✅ Valid"
        if days_left <= 0:
            status = "❌ Expired"
        elif days_left <= 15:
            status = "⚠️ Expiring Soon"

        return {
            "domain": domain,
            "issuer": issuer,
            "valid_from": valid_from.strftime("%Y-%m-%d"),
            "valid_to": valid_to.strftime("%Y-%m-%d"),
            "days_left": days_left,
            "status": status,
            "dns": {
                "CAA": check_caa_record(domain),
                "TXT": check_txt_record(domain)
            }
        }

    except Exception as e:
        return {
            "domain": domain,
            "error": str(e),
            "status": "❌ Error"
        }

def check_caa_record(domain):
    try:
        answers = dns.resolver.resolve(domain, 'CAA')
        return [str(r) for r in answers]
    except Exception:
        return ["No CAA record found or lookup failed"]

def check_txt_record(domain):
    try:
        answers = dns.resolver.resolve(domain, 'TXT')
        return [r.to_text().strip('"') for r in answers]
    except Exception:
        return ["No TXT record found or lookup failed"]

def save_report(data, filename="reports/ssl_report.json"):
    if not os.path.exists("reports"):
        os.makedirs("reports")
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    print(f"✅ SSL scan report saved at {filename}")

if __name__ == "__main__":
    results = [get_certificate_info(domain) for domain in DOMAINS]
    save_report(results)
