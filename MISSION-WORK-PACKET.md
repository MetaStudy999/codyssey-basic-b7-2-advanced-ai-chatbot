# B7-2 Mission Work Packet

> 이 파일은 Codyssey Basic B7-2 Workcell의 실행 계약이다. Control Tower `MetaStudy999/codyssey-basic`은 READ ONLY이며, 이 Workcell은 `MetaStudy999/codyssey-basic-b7-2-advanced-ai-chatbot`만 수정한다.

## 1. Identity

- Mission ID: `B7-2`
- Mission Title: `웹 기반 AI 챗봇 서비스 고도화 프로젝트`
- Mission Repository: `MetaStudy999/codyssey-basic-b7-2-advanced-ai-chatbot`
- Workcell: `Chat 15 / B7-2`
- Started At: `2026-08-08T04:40:00+09:00`
- Active Wave: `20260808-01`

## 2. Control Tower Baseline

- Control Tower Repository: `MetaStudy999/codyssey-basic`
- Frozen Baseline SHA: `0d1581b3e82366988f57e1d76da311c028b8e15e`
- Baseline Rule: 이 Workcell 동안 임의 변경하지 않는다.
- Wave launcher/manifest는 frozen baseline 이후 current `main`에 존재하지만, Governance 판단은 위 frozen SHA를 따른다.

### Required Control Tower Context verified

- `AGENTS.md` @ frozen baseline
- `docs/00-governance/README.md` @ frozen baseline
- `docs/00-governance/source-discovery-fallback-protocol.md` @ frozen baseline
- `docs/00-governance/parallel-mission-execution.md` @ frozen baseline
- `docs/00-governance/work-packets/b7-2.md` starter packet
- `config/waves/20260808-01.yaml` active wave

## 3. Read / Write Boundary

### READ

- Frozen Control Tower baseline
- B7-2 Mission Repository
- B7-2 official Mission source
- B7-1 Repository only for dependency verification
- Official operation material directly related to B7-2

### WRITE

- `MetaStudy999/codyssey-basic-b7-2-advanced-ai-chatbot` only

### DO NOT WRITE

- `MetaStudy999/codyssey-basic`
- `MetaStudy999/codyssey-basic-b7-1-web-ai-chatbot`
- Any other Mission Repository

## 4. G1 Source Inventory

| Source Candidate | Type | State | Location | Notes |
|---|---|---|---|---|
| B7-2 Mission | PDF | `VALID` | `b7-2-mission.pdf` | 7 pages. Functional requirements, constraints, examples verified. |
| B7-2 Mission | Markdown | `DUPLICATE` | `b7-2-mission.md` | Derived Markdown preserving the PDF requirements; no material requirement conflict found. |
| B7-2 Evaluation / rubric | PDF/MD/etc | `MISSING` | Repository root/search/history | No mission-specific Evaluation candidate found in current tree/search; repository history checked from initial tree through mission-material commits and no Evaluation file was found. |
| Official operation material | PDF | `VALID` | `2026년도 코디세이 AI 올인원 제1기 본과정 오리엔테이션 자료_260507.pdf`, p.5 | Project A is `필수`, Project B(B7-2) is `선택`. Mission PDF itself does not state required/optional. |
| Control Tower Source Registry | Markdown | `VALID` | `docs/00-governance/source-registry.md` @ frozen baseline | Records B7-2 as Term Project / Project B and explicitly avoids inventing Mission-PDF required/optional classification. |

- Source Mode: `MISSION-LED`
- Source Confidence: `MEDIUM`
- Source Gaps:
  - B7-2 mission-specific official Evaluation / 평가문항 is not available in the inspected sources.
  - Therefore Evaluation-specific acceptance criteria must not be invented and cannot be used as PASS evidence.
- Required/Optional classification handling:
  - Mission PDF/MD: `UNSPECIFIED` (필수/선택 표기 없음)
  - Official orientation p.5: Project B `선택`
  - This Workcell does **not** rewrite the Mission PDF metadata as `필수` or `선택`; the operation-level classification is recorded separately.
- Source Conflict: `NONE FOUND`

## 5. Mission Contract

### Goal

