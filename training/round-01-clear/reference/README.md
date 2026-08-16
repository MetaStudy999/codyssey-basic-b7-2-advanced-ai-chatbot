# B7-2 Reference — Advanced AI Chatbot Full Stack

공식 B7-2 Project B 요구를 기준으로 만든 **Reference 기준본**입니다. 실제 AI Provider 호출, 팀 PR 이력, 클라우드 배포 URL과 Evidence는 Phase C에서만 확정합니다.

## 서비스 소개

회원가입/로그인 후 사용자별 AI 대화를 관리하고, AI 활용 결과를 게시판으로 공유할 수 있는 풀스택 웹 서비스입니다.

## 기술 스택

- Frontend: HTML + CSS + Vanilla JavaScript
- Backend: FastAPI REST API
- ORM/DB: SQLAlchemy + SQLite (Reference local)
- Auth: PBKDF2 password hash + opaque Bearer access token
- AI: 환경 변수 기반 OpenAI-compatible HTTP endpoint Reference client

> 공식 미션은 특정 frontend framework를 강제하지 않습니다. Reference는 REST API와 frontend 분리를 가장 단순하게 보여주기 위해 별도 HTML/JS client를 사용합니다.

## 배포 URL

**NEEDS-RUNTIME** — Phase C에서 실제 cloud URL을 기록합니다. 가짜 URL을 넣지 않습니다.

## 로컬 실행

```bash
cd training/round-01-clear/reference
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cp .env.example .env
```

`.env`의 실제 `AI_API_URL`, `AI_API_KEY`, `AI_MODEL` 값을 로컬에서만 입력합니다.

```bash
uvicorn backend.main:app --reload
```

- Frontend: `http://localhost:8000`
- API docs: `http://localhost:8000/docs`
- Health: `http://localhost:8000/health`

## 환경 변수

| 이름 | 의미 |
|---|---|
| `DATABASE_URL` | DB 연결 URL. Reference local은 SQLite |
| `AI_API_URL` | AI chat-completion endpoint |
| `AI_API_KEY` | AI API credential |
| `AI_MODEL` | Provider model name |

실제 `.env`는 Git에 올리지 않습니다.

## 프로젝트 구조

```text
reference/
├── .env.example
├── requirements.txt
├── backend/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── security.py
│   ├── dependencies.py
│   ├── ai_client.py
│   └── routers/
│       ├── auth.py
│       ├── chat.py
│       └── posts.py
└── frontend/
    ├── index.html
    └── app.js
```

## 핵심 기능

### 인증

- 회원가입: password를 PBKDF2 hash로 저장
- 로그인: opaque access token 발급, DB에는 token hash만 저장
- 로그아웃: 현재 token row 폐기
- 인증 UI: frontend가 `/api/auth/me`로 상태 확인

### 사용자별 AI Chat

- 사용자별 ChatSession 목록/생성
- Session별 Message 저장
- 다른 사용자 세션은 404
- 최근 대화 context를 AI API로 전달
- AI 응답 DB 저장

### 게시판

- 목록/상세 공개 조회
- 작성 로그인 필요
- 수정/삭제 작성자 본인만 가능
- 타 사용자 수정/삭제는 403

## REST API

전체 명세: `../docs/api-spec.md`

## ERD / Architecture

- `../docs/erd.md`
- `../docs/architecture.md`

## 브랜치 전략 — Phase C

공식 요구대로 실제 협업 시:

```text
feature/* → develop → main
```

main 직접 push 없이 Pull Request를 통해 병합하고, 팀원별 유의미 커밋 10회 이상과 역할/작업 요약을 실제 이력으로 남깁니다. Reference 문서 작성만으로 이 요구를 PASS 처리하지 않습니다.

## 보안 메모

- 실제 API Key/DB password는 `.env`에만 저장합니다.
- Raw access token은 DB에 저장하지 않고 SHA-256 hash만 저장합니다.
- ChatSession은 current user 소유 조건으로 조회합니다.
- Post 수정/삭제는 작성자 ID를 검사합니다.

## Cloud — Phase C

실제 AWS/GCP/Azure/PaaS 중 하나에 배포하고 외부 URL에서 회원가입→로그인→AI chat→게시판 전체 흐름을 검증합니다. 실습 종료 후 불필요 리소스를 정리합니다.
