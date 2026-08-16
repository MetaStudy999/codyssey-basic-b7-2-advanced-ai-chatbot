# B7-2 R01 Environment

## Golden Path

Phase C 기본 경로는 **Python 3.10+ + FastAPI REST backend + browser frontend + relational DB + external AI API**입니다.

Reference local DB는 SQLite를 사용하고, 실제 cloud에서는 `DATABASE_URL`로 환경에 맞게 교체할 수 있습니다.

## 파일 역할

- `setup.sh`: `.venv`와 의존성 설치, `.env.example` 복사 보조
- `verify.sh`: 파일/문법/ownership/secret 패턴 정적 검증
- `inspect_db.py`: 실제 User/Chat/Post 관계를 hash 일부만 표시하며 확인
- `reset.sh`: `.venv`, local SQLite, cache만 제거하고 `.env`는 보존

## 실제 `.env`

`reference/.env.example`을 복사한 뒤 실제 값은 로컬에만 입력합니다.

```text
DATABASE_URL=...
AI_API_URL=...
AI_API_KEY=...
AI_MODEL=...
```

`.env`는 Git에 포함하지 않습니다.

## Phase C 실행

```bash
cd training/round-01-clear/reference
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cp .env.example .env
# .env 실제 값은 로컬에서 편집
uvicorn backend.main:app --reload
```

브라우저: `http://localhost:8000`  
API 문서: `http://localhost:8000/docs`  
Health: `http://localhost:8000/health`

## Runtime 분리

- 실제 AI Provider/model/API key
- 실제 cloud provider/URL
- 실제 team branch/PR/commit

위 세 묶음은 Phase A에서 임의로 확정하지 않고 Phase C에서 실제 환경으로 검증합니다.
