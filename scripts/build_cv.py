"""Builds the ATS-friendly CV (real text, clickable links, photo in header).
   pip install reportlab pillow  &&  python scripts/build_cv.py
Photo: save yours as assets/profile.jpg (square-ish, face centered). Without it, an initials badge is drawn."""
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, KeepTogether

# ---------- CONFIG ----------
PORTFOLIO_URL = ""   # e.g. "https://your-site.vercel.app" (adds a Portfolio link in the header)
GITHUB = "https://github.com/VictorSaraviaUFM"
LINKEDIN = "https://www.linkedin.com/in/victor-saravia-75724937a/"
HERE = os.path.dirname(os.path.abspath(__file__))
PHOTO = os.path.join(HERE, "..", "assets", "profile.jpg")
OUT = os.path.join(HERE, "..", "assets", "resume.pdf")

NAVY, BLUE, MID, SOFT, GRAY, INK, LB = (HexColor(c) for c in ("#0A1A33", "#1D4ED8", "#2F7CF0", "#DCE9FA", "#4B5B75", "#0F172A", "#9CC4F5"))
F, FB, FI = "Helvetica", "Helvetica-Bold", "Helvetica-Oblique"
def S(n, **k):
    return ParagraphStyle(n, fontName=k.pop("fontName", F), fontSize=k.pop("fontSize", 8.6), leading=k.pop("leading", 10.8), textColor=k.pop("textColor", INK), **k)
body, h = S("b"), S("h", fontName=FB, fontSize=9.4, leading=11.5, textColor=BLUE, spaceBefore=5)
bul = S("bu", leftIndent=10, bulletIndent=1)
ptitle = S("pt", fontName=FB, fontSize=9.1, leading=11.2, textColor=NAVY, spaceBefore=2.5)
pmeta = S("pm", fontSize=8, leading=10, textColor=GRAY, fontName=FI)
A = lambda u, t: f'<a href="{u}" color="#1D4ED8">{t}</a>'
B = lambda t: f"<font name='{FB}' color='#0A1A33'>{t}</font>"
def section(t): return [Paragraph(t.upper(), h), HRFlowable(width="100%", thickness=1, color=MID, spaceBefore=1, spaceAfter=2.5)]
def project(title, meta, items):
    return KeepTogether([Paragraph(title, ptitle), Paragraph(meta, pmeta)] + [Paragraph(i, bul, bulletText="•") for i in items])

