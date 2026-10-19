# KAIROS 2027 (Grand Edition) — Hands-On AWS Builder & Website Workspace

**Document Reference:** `teams/05_hands_on_aws_builder_and_website/README.md`  
**Host Entity:** AWS Student Builder Group (AWS SBG) — SIST Chapter  
**Sponsoring Department:** School of Computing, Sathyabama Institute of Science and Technology, Chennai – 600119  
**Technical Team Lead:** **Rikish P** (Technical Team Lead, Reg: `44110664`)  
**Technical Leads:** **Viswanathan Ashok** (Hands-On Builder Lead, Reg: `44110907`, Phone: `+91 9080809088`) & **Shanmugapriyan S** (Technical Team Lead, Reg: `44111257`, Phone: `+91 7550091864`)  
**Executive Review:** **Thenappan T** (President & SBGL, Reg: `44110855`, Phone: `+91 6381801640`)  
**Production URL:** `https://kairos.sathyabama.ac.in`  
**Governing Standards (Executive Planning Framework):** `DOC-00 (Master Brief)` · `DOC-02 (Agenda & Judging Rubrics)` · `DOC-16 (Website Design Specification)` · `DOC-19 (Operations & Logistics CRUD)`  
**Status:** `CONFIRMED MASTER OPERATING STANDARD`  

---

## 1. Team Charter & Operational Scope

### 1.1 Mission & Technical Mandate
Division 5 is the technological powerhouse of KAIROS 2027. It designs, engineers, deploys, and maintains the full-stack cloud ecosystem supporting 2,000+ applicant teams, 100 on-ground finalist teams, 25+ industry jury evaluators, and thousands of public viewers. The team guarantees zero downtime, sub-250ms API response latency, automated AWS Bedrock sandbox orchestration, and unbiased Z-score mathematical scoring normalization.

### 1.2 Core Mandates & Engineering KPIs
- **Production Web Portal:** Deploy Next.js 14 App Router portal at `https://kairos.sathyabama.ac.in` with 100% Lighthouse accessibility and SEO scores.
- **AWS Bedrock Sandboxes:** Provision 100 isolated AWS accounts via AWS Organizations with automated SCP budgets ($500 limit/team) and pre-enabled Claude 3.5 Sonnet / Amazon Titan access.
- **High Concurrency Target:** Registration webhooks and live WebSocket leaderboard endpoints engineered to sustain **10,000 requests per second (RPS)** with < 250ms p99 latency.
- **Mathematical Judging Normalization:** Zero raw score bias; automated Z-score standardization across all evaluation tracks.
- **Continuous Zero-Downtime SLA:** 99.99% uptime throughout the continuous 48-hour on-ground sprint.

### 1.3 Operational Boundaries (Scope of Control)
- **What This Team Controls:** Next.js frontend, AWS Lambda serverless APIs, DynamoDB single-table design, ElastiCache Redis clusters, Bedrock IAM roles, judging portal frontend/backend, Devfolio webhook intake, and Discord bot roles.
- **What This Team Does NOT Control:**
  - *No Graphic Design Creation:* SVG icons, brand colors, and visual motifs are designed by Division 2 (Design). Builder squad consumes Figma tokens.
  - *No Physical LAN Cabling or Switch Drops:* Venue floor Cat6 Ethernet patching and arena Wi-Fi 6 physical access point mounting are handled by Division 6 (Operations).
  - *No Commercial Cloud Credit Procurement:* The $50,000+ AWS credit voucher grants are negotiated by Nikki (Sponsorship Lead) (Division 1). This squad handles programmatic account allocation.

---

## 2. Internal RACI Responsibility Map

```
+------------------------------------------+-------+-------+-------+-------+-------+-------+
| Engineering Deliverable / Workstream     | Rikish| Viswa.| Shan. | Cloud | Front | Pres. |
|                                          | (Tech)| (Lead)| (Eng.)| Lead  | Lead  | Then. |
+------------------------------------------+-------+-------+-------+-------+-------+-------+
| Next.js 14 Portal & Route Architecture   |   A   |   R   |   C   |   I   |   R   |   I   |
| AWS Bedrock Accounts & SCP Budget Guards |   A   |   C   |   R   |   R   |   I   |   C   |
| Devfolio / Form Webhook Applicant Intake |   C   |   A   |   R   |   C   |   R   |   I   |
| Real-time WebSocket Leaderboard Engine   |   A   |   R   |   R   |   C   |   R   |   I   |
| Z-Score Scoring Normalization Algorithm  |   A   |   R   |   C   |   I   |   C   |   C   |
| CloudFront WAF & DDoS Protection Tuning  |   A   |   I   |   R   |   R   |   I   |   I   |
| Post-Event Finalist Code Archival (S3)   |   C   |   A   |   R   |   R   |   I   |   I   |
+------------------------------------------+-------+-------+-------+-------+-------+-------+
```

