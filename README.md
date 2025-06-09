
# 🔐 ScanSafe – SSL & DNS Certificate Scanner

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

> A lightweight Python tool that scans domains for SSL certificate health and retrieves DNS CAA and TXT records — helping you stay ahead of security lapses.

---

## 🚀 Features

- ✅ **SSL Certificate Monitoring**
  - Checks issuer, validity period, and expiry date
  - Flags certificates that are expired or near expiration

- 🌐 **DNS Record Scanner**
  - Retrieves **CAA** records (who is allowed to issue certs)
  - Retrieves **TXT** records (e.g., SPF, DKIM, DMARC)

- 🧾 **JSON Report Generation**
  - Outputs a clean, structured report
  - Ideal for integration into alerting or dashboards

---

## 🧰 Tech Stack

- **Python 3.8+**
- `ssl`, `socket`, `datetime` – for SSL scanning
- `dnspython` – for DNS queries
- `json`, `os` – for file and report handling

---

## 📦 Project Structure

```
ScanSafe-SSL/
├── main.py                # Main logic
├── requirements.txt       # Dependencies
├── reports/
│   └── ssl_report.json    # Auto-generated output
├── README.md              # This file
```

---

## 🛠️ Installation & Setup

1. **Clone the repository:**

```bash
git clone https://github.com/<your-username>/ScanSafe-SSL.git
cd ScanSafe-SSL
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Run the script:**

```bash
python main.py
```

4. **View the report:**

```bash
cat reports/ssl_report.json
```

---

## ✏️ Configuration

To scan your own domains, edit the \`DOMAINS\` list in \`main.py\`:

```python
DOMAINS = [
    "google.com",
    "instagram.com",
    "facebook.com",
    "expired.badssl.com"
]
```

---

## 🧪 Sample Output

```json
[
  {
    "domain": "google.com",
    "issuer": "Google Trust Services LLC",
    "valid_from": "2024-03-20",
    "valid_to": "2024-06-12",
    "days_left": 3,
    "status": "⚠️ Expiring Soon",
    "dns": {
      "CAA": ["0 issue \"pki.goog\""],
      "TXT": ["v=spf1 include:_spf.google.com ~all"]
    }
  }
]
```

---

## 🧠 Why Use ScanSafe?

- Prevent **SSL expiry** downtime
- Improve **DNS transparency** and security
- Demonstrate **real-world DevOps & Python skills**
- Enhance your GitHub & Resume with industry-useful tooling

---

## 🔮 Future Enhancements

- PDF / HTML report generation
- CLI input using `argparse`
- Docker support
- CI/CD integration
- Email or Slack alerts

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙋‍♂️ Author

**Abhishek Jain**  
DevOps | Python Developer | AI & ML Engineer  
[LinkedIn](https://www.linkedin.com/in/abhishekjain-ai)  
[GitHub](https://github.com/<your-username>)

---

> ⭐ Don’t forget to star the repo if you find it useful!