Project A의 AI 챗봇 MVP를 기반으로 사용자 인증, 사용자별 대화 소유권, 게시판, RESTful API, 클라우드 배포와 기술 문서를 갖춘 풀스택 웹 서비스로 고도화한다.

### Required Deliverables

- [ ] 정상 동작하는 full-stack web application source
- [ ] 외부 네트워크에서 접속 가능한 deployed service URL
- [ ] ERD
- [ ] API specification
- [ ] system architecture diagram
- [ ] README with service intro, stack, deploy URL, local run, env setup, project structure
- [ ] team roles and per-member work summary in README or technical docs
- [ ] Git/PR history satisfying the Mission collaboration flow

### Required Functions / Behaviors

- [ ] signup
- [ ] password hash storage
- [ ] login + authentication token/state issuance (JWT 등)
- [ ] logout
- [ ] auth-aware UI before/after login
- [ ] unauthenticated access control for protected chatbot/board write functions
- [ ] user-scoped conversation sessions
- [ ] conversation session create/list
- [ ] own-session message history
- [ ] send message + generate AI response
- [ ] cross-user conversation access blocked with 403 or 404
- [ ] board list/detail/create/update/delete
- [ ] board public list/detail
- [ ] board authenticated create
- [ ] board owner-only update/delete
- [ ] post minimum fields: title, content, author, created_at
- [ ] backend functionality exposed through RESTful APIs
- [ ] frontend communicates with backend through those APIs
- [ ] appropriate URL / HTTP method / status code contracts
- [ ] cloud end-to-end flow: signup → login → AI chat → board

### Constraints

- Python `3.10+`
- API keys/database passwords and other secrets must not be hardcoded.
- Sensitive values must be managed through `.env`/environment variables.
- Each team member: at least 10 meaningful commits (human/team runtime evidence).
- `main` direct push is prohibited by Mission; merge through Pull Request only.
- Mission requires history showing `feature → develop → main` and feature-level PR merges.
- Cloud cost must be managed and unnecessary resources cleaned up after practice.

### Explicit Non-scope / Do not invent

- No Mission requirement mandates React specifically; React appears only in the result example architecture.
- No Mission requirement mandates a specific DB engine.
- No Mission requirement mandates OpenAI or Anthropic specifically; providers appear only as examples.
- No unavailable Evaluation criterion is treated as an official requirement.
- Additional enterprise architecture, OAuth provider integrations, Kubernetes, microservices, or advanced security controls are backlog unless later Source requires them.

## 6. Requirement Traceability

