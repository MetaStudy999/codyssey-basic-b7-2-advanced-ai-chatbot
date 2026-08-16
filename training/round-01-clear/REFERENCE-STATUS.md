# B7-2 R01 — Reference Status

## Phase A 준비 결과

- [x] 공식 Mission PDF/MD 분석
- [x] 별도 Evaluation 파일 부재 확인
- [x] Full-stack Reference architecture
- [x] User/AuthToken/ChatSession/Message/Post ORM
- [x] 회원가입 + password hash
- [x] 로그인 + access token
- [x] 로그아웃 + token revoke
- [x] frontend 로그인 전/후 UI
- [x] 사용자별 ChatSession 소유권 검사
- [x] Session 생성/목록/메시지 조회/전송 API
- [x] AI client env-only configuration
- [x] 최근 대화 context 구성
- [x] AI 실패 502 경로
- [x] 게시판 목록/상세/작성/수정/삭제 REST API
- [x] 작성자 수정/삭제 403 정책
- [x] frontend REST client
- [x] ERD
- [x] API 명세
- [x] Architecture 문서
- [x] Requirements Mapping
- [x] Collaboration Runtime template
- [x] Deployment/Cleanup checklist
- [x] Evidence Guide
- [x] setup/verify/reset/DB inspect
- [x] `.env.example`
- [x] actual secret 미포함 설계

## Phase C에서만 완료

- [ ] 실제 Python/의존성 설치
- [ ] 실제 local server/browser flow
- [ ] 실제 signup/password DB 확인
- [ ] 실제 login/token/logout
- [ ] 실제 AI API Provider/model/key local 설정
- [ ] 실제 AI 응답/대화 저장
- [ ] 실제 2-user ChatSession isolation
- [ ] 실제 2-user Post ownership 403
- [ ] 실제 cloud deployment URL
- [ ] 외부 전체 서비스 flow
- [ ] 실제 feature→develop→main PR 이력
- [ ] main 직접 push 없음 확인
- [ ] 팀원별 10+ 유의미 커밋
- [ ] 실제 팀 역할/작업 요약
- [ ] cloud cleanup/cost 확인
- [ ] Runtime Evidence package
- [ ] 사용자 자기 말 설명
- [ ] BLOCKER/MAJOR 최종 Gate
- [ ] `✅ B7-2 CLEAR`

## 판정

**Reference 핵심 기준본 준비 완료 / Runtime 미시작 / CLEAR 아님**

Phase A 전체 감사에서 B7-1→B7-2 데이터/인증/API 연결성과 다른 미션의 환경·Secret·배포 정책을 다시 횡단 검토합니다.
