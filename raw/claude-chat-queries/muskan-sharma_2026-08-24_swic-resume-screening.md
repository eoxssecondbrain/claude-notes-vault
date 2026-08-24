---
thread_name: "swic-resume-screening"
user: "muskan-sharma"
type: claude-chat
created: 2026-08-24
updated: 2026-08-24
---

[Prior turns preserved from earlier saves in this thread: JD + hard requirements from user; Candidate 1 Rizwan Dirisina 3/10 DISQUALIFY; Candidate 2 Kuldeep Sharma 2/10 DISQUALIFY (submitted twice, same verdict); Candidate 3 Deepak Kumar 7/10 QUALIFY; Candidate 4 Monisha R 6/10 QUALIFY with reservations; Candidate 5 Abhilasha Kumari Singh 7/10 QUALIFY; Candidate 6 Abhishek Mishra 6/10 QUALIFY with scale-mismatch caveat; Candidate 7 Kapil Singhal 4/10 DISQUALIFY due to JD-mirrored resume language plus recent job-hopping; Candidate 8 Rishikesh Gade 7/10 QUALIFY, strongest technical/EDI profile, weak on training evidence; Candidate 9 Samaloy Hazarika 7/10 QUALIFY, best SMB/adoption-monitoring adjacency; Candidate 10 Ravisankar P V 5/10 QUALIFY borderline, weak technical/API depth; Candidate 11 Vengadatchary Ragounadane (Chari R.V.) 1/10 DISQUALIFY, senior engineering executive with no client-implementation experience, total seniority/scope mismatch.]

**User:**
[Uploaded resume PDF: Nalini Naik — Implementation Specialist, eClinicalWorks]

NALINI NAIK
Implementation Specialist | SaaS & Cloud Operations
Immediate Joiner | 8.5+ Years Experience
Email: nalinimsurvase@gmail.com | Mobile: +91-9403535632 | LinkedIn: Nalini Naik
Address: Pune, Maharashtra, India

PROFESSIONAL SUMMARY
Results-driven Implementation Specialist with 8.5+ years of experience in SaaS-based healthcare product implementations and production support. Strong expertise in Apache Tomcat administration, database deployments (MySQL & MSSQL), patch management, server troubleshooting, and client coordination. Proven ability to manage end-to-end deployments, optimize system performance, and ensure high availability in enterprise environments. Currently pursuing AWS Cloud Practitioner and Solutions Architect certifications with a strong interest in transitioning into cloud-focused roles.

CORE SKILLS
Application Deployment & Implementation; Apache Tomcat Installation, Tuning & Troubleshooting; SaaS Environment Support; Patch Deployment (Chef); Database Deployment, Backup & Restoration; MySQL & Microsoft SQL Server; SQL Scripting & Data Validation; Windows & Linux Server Administration; FTP Server Configuration; Client & Vendor Coordination; Production Support & Go-Live Management; Incident & Root Cause Analysis; Cloud Fundamentals (AWS – In Progress)

PROFESSIONAL EXPERIENCE
Implementation Specialist — eClinicalWorks–Mumbai, India — (May 2017 – Sept 2025)
Key Responsibilities & Achievements:
Led end-to-end implementation and deployment of healthcare SaaS applications for multiple clients, ensuring on-time go-lives and system stability.
Performed manual Apache Tomcat installations, configuration, tuning, and troubleshooting in production and SaaS environments.
Executed patch deployments using Chef, ensuring minimal downtime and compliance with release standards.
Handled database deployments using Microsoft SQL Server and MySQL, including schema updates, data migration, and validation.
Designed and executed database backup and restoration strategies using scripts for MySQL and MSSQL to ensure data integrity and disaster recovery.
Configured and managed FTP servers on Windows, enabling secure file transfers between applications and client systems.
Provided production and post-go-live support, performing root cause analysis and resolving application, server, and database issues.
Installed and supported FAX services using WinSCP, PuTTY, and Linux commands, ensuring reliable document transmission.
Coordinated closely with clients, vendors, deployment teams, and support teams to ensure correct functionality and client satisfaction.
Created and maintained technical documentation and SOPs, improving implementation efficiency and reducing recurring issues.
Mentored junior team members and supported cross-team collaboration for faster issue resolution.

