// Edita este archivo para actualizar el contenido del sitio. No necesitas tocar el HTML.
window.SITE_DATA = {
  projects: [
    {
      name: "Hospital Priority Queue",
      area: "QA · Test Automation · CI/CD",
      status: "Public",
      repo: "https://github.com/anasofiaeggenberger/proyecto-final-calidad-automatizacion",
      description: "Flask web app that manages hospital patient intake with a priority queue: priority 1 is most urgent, 5 least, and ties are served first-in-first-out.",
      tech: ["Python", "Flask", "Docker", "Jenkins"],
      highlights: [
        "Layered test strategy: unit, integration and end-to-end tests over a REST API and dashboard.",
        "Jenkins pipeline in Docker with quality gates that block a build when tests fail.",
        "Applied a data structure (priority queue with FIFO tie-breaking) to a realistic triage scenario."
      ]
    },
    {
      name: "EXPOSE",
      area: "Full-stack · Cloud · APIs",
      status: "Public",
      repo: "https://github.com/jricica/EXPOSE",
      description: "Team-built social network for ephemeral content, running on a layered Node.js backend with AWS storage and real-time features.",
      tech: ["React", "TypeScript", "Node.js / Express", "DynamoDB", "S3"],
      highlights: [
        "Layered REST API with JWT authentication and bcrypt password hashing.",
        "AWS services in use: DynamoDB for data, S3 for media, IAM for access control; WebSockets for real-time updates.",
        "Jest tests and shared Git workflow in a multi-person team."
      ]
    },
    {
      name: "Solar Pulso",
      area: "Big Data · Streaming · Batch",
      status: "Private Academic Project",
      repo: "",
      repoNote: "Repository available upon request",
      description: "Data platform for solar panel and meter telemetry (alerts, faults, events) built with Lambda Architecture and run locally.",
      tech: ["Redpanda / Kafka", "Spark Structured Streaming", "Delta Lake", "Cassandra", "Grafana"],
      highlights: [
        "Streaming and batch layers over a Bronze / Silver / Gold data organization stored as Delta Lake and Parquet on MinIO.",
        "Serving layer with Cassandra, DuckDB and a FastAPI service; Grafana dashboards for monitoring.",
        "Team project: hands-on exposure to the trade-offs of a multi-component data architecture."
      ]
    },
    {
      name: "ProyectoWebDevelopment",
      area: "Web Development · APIs · Product",
      status: "Public",
      repo: "https://github.com/VictorSaraviaUFM/ProyectoWebDevelopment",
      description: "Football statistics platform that pairs players, teams and match data with a community space for posts and discussion.",
      tech: ["JavaScript", "HTML/CSS", "REST APIs"],
      highlights: [
        "Integrated external football APIs to present player, team and match statistics.",
        "Built frontend and backend features around a clear product idea: community plus data."
      ]
    }
  ],
  skills: [
    { group: "Programming", note: "Primary: Python", items: ["Python", "Java", "TypeScript", "JavaScript", "SQL", "HTML/CSS"], detail: "Working knowledge in all but Python." },
    { group: "Databases", note: "Concepts first, tools second", items: ["SQL", "PostgreSQL", "MySQL", "Key-Value", "Document", "Time-Series", "Elasticsearch"], detail: "Relational and NoSQL data models; DynamoDB, Cassandra and Redis used in coursework." },
    { group: "Cloud", note: "AWS, academic and project use", items: ["IAM", "RDS", "DynamoDB", "S3", "Amplify"], detail: "" },
    { group: "Engineering & DevOps", note: "", items: ["Git", "GitHub Workflows", "GitHub Secrets", "Docker", "Jenkins", "CI/CD"], detail: "" },
    { group: "Testing & Quality", note: "A differentiator", items: ["Unit Testing", "Integration Testing", "E2E", "Test Automation", "Quality Gates", "Jest"], detail: "" },
    { group: "Big Data", note: "Academic project experience", items: ["Spark Structured Streaming", "Kafka / Redpanda", "Lambda Architecture", "Batch Processing", "Delta Lake"], detail: "" }
  ],
  education: [
    { school: "Universidad Francisco Marroquín", period: "2024 – Present", title: "B.S. in Computer Science", detail: "Academic focus: Machine Learning. Entering final year. Additional coursework in economics (microeconomics, Austrian economics, public choice)." },
    { school: "Colegio Decroly Americano", period: "2012 – 2023", title: "Science and Humanities Diploma", detail: "High Honors · U.S.A. Presidential Award" }
  ],
  certifications: [
    { name: "7 Hábitos de la Gente Proactiva", issuer: "[Add issuer]", date: "[Add date]", link: "" },
    { name: "Scrum Basics", issuer: "[Add issuer]", date: "[Add date]", link: "" }
  ]
};