BAND = 92  # header band height (pt)
def header(c, doc):
    W, H = letter
    c.saveState(); c.setFillColor(NAVY); c.rect(0, H - BAND, W, BAND, stroke=0, fill=1)
    c.setFillColor(MID); c.rect(0, H - BAND - 3, W, 3, stroke=0, fill=1)
    x = 0.55 * inch
    c.setFillColor(white); c.setFont(FB, 24); c.drawString(x, H - 36, "Victor Saravia")
    c.setFillColor(LB); c.setFont(FB, 9.3); c.drawString(x, H - 52, "Computer Science Student  |  Software Engineering · Cloud · Testing · Big Data")
    items = [("Mixco, Guatemala", None), ("saraviavi05@gmail.com", "mailto:saraviavi05@gmail.com"), ("+502 3050 0688", "tel:+50230500688"),
             ("LinkedIn", LINKEDIN), ("GitHub", GITHUB)] + ([("Portfolio", PORTFOLIO_URL)] if PORTFOLIO_URL else [])
    cx, cy = x, H - 70; c.setFont(F, 8.4)
    for i, (t, u) in enumerate(items):
        c.setFillColor(LB if u else HexColor("#C9D6EA")); c.drawString(cx, cy, t); w = stringWidth(t, F, 8.4)
        if u: c.linkURL(u, (cx, cy - 2, cx + w, cy + 9), relative=0)
        cx += w
        if i < len(items) - 1: c.setFillColor(HexColor("#5C7BAA")); c.drawString(cx, cy, "  |  "); cx += stringWidth("  |  ", F, 8.4)
    # photo (circle) on the right
    d, px, py = 66, W - 0.55 * inch - 66, H - BAND / 2 - 33
    c.saveState(); p = c.beginPath(); p.circle(px + d / 2, py + d / 2, d / 2); c.clipPath(p, stroke=0, fill=0)
    if os.path.exists(PHOTO):
        from PIL import Image
        im = Image.open(PHOTO); w, hh = im.size; s = min(w, hh)       # center-crop to square
        im = im.crop(((w - s) // 2, (hh - s) // 6 if hh > w else 0, (w - s) // 2 + s, (hh - s) // 6 + s if hh > w else s)).convert("RGB")
        c.drawInlineImage(im, px, py, d, d)
    else:
        c.setFillColor(HexColor("#12305C")); c.rect(px, py, d, d, stroke=0, fill=1)
        c.setFillColor(LB); c.setFont(FB, 24); c.drawCentredString(px + d / 2, py + d / 2 - 8, "VS")
    c.restoreState(); c.setStrokeColor(MID); c.setLineWidth(1.6); c.circle(px + d / 2, py + d / 2, d / 2, stroke=1, fill=0)
    c.restoreState()

st = []
st += section("Summary")
st.append(Paragraph(
 "Computer Science student starting a final year at Universidad Francisco Marroquín (academic focus: Machine Learning). Through team-built academic projects I have worked hands-on with "
 "AWS (S3, DynamoDB, RDS, IAM, Amplify), SQL and NoSQL databases, REST APIs, test automation with Jenkins and GitHub workflows, and a Lambda-architecture data platform. "
 "Analytical, organized and collaborative; AI-assisted, human-verified: I question, review and test what AI suggests and make sure I understand what I ship.", body))

st += section("Projects")
st.append(project("EXPOSE — Anonymous, Ephemeral Social Network &nbsp;" + A("https://github.com/jricica/EXPOSE", "github.com/jricica/EXPOSE"),
 "Full-stack team project (4 contributors) · React, TypeScript, Node.js, Express, DynamoDB, S3, WebSockets, Jest",
 ["Built, with a team of four, a full-stack app with self-deleting posts, comments, uploads, moderation and real-time updates (WebSockets).",
  "Applied a layered backend (controllers, services, repositories, middleware) exposing REST APIs secured with JWT and bcrypt.",
  "Integrated AWS DynamoDB and S3 through the AWS SDK with IAM-managed access; covered logic with Jest tests."]))
st.append(project("Hospital Priority Queue — Software Quality, Testing &amp; CI/CD &nbsp;" + A("https://github.com/anasofiaeggenberger/proyecto-final-calidad-automatizacion", "GitHub"),
 "Team project · Flask, REST API, Docker, Jenkins",
 ["Developed a Flask dashboard and REST API for hospital triage using a 1–5 priority queue with FIFO ordering within equal priorities.",
  "Designed layered automated testing (unit, integration, end-to-end) to verify ordering rules and API behavior.",
  "Containerized the app with Docker and automated builds and tests in a Jenkins pipeline enforcing quality gates."]))
st.append(project("Solar Pulso — Lambda-Architecture Data Platform &nbsp;<font size=7.8 color='#4B5B75'>Private Academic Project · repository available upon request</font>",
 "Big Data course team project · Redpanda/Kafka, Spark Structured Streaming, Delta Lake, MinIO, Cassandra, DuckDB, FastAPI, Grafana",
 ["Contributed to a platform for solar-panel telemetry, meters, alerts, faults and events, combining streaming and batch processing layers.",
  "Worked with Redpanda ingestion, Spark Structured Streaming and Bronze/Silver/Gold storage in Delta Lake and Parquet on MinIO.",
  "Served results through Cassandra, DuckDB and FastAPI, with Grafana dashboards for monitoring."]))
st.append(project("Football Statistics &amp; Community Platform &nbsp;" + A("https://github.com/VictorSaraviaUFM/ProyectoWebDevelopment", "GitHub"),
 "Web Development course project",
 ["Built a web platform that combines match, player and team statistics (external API integration) with fan posts and discussion.",
  "Worked across frontend, backend and data around a clear product idea: reliable stats plus community."]))

st += section("Technical Skills")
for k, v in [("Programming", "Primary: Python &nbsp;·&nbsp; Working knowledge: Java, TypeScript, JavaScript, SQL, HTML/CSS"),
             ("Databases", "Relational and NoSQL modeling; SQL (PostgreSQL, MySQL); NoSQL: key-value, document, time-series concepts, Elasticsearch; DynamoDB, Cassandra, Redis (academic)"),
             ("Cloud", "AWS (project use): IAM, RDS, DynamoDB, S3, Amplify"),
             ("Engineering &amp; DevOps", "Git, GitHub Workflows and Secrets, Docker, Jenkins, CI/CD"),
             ("Testing &amp; Quality", "Unit, integration and E2E testing, test automation, QA, quality gates, Jest"),
             ("Big Data (academic)", "Spark Structured Streaming, Kafka/Redpanda, Lambda architecture, batch processing, Delta Lake, Parquet, MinIO, DuckDB, Grafana")]:
    st.append(Paragraph(f"{B(k + ':')} {v}", S("s", leading=10.8)))

st += section("Education")
st.append(Paragraph(f"{B('Universidad Francisco Marroquín')}, Guatemala — B.S. Computer Science Engineering, focus: Machine Learning &nbsp;<font color='#4B5B75'>2024 – Present</font>", body))
st.append(Paragraph("Coursework: Data Structures, Algorithms &amp; Complexity, Software Engineering, Web Development, QA &amp; Software Quality Automation, Databases, Data Science, Big Data Processing, Cloud Architecture, Distributed Systems.", body))
st.append(Paragraph(f"{B('Colegio Decroly Americano')} — Bachillerato en Ciencias y Letras &nbsp;<font color='#4B5B75'>2012 – 2023</font> · High Honors; U.S.A. Presidential Award", body))

st += section("Certifications &amp; Licenses")
st.append(Paragraph("Scrum Basics &nbsp;·&nbsp; 7 Hábitos de la Gente Proactiva", body))
st += section("Languages &amp; Interests")
st.append(Paragraph(f"{B('Languages:')} Spanish (native) · English (advanced / fluent) &nbsp;&nbsp;{B('Interests:')} football, strength training", body))
st.append(Paragraph(f"{B('Additional academic interests:')} economics (incentives, coordination, cost-aware decision making).", body))

os.makedirs(os.path.dirname(OUT), exist_ok=True)
SimpleDocTemplate(OUT, pagesize=letter, leftMargin=0.55*inch, rightMargin=0.55*inch, topMargin=BAND + 10, bottomMargin=0.35*inch,
                  title="Victor Saravia - Resume", author="Victor Saravia").build(st, onFirstPage=header, onLaterPages=header)
print("built", os.path.abspath(OUT))