| ID | Requirement | Source | Location | Confidence | Implementation | Test | Evidence | Status |
|---|---|---|---|---|---|---|---|---|
| REQ-B7-2-001 | signup exists | Mission PDF/MD | p.2-3 / 사용자 인증 | HIGH | pending upstream baseline | API/integration | test log | TODO |
| REQ-B7-2-002 | password stored hashed | Mission PDF/MD | p.2 / 사용자 인증 | HIGH | pending | DB/assertion | test log/schema | TODO |
| REQ-B7-2-003 | login issues auth token/state | Mission PDF/MD | p.2 / 사용자 인증 | HIGH | pending | auth test | test log | TODO |
| REQ-B7-2-004 | logout exists | Mission PDF/MD | p.2 / 사용자 인증 | HIGH | pending | auth test | test log/UI | TODO |
| REQ-B7-2-005 | auth state changes UI and protects core functions | Mission PDF/MD | p.2 / 사용자 인증 | HIGH | pending | API + browser | screenshot/log | TODO |
| REQ-B7-2-006 | Project A chatbot is extended for per-user conversations | Mission PDF/MD | p.3 / 사용자별 AI 챗봇 | HIGH | `B7-1` required | regression/ownership | dependency SHA + tests | BLOCKED |
| REQ-B7-2-007 | users can only list/read own chat sessions | Mission PDF/MD | p.3 | HIGH | pending | A/B isolation test | test log | TODO |
| REQ-B7-2-008 | session create/list/history/send/AI response work | Mission PDF/MD | p.3 | HIGH | pending | API integration | test log | TODO |
| REQ-B7-2-009 | cross-user session access returns 403 or 404 | Mission PDF/MD | p.3 | HIGH | pending | IDOR negative test | test log | TODO |
| REQ-B7-2-010 | board supports list/detail/create/update/delete | Mission PDF/MD | p.3 | HIGH | pending | CRUD tests | test log | TODO |
| REQ-B7-2-011 | list/detail public; create authenticated; update/delete owner-only | Mission PDF/MD | p.3 | HIGH | pending | authz matrix | test log | TODO |
| REQ-B7-2-012 | post has title/content/author/created_at minimum | Mission PDF/MD | p.3 | HIGH | pending | schema test | schema/docs | TODO |
| REQ-B7-2-013 | all backend features use RESTful API; frontend calls API | Mission PDF/MD | p.3 | HIGH | pending | route contract | API spec/test | TODO |
| REQ-B7-2-014 | URL/method/status code follow REST rules | Mission PDF/MD | p.3 | HIGH | pending | API contract test | API spec/test | TODO |
| REQ-B7-2-015 | cloud deployment is externally reachable | Mission PDF/MD | p.3 | HIGH | pending | external runtime | URL/screenshot | NEEDS-RUNTIME |
| REQ-B7-2-016 | deployed signup/login/chat/board flow works | Mission PDF/MD | p.3 | HIGH | pending | E2E runtime | browser evidence | NEEDS-RUNTIME |
| REQ-B7-2-017 | feature → develop → main history and feature PR flow | Mission PDF/MD | p.3 / 인프라 및 협업 | HIGH | pending | GitHub history review | PR URLs/graph | TODO |
| REQ-B7-2-018 | ERD includes all entities, relations, major fields, PK/FK | Mission PDF/MD | p.3-4 | HIGH | pending | docs-schema diff | docs | TODO |
| REQ-B7-2-019 | API spec covers every endpoint, request/response/status | Mission PDF/MD | p.4 | HIGH | pending | docs-route diff | docs | TODO |
| REQ-B7-2-020 | architecture shows frontend/backend/DB/AI API/cloud communication | Mission PDF/MD | p.4 | HIGH | pending | docs review | diagram | TODO |
| REQ-B7-2-021 | README contains required six operational sections | Mission PDF/MD | p.4 | HIGH | pending | doc check | README | TODO |
| REQ-B7-2-022 | secrets are not hardcoded and are environment-managed | Mission PDF/MD | p.5 | HIGH | pending | secret/static scan | `.env.example`, scan | TODO |
| REQ-B7-2-023 | every team member has >=10 meaningful commits | Mission PDF/MD | p.5 | HIGH | human/team dependent | Git history | commit links | NEEDS-RUNTIME |
| REQ-B7-2-024 | team roles and individual work summary documented | Mission PDF/MD | p.5 | HIGH | pending | doc review | README/docs | TODO |
| REQ-B7-2-025 | main is merged only via PR | Mission PDF/MD | p.5 | HIGH | repository policy/process | history review | PR URLs | TODO |
| REQ-B7-2-026 | unnecessary cloud resources cleaned after practice | Mission PDF/MD | p.5 | HIGH | human/cloud | runtime checklist | cleanup evidence | NEEDS-RUNTIME |

## 7. Evaluation Mapping

Official mission-specific Evaluation source was not found.

| Evaluation ID | Criterion | Related Requirement | Validation | Evidence | Status |
|---|---|---|---|---|---|
| EVA-B7-2-GAP | Mission-specific Evaluation unavailable | N/A | re-run Source Discovery if Evaluation is later provided | Source Gap record | UNVERIFIED |

No Evaluation criteria are inferred from README, code, examples, or general knowledge.

## 8. Repository Baseline

- Default Branch: `main`
- Mission Repository Baseline Commit: `154322344236308e801a818f89823c6e5b8b1af9`
- Work Branch: `mission/b7-2`
- Runtime / Language: not implemented; Mission requires Python 3.10+
- Dependency Manager: none yet
- Existing Tests: `NO`

### Repository Inventory at G1

```text
/
├── README.md             # title only
├── b7-2-mission.md       # valid Mission derivative
└── b7-2-mission.pdf      # valid official Mission source
```

### Existing Implementation

