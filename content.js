/* ALL SITE CONTENT LIVES HERE. Edit this file to add projects, certificates, skills, experience.
   script.js renders it into index.html. */
window.CONTENT = {
  profile: {
    name: "Victor Saravia",
    headline: "Computer Science student · Software, Cloud, Testing & Data",
    tagline: "I build software the way real teams do: cloud-backed, tested and automated. I'm here to build, contribute and learn alongside people who care about doing it well.",
    photo: "assets/profile.jpg",           // replace this file with your photo
    resume: "assets/resume.pdf",
    email: "saraviavi05@gmail.com",
    phone: "+502 3050 0688",
    phoneHref: "+50230500688",
    linkedin: "https://www.linkedin.com/in/victor-saravia-75724937a/",
    github: "https://github.com/VictorSaraviaUFM",   // confirm this is your public profile
    location: "Mixco, Guatemala"
  },
  about: [
    "I'm a Computer Science engineering student at Universidad Francisco Marroquín, starting my final year with an academic focus on Machine Learning. My project work has been hands-on with real tooling: AWS (S3, DynamoDB, RDS, IAM, Amplify), SQL and NoSQL databases, REST APIs, Jenkins and GitHub workflows, and a Lambda-architecture data platform.",
    "I use AI tools to move faster and explore ideas, then verify: I question the output, review the code and make sure I understand what ships. I'm curious and organized, and I like to go beyond the brief when I can add value. I'm comfortable leading when needed and just as comfortable following someone better placed to lead."
  ],
  traits: [
    ["Analytical", "I question assumptions and weigh cost and trade-offs."],
    ["Collaborative", "Three of my four main projects were built in teams."],
    ["Proactive", "I take initiative beyond what is strictly asked."],
    ["Responsible", "I own mistakes and look for improvements early."]
  ],
  projects: [
    { name: "EXPOSE", type: "Anonymous, ephemeral social network", area: "Full-Stack · Cloud", status: "Public", team: "Team of 4",
      summary: "Full-stack platform where posts disappear automatically, with comments, uploads, moderation and real-time updates.",
      flow: ["React + TypeScript", "Express API", "DynamoDB + S3"],
      highlights: ["Layered backend: controllers, services, repositories, middleware", "REST APIs with JWT authentication and bcrypt; real-time updates over WebSockets", "AWS SDK integration with DynamoDB, S3 and IAM; Jest tests"],
      tags: ["React", "TypeScript", "Node.js", "AWS", "Jest"], repo: "https://github.com/jricica/EXPOSE" },
    { name: "Hospital Priority Queue", type: "Software quality & test automation", area: "QA · CI/CD", status: "Public", team: "Team project",
      summary: "Flask web app and REST API that manages patient care by urgency: priority 1 (highest) to 5, FIFO within the same priority.",
      flow: ["Flask API + dashboard", "Layered tests", "Docker → Jenkins"],
      highlights: ["Unit, integration and end-to-end tests organized in layers", "Jenkins pipeline with quality gates over a Dockerized build", "Clear domain rules (priority + FIFO) verified through automated tests"],
      tags: ["Flask", "Docker", "Jenkins", "E2E testing"], repo: "https://github.com/anasofiaeggenberger/proyecto-final-calidad-automatizacion" },
    { name: "Solar Pulso", type: "Lambda-architecture data platform", area: "Big Data", status: "Private Academic Project", team: "Team project",
      summary: "Data platform for solar panels, meters, alerts, faults and events, combining streaming and batch processing with analytics and monitoring.",
      flow: ["Redpanda → Spark Streaming", "Bronze/Silver/Gold on MinIO", "FastAPI + Grafana"],
      highlights: ["Streaming and batch layers following Lambda architecture", "Delta Lake and Parquet storage in Bronze/Silver/Gold layers", "Serving with Cassandra, DuckDB and FastAPI; Grafana dashboards"],
      tags: ["Spark", "Kafka/Redpanda", "Delta Lake", "Grafana"], repo: "" , note: "Repository available upon request" },
    { name: "Football Statistics Platform", type: "Stats and community web app", area: "Web · APIs", status: "Public", team: "Course project",
      summary: "Web platform that brings match, player and team statistics together with a space for fan posts and discussion.",
      flow: ["External stats APIs", "Backend", "Web frontend"],
      highlights: ["Integration of external APIs for match, player and team data", "Frontend and backend work around a clear product idea: data plus community"],
      tags: ["Web development", "APIs"],   /* TODO: add the real stack */
      repo: "https://github.com/VictorSaraviaUFM/ProyectoWebDevelopment" }
  ],
  skills: [
    { group: "Programming", items: [["Primary", "Python"], ["Working knowledge", "Java · TypeScript · JavaScript · SQL · HTML/CSS"]] },
    { group: "Databases", items: [["Concepts", "Relational vs. NoSQL modeling, trade-offs"], ["SQL", "PostgreSQL · MySQL"], ["NoSQL", "Key-value · Document · Time-series concepts · Elasticsearch"], ["Used academically", "DynamoDB · Cassandra · Redis"]] },
    { group: "Cloud", items: [["AWS (academic / project use)", "IAM · RDS · DynamoDB · S3 · Amplify"]] },
    { group: "Engineering & DevOps", items: [["Practices", "Git · GitHub Workflows & Secrets · Docker · Jenkins · CI/CD"]] },
    { group: "Testing & Quality", items: [["Practices", "Unit · Integration · E2E · Test automation · QA · Quality gates"], ["Tools", "Jest · Jenkins"]] },
    { group: "Big Data", items: [["Academic project experience", "Spark Structured Streaming · Kafka/Redpanda · Lambda architecture · Batch processing · Delta Lake · Parquet · MinIO · DuckDB · Grafana"]] }
  ],
  education: [
    { school: "Universidad Francisco Marroquín", detail: "B.S. Computer Science Engineering · Academic focus: Machine Learning · entering final year", dates: "2024 – Present",
      extra: "Coursework: Data Structures, Algorithms & Complexity, Software Engineering, Web Development, QA & Software Quality Automation, Databases, Data Science, Big Data Processing, Cloud Architecture, Distributed Systems." },
    { school: "Colegio Decroly Americano", detail: "Bachillerato en Ciencias y Letras · High Honors · U.S.A. Presidential Award", dates: "2012 – 2023", extra: "" }
  ],
  languages: "Spanish — Native · English — Advanced / Fluent",
  certifications: [   /* copy an entry to add more; leave link "" if none */
    { name: "Scrum Basics", issuer: "[ISSUER]", date: "[DATE]", link: "" },
    { name: "7 Hábitos de la Gente Proactiva", issuer: "[ISSUER]", date: "[DATE]", link: "" }
  ],
  interests: [
    ["Football & strength training", "Team sport and the gym five days a week keep me consistent and disciplined."],
    ["Economics", "Coursework in microeconomics, Austrian economics and public choice: individuals as the unit of analysis, incentives and coordination. It shapes how I question assumptions and think about cost."],
    ["Learning from people who build", "I study how successful people work, and how projects fail, to learn from both."]
  ]
};