---

## 3. Technical Stack & Cloud Architecture

```text
+-------------------------------------------------------------------------------------------------------+
|                                    KAIROS 2027 FULL CLOUD STACK                                       |
+-------------------+-----------------------------------------------------------------------------------+
| LAYER             | TECHNOLOGIES & SERVICES DEPLOYED                                                  |
+-------------------+-----------------------------------------------------------------------------------+
| Web Frontend      | Next.js 14 (App Router), TypeScript, Tailwind CSS, Framer Motion, Lucide React    |
| Edge & CDN        | Amazon CloudFront, AWS WAF (Web Application Firewall), Amazon Route 53            |
| Compute / Backend | AWS Lambda (Node.js 20.x / Python 3.12), Amazon API Gateway (REST & WebSockets)   |
| Database & State  | Amazon DynamoDB (Single-table design), Amazon ElastiCache (Redis for Leaderboard)|
| Generative AI Hub | Amazon Bedrock (Anthropic Claude 3.5 Sonnet, Amazon Titan, Meta Llama 3 70B)      |
| Storage & Media   | Amazon S3 (Static assets, participant code zip uploads, resume storage)           |
| Communications    | Amazon SES (Automated registration emails & confirmations)                        |
+-------------------+-----------------------------------------------------------------------------------+
```

---

## 4. The 4 Core Engineering Pipelines

1. **Production Web Application (`website_frontend_source/`):** Next.js 14 App Router portal with live 48-hour terminal countdown, interactive problem statement modal, and responsive dark-mode UI.
2. **Cloud Sandboxes & Bedrock (`cloud_sandboxes_and_bedrock/`):** Automated AWS Organizations vending machine script creating 100 sandbox accounts with pre-applied IAM permission boundaries and budget alarm triggers.
3. **Judging & Leaderboard Engine (`judging_and_leaderboard_engine/`):** Real-time judge evaluation UI applying statistical Z-score normalization:
   $$Z_{ij} = \frac{X_{ij} - \mu_j}{\sigma_j}$$
   where $X_{ij}$ is raw score of team $i$ by judge $j$, eliminating lenient and harsh grading skews.
4. **Registration Pipeline (`registration_and_screening_pipeline/`):** Automated Devfolio webhook ingestion, resume parsing, and Discord member verification bot.

---

## 5. Engineering Lifecycle & Operating Cadence

### 5.1 5-Phase Technical Roadmap
1. **Phase 1: Architecture Lock (T-90 to T-60 Days):** DDL schemas, DynamoDB single-table design, and API contracts frozen.
2. **Phase 2: Alpha Web Launch (T-60 Days):** `kairos.sathyabama.ac.in` live for Round 0 national applications.
3. **Phase 3: Sandbox Load Testing (T-14 Days):** 100 AWS sandbox accounts provisioned and tested against Bedrock rate limits.
4. **Phase 4: Live Arena Execution (Event Window Jan 22–24):** Zero-downtime monitoring, WebSocket live stream telemetry, real-time judge scoring intake.
5. **Phase 5: Code Archive & S3 Freeze (T+1 to T+7 Days):** Finalist GitHub repos and project deliverables archived into cold S3 Glacier storage.

### 5.2 Engineering Standards & Branching SLA
- **Test Coverage:** All backend Lambda routes must have automated Jest/PyTest suites with >85% branch coverage.
- **Git Branching Strategy:** `main` (Production - auto-deploys via AWS Amplify/CodePipeline), `staging` (Internal testing), `feature/*` (Individual squad branches). Direct commits to `main` are strictly blocked.
- **Failover SLA:** If API Gateway p99 latency exceeds 500ms for > 2 minutes, CloudFront automatically routes to the static fallback S3 origin.

---

## 6. Subfolder Directory Map & Deliverables

1. [**`website_frontend_source/`**](./website_frontend_source/README.md): Frontend architecture, page route manifests, responsive breakpoints, Tailwind color tokens matching our Obsidian-Violet design system, and UI component catalog.
2. [**`cloud_sandboxes_and_bedrock/`**](./cloud_sandboxes_and_bedrock/README.md): Automated provisioning blueprints for AWS Organizations, Service Control Policies (SCPs) preventing budget overruns, Amazon Bedrock IAM access, and distribution of $50,000+ AWS cloud credit vouchers.
3. [**`judging_and_leaderboard_engine/`**](./judging_and_leaderboard_engine/README.md): The real-time evaluation portal used by 25+ industry judges and evaluators, powered by a mathematical **Z-score normalization algorithm** to eliminate judge bias, with live WebSocket leaderboard streaming.
4. [**`registration_and_screening_pipeline/`**](./registration_and_screening_pipeline/README.md): Automated applicant ingestion engine pulling from Devfolio / Google Forms webhooks, executing dual-phase filtering, dispatching confirmation emails via SES, and assigning Discord roles.