- Already satisfied: Mission source materials exist and are readable.
- Partially satisfied: none of the service functions.
- Missing: full-stack application, auth, DB models, chat implementation, board, REST API, deployment, technical docs, automated tests, runtime/evidence package.
- Existing code risk: none; repository is effectively a source-only starter.

## 9. Mission-specific TOC

```text
B7-2
├── Source / Evaluation Discovery
├── B7-1 Baseline Reuse
├── User / Auth
│   ├── Signup
│   ├── Password Hashing
│   ├── Login / Token
│   └── Logout / Auth-aware UI
├── Conversation Ownership
│   ├── Session Create / List
│   ├── Message History
│   ├── Send / AI Response
│   └── Cross-user Denial
├── Board CRUD / Ownership
├── REST API Contract
├── Frontend Integration
├── Data Model / ERD
├── API Specification
├── System Architecture
├── Cloud Deployment
├── feature → develop → main PR Evidence
├── Runtime / Evidence
├── Learning
└── Handoff
```

## 10. Engineering Plan

### Prompt Engineering

- ROLE: primary mission owner / integrator
- GOAL: complete the current Gate only with Source-traceable requirements
- SCOPE: B7-2 only
- OUTPUT CONTRACT: code + tests + docs + evidence without false PASS
- STOP CONDITION: BLOCKER=0, MAJOR=0, required runtime/evidence done, G8 merged

### Context Engineering

Use only the B7-2 Mission, the frozen Governance baseline, the verified B7-1 final baseline when available, and files/tests relevant to the active Gate.

### Harness Engineering

- Git boundary: current Mission Repository only
- Current branch: `mission/b7-2`
- Final Mission collaboration flow must preserve `feature → develop → main` PR evidence per Source.
- Secret boundary: no credentials/API keys in source, logs, test fixtures, or evidence.
- Evidence boundary: expected output is never presented as actual runtime evidence.

### Loop Engineering

- Self review: 1 pass after build/tests
- Independent review: 1 focused pass only when a complete candidate exists
- Re-validation: BLOCKER/MAJOR fixes only

### Fusion Engineering

Priority: `Source → Test → Runtime → Evidence`.

## 11. Agent Routing

- Orchestrator / Integrator: `ChatGPT`
- Primary Builder: `ChatGPT` in this Workcell; Codex may be used only after a complete baseline exists if needed.
- Independent Reviewer: one focused reviewer after build (not invoked while dependency-blocked)
- Claude: `OFF`
- Gemini: `OFF` (PDF was directly readable/render-verified)
- Grok: `OFF`
- Runtime Authority: `Human`

## 12. Dependency / Drift Check

### Upstream Dependency

- Classification: `REQUIRED`
- Related Mission: `B7-1`
- Official basis: B7-2 explicitly says `Project A의 챗봇 기능을 기반으로` and describes the mission as upgrading the Project A MVP.
- B7-1 current repository status at G1/G2 pre-check: current `main` contains only `README.md`, `b7-1-mission.md`, `b7-1-mission.pdf`; no chatbot implementation or final Handoff is present.
- B7-1 current branches observed: `main` only.
- Reusable upstream artifact: `NOT AVAILABLE YET`
- G2 action: `WAITING-UPSTREAM`

This is not an artificial dependency: the official B7-2 source explicitly requires Project A as the functional baseline. Reimplementing an unrelated Project A substitute here would break provenance and regression/reuse validation.

### Drift

- Control Tower Drift: `NONE affecting this Workcell detected at G1`
- Source Drift: `NONE detected`
- Action: `WAIT` before G2 BUILD; re-check B7-1 final SHA/HANDOFF immediately before build.

## 13. Test Plan

