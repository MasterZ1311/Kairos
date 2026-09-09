# Judging System & Real-Time Leaderboard Specification

> **Subfolder:** `teams/05_hands_on_aws_builder_and_website/judging_and_leaderboard_engine/`  
> **Direct Lead:** **Viswanathan Ashok** (Hands-On Builder Lead, Reg: `44110907`)  
> **Mathematical Architect:** **Shanmugapriyan S** (Technical Lead, Reg: `44111257`)  
> **Jury Governance Lead:** **Chief Safety & Jury Officer (CSO)**  
> **Executive Oversight:** **Thenappan T** (President & SBGL, Reg: `44110855`)  

---

## 1. Scope & Mandate

This folder specifies the backend algorithms, WebSocket architecture, database schema, and mathematical normalization model powering the **Kairos Judging & Live Leaderboard Engine**.

To eliminate traditional hackathon evaluation subjectivity (where a strict judge gives 6/10 while a lenient judge gives 9/10), Kairos 2027 implements an automated **Statistical Z-Score Normalization Engine**.

---

## 2. The Z-Score Normalization Algorithm

For each judge $j$, calculating the mean score $\mu_j$ and standard deviation $\sigma_j$ across all projects they evaluated:

$$Z_{i, j} = \frac{X_{i, j} - \mu_j}{\sigma_j}$$

Where:
- $X_{i, j}$ = Raw score given to team $i$ by judge $j$.
- $\mu_j$ = Mean score given by judge $j$ across their assigned batch of teams.
- $\sigma_j$ = Standard deviation of judge $j$'s scores.
- $Z_{i, j}$ = Normalized Z-Score representing relative performance independent of judge leniency.

The final composite score for team $i$ across $K$ assigned judges is:

$$S_i = \sum_{k=1}^{K} W_k \cdot Z_{i, k}$$

Where $W_k$ represents milestone checkpoint weights:
- **Milestone 1 (Architecture & System Design):** 20%
- **Milestone 2 (Code Originality & AWS Bedrock / API Implementation):** 40%
- **Milestone 3 (Grand Stage Live Pitch & Commercial Feasibility):** 40%

---

## 3. Evaluation Rubric Criteria (100 Points Total)

1. **Technical Complexity & Architecture (25 pts):** Distributed systems design, AWS serverless services, edge resiliency.
2. **Generative AI & Bedrock Innovation (25 pts):** Depth of model adaptation, agentic autonomy, prompt engineering, RAG quality.
3. **Execution, Code Quality & Completeness (20 pts):** Clean GitHub commits, error handling, live functioning prototype.
4. **UI/UX & Developer Ergonomics (15 pts):** Polish, accessibility, responsive ergonomics, design system coherence.
5. **Pitch, Commercial Viability & Impact (15 pts):** Market problem clarity, scalability, monetization roadmap.

---

## 4. API Endpoints & Real-Time WebSockets
- `POST /api/v1/judge/score`: Authenticated JWT endpoint for judges to submit category scores.
- `GET /api/v1/leaderboard/live`: Public WebSocket feed broadcasting sanitized rank movements.
- `POST /api/v1/admin/freeze`: Administrative switch to freeze public leaderboard at H44 (T-4 Hours).
