# B7-2 R01 — Reference Build

## Source of Truth

1. `b7-2-mission.pdf`
2. `b7-2-mission.md`

현재 저장소 `main`에는 별도 `b7-2-evaluation.md`가 없으므로 공식 Mission 요구사항 자체를 검증 Gate로 사용합니다.

## Reference 목표

Project A의 AI Chat MVP를 다음 요소를 가진 풀스택 서비스 기준본으로 확장합니다.

```text
회원가입/로그인/로그아웃
+ 사용자별 AI Chat 소유권
+ 게시판 CRUD/작성자 소유권
+ RESTful API
+ 분리된 Frontend
+ 기술 문서
+ Cloud/협업 Runtime 계획
```

## 최소 충분 기술 선택

- Frontend: HTML/CSS/Vanilla JavaScript
- Backend: FastAPI REST API
- ORM: SQLAlchemy
- Local DB: SQLite
- Password: PBKDF2 hash
- Auth token: opaque Bearer token (`JWT 등`의 허용 범위에서 단순 토큰 방식 선택)
- Token storage: DB에는 raw token 대신 SHA-256 hash 저장
- AI API: `.env` 기반 OpenAI-compatible HTTP endpoint Reference

공식 Mission이 React를 필수로 지정하지 않으므로 React를 불필요한 필수 의존성으로 추가하지 않습니다.

## 구조

```text
training/round-01-clear/
├── REFERENCE-BUILD.md
├── REFERENCE-STATUS.md
├── BEGINNER-GUIDE.md
├── CHECKLIST.md
├── reference/
│   ├── README.md
│   ├── requirements.txt
│   ├── .env.example
│   ├── backend/
│   │   ├── main.py
│   │   ├── database.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── security.py
│   │   ├── dependencies.py
│   │   ├── ai_client.py
│   │   └── routers/{auth,chat,posts}.py
│   └── frontend/{index.html,app.js}
├── environment/
│   ├── README.md
│   ├── setup.sh
│   ├── verify.sh
│   ├── reset.sh
│   └── inspect_db.py
├── docs/
│   ├── erd.md
│   ├── api-spec.md
│   ├── architecture.md
│   ├── requirements-mapping.md
│   ├── collaboration.md
│   └── deployment-checklist.md
└── evidence/README.md
```

## Requirement Design

### 인증

- Signup에서 비밀번호 PBKDF2 hash
- Login 성공 시 access token 발급
- DB에는 token hash만 저장
- Logout에서 현재 token 폐기
- `/api/auth/me`로 frontend 로그인 상태 확인

### Chat ownership

`ChatSession.user_id`를 current user와 항상 함께 조회합니다. 다른 사용자의 session은 404로 처리하여 존재 여부도 노출하지 않습니다.

### Chat 기능

- session 생성
- session 목록
- message history
- user message 저장
- 최근 context 구성
- AI API 호출
- assistant message 저장

실제 AI Provider는 Runtime에서 확정합니다.

### Board ownership

- 목록/상세: 공개
- 작성: 인증 필요
- 수정/삭제: 작성자만
- 다른 로그인 사용자: 403

### REST

Backend의 핵심 기능은 `/api/auth`, `/api/chat`, `/api/posts` REST endpoint로 제공합니다. Frontend는 `fetch()`로 이 API를 사용합니다.

### Technical docs

ERD, API 명세, Architecture를 미리 작성합니다. 실제 cloud/팀 이력 값은 NEEDS-RUNTIME으로 남깁니다.

## Phase C 전용 항목

Reference로 허위 충족시키지 않는 항목:

- 실제 AI API key/provider/model 및 실제 AI 응답
- 실제 2-user ownership Runtime
- 실제 cloud 외부 URL
- 배포 환경 전체 flow
- 실제 `feature → develop → main` PR 이력
- 실제 팀원별 10+ 유의미 커밋
- 실제 팀 역할/개인 작업 요약
- 실제 cloud 비용/cleanup Evidence

## Phase A 판정 규칙

코드·문서·verify 설계가 준비되어도 Runtime은 `⬜ NOT STARTED`, Project는 CLEAR가 아닙니다.
