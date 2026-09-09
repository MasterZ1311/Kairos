# KAIROS 2027 — Applicant Webhook Data Schema & Verification Rules

> **Data Engineer:** Viswanathan Ashok (Reg: `44110907`)  
> **Database:** Amazon DynamoDB (`Kairos2027_Applicants`)  

---

## 1. DynamoDB Table Schema

- **Partition Key (PK):** `TEAM#[UUID]`
- **Sort Key (SK):** `METADATA`
- **Global Secondary Index (GSI1):** `GSI1PK = STATUS#[PENDING/SEMIFINALIST/FINALIST]`

```json
{
  "teamId": "KAIROS-2027-TM-0492",
  "teamName": "NeuralMesh",
  "trackId": "TRACK_1_AGENTIC_AI",
  "college": "National Institute of Technology, Trichy",
  "state": "Tamil Nadu",
  "abstractTitle": "Decentralized Multi-Agent Swarms on AWS Bedrock",
  "githubRepo": "https://github.com/neuralmesh/kairos-prototype",
  "lead": {
    "name": "Arjun Sundaram",
    "email": "arjun.sundaram@gmail.com",
    "phone": "+91 9840192831",
    "tshirtSize": "L",
    "gender": "Male"
  },
  "members": [
    { "name": "Kavitha R", "email": "kavitha.r@gmail.com", "tshirtSize": "M", "gender": "Female" },
    { "name": "Siddharth N", "email": "siddharth.n@gmail.com", "tshirtSize": "L", "gender": "Male" },
    { "name": "Deepak M", "email": "deepak.m@gmail.com", "tshirtSize": "XL", "gender": "Male" }
  ],
  "screeningScore": 92.5,
  "status": "SHORTLISTED_FINALIST",
  "assignedHackerBay": "BAY-LH1-08",
  "appliedAt": "2026-11-14T14:22:10Z"
}
```
