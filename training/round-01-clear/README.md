# B7-2 Round 01 — CLEAR

구분: **선택 Term Project / 고도화 (OPTIONAL / ADVANCED)**  
현재 모드: **Phase A — REFERENCE BUILD**  
Runtime Project 상태: **⬜ NOT STARTED**

## 현재 판정

Project B의 풀스택 AI Chatbot **Reference 핵심 기준본을 준비했습니다.** 실제 AI API, 2-user 소유권, cloud URL, 팀 Git 이력과 Evidence는 Phase C에서 검증하므로 아직 `✅ CLEAR`가 아닙니다.

## 핵심 문서

- `REFERENCE-BUILD.md`
- `REFERENCE-STATUS.md`
- `BEGINNER-GUIDE.md`
- `CHECKLIST.md`
- `reference/README.md`
- `docs/erd.md`
- `docs/api-spec.md`
- `docs/architecture.md`
- `docs/requirements-mapping.md`
- `docs/collaboration.md`
- `docs/deployment-checklist.md`
- `evidence/README.md`

## Reference 핵심

- 회원가입 / password hash
- 로그인 / Bearer access token / logout revoke
- 사용자별 ChatSession / Message
- 다른 사용자 ChatSession 404
- 실제 AI API를 위한 env-only client
- 게시판 REST CRUD + 작성자 수정/삭제 403
- 분리된 frontend REST client
- ERD / API / Architecture
- setup / verify / reset / DB inspect

Reference가 존재한다는 이유만으로 Runtime PASS를 표시하지 않습니다.
