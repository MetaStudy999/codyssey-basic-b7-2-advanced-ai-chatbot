# B7-2 REST API Specification

Base URL (local): `http://localhost:8000`

인증이 필요한 API는 `Authorization: Bearer <token>` 헤더를 사용합니다.

| Method | URL | 인증 | 요청 | 성공 응답 | 주요 오류 |
|---|---|---|---|---|---|
| POST | `/api/auth/signup` | X | email, username, password | 201 User | 409, 422 |
| POST | `/api/auth/login` | X | email, password | 200 access token | 401 |
| POST | `/api/auth/logout` | O | - | 204 | 401 |
| GET | `/api/auth/me` | O | - | 200 current user | 401 |
| GET | `/api/chat/sessions` | O | - | 200 own sessions | 401 |
| POST | `/api/chat/sessions` | O | title | 201 session | 401, 422 |
| GET | `/api/chat/sessions/{id}/messages` | O/소유자 | - | 200 messages | 401, 404 |
| POST | `/api/chat/sessions/{id}/messages` | O/소유자 | content | 201 AI message | 401, 404, 502 |
| GET | `/api/posts` | X | - | 200 posts | - |
| GET | `/api/posts/{id}` | X | - | 200 post | 404 |
| POST | `/api/posts` | O | title, content | 201 post | 401, 422 |
| PUT | `/api/posts/{id}` | O/작성자 | title, content | 200 post | 401, 403, 404 |
| DELETE | `/api/posts/{id}` | O/작성자 | - | 204 | 401, 403, 404 |
| GET | `/health` | X | - | 200 `{status: ok}` | - |

## 소유권 정책

### Chat

ChatSession 조회는 항상 `session.id == id AND session.user_id == current_user.id` 조건을 사용합니다. 다른 사용자의 세션 존재 여부를 드러내지 않기 위해 404를 반환합니다.

### Post

목록/상세 조회는 공개합니다. 작성은 로그인 필요, 수정/삭제는 작성자 본인만 가능하며 다른 로그인 사용자가 시도하면 403을 반환합니다.

## AI message

사용자 메시지를 저장한 후 동일 세션의 최근 메시지를 AI API에 전달합니다. Provider 설정 오류/네트워크/응답 형식 오류는 502로 응답합니다. 실제 Provider별 URL/model은 Phase C Runtime에서 확정합니다.
