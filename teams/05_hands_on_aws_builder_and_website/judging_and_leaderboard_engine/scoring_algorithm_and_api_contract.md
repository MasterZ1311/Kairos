# KAIROS 2027 — Scoring Algorithm Implementation & API Contract

> **Lead Architect:** Viswanathan Ashok (Reg: `44110907`)  
> **Math Lead:** Shanmugapriyan S (Reg: `44111257`)  

---

## 1. OpenAPI 3.0 Contract Specification (YAML Snippet)

```yaml
openapi: 3.0.3
info:
  title: Kairos 2027 Scoring & Judging API
  version: 1.0.0
paths:
  /api/v1/judge/evaluate:
    post:
      summary: Submit evaluation scores for a team
      security:
        - BearerAuth: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - teamId
                - judgeId
                - milestone
                - criteriaScores
              properties:
                teamId:
                  type: string
                  example: "TEAM-AI-042"
                judgeId:
                  type: string
                  example: "JUDGE-AWS-007"
                milestone:
                  type: string
                  enum: ["MILESTONE_1", "MILESTONE_2", "MILESTONE_3"]
                criteriaScores:
                  type: object
                  properties:
                    technicalComplexity:
                      type: integer
                      minimum: 1
                      maximum: 25
                    bedrockInnovation:
                      type: integer
                      minimum: 1
                      maximum: 25
                    codeCompleteness:
                      type: integer
                      minimum: 1
                      maximum: 20
                    uxErgonomics:
                      type: integer
                      minimum: 1
                      maximum: 15
                    pitchFeasibility:
                      type: integer
                      minimum: 1
                      maximum: 15
                notes:
                  type: string
```

---

## 2. Python Z-Score Calculation Engine (Lambda Handler)

```python
import numpy as np

def calculate_normalized_standings(judge_submissions):
    """
    Groups raw scores by judgeId, calculates mean and stddev,
    and returns normalized Z-scores per team.
    """
    judges = {}
    for sub in judge_submissions:
        jid = sub['judgeId']
        judges.setdefault(jid, []).append(sub['totalRaw'])
        
    judge_stats = {
        jid: {
            'mean': np.mean(scores),
            'std': np.std(scores) if np.std(scores) > 0 else 1.0
        }
        for jid, scores in judges.items()
    }
    
    team_scores = {}
    for sub in judge_submissions:
        jid = sub['judgeId']
        tid = sub['teamId']
        z_score = (sub['totalRaw'] - judge_stats[jid]['mean']) / judge_stats[jid]['std']
        team_scores.setdefault(tid, []).append(z_score)
        
    final_rankings = sorted(
        [{'teamId': tid, 'compositeScore': float(np.mean(scores))} for tid, scores in team_scores.items()],
        key=lambda x: x['compositeScore'],
        reverse=True
    )
    return final_rankings
```
