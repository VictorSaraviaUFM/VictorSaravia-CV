import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, KeepTogether
from reportlab.lib.units import inch

NAVY, BLUE, LIGHT, GRAY, INK = HexColor("#0A1A3A"), HexColor("#1F5FD6"), HexColor("#DCE9FF"), HexColor("#4D5C78"), HexColor("#0A1A3A")
PHOTO = "assets/profile.jpg"  # set to your photo; if missing, a placeholder is drawn
W, H = letter
HEAD = 1.55 * inch
LINKS = [("saraviavi05@gmail.com", "mailto:saraviavi05@gmail.com"), ("+502 3050 0688", "tel:+50230500688"),
         ("LinkedIn", "https://www.linkedin.com/in/victor-saravia-75724937a/"), ("GitHub", "https://github.com/VictorSaraviaUFM")]

def header(c, d):
    c.saveState()
    c.setFillColor(NAVY); c.rect(0, H - HEAD, W, HEAD, stroke=0, fill=1)
    c.setFillColor(BLUE); c.rect(0, H - HEAD - 4, W, 4, stroke=0, fill=1)
    c.setFillColor(white); c.setFont("Helvetica-Bold", 26); c.drawString(0.55*inch, H - 0.7*inch, "Victor Saravia")
    c.setFillColor(HexColor("#9CC2FF")); c.setFont("Helvetica", 10.5)
    c.drawString(0.55*inch, H - 0.93*inch, "Computer Science Student | Software, Cloud, Testing & Data")
    c.setFont("Helvetica", 9); x, y = 0.55*inch, H - 1.2*inch
    c.setFillColor(white); c.drawString(x, y + 0.0, "Mixco, Guatemala")
    x += c.stringWidth("Mixco, Guatemala", "Helvetica", 9) + 10
    for label, url in LINKS:
        c.setFillColor(HexColor("#9CC2FF")); c.drawString(x, y, label)
        w = c.stringWidth(label, "Helvetica", 9); c.linkURL(url, (x, y - 2, x + w, y + 9), relative=0)
        x += w
        if label != "GitHub": c.setFillColor(white); c.drawString(x, y, "  |  "); x += c.stringWidth("  |  ", "Helvetica", 9)
    # photo (circle) at right
    cx, cy, r = W - 0.55*inch - 0.5*inch, H - HEAD/2, 0.5*inch
    if os.path.exists(PHOTO):
        p = c.beginPath(); p.circle(cx, cy, r); c.clipPath(p, stroke=0, fill=0)
        c.drawImage(PHOTO, cx - r, cy - r, 2*r, 2*r, preserveAspectRatio=True, anchor="c", mask="auto")
        c.restoreState(); c.saveState()
    else:
        c.setFillColor(HexColor("#12327A")); c.circle(cx, cy, r, stroke=0, fill=1)
        c.setFillColor(HexColor("#9CC2FF")); c.setFont("Helvetica", 9); c.drawCentredString(cx, cy - 3, "Photo")
    c.setStrokeColor(BLUE); c.setLineWidth(2.5); c.circle(cx, cy, r, stroke=1, fill=0)
    c.restoreState()

doc = BaseDocTemplate("assets/resume.pdf", pagesize=letter, title="Victor Saravia - Resume", author="Victor Saravia")
doc.addPageTemplates([PageTemplate(id="p", frames=[Frame(0.55*inch, 0.4*inch, W - 1.1*inch, H - HEAD - 0.6*inch, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)], onPage=header)])

body = ParagraphStyle("b", fontName="Helvetica", fontSize=8.6, leading=11, textColor=INK)
sec = ParagraphStyle("s", fontName="Helvetica-Bold", fontSize=10.5, leading=13, textColor=BLUE, spaceBefore=7, spaceAfter=2)
pt = ParagraphStyle("pt", parent=body, fontName="Helvetica-Bold", fontSize=9.4, leading=12, spaceBefore=3)
bl = ParagraphStyle("bl", parent=body, leftIndent=10, bulletIndent=0)
meta = ParagraphStyle("m", parent=body, textColor=GRAY, fontSize=8.2)
S = []
def H2(t):
    S.append(Paragraph(t, sec))
    from reportlab.platypus import HRFlowable
    S.append(HRFlowable(width="100%", thickness=0.8, color=BLUE, spaceAfter=3))

H2("Professional Summary")
S.append(Paragraph("Computer Science student at Universidad Francisco Marroquín entering my final year, with hands-on experience building software in teams: a full-stack app on AWS, a hospital queue system delivered through an automated Jenkins CI/CD pipeline, and a Lambda-architecture streaming data platform. Comfortable across SQL and NoSQL databases, cloud services, automated testing and data processing. I use AI to explore and prototype faster, then review and verify everything I ship. Academic focus: Machine Learning.", body))