Tools & Technologies: Apache Tomcat, Chef, SQL Server Management Studio (SSMS), MySQL, MSSQL, WinSCP, PuTTY, FTP, Windows Server, Linux

Education
Bachelor of Engineering (BE) | P.E.S. Modern College of Engineering, Pune (2013 - 2016)

CERTIFICATIONS & LEARNING
CDAC-PGDAC (Post Graduation Diploma in Advanced Computing)
AWS Certified Cloud Practitioner – In Progress
AWS Solutions Architect (Associate) – In Progress

TECHNICAL SKILLS
Application & Middleware: Apache Tomcat
Databases: MySQL, Microsoft SQL Server
Scripting & Queries: SQL (SELECT, INSERT, UPDATE, DELETE, JOIN)
Servers & OS: Windows, Linux
DevOps / Deployment: Chef, Patch Management
Tools: WinSCP, PuTTY, FTP Tools, RDP, SSMS, MS Office

"check"

**Assistant:**
**Nalini Naik — Implementation Specialist, eClinicalWorks**

Score: 4/10
Decision: DISQUALIFY

Personally implemented software: Partially demonstrated, but the flavor of "implementation" here is notably different from what the JD needs. "Led end-to-end implementation and deployment of healthcare SaaS applications for multiple clients, ensuring on-time go-lives and system stability" is real first-person ownership language. But nearly every supporting bullet is infrastructure/ops work — Apache Tomcat installation and tuning, Chef patch deployment, database backup/restoration scripting, FTP server configuration, WinSCP/PuTTY/Linux administration. This reads as an IT/systems deployment specialist keeping a healthcare SaaS platform running and installed correctly, not someone mapping a client's business workflows (quoting, inventory, order desk) into the software and configuring it around how the business actually operates. It's implementation in the infrastructure sense, not the business-process sense the JD is asking for.

Hands-on technical work: Strong on the database/SQL side — "SQL Scripting & Data Validation," explicit SELECT/INSERT/UPDATE/DELETE/JOIN work, data migration and schema updates, backup/restoration design. But there is no mention anywhere of APIs, webhooks, or software/data integrations — a real, direct gap against a hard requirement the JD names explicitly. The technical skill set here is server/database administration, not integration work.

Training skeptical non-technical users / driving adoption: Not demonstrated at all — this is the clearest gap. There is no training bullet anywhere in the resume. The client-facing work described is "Client & Vendor Coordination" and "coordinated closely with clients, vendors, deployment teams, and support teams to ensure correct functionality" — this reads as IT-to-IT coordination with a client's technical staff, not end-user enablement, let alone getting skeptical, non-technical floor-level people to actually use a new tool day to day. Given this is one of your four explicit hard requirements, its complete absence here is disqualifying on its own terms.

Job stability: Excellent on paper — a single employer (eClinicalWorks) for 8.5 years (May 2017–Sept 2025), the longest single tenure of any candidate reviewed today. Worth noting: the resume is tagged "Immediate Joiner" and her employment ended nearly a year ago (Sept 2025, vs. today's date of Aug 2026), with no explanation for the gap — worth a direct question, though not a disqualifier on its own.

Nice-to-haves: None. eClinicalWorks is a large, established healthcare EHR vendor — not industrial/distribution, not early-stage, and the work described (server/database admin for an internal SaaS platform) doesn't show a high-ownership, client-adoption-driving environment.

Net: strong technical database/SQL skills and outstanding tenure at one company, but the profile reads as an infrastructure deployment engineer, not a business-implementation consultant who trains end users and drives adoption — and that gap sits directly on one of your four hard requirements plus the API/integration half of another.

Send the next one.