| Test | Requirement | Command / Method | Expected | Actual | Status |
|---|---|---|---|---|---|
| signup/hash | 001-002 | API + DB assertion | account created, hash != password | upstream/build pending | TODO |
| login/logout/auth UI | 003-005 | API + UI integration | correct auth transitions | pending | TODO |
| user A/B chat isolation | 006-009 | two-user integration test | only own sessions visible | pending | TODO |
| direct cross-user access | 009 | GET/POST with foreign id | 403 or 404 | pending | TODO |
| chat flow | 008 | create/list/history/send | AI response and persisted history | pending | TODO |
| board CRUD | 010-012 | API integration | complete CRUD | pending | TODO |
| board authorization | 011 | owner/non-owner matrix | update/delete denied to non-owner | pending | TODO |
| REST contract | 013-014 | route/method/status assertions | spec matches implementation | pending | TODO |
| docs/schema alignment | 018-020 | compare routes/models/docs | no material mismatch | pending | TODO |
| secret scan | 022 | repository scan | no committed real secrets | pending | TODO |
| external E2E | 015-016 | browser/API against deployed URL | signup→login→chat→board works | human/cloud needed | NEEDS-RUNTIME |
| collaboration history | 017,023,025 | GitHub PR/commit review | required flow/evidence exists | human/team needed | NEEDS-RUNTIME |
| cleanup | 026 | cloud console/checklist | unnecessary resources removed | human/cloud needed | NEEDS-RUNTIME |

## 14. Runtime Plan

| Runtime Check | AI possible | Human required | Evidence | Status |
|---|---|---|---|---|
| local API/UI flow | partially | yes for final browser acceptance | terminal/browser capture | TODO |
| two-user ownership behavior | automated + browser | final confirmation recommended | test log/screenshots | TODO |
| real AI response | depends on API key/network | yes if external credential required | redacted screenshot/log | NEEDS-RUNTIME |
| deployed URL external access | no final authority | yes | URL + screenshot/HTTP response | NEEDS-RUNTIME |
| team commit/PR evidence | inspectable after team activity | yes for genuine team contributions | PR URLs/commit graph | NEEDS-RUNTIME |
| cloud cleanup | no | yes | checklist/resource list | NEEDS-RUNTIME |

## 15. Evidence Plan

| Evidence | Requirement | Capture Method | Location | Status |
|---|---|---|---|---|
| automated test report | auth/chat/board/API | test output | `evidence/tests/` | TODO |
| ownership negative tests | chat/board | two-user test log | `evidence/security/` | TODO |
| ERD | 018 | Mermaid/image/doc | `docs/` | TODO |
| API spec | 019 | Markdown/OpenAPI-linked doc | `docs/` | TODO |
| architecture | 020 | Mermaid/image/doc | `docs/` | TODO |
| deployment evidence | 015-016 | URL + screenshot/HTTP | `evidence/runtime/` | NEEDS-RUNTIME |
| PR/branch evidence | 017,023,025 | PR links + graph | `evidence/collaboration/` or README | NEEDS-RUNTIME |
| cleanup evidence | 026 | checklist/capture | `evidence/runtime/` | NEEDS-RUNTIME |

## 16. Completion Gates

| Gate | Exit Condition | Status |
|---|---|---|
| G1 SOURCE | Source candidates, states, mode, gaps, provenance, repo inventory confirmed | PASS |
| G2 BUILD | required implementation exists on verified B7-1 baseline | BLOCKED (`WAITING-UPSTREAM`) |
| G3 TEST | required automated/reliable tests pass | TODO |
| G4 REVIEW | BLOCKER=0, MAJOR=0 | TODO |
| G5 RUNTIME | real environment validation complete or accurately tracked | TODO |
| G6 EVIDENCE | required evidence complete | TODO |
| G7 LEARN | implementation-aligned learning material complete | TODO |
| G8 MERGE | Mission PR/merge complete | TODO |

## 17. STOP / WAIT Rule

### Current stop condition

Do not start G2 implementation until the required B7-1 functional baseline is available and its final/reusable SHA can be recorded.

While waiting, do not fabricate Project A code, team contributions, cloud deployment, runtime results, Evaluation criteria, or PASS evidence.

### Mission completion stop rule

Stop further enhancement once official Mission requirements are met, Evaluation is either satisfied or its Gap remains explicitly recorded, BLOCKER=0, MAJOR=0, required tests/runtime/evidence are complete, and G8 merge is complete.

## 18. Handoff Contract

When the Mission actually completes, create:

- `HANDOFF.md`
- `mission-result.yaml`

The Control Tower remains READ ONLY in this Workcell. Serial integration will consume the Handoff later.