H2("Projects")
def proj(name, link, label, sub, bullets):
    items = [Paragraph(f'{name} <font color="#4D5C78" size="8.2">| {sub}</font>  <link href="{link}" color="#1F5FD6">{label}</link>' if link else f'{name} <font color="#4D5C78" size="8.2">| {sub}</font>  <font color="#4D5C78" size="8.2">{label}</font>', pt)]
    items += [Paragraph(b, bl, bulletText="\u2022") for b in bullets]
    S.append(KeepTogether(items))
proj("Hospital Priority Queue", "https://github.com/anasofiaeggenberger/proyecto-final-calidad-automatizacion", "GitHub", "Python, Flask, Docker, Jenkins", [
 "Built a Flask web app, REST API and dashboard managing patient intake with a priority queue (1 = most urgent, 5 = least; FIFO on ties).",
 "Implemented layered automated testing (unit, integration, end-to-end) and a Jenkins CI/CD pipeline in Docker with quality gates.",
 "Demonstrates QA, test automation and CI/CD practices applied to a realistic triage scenario."])
proj("EXPOSE | Ephemeral-content social network", "https://github.com/jricica/EXPOSE", "GitHub", "React, TypeScript, Node.js, Express, AWS", [
 "Team-developed full-stack app with a layered REST API, JWT authentication, bcrypt password hashing and WebSockets.",
 "Worked with AWS DynamoDB, S3 and IAM for data, media storage and access control; Jest for testing.",
 "Practiced team Git workflows across frontend, backend, cloud and database layers."])
proj("Solar Pulso | Solar telemetry data platform", "", "Private Academic Project, repository available upon request", "Kafka/Redpanda, Spark, Delta Lake, Cassandra, Grafana", [
 "Team project implementing Lambda Architecture: Spark Structured Streaming plus a batch layer over Bronze/Silver/Gold data in Delta Lake and Parquet on MinIO.",
 "Served data through Cassandra, DuckDB and a FastAPI service, with Grafana dashboards for panels, meters, alerts and faults.",
 "Gained practical exposure to streaming vs. batch trade-offs in a multi-component architecture."])
proj("ProyectoWebDevelopment | Football statistics platform", "https://github.com/VictorSaraviaUFM/ProyectoWebDevelopment", "GitHub", "JavaScript, HTML/CSS, REST APIs", [
 "Integrated external football APIs to present player, team and match statistics alongside community posts and discussion.",
 "Built frontend and backend features around a product idea: community plus data."])

H2("Skills")
for k, v in [("Programming", "Python (primary); working knowledge of Java, TypeScript, JavaScript, SQL, HTML/CSS"),
 ("Databases", "SQL, PostgreSQL, MySQL; NoSQL models: key-value, document, time-series; Elasticsearch; DynamoDB, Cassandra and Redis in coursework"),
 ("Cloud", "AWS: IAM, RDS, DynamoDB, S3, Amplify (academic and project use)"),
 ("Engineering & DevOps", "Git, GitHub Workflows and Secrets, Docker, Jenkins, CI/CD"),
 ("Testing & Quality", "Unit, integration and end-to-end testing, test automation, quality gates, CI-based testing, Jest"),
 ("Big Data (academic project)", "Spark Structured Streaming, Kafka/Redpanda, Lambda Architecture, batch processing, Delta Lake, Parquet, MinIO, DuckDB, Grafana")]:
    S.append(Paragraph(f"<b>{k}:</b> {v}", ParagraphStyle("k", parent=body, spaceAfter=1.5)))

H2("Education")
S.append(Paragraph("<b>Universidad Francisco Marroquín</b>, Guatemala | B.S. in Computer Science, Machine Learning focus <font color='#4D5C78'>| 2024 - Present</font>", body))
S.append(Paragraph("<b>Colegio Decroly Americano</b> | Science and Humanities Diploma, High Honors, U.S.A. Presidential Award <font color='#4D5C78'>| 2012 - 2023</font>", body))

H2("Certifications, Languages & Interests")
S.append(Paragraph("<b>Certifications:</b> 7 Hábitos de la Gente Proactiva; Scrum Basics", body))
S.append(Paragraph("<b>Languages:</b> Spanish (native); English (advanced / fluent)", body))
S.append(Paragraph("<b>Working style:</b> analytical, organized, proactive and collaborative; leads when needed and works well under others' leadership. <b>Interests:</b> football, gym, economics, deep conversations.", body))
doc.build(S)
