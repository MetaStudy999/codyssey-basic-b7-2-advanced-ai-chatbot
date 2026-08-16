# B7-2 Runtime Evidence Guide

이 디렉터리에는 **Phase C에서 실제로 수행한 결과만** 저장합니다. Reference 예상 출력, 가짜 URL, 가짜 PR/commit 이력은 Evidence로 사용하지 않습니다.

## A. 인증

1. 회원가입 성공
2. DB의 `password_hash`가 평문 비밀번호가 아님을 확인
3. 로그인 실패(잘못된 비밀번호)
4. 로그인 성공 + token 발급
5. 로그인 전/후 UI 차이
6. 로그아웃 후 같은 token 사용 시 401

## B. 사용자별 AI Chat

7. User A ChatSession 생성/목록
8. User A 메시지 저장
9. 실제 AI 응답 생성/저장
10. User A 대화 재조회
11. User B가 User A session 접근 → 403 또는 404
12. DB에서 ChatSession.user_id / Message.session_id 관계 확인

## C. 게시판

13. 비로그인 게시글 목록/상세 조회
14. 비로그인 작성 요청 → 401
15. 로그인 사용자 게시글 작성
16. 작성자 본인 수정/삭제
17. 다른 로그인 사용자의 수정/삭제 → 403
18. 게시글 작성자/작성일시 확인

## D. REST / 기술 문서

19. API별 HTTP method/status 실제 결과
20. `docs/erd.md`
21. `docs/api-spec.md`
22. `docs/architecture.md`
23. README 로컬 실행 절차 재현

## E. Cloud

24. 실제 배포 URL
25. 외부 네트워크 `/health` 200
26. 외부 환경에서 회원가입→로그인→AI Chat→게시판 전체 흐름
27. 배포 환경 Secret이 소스/로그에 노출되지 않음

## F. Git / Collaboration

28. `feature/* → develop → main` 실제 브랜치/PR 이력
29. `main` 직접 push 없이 PR 병합 근거
30. 팀원별 유의미 커밋 10회 이상
31. 팀 역할/개인별 작업 요약

## G. Cleanup

32. 실습 종료 후 불필요한 cloud 리소스 정리
33. Billing/Resource 목록 최종 확인

## 권장 파일 이름

```text
01-signup.txt
02-password-hash.txt
03-login-fail.txt
04-login-success.txt
05-auth-ui.png
06-logout-token.txt
07-chat-user-a.txt
08-ai-response.png
09-chat-isolation.txt
10-post-public.txt
11-post-auth.txt
12-post-owner-403.txt
13-api-runtime.txt
14-external-health.txt
15-deployed-flow.md
16-git-pr-history.md
17-cleanup.md
```

## Secret 금지

다음을 Evidence에 복사하지 않습니다.

- 실제 `AI_API_KEY`
- 실제 `.env` 전체 내용
- 실제 Bearer token 전체 값
- DB password
- Private Key

필요하면 값 자체가 아니라 "설정되어 있음" 또는 일부 마스킹된 형태만 증빙합니다.
