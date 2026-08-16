# B7-2 Cloud Deployment / Cleanup Checklist

이 문서는 **Phase C 실제 배포**에서 사용합니다. Reference 단계에서는 특정 클라우드와 가짜 URL을 확정하지 않습니다.

## 1. 배포 전

- [ ] Python 3.10+ 런타임 선택
- [ ] `requirements.txt` 설치 가능 확인
- [ ] 실제 DB 전략 확정(SQLite persistent disk 또는 PostgreSQL 등)
- [ ] `DATABASE_URL`을 Secret/Environment로 설정
- [ ] `AI_API_URL`을 Environment로 설정
- [ ] `AI_API_KEY`를 Secret로 설정
- [ ] `AI_MODEL`을 Environment로 설정
- [ ] `.env` 실제 파일을 배포 artifact/Git에 포함하지 않음
- [ ] 외부에서 `/health` 확인 가능한 배포 방식 준비

## 2. 배포 후 Acceptance

배포 URL: **NEEDS-RUNTIME**

- [ ] 외부 네트워크에서 `/health` → 200
- [ ] 회원가입
- [ ] 로그인 → access token
- [ ] 로그인 전/후 UI 변화
- [ ] ChatSession 생성
- [ ] 메시지 전송 → 실제 AI 응답
- [ ] 대화 재조회
- [ ] 게시글 작성
- [ ] 게시글 목록/상세
- [ ] 본인 글 수정/삭제
- [ ] 다른 사용자 글 수정/삭제 → 403
- [ ] 다른 사용자 ChatSession 접근 → 403 또는 404
- [ ] 로그아웃 후 기존 token이 더 이상 사용되지 않음

## 3. 협업 이력

- [ ] 실제 `feature/* → develop → main` 흐름
- [ ] `main` 직접 push 없음
- [ ] 기능 단위 PR 이력
- [ ] 팀원별 유의미한 커밋 10회 이상
- [ ] README 또는 문서에 팀원 역할/개인별 작업 요약

## 4. Evidence

- [ ] 배포 URL
- [ ] 외부 `/health`
- [ ] 전체 사용자 흐름
- [ ] 2-user ownership 테스트
- [ ] AI API 실제 응답
- [ ] PR/commit links
- [ ] ERD/API/Architecture 문서
- [ ] Secret 노출 검사

## 5. 과금/리소스 정리

실습 종료 후 실제 사용한 Provider 콘솔에서 다음을 확인합니다.

- [ ] 불필요한 VM/container/service 종료 또는 삭제
- [ ] 불필요한 DB 삭제 또는 과금 중지
- [ ] 고정 IP/Load Balancer/Volume 등 잔여 유료 리소스 확인
- [ ] 불필요한 Secret/환경변수 제거 또는 rotation
- [ ] Provider Billing/Resource 목록 최종 확인
- [ ] 정리 결과를 Evidence로 기록

실제 Provider마다 리소스 이름과 과금 구조가 다르므로 Phase C에서 선택한 환경에 맞춰 세부 절차를 확정합니다.
