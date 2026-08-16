# B7-2 Requirement → Implementation → Verification → Evidence

Source of Truth: `b7-2-mission.pdf` → `b7-2-mission.md`. 현재 저장소 `main`에는 별도 `b7-2-evaluation.md`가 없으므로 공식 Mission 요구를 직접 Gate로 사용합니다.

| ID | 공식 요구사항 | Reference 구현 | 검증 | Phase C Evidence |
|---|---|---|---|---|
| R01 | 회원가입 + password hash | `/api/auth/signup`, PBKDF2 | 가입 후 DB hash 확인 | API/DB |
| R02 | 로그인 + token 발급 | `/api/auth/login`, opaque Bearer token | 정상/실패 로그인 | 응답/UI |
| R03 | 로그아웃 | `/api/auth/logout`, token row 삭제 | logout 후 token 401 | 응답 |
| R04 | 인증 상태 UI | frontend `/api/auth/me` | 로그인 전/후 | 화면 |
| R05 | AI/게시판 write 비인증 차단 | `get_current_user` dependency | 401 | API 결과 |
| R06 | 사용자별 ChatSession | `ChatSession.user_id` | user A/B 분리 | 2-user test |
| R07 | 세션 생성/목록/메시지 조회/전송 | chat router | 전체 API 흐름 | API/UI |
| R08 | 다른 사용자 chat 접근 403/404 | `owned_session()` 404 | cross-user access | 404 Evidence |
| R09 | AI 응답 생성/저장 | `ai_client.py`, Message | actual AI call | 대화 화면/DB |
| R10 | Post 목록/상세 | public GET APIs | anonymous GET | API/UI |
| R11 | Post 작성 로그인 필요 | POST + auth | 401/201 | API/UI |
| R12 | Post 수정/삭제 본인만 | owner check 403 | user A/B | 403 Evidence |
| R13 | RESTful API | auth/chat/posts routers | method/status review | API spec/runtime |
| R14 | frontend는 REST 통신 | `frontend/app.js` fetch | browser dev flow | UI |
| R15 | cloud 외부 URL | NEEDS-RUNTIME | external network | 배포 URL |
| R16 | feature→develop→main | NEEDS-RUNTIME Git history | branch/PR audit | PR links |
| R17 | 팀원별 10+ meaningful commits | NEEDS-RUNTIME | git log | commit links |
| R18 | 팀 역할/작업 요약 | collaboration template | 문서 확인 | 실제 팀 정보 |
| R19 | ERD | `docs/erd.md` | Mermaid/document review | 문서 |
| R20 | API 명세 | `docs/api-spec.md` | endpoint coverage | 문서 |
| R21 | architecture diagram | `docs/architecture.md` | component/flow review | 문서 |
| R22 | README 필수 항목 | `reference/README.md` | document review | 재현 |
| R23 | secret `.env` | `.env.example` + `.gitignore` | secret scan | scan result |
| R24 | cloud cleanup/cost | deployment checklist | actual cleanup | cleanup evidence |

## Runtime 원칙

Cloud URL, 실제 AI API, 실제 team branch/PR/commit, two-user isolation은 Reference 문서 존재만으로 PASS 처리하지 않습니다.
