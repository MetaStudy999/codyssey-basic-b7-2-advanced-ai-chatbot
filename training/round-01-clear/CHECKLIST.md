# B7-2 Round 01 — Project Clear Checklist

현재 모드: **Phase A — REFERENCE BUILD**  
Runtime Project 상태: **⬜ NOT STARTED**

> 현재 저장소 `main`에는 별도 Evaluation 파일이 없으므로 공식 Mission PDF/MD 요구사항을 Gate로 사용합니다. Reference 파일 존재만으로 Runtime PASS/CLEAR 처리하지 않습니다.

## A. Source

- [x] `b7-2-mission.pdf` 확인
- [x] `b7-2-mission.md` 분석
- [x] 별도 `b7-2-evaluation.md` 부재 확인
- [x] 필수 기능 / 실제환경 / 제출물 / 제약 분리

## B. Reference Build

- [x] `REFERENCE-BUILD.md`
- [x] `REFERENCE-STATUS.md`
- [x] `reference/README.md`
- [x] Backend REST 구조
- [x] Frontend REST client
- [x] Environment setup/verify/reset/inspect
- [x] Requirements Mapping
- [x] ERD
- [x] API Specification
- [x] System Architecture
- [x] Collaboration template
- [x] Deployment/Cleanup checklist
- [x] Evidence Guide
- [x] Beginner Guide

## C. 사용자 인증 Reference

- [x] 회원가입 API
- [x] 비밀번호 PBKDF2 hash
- [x] 로그인 API
- [x] 로그인 성공 access token 발급
- [x] raw token 대신 DB token hash 저장
- [x] Bearer current-user dependency
- [x] 로그아웃 token revoke
- [x] 로그인 전/후 frontend UI 분기
- [x] 비인증 보호 API 401 설계

## D. 사용자별 AI Chat Reference

- [x] ChatSession user FK
- [x] Message session FK
- [x] 내 session 목록
- [x] 새 session 생성
- [x] message history
- [x] message send
- [x] 최근 context 구성
- [x] env-only AI API client
- [x] AI response Message 저장
- [x] 다른 user session 접근 404 ownership 정책
- [x] AI 오류 502 경로

## E. 게시판 Reference

- [x] Post title/content/author/created_at/updated_at
- [x] 목록 공개 GET
- [x] 상세 공개 GET
- [x] 작성 인증 POST
- [x] 본인 수정 PUT
- [x] 본인 삭제 DELETE
- [x] 타 사용자 수정/삭제 403

## F. REST / Frontend

- [x] `/api/auth/*`
- [x] `/api/chat/*`
- [x] `/api/posts*`
- [x] HTTP methods/status 설계
- [x] Frontend `fetch()` 통신
- [x] `/health`
- [x] frontend가 API 결과로 UI 갱신

## G. 기술 문서

- [x] 모든 핵심 Entity/FK를 ERD에 기록
- [x] API URL/method/auth/request/response/status 문서화
- [x] Frontend/Backend/DB/AI/Cloud Architecture 흐름
- [x] README 서비스 소개
- [x] README 기술 스택
- [x] README 로컬 실행
- [x] README 환경변수
- [x] README 구조
- [x] 배포 URL은 가짜값 대신 NEEDS-RUNTIME

## H. Secret / Environment

- [x] `.env.example` placeholder
- [x] AI API key source code hard-code 금지
- [x] DB URL environment 지원
- [x] Secret-pattern 검증 스크립트 준비
- [x] DB inspect가 password/token 전체값을 출력하지 않음
- [ ] 실제 `.env` Git 비포함 최종 확인
- [ ] 실제 Secret 로그/Evidence 미노출 확인

## I. Reference Verify

- [x] 파일 구조 검사 준비
- [x] Python `compileall` 준비
- [x] JS syntax 검사 optional 준비
- [x] 5 core ORM entity 검사
- [x] password hash 사용 검사
- [x] access token 발급 검사
- [x] Chat ownership 검사
- [x] Post ownership 검사
- [x] AI key env 검사
- [x] credential pattern scan 준비
- [ ] `bash environment/verify.sh` 실제 실행

## J. Runtime Local — Phase C

- [ ] Python 3.10+
- [ ] 가상환경 / dependency 설치
- [ ] 실제 `.env` local 구성
- [ ] FastAPI 기동
- [ ] Frontend 정상 로드
- [ ] `/health` 200
- [ ] User A 회원가입
- [ ] password hash DB 확인
- [ ] 로그인 실패/성공
- [ ] token 발급
- [ ] ChatSession 생성/목록
- [ ] 실제 AI 메시지/응답
- [ ] 대화 재조회
- [ ] 게시판 CRUD
- [ ] logout 후 token 401

## K. Ownership Runtime — Phase C

- [ ] User B 별도 가입/로그인
- [ ] User B는 User A ChatSession 목록에서 볼 수 없음
- [ ] User B가 User A ChatSession 직접 접근 → 403/404
- [ ] User B가 User A Post 수정 → 403
- [ ] User B가 User A Post 삭제 → 403

## L. Cloud Runtime — Phase C

- [ ] 실제 Cloud/PaaS 선택
- [ ] 실제 Secret/Environment 설정
- [ ] 실제 외부 URL
- [ ] 외부 `/health` 200
- [ ] 외부 회원가입→로그인→AI Chat→게시판 전체 flow
- [ ] 실습 종료 후 불필요 리소스 cleanup
- [ ] Billing/Resource 최종 확인

## M. Git / Collaboration Runtime

- [ ] 실제 `feature/* → develop → main`
- [ ] main 직접 push 없음
- [ ] 기능별 Pull Request 이력
- [ ] 모든 팀원 유의미 커밋 10회 이상
- [ ] 실제 팀 역할 기록
- [ ] 실제 개인별 작업 요약

## N. Evidence

- [x] Evidence 수집 계획
- [ ] 인증 Evidence
- [ ] AI Chat Evidence
- [ ] 2-user ownership Evidence
- [ ] Post ownership Evidence
- [ ] REST status Evidence
- [ ] 실제 배포 URL Evidence
- [ ] Git/PR/commit Evidence
- [ ] cloud cleanup Evidence
- [ ] Secret 노출 없음 최종 확인

## O. CLEAR Gate

- [x] Mission 요구 분석
- [x] 최소 충분 Reference 구현 준비
- [x] 기술 문서 준비
- [x] 검증 도구 준비
- [x] Runtime 전용 항목 명확히 분리
- [ ] Reference verify 실제 실행
- [ ] 실제 AI Runtime
- [ ] 실제 ownership Runtime
- [ ] 실제 cloud Runtime
- [ ] 실제 협업 이력
- [ ] Evidence 완료
- [ ] BLOCKER 0 / MAJOR 0 최종 감사
- [ ] **✅ B7-2 PROJECT CLEAR**
